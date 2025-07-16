import tkinter as tk
import requests

class UsuarioGUI:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ingreso de Usuarios")

        # Etiqueta y campo de texto para el nombre de usuario
        self.etiqueta_usuario = tk.Label(self.ventana, text="Nombre de usuario:")
        self.etiqueta_usuario.grid(column=0, row=0)
        self.campo_usuario = tk.Entry(self.ventana)
        self.campo_usuario.grid(column=1, row=0)

        # Etiqueta y campo de texto para el ID del usuario
        self.etiqueta_id_usuario = tk.Label(self.ventana, text="ID del usuario:")
        self.etiqueta_id_usuario.grid(column=0, row=1)
        self.campo_id_usuario = tk.Entry(self.ventana)
        self.campo_id_usuario.grid(column=1, row=1)

        # Botón para obtener todos los usuarios
        self.boton_obtener_todos = tk.Button(self.ventana, text="Obtener todos los usuarios", command=self.obtener_todos_usuarios)
        self.boton_obtener_todos.grid(column=1, row=2)

        # Botón para obtener un usuario por ID
        self.boton_obtener_por_id = tk.Button(self.ventana, text="Obtener usuario por ID", command=self.obtener_usuario_por_id)
        self.boton_obtener_por_id.grid(column=1, row=3)

        # Mensaje de error
        self.mensaje_error = tk.Label(self.ventana, text="", fg="red")
        self.mensaje_error.grid(column=1, row=4)

        # Cuadro de texto para mostrar resultados
        self.cuadro_resultado = tk.Text(self.ventana, height=15, width=60)
        self.cuadro_resultado.grid(column=0, row=5, columnspan=2, padx=5, pady=5)

    def obtener_todos_usuarios(self):
        self.cuadro_resultado.delete(1.0, tk.END)
        try:
            respuesta = requests.get("http://localhost:8000/user/")
            usuarios = respuesta.json()
            if not usuarios:
                self.mensaje_error.config(text="No hay usuarios registrados")
                return
            self.mensaje_error.config(text="Usuarios obtenidos con éxito")
            for usuario in usuarios:
                texto = (
                    f"ID: {usuario['id']}\n"
                    f"Nombre: {usuario['nombre']}\n"
                    f"Apellido: {usuario['apellido']}\n"
                    f"Dirección: {usuario.get('direccion', '')}\n"
                    f"Teléfono: {usuario.get('telefono', '')}\n"
                    f"Correo: {usuario.get('correo', '')}\n"
                    f"Creación: {usuario.get('creacion', '')}\n"
                    f"Estado: {'Activo' if usuario.get('estado', True) else 'Inactivo'}\n"
                    f"{'-'*40}\n"
                )
                self.cuadro_resultado.insert(tk.END, texto)
        except requests.exceptions.RequestException:
            self.mensaje_error.config(text="Error al obtener usuarios")

    def obtener_usuario_por_id(self):
        self.cuadro_resultado.delete(1.0, tk.END)
        try:
            user_id = int(self.campo_id_usuario.get())
            respuesta = requests.get(f"http://localhost:8000/user/{user_id}")
            if respuesta.status_code == 404:
                self.mensaje_error.config(text="Usuario no encontrado")
                return
            usuario = respuesta.json()
            self.mensaje_error.config(text="Usuario obtenido con éxito")
            texto = (
                f"ID: {usuario['id']}\n"
                f"Nombre: {usuario['nombre']}\n"
                f"Apellido: {usuario['apellido']}\n"
                f"Dirección: {usuario.get('direccion', '')}\n"
                f"Teléfono: {usuario.get('telefono', '')}\n"
                f"Correo: {usuario.get('correo', '')}\n"
                f"Creación: {usuario.get('creacion', '')}\n"
                f"Estado: {'Activo' if usuario.get('estado', True) else 'Inactivo'}\n"
            )
            self.cuadro_resultado.insert(tk.END, texto)
        except ValueError:
            self.mensaje_error.config(text="ID inválido")
        except requests.exceptions.RequestException:
            self.mensaje_error.config(text="Error al obtener usuario")

    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    gui = UsuarioGUI()
    gui.run()
