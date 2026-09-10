# Guía IA — Versión 8 (la facturación; estudiante :8166)

Entregue esta carpeta + su front v7 construido, con este encargo:

```
Construye la v8 de 2_spec.md sobre mi front v7: blueprint de facturas
(lista con nombres y badges, detalle, crear con selects de cliente/
vendedor y 5 renglones producto+cantidad, anular con confirmación).
El front NO calcula subtotales ni total ni stock: eso lo hace la BD vía
la API (POST /api/factura y /anular). Errores 422, del trigger y el 409
SIEMPRE vestidos con la marca. La API no se toca. Fases de 8_tasks.md.
```

Si la IA intenta calcular el total en el front o editar facturas,
deténgala: violó la spec. El cierre (quickstart) lo corre usted.
