# 🚀 CRUD API con FastAPI + SQLAlchemy + MySQL
Este proyecto implementa un sistema CRUD modular utilizando FastAPI, con integración de SQLAlchemy ORM, MySQL como motor de base de datos, y tests automatizados usando pytest y TestClient.
---
## 📌 Características principales

- ⚡ FastAPI para creación de endpoints rápidos y tipados

- 🧠 SQLAlchemy ORM para modelos de datos relacionales

- 🛡️ Validaciones avanzadas con Pydantic v2

- 🐬 Persistencia con MySQL vía PyMySQL

- 📑 Swagger UI y OpenAPI disponibles en /docs

- 🔎 Manejo de errores detallado con HTTPException y validaciones personalizadas

- ✅ Tests de integración con pytest y httpx

- 🧪 Preparado para ambientes de testing con configuración desacoplada

- 🔗 Acceso a la documentación interactiva
📍 Navegá a 👉 http://127.0.0.1:8000/docs para acceder a Swagger UI

# ⚙️ Instalación y ejecución
- 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/NicolasAndresCL/FastAPI.git
cd FastAPI
```
- 2️⃣ Crear entorno virtual y activar
```bash
python -m venv env
source env/bin/activate  # o .\env\Scripts\activate en Windows
```
- 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```
- 4️⃣ Configurar la base de datos

Asegurate de tener MySQL instalado y en ejecución.

Creá la base de datos desde MySQL:

```sql
CREATE DATABASE fastapi_db;
Modificá las credenciales en core/database.py
```
- 5️⃣ Ejecutar el servidor
```bash
uvicorn app.main:app --reload
```
- 🧪 También podés ejecutar directamente el main.py con:

```python
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", port=8000, reload=True)
```

# ✅ Mejoras recientes

- 🔁 Refactorización completa de rutas y lógica de negocio

- 🧩 Separación en capas: routers, schemas, repository, services, models

- 📦 Tests funcionales con pytest y TestClient

- 🛡️ Validaciones manuales + automáticas de entrada

- 🧵 Migración a Pydantic v2 (model_dump en lugar de dict())

- 📁 .gitignore actualizado y entorno virtual limpio

- 💥 Test de creación de usuario pasando correctamente

# 🏗️ Estructura del Proyecto
```bash
FastAPI/
│
├── app/
│   ├── core/            # Configuraciones base (DB, settings)
│   ├── models/          # Modelos SQLAlchemy
│   ├── schemas/         # Esquemas de entrada/salida (Pydantic)
│   ├── repository/      # Lógica de acceso a datos (CRUD)
│   ├── routers/         # Endpoints separados por dominio
│   ├── services/        # Reglas de negocio y helpers
│   └── main.py          # Punto de entrada FastAPI
│
├── tests/               # Tests con pytest
│   └── test_users.py
├── requirements.txt
└── README.md
```

# 📦 Dependencias clave

```Paquete	Propósito
fastapi	Framework principal API
uvicorn	Servidor ASGI
sqlalchemy	ORM
pymysql	Driver MySQL
httpx	Requerido por TestClient
email-validator	Validación de campos tipo EmailStr
cryptography	Autenticación con MySQL (caching_sha2)
pytest	Framework de testing
```