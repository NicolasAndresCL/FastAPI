# Para acceder al Swagger UI ir a localhost http://127.0.0.1:8000/docs

# Dos formas de ejecutar fastapi
    1. uvicorn main:app
    2. Agregar el siguiente bloque de codigo:

    if __name__ == "__main__":
        uvicorn.run("main:app", port=8000)

    Y luego correr main.py

# CRUD básico
    