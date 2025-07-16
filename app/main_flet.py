import flet as ft
import requests

API_URL = "http://localhost:8000/user"

def main(page: ft.Page):
    page.title = "Panel de Usuarios FastAPI"
    page.scroll = "adaptive"
    page.theme_mode = "light"
    page.window_width = 800

    mensaje = ft.Text(color=ft.Colors.RED)

    input_id = ft.TextField(label="ID del Usuario", width=200)

    resultado = ft.TextField(
        multiline=True,
        min_lines=10,
        max_lines=20,
        label="Resultado",
        read_only=True,
        expand=True,
        text_style=ft.TextStyle(font_family="Consolas")
    )

    def mostrar_usuarios():
        resultado.value = ""
        mensaje.value = ""
        try:
            r = requests.get(f"{API_URL}/")
            r.raise_for_status()
            usuarios = r.json()
            if not usuarios:
                mensaje.value = "No hay usuarios registrados"
                return
            for u in usuarios:
                resultado.value += (
                    f"ID: {u['id']}\n"
                    f"Nombre: {u['nombre']}\n"
                    f"Apellido: {u['apellido']}\n"
                    f"Correo: {u.get('correo','')}\n"
                    f"Estado: {'Activo' if u.get('estado', True) else 'Inactivo'}\n"
                    f"{'-'*40}\n"
                )
        except Exception as e:
            mensaje.value = f"Error al obtener usuarios: {e}"
        page.update()

    def buscar_por_id(e):
        resultado.value = ""
        mensaje.value = ""
        try:
            user_id = int(input_id.value.strip())
            r = requests.get(f"{API_URL}/{user_id}")
            if r.status_code == 404:
                mensaje.value = "Usuario no encontrado"
                return
            r.raise_for_status()
            u = r.json()
            resultado.value = (
                f"ID: {u['id']}\n"
                f"Nombre: {u['nombre']}\n"
                f"Apellido: {u['apellido']}\n"
                f"Correo: {u.get('correo','')}\n"
                f"Estado: {'Activo' if u.get('estado', True) else 'Inactivo'}\n"
            )
        except ValueError:
            mensaje.value = "ID inválido"
        except Exception as e:
            mensaje.value = f"Error: {e}"
        page.update()

    botones = ft.Row([
        ft.ElevatedButton("Obtener todos los usuarios", on_click=lambda e: mostrar_usuarios()),
        ft.ElevatedButton("Buscar por ID", on_click=buscar_por_id)
    ])

    page.add(
        ft.Row([input_id, botones], vertical_alignment=ft.CrossAxisAlignment.CENTER),
        mensaje,
        resultado
    )

ft.app(target=main)
