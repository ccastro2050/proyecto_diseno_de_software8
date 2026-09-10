"""
cliente_api.py — La capa de datos del FRONT.

Es al front lo que el repositorio es al back: la ÚNICA pieza que sabe
dónde viven los datos (la API). Traduce respuestas HTTP a tuplas
(ok, datos, errores) — y NUNCA decide negocio.
"""

import os

import requests

# El hostname interno del compose (api-facturas), jamás localhost:
URL_API = os.environ.get("API_FACTURAS_URL", "http://localhost:8065")
TIEMPO_MAXIMO = 10  # segundos: si la API no contesta, el front lo dice


def _llamar(metodo: str, ruta: str, **kwargs):
    """Ejecuta la petición y unifica el manejo de 'API caída'."""
    try:
        respuesta = requests.request(
            metodo, f"{URL_API}{ruta}", timeout=TIEMPO_MAXIMO, **kwargs
        )
        return respuesta
    except requests.RequestException:
        return None  # la API no está disponible


def _errores_del_422(cuerpo: dict) -> list[str]:
    """El 422 de la API trae la lista errores[]; se muestra uno por aviso."""
    errores = cuerpo.get("errores") or cuerpo.get("errors") or []
    if isinstance(errores, list):
        return [str(e) for e in errores] or [cuerpo.get("mensaje", "Datos inválidos.")]
    if isinstance(errores, dict):
        return [f"{campo}: {'; '.join(m)}" for campo, m in errores.items()]
    return [str(errores)]


def listar_productos():
    r = _llamar("GET", "/api/producto")
    if r is None:
        return False, [], ["El servicio no está disponible."]
    if r.status_code == 204:
        return True, [], []
    if r.status_code == 200:
        return True, r.json().get("datos", []), []
    return False, [], [r.json().get("mensaje", "Error al consultar.")]


def obtener_producto(codigo: str):
    r = _llamar("GET", f"/api/producto/{codigo}")
    if r is None:
        return False, None, ["El servicio no está disponible."]
    if r.status_code == 200:
        return True, r.json(), []
    return False, None, [r.json().get("mensaje", "No se pudo consultar.")]


def crear_producto(datos: dict):
    r = _llamar("POST", "/api/producto", json=datos)
    if r is None:
        return False, ["El servicio no está disponible."]
    if r.status_code == 200:
        return True, []
    if r.status_code == 422:
        return False, _errores_del_422(r.json())
    cuerpo = r.json()
    return False, [cuerpo.get("mensaje", ""), cuerpo.get("detalle", "")]


def actualizar_producto(codigo: str, datos: dict):
    """PATCH: viaja SOLO lo diligenciado (la pareja didáctica, en botones)."""
    r = _llamar("PATCH", f"/api/producto/{codigo}", json=datos)
    if r is None:
        return False, ["El servicio no está disponible."]
    if r.status_code == 200:
        return True, []
    if r.status_code == 422:
        return False, _errores_del_422(r.json())
    return False, [r.json().get("mensaje", "No se pudo actualizar.")]


def eliminar_producto(codigo: str):
    r = _llamar("DELETE", f"/api/producto/{codigo}")
    if r is None:
        return False, ["El servicio no está disponible."]
    if r.status_code == 200:
        return True, []
    return False, [r.json().get("mensaje", "No se pudo eliminar.")]


def verificar_credenciales(usuario: str, contrasena: str):
    """El login: 200 válida · 401 incorrecta · 404 no existe."""
    r = _llamar(
        "POST",
        "/api/usuario/verificar-contrasena",
        params={"valor_usuario": usuario, "valor_contrasena": contrasena},
    )
    if r is None:
        return False, "El servicio no está disponible."
    if r.status_code == 200:
        return True, ""
    if r.status_code == 401:
        return False, "Credenciales incorrectas."
    if r.status_code == 404:
        return False, "El usuario no existe."
    return False, "No se pudo validar (intente de nuevo)."


# ── v7: las funciones GENÉRICAS (una por operación, para TODO el registro) ──


def listar(endpoint: str):
    r = _llamar("GET", endpoint)
    if r is None:
        return False, [], ["El servicio no está disponible."]
    if r.status_code == 204:
        return True, [], []
    if r.status_code == 200:
        return True, r.json().get("datos", []), []
    return False, [], [r.json().get("mensaje", "Error al consultar.")]


def obtener(endpoint: str, pk):
    r = _llamar("GET", f"{endpoint}/{pk}")
    if r is None:
        return False, None, ["El servicio no está disponible."]
    if r.status_code == 200:
        return True, r.json(), []
    return False, None, [r.json().get("mensaje", "No se pudo consultar.")]


def crear(endpoint: str, datos: dict):
    r = _llamar("POST", endpoint, json=datos)
    if r is None:
        return False, ["El servicio no está disponible."]
    if r.status_code == 200:
        return True, []
    if r.status_code == 422:
        return False, _errores_del_422(r.json())
    cuerpo = r.json()
    return False, [cuerpo.get("mensaje", ""), cuerpo.get("detalle", "")]


def actualizar(endpoint: str, pk, datos: dict):
    r = _llamar("PATCH", f"{endpoint}/{pk}", json=datos)
    if r is None:
        return False, ["El servicio no está disponible."]
    if r.status_code == 200:
        return True, []
    if r.status_code == 422:
        return False, _errores_del_422(r.json())
    return False, [r.json().get("mensaje", "No se pudo actualizar.")]


def borrar(endpoint: str, pk):
    r = _llamar("DELETE", f"{endpoint}/{pk}")
    if r is None:
        return False, ["El servicio no está disponible."]
    if r.status_code == 200:
        return True, []
    return False, [r.json().get("mensaje", "No se pudo eliminar.")]


def es_administrador(email: str) -> bool:
    """v7: ¿el usuario tiene el rol Administrador? (rol_usuario de la v3)."""
    r = _llamar("GET", f"/api/rol-usuario/usuario/{email}")
    if r is None or r.status_code != 200:
        return False
    asignaciones = r.json().get("datos", [])
    return any(a.get("fkidrol") == 1 for a in asignaciones)


# ── v8: la facturación (los SPs de la v2, ahora con pantalla) ──────────


def listar_facturas():
    r = _llamar("GET", "/api/factura")
    if r is None:
        return False, [], ["El servicio no está disponible."]
    if r.status_code == 200:
        return True, r.json().get("datos", []), []
    return False, [], [r.json().get("mensaje", "Error al consultar facturas.")]


def obtener_factura(numero: int):
    r = _llamar("GET", f"/api/factura/{numero}")
    if r is None:
        return False, None, ["El servicio no está disponible."]
    if r.status_code == 200:
        return True, r.json(), []
    return False, None, [r.json().get("mensaje", "Factura no encontrada.")]


def crear_factura(datos: dict):
    r = _llamar("POST", "/api/factura", json=datos)
    if r is None:
        return False, None, ["El servicio no está disponible."]
    if r.status_code == 200:
        return True, r.json(), []
    if r.status_code == 422:
        return False, None, _errores_del_422(r.json())
    cuerpo = r.json()
    return False, None, [cuerpo.get("mensaje", ""), cuerpo.get("detalle", "")]


def anular_factura(numero: int):
    r = _llamar("POST", f"/api/factura/{numero}/anular")
    if r is None:
        return False, ["El servicio no está disponible."]
    if r.status_code == 200:
        return True, []
    # 404 no existe · 409 ya anulada — los mensajes de la API, tal cual:
    return False, [r.json().get("mensaje", "No se pudo anular.")]
