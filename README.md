# Aplicación REST modular con FastAPI
---
Este proyecto implementa un sistema CRUD modular utilizando FastAPI, con integración de SQLAlchemy ORM, persistencia en MySQL y tests automatizados con Pytest + TestClient. Además, incluye una interfaz gráfica de escritorio desarrollada en Python puro (Tkinter, PySide6 y Flet) para consumir los endpoints de forma visual, y administración vía SQLAdmin.

## 📌 Características principales
- ⚡ FastAPI para creación de endpoints rápidos y tipados

- 🧠 SQLAlchemy ORM para modelos de datos relacionales

- 🛡️ Validaciones avanzadas con Pydantic v2

- 🐬 Persistencia con MySQL vía PyMySQL

- 📑 Swagger UI y OpenAPI disponibles en /docs

- 🔎 Manejo de errores detallado con HTTPException y validaciones personalizadas

- ✅ Tests de integración con Pytest y httpx

- 🧪 Preparado para ambientes de testing con configuración desacoplada

- 💻 GUI para consumo de endpoints desde escritorio

- 🛠️ Panel administrativo con SQLAdmin

## ⚙️ Instalación y ejecución
- 1️⃣ Clonar el repositorio:
```
bash
git clone https://github.com/NicolasAndresCL/FastAPI.git
cd FastAPI
```
- 2️⃣ Crear entorno virtual y activar:
```
bash
python -m venv env
source env/bin/activate  # o .\env\Scripts\activate en Windows
```
- 3️⃣ Instalar dependencias:
```
bash
pip install -r requirements.txt
```
- 4️⃣ Configurar la base de datos:

>Asegurate de tener MySQL instalado y en ejecución.
```
sql
CREATE DATABASE fastapi_db;
```
>📌 Modificá las credenciales en db/database.py

- 5️⃣ Ejecutar el servidor:
```
bash
uvicorn app.main:app --reload
```
## 🧪 GUI integrada (opcional)
>Además del API REST, el proyecto incluye interfaces gráficas para consultar los usuarios:

GUI	      |  Archivo	    | Framework
:--------:|:---------------:|------
Tkinter	  | main_tkinter.py | Python StdLib
PySide6	  | main_pyside6.py	|Qt for Python
Flet	  |main_flet.py	    |Flet Web/Local

>Cada interfaz permite consumir endpoints como /user/ y /user/{id} desde escritorio, con estructura clara, manejo de errores y estilo profesional. Ideal para pruebas técnicas o demostraciones offline.

## 🛡️ Panel administrativo con SQLAdmin
El proyecto incluye integración con SQLAdmin, una herramienta para generar un panel de administración visual sobre modelos SQLAlchemy.

▶️ Acceso:
http
```
http://127.0.0.1:8000/admin
```
Login por defecto

__Funcionalidad:__

- Listado y edición de usuarios

- Búsqueda, creación y eliminación desde el panel

- Relación directa con tu ORM definido en models/


## 🏗️ Estructura del Proyecto
```
bash
FASTAPI/
│
├── app/
│   ├── db/                 # Configuración de base de datos y ORM
│   │   ├── config.py
│   │   ├── database.py
│   │   └── models.py
│   ├── dependencies/       # Inyección de dependencias (autenticación, DB)
│   ├── models/             # Modelos adicionales o compartidos
│   ├── repository/         # Lógica CRUD desacoplada por dominio
│   │   └── user.py
│   ├── routers/            # Endpoints organizados por dominio
│   │   └── user.py
│   ├── schemas/            # Esquemas Pydantic v2 para validación y respuestas
│   ├── tests/              # Test unitarios y funcionales (pytest + TestClient)
│   |── main.py             # Punto de entrada principal de la API
|   ├── main_flet.py        # Lógica adicional y helpers (incluye GUI)
│   ├── main_pyside6.py
│   └── main_tkinter.py│
├── schemas.py              # Archivo raíz compartido de esquemas (legacy o común)
├── .env                    # Variables de entorno (credenciales, configuración)
├── requirements.txt        # Lista de dependencias para instalar
└── env/                    # Entorno virtual local (no se sube)
```

## 📦 Dependencias clave
Paquete	    |Propósito
:----------:|:---------
fastapi	    |Framework principal API
uvicorn	    |Servidor ASGI
sqlalchemy	|ORM para modelos
pymysql	    |Driver MySQL
httpx	    |Cliente HTTP para tests
email-validator|	Validación de campos tipo EmailStr
cryptography	|Autenticación con MySQL
pytest	|Framework de testing
SQLAdmin	|Panel visual para administración de modelos
flet, PySide6, requests	|Para interfaz gráfica local	