# Quickstart — Versión 7

## 1. Arranque
`docker compose up -d --build` → API :8065 · front :8066.

## 2. Regresión
El smoke de la [v6](../v6_front_producto/7_quickstart.md) en :8066; el
diagnóstico de :8065 dice `"version":"v7"`.

## 3. Lo nuevo (criterios 2 a 4)
Cree el usuario demo y hágalo admin (una vez, por la API):

```powershell
curl.exe -X POST http://localhost:8065/api/usuario -H "Content-Type: application/json" -d "{\"email\":\"demo@correo.com\",\"contrasena\":\"Demo123!\"}"
curl.exe -X POST http://localhost:8065/api/rol-usuario -H "Content-Type: application/json" -d "{\"fkemail\":\"demo@correo.com\",\"fkidrol\":1}"
```

En el navegador (localhost:8066, demo@correo.com / Demo123!):
el menú completo (admin) · cadena E200 → P020 → cliente → vendedor con
selects · asignar rol 2 a demo y quitarlo · crear un usuario sin roles,
entrar con él: menú corto y rebote por URL.

## 4. Si algo falla
| Síntoma | Causa |
|---|---|
| No aparecen las secciones admin | Sin rol 1, o no reentró (el rol se lee al ENTRAR) |
| Un select vacío | La entidad fuente sin filas o la API aún compilando |
