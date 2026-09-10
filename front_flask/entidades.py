"""
entidades.py — El REGISTRO del front (v7): los metadatos de cada entidad.

El molde del front no se copia 12 veces: se DESCRIBE cada entidad
(endpoint, PK, campos, llaves foráneas, permisos) y las rutas genéricas
hacen el resto. Las reglas de negocio siguen TODAS en la API.

Cada campo: (nombre, etiqueta, fk) — fk = clave de OTRA entidad del
registro cuando el campo es una llave foránea (el formulario lo vuelve
un <select> cargado desde la API).
"""

ENTIDADES = {
    "producto": dict(titulo="Productos", endpoint="/api/producto", pk="codigo",
        campos=[("codigo", "Código", None), ("nombre", "Nombre", None),
                ("stock", "Stock", None), ("valorunitario", "Valor unitario", None)],
        solo_admin=False, editable=True),
    "persona": dict(titulo="Personas", endpoint="/api/persona", pk="codigo",
        campos=[("codigo", "Código", None), ("nombre", "Nombre", None),
                ("email", "Email", None), ("telefono", "Teléfono", None)],
        solo_admin=False, editable=True),
    "empresa": dict(titulo="Empresas", endpoint="/api/empresa", pk="codigo",
        campos=[("codigo", "Código", None), ("nombre", "Nombre", None)],
        solo_admin=False, editable=True),
    "cliente": dict(titulo="Clientes", endpoint="/api/cliente", pk="id",
        campos=[("credito", "Crédito", None),
                ("fkcodpersona", "Persona", "persona"),
                ("fkcodempresa", "Empresa (opcional)", "empresa")],
        solo_admin=False, editable=True, pk_generada=True),
    "vendedor": dict(titulo="Vendedores", endpoint="/api/vendedor", pk="id",
        campos=[("carnet", "Carnet", None), ("direccion", "Dirección", None),
                ("fkcodpersona", "Persona", "persona")],
        solo_admin=False, editable=True, pk_generada=True),
    "usuario": dict(titulo="Usuarios", endpoint="/api/usuario", pk="email",
        campos=[("email", "Email", None), ("contrasena", "Contraseña", None)],
        solo_admin=True, editable=True, ocultar_en_lista=["contrasena"]),
    "rol": dict(titulo="Roles", endpoint="/api/rol", pk="id",
        campos=[("nombre", "Nombre", None)],
        solo_admin=True, editable=True, pk_generada=True),
    "ruta": dict(titulo="Rutas", endpoint="/api/ruta", pk="id",
        campos=[("ruta", "Ruta", None), ("descripcion", "Descripción", None)],
        solo_admin=True, editable=True, pk_generada=True),
    # Las tablas PUENTE: PK compuesta, sin editar (se quita y se pone):
    "rol-usuario": dict(titulo="Roles por usuario", endpoint="/api/rol-usuario",
        pk=("fkemail", "fkidrol"),
        campos=[("fkemail", "Usuario", "usuario"), ("fkidrol", "Rol", "rol")],
        solo_admin=True, editable=False, puente=True),
    "rutarol": dict(titulo="Permisos (ruta-rol)", endpoint="/api/rutarol",
        pk=("fkidruta", "fkidrol"),
        campos=[("fkidruta", "Ruta", "ruta"), ("fkidrol", "Rol", "rol")],
        solo_admin=True, editable=False, puente=True),
}

ID_ROL_ADMINISTRADOR = 1  # el rol semilla "Administrador"
