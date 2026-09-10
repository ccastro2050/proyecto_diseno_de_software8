"""
rutas_entidades.py — Las rutas GENÉRICAS del front (v7).

Un solo juego de vistas atiende a TODAS las entidades del registro:
la entidad llega en la URL (/e/<clave>) y sus metadatos salen de
entidades.py. Las reglas de negocio siguen en la API.
"""

from flask import Blueprint, abort, flash, redirect, render_template, request, session, url_for

import cliente_api
from entidades import ENTIDADES, ID_ROL_ADMINISTRADOR

bp = Blueprint("entidades", __name__)


def _config(clave):
    cfg = ENTIDADES.get(clave)
    if cfg is None:
        abort(404)
    if cfg["solo_admin"] and not session.get("es_admin"):
        flash("Esa sección es solo para administradores.", "error")
        abort(redirect(url_for("listar")))
    return cfg


def _opciones_fk(cfg):
    """Para cada campo FK, trae las opciones desde la API (los selects)."""
    opciones = {}
    for nombre, _, fk in cfg["campos"]:
        if fk:
            fuente = ENTIDADES[fk]
            ok, datos, _ = cliente_api.listar(fuente["endpoint"])
            pk = fuente["pk"]
            etiqueta = fuente["campos"][1][0] if len(fuente["campos"]) > 1 else pk
            opciones[nombre] = [(str(d[pk]), f"{d[pk]} — {d.get(etiqueta, '')}") for d in datos] if ok else []
    return opciones


@bp.route("/e/<clave>")
def lista(clave):
    cfg = _config(clave)
    ok, datos, errores = cliente_api.listar(cfg["endpoint"])
    for e in errores:
        flash(e, "error")
    return render_template("entidades/lista.html", clave=clave, cfg=cfg, datos=datos)


@bp.route("/e/<clave>/nuevo", methods=["GET", "POST"])
def crear(clave):
    cfg = _config(clave)
    if request.method == "POST":
        datos = {n: request.form.get(n, "").strip() for n, _, _ in cfg["campos"]}
        # Los opcionales vacíos no viajan (la API decide sus defaults):
        datos = {k: v for k, v in datos.items() if v != ""}
        ok, errores = cliente_api.crear(cfg["endpoint"], datos)
        if ok:
            flash("Registro creado.", "exito")
            return redirect(url_for("entidades.lista", clave=clave))
        for e in errores:
            flash(e, "error")
        return render_template("entidades/formulario.html", clave=clave, cfg=cfg,
                               registro=datos, editando=False, opciones=_opciones_fk(cfg))
    return render_template("entidades/formulario.html", clave=clave, cfg=cfg,
                           registro={}, editando=False, opciones=_opciones_fk(cfg))


@bp.route("/e/<clave>/<pk>/editar", methods=["GET", "POST"])
def editar(clave, pk):
    cfg = _config(clave)
    if not cfg["editable"]:
        abort(404)  # los puentes no se editan: se quita y se pone
    if request.method == "POST":
        datos = {n: request.form.get(n, "").strip() for n, _, _ in cfg["campos"]
                 if n != cfg["pk"] and request.form.get(n, "").strip() != ""}
        ok, errores = cliente_api.actualizar(cfg["endpoint"], pk, datos)
        if ok:
            flash("Registro actualizado.", "exito")
            return redirect(url_for("entidades.lista", clave=clave))
        for e in errores:
            flash(e, "error")
    ok, registro, errores = cliente_api.obtener(cfg["endpoint"], pk)
    if not ok:
        for e in errores:
            flash(e, "error")
        return redirect(url_for("entidades.lista", clave=clave))
    return render_template("entidades/formulario.html", clave=clave, cfg=cfg,
                           registro=registro, editando=True, opciones=_opciones_fk(cfg))


@bp.route("/e/<clave>/<pk>/eliminar", methods=["POST"])
def eliminar(clave, pk):
    cfg = _config(clave)
    ok, errores = cliente_api.borrar(cfg["endpoint"], pk)
    flash("Registro eliminado." if ok else " ".join(errores), "exito" if ok else "error")
    return redirect(url_for("entidades.lista", clave=clave))


@bp.route("/e/<clave>/<a>/<b>/eliminar", methods=["POST"])
def eliminar_puente(clave, a, b):
    """El DELETE de PK compuesta: la pareja EXACTA (regla dura de la v3)."""
    cfg = _config(clave)
    if not cfg.get("puente"):
        abort(404)
    ok, errores = cliente_api.borrar(cfg["endpoint"], f"{a}/{b}")
    flash("Asignación retirada." if ok else " ".join(errores), "exito" if ok else "error")
    return redirect(url_for("entidades.lista", clave=clave))
