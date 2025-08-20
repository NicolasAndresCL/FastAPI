# tests/conftest.py

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.database import Base, get_db
from app.main import create_app
from app.db import models # Asegúrate de importar tus modelos aquí

# Usamos una base de datos en memoria para los tests
SQLALCHEMY_TEST_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_TEST_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Fixture de la base de datos de prueba.
# Scope="function" garantiza que se ejecute para cada test.
@pytest.fixture(scope="function")
def db_session():
    # Conectarse al motor y crear la sesión
    connection = engine.connect()
    db = TestingSessionLocal(bind=connection)
    
    # Crear todas las tablas en el inicio de la prueba
    Base.metadata.create_all(bind=engine)
    try:
        yield db
    finally:
        db.close()
        # Eliminar todas las tablas al final de la prueba para limpieza
        Base.metadata.drop_all(bind=engine)
        connection.close()

# Fixture para el cliente de prueba de FastAPI
@pytest.fixture(scope="function")
def client(db_session):
    app = create_app()

    # Sobreescribir la dependencia de la base de datos de la app
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    # No es necesario limpiar la base de datos aquí, la fixture db_session ya lo hace.


# Fixture para un usuario "semilla"
@pytest.fixture(scope="function")
def usuario_seed(db_session):
    usuario = models.User(
        nombre="Test",
        apellido="User",
        telefono="999999999",
        correo="test@example.com",
    )
    db_session.add(usuario)
    db_session.commit()
    db_session.refresh(usuario)
    return {"id": usuario.id, "correo": usuario.correo}