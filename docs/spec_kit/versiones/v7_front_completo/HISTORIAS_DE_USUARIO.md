# Historias de usuario — Versión 7

> Formato del curso. Personas: Marcela Ríos (auxiliar) y Álvaro Mejía
> (administrador).

## Historia de Usuario 1
| | | |
|---|---|---|
| **Número:** 1 | **Usuario:** Marcela Ríos — auxiliar | **Iteración asignada:** v7 |
| **Nombre historia:** Gestionar toda la operación desde el navegador | | |
| **Diseñada por:** Carlos Arturo Castro Castro | **Prioridad:** Alta | **Riesgo:** Medio |
| **Puntos estimados:** 3 | **Horas estimadas:** 12 | **Programador responsable:** el estudiante ([GUIA_IA7](GUIA_IA7.md)) |

**Descripción:** Yo, Marcela Ríos, como auxiliar, quiero registrar
empresas, personas, clientes y vendedores con formularios donde las
relaciones se escojan de una LISTA (no digitando códigos), para
completar la cadena comercial sin errores de tipeo.

**Criterios de aceptación:**
1. Cada entidad tiene su sección con tabla y formularios; los errores de
   la API, visibles.
2. Cliente y vendedor eligen persona (y empresa) en un select del sistema.
3. La cadena E200 → P020 → cliente → vendedor queda creada sin Swagger.

## Historia de Usuario 2
| | | |
|---|---|---|
| **Número:** 2 | **Usuario:** Álvaro Mejía — administrador | **Iteración asignada:** v7 |
| **Nombre historia:** Que cada quien vea SOLO lo suyo | | |
| **Diseñada por:** Carlos Arturo Castro Castro | **Prioridad:** Alta | **Riesgo:** Alto |
| **Puntos estimados:** 3 | **Horas estimadas:** 10 | **Programador responsable:** el estudiante ([GUIA_IA7](GUIA_IA7.md)) |

**Descripción:** Yo, Álvaro Mejía, como administrador, quiero que
usuarios, roles, rutas y asignaciones solo los vea quien tenga el rol
Administrador, y asignar o quitar roles con un clic, para gobernar el
acceso sin tocar la base de datos.

**Criterios de aceptación:**
1. Sin el rol 1, esas secciones no aparecen y por URL rebotan con aviso.
2. Con el rol 1, asigno un rol y QUITO esa pareja exacta (sin editar).
3. La lista de usuarios jamás muestra contraseñas.
