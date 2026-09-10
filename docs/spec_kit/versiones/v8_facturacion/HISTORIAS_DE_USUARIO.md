# Historias de usuario — Versión 8

> Formato del curso. Personas: Marcela Ríos (auxiliar) y Álvaro Mejía
> (administrador).

## Historia de Usuario 1
| | | |
|---|---|---|
| **Número:** 1 | **Usuario:** Marcela Ríos — auxiliar | **Iteración asignada:** v8 |
| **Nombre historia:** Facturar desde el navegador | | |
| **Diseñada por:** Carlos Arturo Castro Castro | **Prioridad:** Alta | **Riesgo:** Alto |
| **Puntos estimados:** 3 | **Horas estimadas:** 14 | **Programador responsable:** el estudiante ([GUIA_IA8](GUIA_IA8.md)) |

**Descripción:** Yo, Marcela Ríos, como auxiliar, quiero crear una
factura eligiendo cliente, vendedor y productos de listas, y que el
sistema calcule solo los subtotales, el total y el stock, para facturar
sin calculadora y sin miedo a dañar el inventario.

**Criterios de aceptación:**
1. El formulario ofrece cliente, vendedor y renglones como listas del
   sistema (nada se digita por código).
2. Al facturar veo el total CALCULADO y el stock descontado; si pido más
   de lo que hay, el sistema me lo dice con palabras (el trigger).
3. El detalle muestra los renglones con sus subtotales.

## Historia de Usuario 2
| | | |
|---|---|---|
| **Número:** 2 | **Usuario:** Álvaro Mejía — administrador | **Iteración asignada:** v8 |
| **Nombre historia:** Anular sin dañar el inventario | | |
| **Diseñada por:** Carlos Arturo Castro Castro | **Prioridad:** Alta | **Riesgo:** Medio |
| **Puntos estimados:** 2 | **Horas estimadas:** 8 | **Programador responsable:** el estudiante ([GUIA_IA8](GUIA_IA8.md)) |

**Descripción:** Yo, Álvaro Mejía, como administrador, quiero anular una
factura equivocada con un clic (confirmando), y que el inventario vuelva
solo a su estado, para corregir errores sin tocar la base de datos.

**Criterios de aceptación:**
1. Anular pide confirmación, deja la factura en rojo ("anulada") y el
   stock queda restaurado (verificable en Productos).
2. Una factura anulada no ofrece el botón; si dos personas anulan a la
   vez, la segunda ve el aviso "ya está anulada" (409), no un error técnico.
