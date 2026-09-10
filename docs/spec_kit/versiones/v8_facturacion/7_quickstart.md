# Quickstart — Versión 8

## 1. Arranque
`docker compose up -d --build` → API :8065 · front :8066.

## 2. Regresión
Smokes de la [v6](../v6_front_producto/7_quickstart.md) y la
[v7](../v7_front_completo/7_quickstart.md) en :8066; el diagnóstico de
:8065 dice `"version":"v8"`.

## 3. Lo nuevo (criterios 2 a 5) — en el navegador
Con el usuario admin del README (demo@correo.com / Demo123!):

1. **Facturas** en el menú → las 6 semilla con nombres y badges.
2. Anote el stock de PR001 (Productos) → Nueva factura: cliente 1,
   vendedor 1, renglón PR001 × 2 → Facturar → la lista muestra la nueva
   con TOTAL calculado; el stock de PR001 bajó 2.
3. Ver → los renglones con subtotales (de la BD).
4. Anular → badge rojo y stock restaurado; anular otra vez (desde otra
   pestaña con la factura abierta) → el mensaje del 409.
5. Nueva factura sin renglones → el 422 vestido; con cantidad 9999 → el
   mensaje del trigger "Stock insuficiente…".

## 4. Si algo falla
| Síntoma | Causa |
|---|---|
| "requiere mínimo 1 producto" | Ningún renglón tenía producto Y cantidad |
| 500 con FK al facturar | Cliente/vendedor sin seleccionar (viajó vacío) |
| El total no aparece "en vivo" | Correcto: el total lo dice la BD al facturar (D3) |
