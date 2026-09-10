# Plan — Versión 8: la facturación con pantalla

## 1. La secuencia completa (nadie calcula en el camino)

```mermaid
sequenceDiagram
    autonumber
    actor U as Usuario
    participant F as front (rutas_facturas)
    participant A as API (INTACTA)
    participant BD as BD (SP + triggers)
    U->>F: POST del formulario (cliente, vendedor, renglones)
    F->>A: POST /api/factura {fkidcliente, fkidvendedor, productos[]}
    A->>BD: CALL sp_insertar_factura... (la transacción)
    Note over BD: los TRIGGERS validan stock, calculan<br/>subtotales, descuentan y fijan el total
    BD-->>A: el JSON de la factura completa
    A-->>F: 200 (o 422 / 500 del trigger)
    F-->>U: redirección con mensaje — o el error VESTIDO
```

## 2. Inventario
**Nuevos:** `rutas_facturas.py` (blueprint: lista, detalle, crear,
anular) · `templates/facturas/{lista,detalle,formulario}.html`.
**Crecen:** `cliente_api.py` (listar/obtener/crear/anular factura) ·
`app.py` (blueprint) · `base.html` (enlace Facturas) · `Program.cs` (v8).

## 3. Decisiones aterrizadas
- El formulario ofrece **5 renglones fijos** (selects + cantidad): los
  diligenciados viajan; server-side puro, sin JavaScript (D5 de la v6).
- El botón Anular solo existe en facturas ACTIVAS; el 409 igual queda
  cubierto (dos pestañas abiertas) y se muestra vestido.
- Los nombres de cliente/vendedor en la lista NO los busca el front:
  vienen del SP (la API) — cero JOINs en Python.

## 4. Chequeo de constitución

> **La compuerta 2** del método (ver [SDD_SPECKIT](../../../SDD_SPECKIT.md)):
> antes de pasar a `8_tasks.md` se revisa la
> [constitución](../../1_constitution.md) **artículo por artículo**. Si algo
> no cumple, o se corrige el plan, o se enmienda la constitución. Nunca se
> deja pasar "por esta vez".

| Artículo | Cómo lo cumple esta versión |
|---|---|
| **1** — El curso es POR VERSIONES y la especificación manda | El alcance de esta versión es el que declara [2_spec.md](2_spec.md) §2, y **no anticipa** nada de las siguientes. Cierra con commit y tag. |
| **2** — Stack: C# y ASP.NET Core, con el SQL a la vista | C# sobre ASP.NET Core, SQL escrito a mano y **siempre parametrizado**, sin ORM de entidades. Los paquetes son los que el artículo permite (§1 de este plan). |
| **3** — Arquitectura en capas con interfaces, desde el día 1 | Controlador → interfaz de servicio → interfaz de repositorio → repositorio (§3 de este plan). Solo el ensamblador conoce clases concretas. |
| **4** — Un solo comando | `docker compose up -d --build` deja la versión funcionando (§5 de este plan). |
| **5** — La base de datos viene DADA | La BD `bdfacturas` viene dada por los scripts de `db/`; esta versión solo nombra las tablas que su alcance le permite ([5_data_model.md](5_data_model.md)). |
| **6** — Todo en español, comentado para principiantes | Nombres, rutas y mensajes en español, con comentarios línea a línea en el código. |
| **7** — Contratos exactos | [6_contracts.md](6_contracts.md) fija verbos, rutas, códigos y formatos exactos, incluidos los desenlaces de error. |
| **8** — Convenciones fijas | Puertos, rutas, sobre de respuesta y catálogo de errores, tal como los fija el artículo. |

**Complejidad justificada:** si esta versión se desvía de algún artículo,
la desviación va aquí, con la alternativa más simple que se descartó y por
qué no sirvió. Sin desviaciones anotadas, se entiende que no las hay.
