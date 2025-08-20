# 🚀 Aplicación REST modular con FastAPI + Alembic + Pytest

Este proyecto implementa un sistema CRUD escalable y profesional utilizando **FastAPI**, con integración de **SQLAlchemy ORM**, persistencia en **MySQL**, migraciones con **Alembic** y tests automatizados con **Pytest + TestClient**. Además, incluye una interfaz gráfica de escritorio (Tkinter, PySide6, Flet) para consumir los endpoints visualmente, y un panel administrativo vía SQLAdmin.

## 📌 Características principales

- ⚡ **FastAPI** para endpoints rápidos, tipados y documentados
- 🧠 **SQLAlchemy ORM** para modelos relacionales
- 🛡️ **Pydantic v2** para validaciones avanzadas
- 🐬 **MySQL** como motor de persistencia vía PyMySQL
- 🔄 **Alembic** para migraciones versionadas de base de datos
- 📑 **Swagger UI / OpenAPI** disponible en `/docs`
- 🔎 Manejo de errores con `HTTPException` y validaciones personalizadas
- ✅ Tests de integración con **Pytest** y **httpx**
- 🧪 Entorno de testing reproducible con **SQLite** en memoria y fixtures aislados
- 💻 GUI local con **Tkinter**, **PySide6** y **Flet**
- 🛠️ Panel administrativo visual con **SQLAdmin**

## ⚙️ Instalación y ejecución

1. **Clonar el repositorio**
    ```bash
    git clone https://github.com/NicolasAndresCL/FastAPI.git
    cd FastAPI
    ```

2. **Crear entorno virtual**
    ```bash
    python -m venv env
    source env/bin/activate  # o .\env\Scripts\activate en Windows
    ```

3. **Instalar dependencias**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configurar base de datos MySQL**
    ```sql
    CREATE DATABASE fastapi_db;
    ```
    > 📌 Editar credenciales en `app/db/database.py`

5. **Ejecutar servidor**
    ```bash
    uvicorn app.main:app --reload
    ```

## 🔄 Migraciones con Alembic

Este proyecto incluye configuración completa de Alembic para versionar cambios en la base de datos.

```bash
alembic init alembic
alembic revision --autogenerate -m "Agregar campo telefono a User"
alembic upgrade head
```

**Archivos clave:**
- `alembic.ini`
- `alembic/env.py`
- `alembic/versions/*.py`

## 🧪 Testing reproducible con Pytest

El entorno de pruebas usa **SQLite en memoria**, con creación y destrucción automática de tablas por test. Los fixtures están definidos en `tests/conftest.py`:

- `db_session`: sesión aislada por test
- `client`: cliente FastAPI con override de `get_db`
- `usuario_seed`: usuario semilla reproducible

```bash
pytest -v
```

## 💻 GUI integrada (opcional)

Este proyecto incluye interfaces gráficas para consumir los endpoints desde escritorio:

| GUI      | Archivo           | Framework         |
|----------|-------------------|------------------|
| Tkinter  | main_tkinter.py   | Python StdLib    |
| PySide6  | main_pyside6.py   | Qt for Python    |
| Flet     | main_flet.py      | Flet Web/Local   |

Cada GUI permite consultar `/user/` y `/user/{id}` con manejo de errores, estilo profesional y estructura clara. Ideal para pruebas técnicas o demostraciones offline.

## 🛡️ Panel administrativo con SQLAdmin

**Acceso:**  
[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

**Funcionalidades:**
- Listado, búsqueda y edición de usuarios
- Creación y eliminación desde el panel
- Relación directa con modelos SQLAlchemy

## 🏗️ Estructura del Proyecto

```plaintext
FASTAPI/
│
├── app/
│   ├── db/                 # Configuración de base de datos y ORM
│   │   ├── database.py
│   │   ├── models.py
│   │   └── config.py
│   ├── repository/         # Lógica CRUD desacoplada
│   ├── routers/            # Endpoints organizados por dominio
│   ├── schemas/            # Validación con Pydantic v2
│   ├── dependencies/       # Inyección de dependencias
│   ├── tests/              # Tests con Pytest + TestClient
│   ├── main.py             # Entrada principal de la API
│   ├── main_flet.py        # GUI con Flet
│   ├── main_pyside6.py     # GUI con PySide6
│   └── main_tkinter.py     # GUI con Tkinter
├── alembic/                # Migraciones de base de datos
├── alembic.ini             # Configuración de Alembic
├── requirements.txt        # Dependencias del proyecto
├── .env                    # Variables de entorno
└── env/                    # Entorno virtual local (no se sube)
```

## 📦 Dependencias clave

| Paquete         | Propósito                        |
|-----------------|----------------------------------|
| fastapi         | Framework principal API          |
| uvicorn         | Servidor ASGI                    |
| sqlalchemy      | ORM relacional                   |
| pymysql         | Driver MySQL                     |
| alembic         | Migraciones de base de datos     |
| httpx           | Cliente HTTP para tests          |
| pytest          | Framework de testing             |
| email-validator | Validación de EmailStr           |
| cryptography    | Seguridad y autenticación        |
| SQLAdmin        | Panel visual para modelos        |
| flet, PySide6   | GUI local multiplataforma        |

Portafolio: nicolasandrescl.pythonanywhere.com
