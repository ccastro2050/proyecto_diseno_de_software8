# Decisiones — Versión 8

## D1 — ¿Renglones dinámicos (JavaScript) o filas fijas?
**Opciones:** (a) botón "agregar renglón" con JS · (b) 5 filas fijas y
viajan las diligenciadas. **Decisión: (b)** — mantiene el front
server-side puro del curso (v6-D5) y 5 renglones cubren el caso
didáctico; quien necesite más, factura dos veces. El JS dinámico queda
como extensión natural para el proyecto de aula.

## D2 — ¿Por qué no editar ni borrar facturas?
Regla de negocio de la v2: anular ES la operación (borrado lógico con
stock restaurado). La pantalla obedece la spec, no la "completa".

## D3 — El front sigue sin calcular
La tentación de mostrar el total "en vivo" mientras se diligencian
renglones exigiría calcular en el navegador — y el total tiene UN dueño
(el trigger). Se muestra el total cuando la BD lo diga. La coherencia
vale más que el efecto.
