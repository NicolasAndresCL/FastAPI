import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.database import Base, get_db
from app.main import create_app
from app.db import models 

SQLALCHEMY_TEST_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_TEST_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    connection = engine.connect()
    db = TestingSessionLocal(bind=connection)
    
    Base.metadata.create_all(bind=engine)
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)
        connection.close()

@pytest.fixture(scope="function")
def client(db_session):
    app = create_app()

    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client


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