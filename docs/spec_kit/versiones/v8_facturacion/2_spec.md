# Especificación — Versión 8: la facturación en el navegador (el cierre)

> **Versión 8** ([mapa](../0_mapa_versiones.md)) · Acumulativa: v1–v7
> intactas. La operación de negocio más rica del sistema — los SPs y
> triggers de la v2 — por fin con pantalla. Con esto la ruta del curso
> queda COMPLETA: API específica tri-motor + front completo.

## 1. Propósito
Crear, consultar y anular facturas desde el navegador, con la regla de
oro intacta: **el front no calcula NADA** — subtotales, total y stock
los pone la BD (triggers) a través de la API.

## 2. Alcance
**Incluye:** `/facturas` (lista con estado y total) · `/facturas/{n}`
(detalle maestro-renglones con nombres resueltos) · `/facturas/nueva`
(selects de cliente/vendedor + hasta 5 renglones producto+cantidad) ·
anular con confirmación (stock restaurado) · estados vestidos con la
marca (activa Verde Páramo, anulada Rojo Anulada).
**NO incluye:** editar/borrar facturas (anular ES la operación de
negocio, regla de la v2) · dashboards.

## 3. Requisitos funcionales
- **RF1** Listar: número, fecha, cliente y vendedor POR NOMBRE (los
  resolvió el SP), total y estado como badge de la marca.
- **RF2** Detalle: encabezado + renglones con subtotales de la BD.
- **RF3** Crear: selects cargados de la API; renglones diligenciados
  viajan como `productos:[{codigo, cantidad}]` al SP; el 422 y los
  errores del trigger (stock insuficiente) se muestran vestidos.
- **RF4** Anular: solo visible en facturas activas; 409 de la doble
  anulación y 404 mostrados como mensajes.

## 4. Criterios de aceptación
1. **Regresión:** smokes v6 y v7 sin cambios; diagnóstico `"version":"v8"`.
2. `/facturas` muestra las 6 semilla con nombres y badges.
3. Crear una factura (cliente 1, vendedor 1, PR001×2) desde el
   formulario: aparece con total CALCULADO y el stock de PR001 bajó
   (verificable por la API); el detalle muestra los renglones.
4. Anularla: mensaje de stock restaurado y badge en rojo; anularla otra
   vez → el mensaje del 409, vestido.
5. Crear con renglones vacíos → el 422 de la petición, vestido; con
   cantidad 9999 → el mensaje del trigger (stock insuficiente).

## 5. TERMINADA
Criterios en verde → tag `v8` → **la ruta del curso está COMPLETA**.

## 6. Clarificaciones

> **Qué es esta sección:** el registro de las ambigüedades detectadas ANTES
> de planear, con la respuesta que se acordó y su razón. Es **la compuerta
> 1** del método (ver [SDD_SPECKIT](../../../SDD_SPECKIT.md)): mientras
> quede un `[NECESITA ACLARACIÓN: …]` en los requisitos de arriba, esta
> versión no pasa a la planeación.
>
> Las entradas de abajo se reconstruyeron **al cerrar la versión**, a
> partir de las decisiones que sus propios contratos ya dejaban fijadas.
> De aquí en adelante esta sección se llena **en vivo**, antes del
> `3_plan.md` — que es como debe ser.

| # | La pregunta | La respuesta acordada, con su razón | Dónde quedó |
|---|---|---|---|
| C1 | Una factura equivocada, ¿se borra o se anula? | Se **anula**: borrado lógico que restaura el stock. La factura es un hecho contable; borrarla perdería la trazabilidad. | RF de anulación · contrato de anular |
| C2 | Anular dos veces la misma factura, ¿qué responde? | **409**: el conflicto es de estado, no de forma ni de existencia. La factura existe (no es 404) y el body está bien (no es 422). | Contrato de anular |

**Cómo se escribe una entrada nueva:** la pregunta tal como se hizo (no
"revisar el borrado", sino "¿físico o lógico?"), la respuesta **con su
razón**, y el documento donde quedó plasmada. Si la respuesta cambia un
requisito, se corrige el requisito allá arriba: esta sección lo registra,
no lo reemplaza.

## 7. Definición de TERMINADA

Esta versión está terminada — y solo entonces se escribe la spec de la
siguiente — cuando:

1. Todos los **criterios de aceptación** pasan, verificados con el smoke
   test de [7_quickstart.md](7_quickstart.md), **corrido por una persona**.
   "Me funciona" no es evidencia.
2. La lista de [9_checklist.md](9_checklist.md) está en verde y firmada.
3. No queda ningún `[NECESITA ACLARACIÓN: …]` en este documento.
4. Se hace commit y **tag** de la versión, según la
   [constitución](../../1_constitution.md).
