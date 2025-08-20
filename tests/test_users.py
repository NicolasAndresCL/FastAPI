def test_crear_usuario(client):
    payload = {
        "nombre": "Nicolás",
        "apellido": "Cano",
        "telefono": "123456789",
        "correo": "nico@example.com"
    }

    response = client.post("/user/", json=payload)
    assert response.status_code in [200, 201]
    data = response.json()
    assert data["correo"] == payload["correo"]


def test_obtener_usuarios(client, usuario_seed):
    response = client.get("/user/")
    assert response.status_code == 200
    usuarios = response.json()
    assert isinstance(usuarios, list)
    assert any(u["correo"] == usuario_seed["correo"] for u in usuarios)


def test_obtener_usuario_por_id(client, usuario_seed):
    user_id = usuario_seed["id"]
    response = client.get(f"/user/{user_id}")
    assert response.status_code == 200
    assert response.json()["correo"] == usuario_seed["correo"]
