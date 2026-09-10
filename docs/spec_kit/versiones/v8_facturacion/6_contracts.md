# Contratos — Versión 8: las pantallas de facturación

> Base `http://localhost:8066` · Los 51 de la API, intactos.

```
GET  /facturas               -> 200 tabla: numero, fecha, NOMBRES, total, badge estado
GET  /facturas/<n>           -> 200 detalle maestro + renglones · inexistente -> rebote con mensaje
GET  /facturas/nueva         -> 200 formulario (selects de la API + 5 renglones)
POST /facturas/nueva         -> 302 con "Factura N creada..." · errores 422/trigger VESTIDOS
POST /facturas/<n>/anular    -> 302 "stock RESTAURADO" · 409 doble anulación / 404, vestidos
```
