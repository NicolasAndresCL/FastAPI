from fastapi.testclient import TestClient
from app.main import app  # Asegurate de importar tu instancia FastAPI

client = TestClient(app)

def test_crear_usuario():
    payload = {
        "nombre": "Nicolás",
        "apellido": "Cano",
        "telefono": "123456789",
        "correo": "nico@example.com",
        "password": "segura123"
    }

    response = client.post("/user/", json=payload)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200  # o 201 si usás ese código
    assert response.json()["correo"] == "nico@example.com"

def test_obtener_usuarios(client, test_db):
    response = client.get("/user/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_obtener_usuario_por_id(client, test_db, usuario_seed):
    response = client.get(f"/user/{usuario_seed['id']}")
    assert response.status_code == 200
    assert response.json()["correo"] == usuario_seed["correo"]
