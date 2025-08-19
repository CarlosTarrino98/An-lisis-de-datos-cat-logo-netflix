# 🎬 Análisis Interactivo del Catálogo de Netflix con Dash

Este proyecto es una aplicación web desarrollada con Dash (Plotly) que permite analizar visual e interactivamente el catálogo de contenidos de Netflix. Está diseñada para ejecutarse localmente, facilitando su reproducción sin necesidad de configuraciones complejas.

---

## 📁 Estructura del Proyecto

```bash
netflix_dash_analisis/
├── app.py                        # Archivo principal para lanzar la aplicación Dash
├── requirements.txt              # Dependencias necesarias del proyecto
│
├── data/
│   └── netflix.csv               # Dataset con información del catálogo de Netflix
│
├── assets/                       # Archivos estáticos (CSS, JS e imágenes)
│   ├── bootstrap-icons.css
│   ├── custom.css
│   ├── custom.js
│   └── images/
│       ├── netflix.png
│       └── portada.jpg
│
├── pages/                        # Estructura de páginas y secciones de la app
│   ├── home.py                   # Página principal
│   ├── analysis.py               # Página con las pestañas de características y gráficos
│   └── sections/                 # Carpeta que agrupa scripts para gráficos y limpieza
│       ├── __init__.py
│       ├── data_loader.py        # Limpieza y carga del dataset
│       ├── figures.py            # Definición de todos los gráficos
│       ├── section_characteristics.py  # Vista para características del dataset
│       └── section_graphics.py   # Vista para el análisis gráfico
```

---

## ✅ Requisitos

- **Python 3.9+**
- **PyCharm** (con la versión Community es suficiente)
- Sistema operativo Windows u otro compatible

---

## ⚙️ Instalación y ejecución

1. **Descomprime** el archivo `.zip` del proyecto.
2. Abre la carpeta `netflix_dash_analisis` con **PyCharm** en un nuevo proyecto.
3. Abre la terminal en pycharm y situate en el directorio del proyecto:

```bash
cd C:\tu\ruta\a\netflix_dash_analisis
```

4. Crea y activa un entorno virtual (por ejemplo, llamado .venv).

```bash
python -m venv .venv
```

6. Activa el entorno virtual:

```bash
.venv\Scripts\activate 
```

7. Instala todas las librerías necesarias:

```bash
pip install -r requirements.txt
```

8. Comprueba que todo está bien

```bash
pip list
```

9. Lanza la aplicación desde `app.py`:

```bash
python app.py
```

10. Abre tu navegador y accede a: [http://127.0.0.1:8050](http://127.0.0.1:8050)

---