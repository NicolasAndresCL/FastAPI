
# 🖥️ GUI para consulta de usuarios en FastAPI

Este módulo incluye tres implementaciones de interfaz gráfica desarrolladas en Python puro para consumir endpoints de una API construida con FastAPI. Las interfaces permiten consultar todos los usuarios o uno específico por ID, mostrando los resultados con estructura clara y estilo profesional.

## 🚀 Tecnologías utilizadas
| GUI	 | Framework	    |Dependencias principales   
|:------:|:----------------:|:------------------------:|
|Tkinter |	Python StdLib	|  requests
|PySide6 |  Qt + Python	    |  PySide6, requests
|Flet	 | Flutter + Py	    |  flet, requests

## 📂 Estructura del proyecto
```
gui/
├── main_tkinter.py      # Versión con Tkinter
├── main_pyside6.py      # Versión con PySide6
├── main_flet.py         # Versión con Flet
├── README.md            # Este archivo
```

## 🧪 Funcionalidades compartidas

>✅ Consulta de todos los usuarios (GET /user/)

>✅ Búsqueda de usuario por ID (GET /user/{id})

>🧩 Formato claro del resultado: ID, nombre, apellido, correo, estado…

>💬 Manejo de errores: ID inválido, usuario no encontrado, error de conexión

>🔄 Interfaz interactiva con campos dinámicos y diseño adaptable

## 🖼️ 1. Tkinter
Archivo: main_tkinter.py Características:

- Widgets estándar (Entry, Button, Text)

- Diseño por grid() y lógica procedural

- Ideal para entornos minimalistas o pruebas locales

## 🎨 2. PySide6
Archivo: main_pyside6.py Características:

- Distribución con QVBoxLayout, QTextEdit, QLineEdit

- Visual profesional con estilos personalizados

- Estructura orientada a objetos para escalabilidad

## 🌐 3. Flet
Archivo: main_flet.py Características:

- UI tipo web, reactiva y responsiva

- Layout declarativo con widgets como TextField, ElevatedButton

P- uede ejecutarse como ventana nativa o navegador local

## 🔧 Requisitos por GUI

**Tkinter**
```
bash
pip install requests
```

**PySide6**
```
bash
pip install PySide6 requests
```
**Flet**
```
bash
pip install flet requests
```
## 🧠 Enfoque y propósito

Estas interfaces fueron desarrolladas como parte de un proceso de preparación técnica para entrevistas orientadas al desarrollo backend y data engineering. El objetivo fue simular clientes reales que interactúan con una API, incorporando buenas prácticas en UX, manejo de errores y presentación de resultados.

## 📘 Mejores prácticas aplicadas

>Separación clara de lógica API y visual
>
>Manejo robusto de excepciones HTTP
>
>Tipografía técnica (Consolas) para resultados legibles
>
>Estructura de proyecto fácilmente adaptable a nuevas entidades (productos, compras…)

__🚀 Próximos pasos__
>>Agregar funcionalidades de escritura (POST) desde cada GUI
>>
>>Modularizar la lógica de comunicación con la API
>>
>>Documentar la experiencia en posts técnicos o videos cortos
>>
>>Añadir capturas y demo como parte de tu portafolio técnico