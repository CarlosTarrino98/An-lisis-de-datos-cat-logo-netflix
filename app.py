# Importamos las librerías principales de Dash necesarias para construir la aplicación web
import dash  # Librería principal para crear apps web interactivas en Python
import dash_bootstrap_components as dbc  # Permite utilizar estilos y componentes de Bootstrap fácilmente
from dash import dcc, page_container  # dcc contiene componentes como Tabs, Graphs, etc. page_container gestiona las páginas

# Creamos la instancia principal de la aplicación Dash
# - __name__: nombre del módulo actual, necesario para rutas estáticas
# - use_pages=True: habilita la funcionalidad multipágina (carga automática de archivos en la carpeta 'pages')
# - external_stylesheets: aplica un tema visual (Bootstrap "Cyborg" en este caso)
# - suppress_callback_exceptions=True: permite que callbacks funcionen aunque aún no se haya cargado la vista asociada
app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.CYBORG],
    suppress_callback_exceptions=True
)

# Establecemos el título que aparecerá en la pestaña del navegador
app.title = "Netflix Dash"

# Layout global de la aplicación. Se define una estructura básica con un contenedor fluido de Bootstrap
app.layout = dbc.Container([

    # Componente para capturar y manejar la URL (permite cambiar de página sin recargar el navegador)
    dcc.Location(id="url", refresh=False),

    # Este contenedor mostrará dinámicamente la página activa (por ejemplo: home, análisis, etc.)
    page_container

], fluid=True, className="no-padding")  # fluid=True para que ocupe el 100% del ancho de la pantalla

# Punto de entrada de la aplicación
# Esto permite ejecutar el servidor solo cuando el archivo se ejecuta directamente (no cuando se importa)
if __name__ == "__main__":
    app.run(debug=True)  # Modo debug activo: recarga automática y mensajes de error más detallados
