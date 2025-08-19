# Importación de los componentes de Dash necesarios para crear la interfaz y las pestañas
from dash import html, dcc, register_page, callback, Output, Input

# Importamos las dos secciones que forman esta vista:
# - section_characteristics: muestra las tablas con tipos, descripciones y estadísticas
# - section_graphics: muestra todos los gráficos visuales
import pages.sections.section_characteristics as section_characteristics
import pages.sections.section_graphics as section_graphics

# Este archivo representa una página del sistema multipágina de Dash.
# Se registra la ruta "/analisis" como URL para acceder a esta vista.
register_page(__name__, path="/analisis")

# Definición del diseño visual (layout) de esta página
layout = html.Div([

    # Botón que permite volver al inicio. Se representa como un ícono de flecha hacia la izquierda.
    html.Div([
        dcc.Link(
            html.I(className="bi bi-arrow-bar-left fs-2 text-light", title="Volver al inicio"),
            href="/"
        )
    ], className="d-flex justify-content-start mb-2"),  # Alineación del botón a la izquierda

    # Título principal de la sección
    html.H2("ANALISIS DEL CONJUNTO DE DATOS", className="text-center text-danger text-gradient my-4 fw-bold"),

    # Componente de pestañas (Tabs) para separar la interfaz en dos secciones: características y análisis visual
    dcc.Tabs(
        id="tabs",                   # ID que usaremos para identificar el valor de la pestaña activa
        value="tab-1",              # Valor inicial seleccionado
        children=[
            dcc.Tab(
                label="Características y caracterización",  # Texto visible en la pestaña
                value="tab-1",                               # Valor interno para identificarla
                className="tab",                             # Estilo general
                selected_className="tab--selected"           # Estilo cuando está activa
            ),
            dcc.Tab(
                label="Análisis visual",
                value="tab-2",
                className="tab",
                selected_className="tab--selected"
            ),
        ],
        className="mb-4"  # Espaciado inferior
    ),

    # Div contenedor donde se renderizará el contenido dinámico de cada pestaña
    html.Div(id="tabs-content")
])

# Callback de Dash que actualiza el contenido según la pestaña seleccionada
@callback(
    Output("tabs-content", "children"),  # Indicamos que cambiaremos el contenido de este div
    Input("tabs", "value")               # La función se activa cuando cambia el valor de la pestaña activa
)
def render_content(tab):
    # Si se selecciona la pestaña 1, se muestra la tabla con descripciones y estadísticas del dataset
    if tab == "tab-1":
        return section_characteristics.layout()

    # Si se selecciona la pestaña 2, se muestra el análisis visual (gráficos)
    elif tab == "tab-2":
        return section_graphics.layout()
