from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTextEdit
)
from PySide6.QtGui import QFont, QColor
import requests
import sys

API_URL = "http://localhost:8000/user"

class UsuarioGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ingreso de Usuarios")
        self.setMinimumWidth(600)

        layout_principal = QVBoxLayout()

        # ID de usuario
        fila_id = QHBoxLayout()
        etiqueta_id = QLabel("ID del usuario:")
        self.campo_id = QLineEdit()
        fila_id.addWidget(etiqueta_id)
        fila_id.addWidget(self.campo_id)
        layout_principal.addLayout(fila_id)

        # Botones
        fila_botones = QHBoxLayout()
        boton_todos = QPushButton("Obtener todos los usuarios")
        boton_todos.clicked.connect(self.obtener_todos_usuarios)
        boton_por_id = QPushButton("Obtener usuario por ID")
        boton_por_id.clicked.connect(self.obtener_usuario_por_id)
        fila_botones.addWidget(boton_todos)
        fila_botones.addWidget(boton_por_id)
        layout_principal.addLayout(fila_botones)

        # Mensaje de error
        self.mensaje_error = QLabel("")
        self.mensaje_error.setStyleSheet("color: red")
        layout_principal.addWidget(self.mensaje_error)

        # Área de resultados
        self.resultado = QTextEdit()
        self.resultado.setFont(QFont("Consolas", 10))
        self.resultado.setReadOnly(True)
        layout_principal.addWidget(self.resultado)

        self.setLayout(layout_principal)

    def obtener_todos_usuarios(self):
        self.resultado.clear()
        try:
            respuesta = requests.get(f"{API_URL}/")
            respuesta.raise_for_status()
            usuarios = respuesta.json()
            if not usuarios:
                self.mensaje_error.setText("No hay usuarios registrados")
                return
            self.mensaje_error.setText("Usuarios obtenidos con éxito")
            for u in usuarios:
                self.resultado.append(self.formatear_usuario(u))
        except requests.exceptions.RequestException:
            self.mensaje_error.setText("Error al obtener usuarios")

    def obtener_usuario_por_id(self):
        self.resultado.clear()
        try:
            user_id = int(self.campo_id.text())
            respuesta = requests.get(f"{API_URL}/{user_id}")
            if respuesta.status_code == 404:
                self.mensaje_error.setText("Usuario no encontrado")
                return
            respuesta.raise_for_status()
            usuario = respuesta.json()
            self.mensaje_error.setText("Usuario obtenido con éxito")
            self.resultado.setText(self.formatear_usuario(usuario))
        except ValueError:
            self.mensaje_error.setText("ID inválido")
        except requests.exceptions.RequestException:
            self.mensaje_error.setText("Error al obtener usuario")

    def formatear_usuario(self, usuario):
        return (
            f"ID: {usuario['id']}\n"
            f"Nombre: {usuario['nombre']}\n"
            f"Apellido: {usuario['apellido']}\n"
            f"Dirección: {usuario.get('direccion', '')}\n"
            f"Teléfono: {usuario.get('telefono', '')}\n"
            f"Correo: {usuario.get('correo', '')}\n"
            f"Creación: {usuario.get('creacion', '')}\n"
            f"Estado: {'Activo' if usuario.get('estado', True) else 'Inactivo'}\n"
            f"{'-'*40}"
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = UsuarioGUI()
    gui.show()
    sys.exit(app.exec())
