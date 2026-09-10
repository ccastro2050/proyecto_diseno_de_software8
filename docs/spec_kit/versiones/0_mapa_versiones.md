# Mapa de versiones del curso

> La ruta completa del proyecto. Cada versión se especifica SOLO cuando la
> anterior está cerrada (commit + tag). Este mapa da la dirección; las
> specs de cada versión dan el detalle.

| Versión | Qué agrega | Estado |
|---|---|---|
| **v1** | `api_facturas` (C#/ASP.NET Core): CRUD completo de `producto` contra **PostgreSQL** — capas + interfaces + peticiones por verbo | **En curso** ([spec](v1_producto_postgres/2_spec.md)) |
| v2 | Más entidades (persona, factura maestro-detalle…) aprovechando los triggers y SPs de la BD | Sin especificar |
| **v3** | **El resto de las entidades** contra PostgreSQL: empresa, cliente, vendedor, usuario (contraseña con **BCrypt** + verificar-contrasena), rol, ruta y las tablas puente rol_usuario y rutarol — TODA la bdfacturas cubierta con UN motor antes de cambiar de motor | **Cerrada** — tag `v3` ([spec](v3_resto_entidades/2_spec.md)) |
| **v4** | Segundo motor (**SQL Server**): la MISMA bdfacturas en dialecto T-SQL, los 11 repositorios SqlClient, la **fábrica de repositorios** (el motor se decide en UN punto), el interruptor `MOTOR_BD` y el contenedor **sqlserver-init** (la lección prometida en v1) — cero endpoints nuevos | **Cerrada** — tag `v4` ([spec](v4_sqlserver/2_spec.md)) |
| **v5** | Tercer motor (**MariaDB**): la MISMA bdfacturas (se siembra sola, como PostgreSQL), los 11 repositorios MySqlConnector, y la cuenta de la fábrica pagada por segunda vez — UNA clase y UN case | **Cerrada** — tag `v5` ([spec](v5_mariadb/2_spec.md)) |
| **v6** | **El front NACE** (Flask + Jinja2 + Bootstrap, :8066): la marca del [MANUAL_DE_MARCA](../../MANUAL_DE_MARCA.md), login con sesión sobre verificar-contrasena, y el CRUD de producto desde el navegador | **Cerrada** — tag `v6` ([spec](v6_front_producto/2_spec.md)) |
| **v7** | **El front COMPLETO**: las 12 entidades con el patrón registro (metadatos + vistas genéricas), llaves foráneas como select y el menú por roles | **Cerrada** — tag `v7` ([spec](v7_front_completo/2_spec.md)) |
| **v8** | **La facturación en pantalla**: crear maestro-detalle (selects + renglones), anular con stock restaurado, estados con la marca — **la ruta del curso, COMPLETA** | **Cerrada** — tag `v8` ([spec](v8_facturacion/2_spec.md)) |

> **El destino del curso:** la v5 deja la API específica COMPLETA y
> multi-motor (toda la bdfacturas, tres motores por configuración). La
> v6 le pone encima un front Flask (Jinja2) completo, con login y
> control de acceso. Cada versión intermedia es un paso deliberado de ese camino.

**Reglas del mapa** (constitución, Artículo 1): no se anticipa nada de una
versión futura; una versión cerrada no se reabre (los ajustes van en la
siguiente); el repositorio siempre muestra la versión en curso funcionando.
