# Importamos los módulos necesarios de Dash
from dash import html, dcc, register_page

# Registramos esta página dentro del sistema multipágina de Dash
# Al establecer path="/" se convierte en la página inicial (home)
register_page(__name__, path="/")

# Definimos la estructura (layout) que se mostrará en la página de inicio
layout = html.Div([
    # Contenedor de pantalla completa con fondo personalizado
    html.Div([

        # Contenedor centrado con estilos flexbox para centrar vertical y horizontalmente
        html.Div([

            # Título grande con clase CSS personalizada (estilo Netflix)
            html.H1("NETFLIX", className="text-center text-danger titulo-netflix"),

            # Subtítulo explicando brevemente el propósito de la app
            html.H4("Análisis visual del conjunto de datos", className="text-center text-body-tertiary mb-4 fw-bold"),

            # Frase secundaria en cursiva como introducción
            html.P("Catálogo de películas y series", className="text-secondary fst-italic mb-3"),

            # Enlace que lleva a la página de análisis (/analisis)
            # Se muestra como un ícono personalizado animado en forma de gráfico circular
            dcc.Link(
                html.Img(
                    src="/assets/images/netflix.png",      # Ruta de la imagen del botón
                    height="50px",
                    title="Pulsar para comenzar",          # Tooltip al pasar el ratón
                    className="bi bi-pie-chart-fill icon-analisis my-4"  # Estilo animado personalizado
                ),
                href="/analisis"  # Página de destino
            ),

            # Autor del proyecto (tu nombre)
            html.Small(
                "Carlos Tarriño Espinosa",
                className="text-secondary text-center mt-4"
            ),

        ], className="container d-flex flex-column justify-content-center align-items-center h-100")  # Centrado total del contenido
    ], className="vh-100 p-0", id="hero")  # Fondo de pantalla completa con ID usado en CSS
])
