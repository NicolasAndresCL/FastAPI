🚀 CRUD con FastAPI, SQLAlchemy y MySQL
Este proyecto implementa un CRUD básico con FastAPI, ahora mejorado con SQLAlchemy y MySQL para una gestión más eficiente de la base de datos.

📌 Características
✔️ FastAPI para la creación de endpoints. ✔️ Integración con SQLAlchemy ORM para modelos de datos estructurados. ✔️ Base de datos MySQL configurada en database.py. ✔️ Operaciones CRUD con persistencia de datos en MySQL. ✔️ Swagger UI para probar los endpoints.

🔗 Acceso a Swagger UI
Para acceder a la documentación interactiva, visita: 👉 http://127.0.0.1:8000/docs

⚙️ Cómo ejecutar el proyecto

1️⃣ Clona el repositorio
bash
git clone https://github.com/NicolasAndresCL/FastAPI.git

cd FastAPI

2️⃣ Instala las dependencias
bash
pip install -r requirements.txt

3️⃣ Configura la base de datos
Asegúrate de tener MySQL instalado.

Modifica database.py para configurar la conexión.

Crea la base de datos con:

sql
CREATE DATABASE fastapi_db;

4️⃣ Ejecutar FastAPI
Puedes iniciar el servidor con:

bash
uvicorn main:app --reload

O bien, puedes agregar este bloque a main.py y ejecutarlo directamente:

python
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000)

🏗️ Estructura del Proyecto
FastAPI/
│── app/
│   ├── db/
│   │   ├── database.py  # Configuración de la conexión con MySQL
│   │   ├── models.py    # Modelos SQLAlchemy
│   ├── routers/
│   │   ├── user.py      # Endpoints para la gestión de usuarios
│   ├── schemas.py       # Definiciones Pydantic
│── main.py              # Archivo principal de la aplicación
│── requirements.txt      # Librerías necesarias
│── README.md            # Documentación

📢 Mejoras recientes
✅ Integración con MySQL usando database.py. ✅ Uso de SQLAlchemy ORM para modelos estructurados. ✅ Persistencia de datos en la base de datos, eliminando la lista en memoria. ✅ Corrección y optimización de rutas en user.py.
