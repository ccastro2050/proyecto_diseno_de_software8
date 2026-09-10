# Contratos — Versión 7: las pantallas genéricas

> Base `http://localhost:8066` · Los 51 de la API, intactos.

```
GET  /e/<entidad>                  -> 200 tabla · solo_admin sin rol -> rebote con aviso
GET  /e/<entidad>/nuevo            -> 200 formulario (FKs como select) · POST -> 302 o errores
GET  /e/<entidad>/<pk>/editar      -> 200 precargado · POST -> PATCH parcial (puentes: 404)
POST /e/<entidad>/<pk>/eliminar    -> 302 con mensaje
POST /e/<puente>/<a>/<b>/eliminar  -> 302 (la pareja exacta)
```

Entidades: producto, persona, empresa, cliente, vendedor (todos) ·
usuario, rol, ruta, rol-usuario, rutarol (solo admin). La lista de
usuario solo muestra emails.
