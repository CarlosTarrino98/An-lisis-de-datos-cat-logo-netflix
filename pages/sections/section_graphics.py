# Importación de componentes esenciales de Dash para diseño y callbacks
from dash import dcc, html, callback, Input, Output, State

# Importación de funciones de gráficos desde figures.py
from pages.sections.figures import *
import dash_bootstrap_components as dbc

# Importación específica de un gráfico que necesita interacción con radio buttons
from pages.sections.figures import get_bar_plot_by_period



def layout():
    return html.Div([
        # Índice de navegación
        html.Div([
            html.H5("Índice", className="text-center text-gradient my-3"),

            html.Div(
                className="container w-75",
                children=html.Div(
                    className="row justify-content-center",
                    children=[
                        # Primera columna del índice
                        html.Div(
                            className="col-md-4 text-center",
                            children=html.Ul([
                                html.Li(
                                    html.A("Comparativa de Películas y Series", href="#grafico1", className="indice-link"),
                                    className="mb-2"
                                ),
                                html.Li(
                                    html.A("Distribución de Calificaciones", href="#grafico2", className="indice-link"),
                                    className="mb-2"
                                ),

                                html.Li(
                                    html.A("Heatmap de Tipo de Contenido y Clasificaciones", href="#grafico3", className="indice-link"),
                                    className="mb-2"
                                ),
                                html.Li(
                                    html.A("Cantidad de Estrenos por fecha", href="#grafico4", className="indice-link"),
                                    className="mb-2"
                                ),
                            ], className="list-unstyled")
                        ),
                        # Segunda columna del índice
                        html.Div(
                            className="col-md-4 text-center",
                            children=html.Ul([
                                html.Li(
                                    html.A("Cantidad de Agregados por año", href="#grafico5", className="indice-link"),
                                    className="mb-2"
                                ),
                                html.Li(
                                    html.A("Duración de Películas y Series", href="#grafico6", className="indice-link"),
                                    className="mb-2"
                                ),
                                html.Li(
                                    html.A("Distribución Geográfica del Contenido", href="#grafico8", className="indice-link"),
                                    className="mb-2"
                                ),
                                html.Li(
                                    html.A("Evolución Temporal del Contenido por País", href="#grafico9", className="indice-link"),
                                    className="mb-2"
                                ),
                            ], className="list-unstyled")
                        ),
                        # Tercera columna del índice
                        html.Div(
                            className="col-md-4 text-center",
                            children=html.Ul([
                                html.Li(
                                    html.A("Distribución del Contenido por Género", href="#grafico10", className="indice-link"),
                                    className="mb-2"
                                ),
                                html.Li(
                                    html.A("Género Predominante por País", href="#grafico11", className="indice-link"),
                                    className="mb-2"
                                ),
                                html.Li(
                                    html.A("Actores y Directores más Frecuentes", href="#grafico12", className="indice-link"),
                                    className="mb-2"
                                ),
                                html.Li(
                                    html.A("Relación entre Directores, Géneros y Actores", href="#grafico13", className="indice-link"),
                                    className="mb-2"
                                ),
                            ], className="list-unstyled")
                        ),
                    ]
                )
            )
        ], className="mb-5"),

        # 1 y 2. Comparativa de Películas y Series y Distribución de Calificaciones
        dbc.Row([
            dbc.Col(
                html.Div([
                    # Título del gráfico
                    html.H5("Comparativa de Películas y Series", className="text-center text-danger my-4", id="grafico1"),
                    # Descripción del gráfico
                    html.P(
                        "Proporción de películas y series disponibles en el catálogo de Netflix.",
                        className="text-body-secondary text-center mb-3"
                    ),
                    # Gráfico
                    dcc.Graph(figure=get_pie_chart_type()),

                    # Botón para mostrar la interpretación del gráfico
                    dbc.Button("Ver interpretación", id="btn-explica-1", color="danger", className="mt-2"),
                    dbc.Collapse(
                        dbc.Card(
                            dbc.CardBody(
                                html.P(
                                    "Se observa que las películas representan aproximadamente el 70% del catálogo, mientras que las series abarcan el 30% restante. "
                                    "Esto indica que Netflix prioriza el contenido cinematográfico, aunque también mantiene una oferta sólida de series para fidelizar a largo plazo."
                                ), className="mx-3 my-2" , style={"textAlign": "justify"}
                            )
                        ),
                        id="collapse-explica-1",
                        is_open=False,
                        className="mt-2"
                    )
                ]),
                width=6
            ),
            dbc.Col(
                html.Div([
                    html.H5("Distribución de Calificaciones", className="text-center text-danger my-4", id="grafico2"),
                    html.P(
                        "Distribución de las clasificaciones de edad del contenido disponible en Netflix.",
                        className="text-body-secondary text-center mb-3"
                    ),
                    dcc.Graph(figure=get_bubble_chart_rating()),

                    dbc.Button("Ver interpretación", id="btn-explica-2", color="danger", className="mt-2"),
                    dbc.Collapse(
                        dbc.Card(
                            dbc.CardBody(
                                html.P(
                                    "Se aprecia que la mayoría del contenido se concentra en las clasificaciones TV-MA y TV-14, dirigidas a una audiencia adolescente y adulta. "
                                    "Esto indica una oferta predominante de contenido con temáticas maduras. Las clasificaciones familiares como PG, TV-Y o TV-G aparecen con menor frecuencia, "
                                    "sugiriendo que el contenido infantil no es el foco principal del catálogo."
                                ), className="mx-3 my-2" , style={"textAlign": "justify"}
                            )
                        ),
                        id="collapse-explica-2",
                        is_open=False,
                        className="mt-2"
                    )
                ]),
                width=6
            ),
        ], className="mb-5 mx-5 scroll-section"),

        # 3. Heatmap tipo vs clasificación
        dbc.Row([
            dbc.Col(
                html.Div([
                    html.H5("Heatmap de Tipo de Contenido y Clasificaciones", className="text-center text-danger my-4",
                            id="grafico3"),
                    html.P(
                        "Análisis cruzado entre tipo de contenido y su clasificación por edad.",
                        className="text-body-secondary text-center mb-3"
                    ),
                    dcc.Graph(figure=get_heatmap_type_rating()),

                    dbc.Button("Ver interpretación", id="btn-explica-3", color="danger", className="mt-2"),
                    dbc.Collapse(
                        dbc.Card(
                            dbc.CardBody(
                                html.P(
                                    "Aunque en ambos tipos de contenido predominan las clasificaciones TV-MA y TV-14, "
                                    "se aprecia una mayor diversidad de clasificaciones en las películas. Las películas están "
                                    "distribuidas en una gama más amplia de categorías, incluyendo desde contenidos infantiles "
                                    "(G, PG) hasta clasificaciones restringidas (NC-17, UR, NR). En cambio, las series se concentran "
                                    "casi exclusivamente en público adolescente y adulto, con muy poca presencia en clasificaciones más familiares. "
                                    "Esto sugiere que Netflix utiliza el formato película para cubrir un espectro más amplio de audiencias, "
                                    "mientras que las series se enfocan principalmente en temáticas maduras y complejas, posiblemente debido "
                                    "a su capacidad de desarrollar tramas largas dirigidas a un público más específico."
                                ), className="mx-3 my-2" , style={"textAlign": "justify"}
                            )
                        ),
                        id="collapse-explica-3",
                        is_open=False,
                        className="mt-2"
                    )
                ]),
                width=12
            )
        ], className="mb-5 mx-5 scroll-section"),

        # 4. Cantidad de Estrenos por fecha
        dbc.Row([
            dbc.Col(
                html.Div([
                    html.H5("Cantidad de Estrenos por fecha", className="text-center text-danger my-4", id="grafico4"),
                    html.P(
                        "Distribución de los títulos del catálogo de Netflix según su fecha de lanzamiento original.",
                        className="text-body-secondary text-center mb-3"
                    ),

                    # Selector para elegir periodo: año, mes o día
                    dcc.RadioItems(
                        id="radioItems-periodo",
                        options=[
                            {"label": "Año", "value": "año"},
                            {"label": "Mes", "value": "mes"},
                            {"label": "Día de la semana", "value": "día"}
                        ],
                        value="año", # Valor por defecto
                        labelStyle={"display": "inline-block", "margin": "0 15px"},
                        inputStyle={"margin-right": "5px"},
                        className="text-center text-body-secondary mb-4 custom-radio-group"
                    ),

                    # El gráfico cambiará dinámicamente según la opción seleccionada
                    dcc.Graph(id="grafico-periodo"),

                    dbc.Button("Ver interpretación", id="btn-explica-4", color="danger", className="mt-2"),
                    dbc.Collapse(
                        dbc.Card(
                            dbc.CardBody([
                                html.P(
                                    "El número de estrenos por año muestra una clara tendencia ascendente desde los años 90, con un crecimiento especialmente marcado a partir del 2000. Esto refleja no solo la evolución de la industria audiovisual, sino también la inclusión en el catálogo de Netflix de producciones más recientes y actuales en comparación con obras más antiguas, que son menos frecuentes."),
                                html.P(
                                    "En términos mensuales, la distribución de estrenos es bastante homogénea, aunque destacan los meses de julio y diciembre como los más representados. Esto podría deberse a que muchas producciones tienden a estrenarse en verano o a finales de año, coincidiendo con periodos de mayor consumo de entretenimiento a nivel global."),
                                html.P(
                                    "Por días de la semana, los datos revelan que la mayoría de los estrenos originales se concentraron en viernes, lo cual es coherente con las prácticas tradicionales de la industria cinematográfica y televisiva, que aprovechan el inicio del fin de semana para maximizar la audiencia. Lunes y domingos, en cambio, son los días con menor número de estrenos."),

                            ], className="mx-3 my-2" , style={"textAlign": "justify"})
                        ),
                        id="collapse-explica-4",
                        is_open=False,
                        className="mt-2"
                    )
                ]),
                width=12
            )
        ], className="mb-5 mx-5 scroll-section"),

        # 5. Cantidad de Agregados por año
        dbc.Row([
            dbc.Col(
                html.Div([
                    html.H5("Cantidad de Agregados por año", className="text-center text-danger my-4", id="grafico5"),
                    html.P(
                        "Evolución de la cantidad de contenidos agregados a Netflix a lo largo de los años.",
                        className="text-body-secondary text-center mb-3"
                    ),
                    dcc.Graph(figure=get_line_chart_date_added()),

                    dbc.Button("Ver interpretación", id="btn-explica-5", color="danger", className="mt-2"),
                    dbc.Collapse(
                        dbc.Card(
                            dbc.CardBody([
                                html.P(
                                    "El número de contenidos agregados a Netflix por año muestra un crecimiento sostenido desde 2014, con un incremento muy notable a partir de 2015. Esta tendencia refleja una fuerte estrategia de expansión por parte de la plataforma, que intensificó significativamente su producción y adquisición de contenido en esos años."),
                                html.P(
                                    "El pico de contenidos agregados se observa en 2019, con aproximadamente 2000 incorporaciones. A partir de ese año, se evidencia una leve disminución, posiblemente atribuida a factores como la saturación del catálogo, cambios en la estrategia de contenido o el impacto inicial de la pandemia en las producciones del año siguiente."),
                                html.P(
                                    "Antes de 2015, la cantidad de agregados anuales era muy baja, lo que indica que Netflix aún no había adoptado su modelo actual de producción y distribución intensiva. El salto exponencial posterior marca el periodo en el que la plataforma se consolidó como líder global del streaming.")
                            ], className="mx-3 my-2" , style={"textAlign": "justify"})
                        ),
                        id="collapse-explica-5",
                        is_open=False,
                        className="mt-2"
                    )
                ]),
                width=12
            )
        ], className="mb-5 mx-5 scroll-section"),

        # 6 y 7. Duración de películas y series
        dbc.Row([
            dbc.Col(
                html.Div([
                    html.H5("Duración de Películas", className="text-center text-danger my-4",
                            id="grafico6"),
                    html.P(
                        "Análisis de la duración de las películas disponibles en Netflix.",
                        className="text-body-secondary text-center mb-3"
                    ),
                    dcc.Graph(figure=get_histogram_duration_movies()),

                    dbc.Button("Ver interpretación", id="btn-explica-6", color="danger", className="mt-2"),
                    dbc.Collapse(
                        dbc.Card(
                            dbc.CardBody([
                                html.P(
                                    "La duración de las películas disponibles en Netflix presenta una distribución centrada principalmente entre los 80 y 120 minutos, con un pico notable alrededor de los 100 minutos. Esto indica que la mayoría de los filmes se ajustan a la duración estándar del cine comercial, favoreciendo una experiencia cómoda y predecible para el espectador."),
                                html.P(
                                    "El gráfico también muestra una menor proporción de películas con duraciones inferiores a los 60 minutos o superiores a los 150, lo que sugiere que los contenidos extremos en duración —como cortometrajes o películas muy extensas— son menos comunes en el catálogo."),
                                html.P(
                                    "La forma de la distribución tiene una ligera simetría con una caída gradual en ambos extremos, lo que reafirma que la plataforma prioriza la producción y adquisición de películas dentro de una duración convencional.")
                            ], className="mx-3 my-2" , style={"textAlign": "justify"})
                        ),
                        id="collapse-explica-6",
                        is_open=False,
                        className="mt-2"
                    )
                ]),
                width=6
            ),
            dbc.Col(
                html.Div([
                    html.H5("Duración de Series", className="text-center text-danger my-4",
                            id="grafico7"),
                    html.P(
                        "Análisis de la duración de las series presentes en Netflix.",
                        className="text-body-secondary text-center mb-3"
                    ),
                    dcc.Graph(figure=get_histogram_duration_series()),

                    dbc.Button("Ver interpretación", id="btn-explica-7", color="danger", className="mt-2"),
                    dbc.Collapse(
                        dbc.Card(
                            dbc.CardBody([
                                html.P(
                                    "En el caso de las series, la mayoría cuenta con solo 1 temporada, evidenciando una clara preferencia por formatos de corta duración como miniseries o series limitadas. Este tipo de contenido permite un consumo rápido y se adapta a los hábitos modernos de visualización por streaming."),
                                html.P(
                                    "A partir de las 3 temporadas, la cantidad de series disminuye drásticamente, siendo escasas aquellas que superan las 5 temporadas. Esto podría reflejar una política editorial enfocada en renovar contenidos basándose en métricas de rendimiento o simplemente la naturaleza cambiante del catálogo."),
                                html.P(
                                    "El gráfico muestra una distribución claramente sesgada hacia la izquierda, donde las series largas son una minoría, lo que puede responder a la intención de Netflix de diversificar su oferta con historias breves y fáciles de consumir.")
                            ], className="mx-3 my-2" , style={"textAlign": "justify"})

                        ),
                        id="collapse-explica-7",
                        is_open=False,
                        className="mt-2"
                    )
                ]),
                width=6
            ),
        ], className="mb-5 mx-5 scroll-section"),

        # 8. Contenidos por país
        dbc.Row([
            dbc.Col(
                html.Div([
                    html.H5("Distribución Geográfica del Contenido", className="text-center text-danger my-4", id="grafico8"),
                    html.P(
                        "Análisis de los países que más contenidos aportan al catálogo de Netflix.",
                        className="text-body-secondary text-center mb-3"
                    ),
                    dcc.Graph(figure=get_bar_chart_country()),

                    dbc.Button("Ver interpretación", id="btn-explica-8", color="danger", className="mt-2"),
                    dbc.Collapse(
                        dbc.Card(
                            dbc.CardBody([
                                html.P(
                                    "Estados Unidos lidera con amplia diferencia el número de contenidos disponibles en Netflix, aportando más de 3500 títulos. Esto refleja no solo la magnitud de su industria audiovisual, sino también el origen estadounidense de la propia plataforma, que naturalmente prioriza la inclusión de producciones locales."),
                                html.P(
                                    "India ocupa el segundo lugar con más de 1000 títulos, lo que confirma el creciente protagonismo del cine y la televisión indios en el catálogo global de Netflix. Esta tendencia puede estar influida por el enorme mercado de usuarios en ese país y la fuerte producción nacional."),
                                html.P(
                                    "Otros países con una presencia significativa incluyen Reino Unido, Canadá, Francia, Japón, España y Corea del Sur, lo que evidencia una apuesta de Netflix por la diversidad internacional. Por otro lado, países como Argentina, Nigeria, Hong Kong(*) o Turquía aportan un volumen menor de títulos, pero contribuyen al componente multicultural de la plataforma."),

                                html.Small("* Aunque Hong Kong es tratado en el conjunto de datos como un país, en realidad es una Región Administrativa Especial de China.", className="text-muted")
                            ], className="mx-3 my-2" , style={"textAlign": "justify"})

                        ),
                        id="collapse-explica-8",
                        is_open=False,
                        className="mt-2"
                    )
                ]),
                width=12
            )
        ], className="mb-5 mx-5 scroll-section"),

        # 9. Evolución Temporal del Contenido por País
        dbc.Row([
            dbc.Col(
                html.Div([
                    html.H5(
                        "Evolución Temporal del Contenido por País", className="text-center text-danger my-4", id="grafico9"
                    ),
                    html.P(
                        "Visualización animada que representa la evolución temporal de la incorporación de nuevos contenidos al catálogo de Netflix en los distintos países.",
                        className="text-body-secondary text-center mb-3"
                    ),
                    html.Div(
                        dcc.Graph(figure=get_animated_choropleth_map(),style={"width": "80%", "height": "80vh"}),
                        style={"display": "flex", "justifyContent": "center"}
                    ),

                    dbc.Button("Ver interpretación", id="btn-explica-9", color="danger", className="mt-2"),
                    dbc.Collapse(
                        dbc.Card(
                            dbc.CardBody([
                                html.P(
                                    "La visualización muestra una evolución clara en la distribución geográfica de los contenidos agregados a Netflix entre 2008 y 2021. En los primeros años (2008-2014), Estados Unidos domina casi por completo la producción y el aporte de contenido al catálogo, reflejando el origen y la estrategia inicial centrada en producciones locales."),
                                html.P(
                                    "A partir de 2015 comienza a observarse una expansión progresiva hacia otros países como Canadá, Reino Unido, Francia y Japón. Esta diversificación marca el inicio de una estrategia más global por parte de Netflix, orientada a atraer públicos internacionales mediante la inclusión de contenido regional."),
                                html.P(
                                    "Desde 2016 hasta 2021 se evidencia un crecimiento significativo en países como India y Corea del Sur, que se convierten en factores clave dentro del ecosistema de contenidos. Este cambio refleja tanto la inversión directa de Netflix en producciones originales locales como la adquisición de derechos de distribución de contenidos populares en dichos mercados."),
                                html.P(
                                    "En resumen, la evolución temporal del contenido por país no solo evidencia la expansión global de Netflix, sino también su adaptación cultural, apostando por la producción local y el consumo personalizado en función de las audiencias regionales.")
                            ], className="mx-3 my-2" , style={"textAlign": "justify"})
                        ),
                        id="collapse-explica-9",
                        is_open=False,
                        className="mt-2"
                    )
                ],style={"width": "100%"}),
                width=12
            )
        ], className="mb-5 mx-5 scroll-section"),

        # 10. Distribución del Contenido por Género
        dbc.Row([
            dbc.Col(
                html.Div([
                    html.H5("Distribución del Contenido por Género", className="text-center text-danger my-4", id="grafico10"),
                    html.P(
                        "Análisis de los géneros más comunes en el catálogo de Netflix.",
                        className="text-body-secondary text-center mb-3"
                    ),
                    dcc.Graph(figure=get_treemap_genres()),

                    dbc.Button("Ver interpretación", id="btn-explica-10", color="danger", className="mt-2"),
                    dbc.Collapse(
                        dbc.Card(
                            dbc.CardBody([
                                html.P(
                                    "El género más representado en el catálogo de Netflix es 'International Movies', lo que destaca el enfoque global de la plataforma al ofrecer cine de múltiples regiones y culturas. Esto refuerza la estrategia de Netflix de atraer audiencias internacionales mediante producciones locales."),
                                html.P(
                                    "Los géneros 'Dramas', 'Comedies' e 'International TV Shows' también ocupan una porción significativa, lo cual refleja una combinación de contenido emocional, entretenimiento ligero y diversidad cultural. Esta mezcla permite satisfacer una amplia gama de gustos y preferencias."),
                                html.P(
                                    "Géneros como 'Documentaries', 'Action & Adventure', 'Romantic Movies' y 'Crime TV Shows' muestran una notable presencia, lo que evidencia la variedad temática del catálogo. En contraste, categorías más específicas como 'Anime Features', 'TV Mysteries', 'TV Horror' o 'Cult Movies' presentan menor volumen, aunque conservan un nicho importante dentro de la oferta de contenido."),
                                html.P(
                                    "En resumen, la distribución por géneros refleja una estrategia de Netflix orientada a la diversidad, con una fuerte presencia internacional y un balance entre entretenimiento generalista y nichos culturales específicos.")
                            ], className="mx-3 my-2" , style={"textAlign": "justify"})
                        ),
                        id="collapse-explica-10",
                        is_open=False,
                        className="mt-2"
                    )
                ]),
                width=12
            )
        ], className="mb-5 mx-5 scroll-section"),

        # 11. Género predominante por país
        dbc.Row([
            dbc.Col(
                html.Div([
                    html.H5(
                        "Género predominante por país",
                        className="text-center text-danger my-4",
                        id="grafico11"
                    ),
                    html.P(
                        "Mapa que analiza el género predominante en cada país y la cantidad de contenidos que lo representan.",
                        className="text-body-secondary text-center mb-3"
                    ),
                    html.Div(
                        dcc.Graph(
                            figure=get_choropleth_dominant_genre(),
                            style={"width": "80%", "height": "80vh"}
                        ),
                        style={"display": "flex", "justifyContent": "center"}
                    ),

                    dbc.Button("Ver interpretación", id="btn-explica-11", color="danger", className="mt-2"),
                    dbc.Collapse(
                        dbc.Card(
                            dbc.CardBody([
                                html.P(
                                    "Además de la distribución general de géneros, observar qué tipo de contenido predomina en cada país permite comprender mejor las preferencias culturales y cómo Netflix adapta su catálogo según el mercado. Esta perspectiva geográfica-cultural ofrece una visión profunda del alcance global de la plataforma."),

                                html.P(
                                    "'International Movies' se posiciona como el género más representado en una amplia variedad de países, incluyendo gran parte de América Latina, Europa, Asia y África. Esta predominancia evidencia la estrategia de Netflix de ofrecer un catálogo diverso, adaptado a públicos que valoran producciones extranjeras y multilingües, especialmente en regiones donde la producción local no tiene aún una presencia mayoritaria."),

                                html.P(
                                    "Por otro lado, el género 'Dramas' predomina en países como Estados Unidos, Australia, Egipto, Grecia y varias regiones de Europa del Este y África. Esta preferencia por narrativas intensas y personales refleja un consumo más tradicional del entretenimiento, centrado en historias profundas y de carácter emocional o histórico."),

                                html.P(
                                    "La distribución del género más visto por país refleja no solo diferencias culturales en el consumo de entretenimiento, sino también la capacidad de Netflix para adaptar su catálogo y destacar tipos de contenido según los gustos locales. Esta flexibilidad en la curaduría de su oferta permite a la plataforma consolidarse como un referente global del entretenimiento personalizado.")
                            ], className="mx-3 my-2" , style={"textAlign": "justify"})
                        ),
                        id="collapse-explica-11",
                        is_open=False,
                        className="mt-2"
                    )
                ]),
                width=12
            )
        ], className="mb-5 mx-5 scroll-section"),

        # 12 y 13. Actores y directores más frecuentes
        dbc.Row([
            html.H5("Actores y directores más frecuentes", className="text-center text-danger my-4", id="grafico12"),
            html.P(
                "Cantidad de apariciones de los actores y directores más destacados.",
                className="text-body-secondary text-center mb-3"
            ),

            dbc.Col(
                html.Div([
                    dcc.Graph(figure=get_bar_chart_top_actors()),

                    dbc.Button("Ver interpretación", id="btn-explica-12", color="danger", className="mt-2"),
                    dbc.Collapse(
                        dbc.Card(
                            dbc.CardBody([
                                html.P(
                                    "El análisis de los actores más frecuentes en el catálogo de Netflix revela un claro dominio de intérpretes indios. Encabeza la lista Anupam Kher con más de 40 apariciones, seguido por Shah Rukh Khan, Julie Tejwani y otros referentes del cine de la India. Esto refleja el peso significativo de Bollywood dentro de la plataforma, así como la fuerte demanda de producciones del sur de Asia."),
                                html.P(
                                    "Además, también aparecen actores japoneses y estadounidenses como Takahiro Sakurai o Samuel L. Jackson, lo que indica una presencia multicultural aunque claramente liderada por el mercado indio.")
                            ], className="mx-3 my-2" , style={"textAlign": "justify"})
                        ),
                        id="collapse-explica-12",
                        is_open=False,
                        className="mt-2"
                    )
                ]),
                width=6
            ),
            dbc.Col(
                html.Div([
                    dcc.Graph(figure=get_bar_chart_top_directors()),

                    dbc.Button("Ver interpretación", id="btn-explica-13", color="danger", className="mt-2"),
                    dbc.Collapse(
                        dbc.Card(
                            dbc.CardBody([
                                html.P(
                                    "En cuanto a los directores, el liderazgo lo ocupa Rajiv Chilaka, conocido por dirigir animaciones infantiles, seguido muy de cerca por Jan Suter y Raúl Campos, quienes han trabajado en documentales y comedias mexicanas. Esta tendencia sugiere un gran volumen de producciones animadas y regionales dentro del catálogo."),
                                html.P(
                                    "Aunque también se encuentran figuras icónicas como Steven Spielberg o Martin Scorsese, su presencia es menor en comparación, lo que indica que la recurrencia no está necesariamente ligada al prestigio, sino al volumen de obras disponibles en la plataforma.")
                            ], className="mx-3 my-2" , style={"textAlign": "justify"})
                        ),
                        id="collapse-explica-13",
                        is_open=False,
                        className="mt-2"
                    )
                ]),
                width=6
            )
        ], className="mb-5 ms-3 scroll-section"),

        # 13. Sunburst Chart: Director → Género → Actor
        dbc.Row([
            dbc.Col(
                html.Div([
                    html.H5("Relación entre Directores, Géneros y Actores", className="text-center text-danger my-4", id="grafico13"),
                    html.P(
                        "Este gráfico sunburst muestra la relación jerárquica entre los 5 directores más frecuentes, "
                        "sus 3 géneros principales y los 2 actores más comunes en cada caso, "
                        "usando solo combinaciones con todos los datos disponibles. "
                        "Representa las colaboraciones más frecuentes de forma visual y estructurada..",
                        className="text-body-secondary text-center mb-3"
                    ),
                    dcc.Graph(figure=get_sunburst_director_genre_actor(),style={"height": "70vh", "width": "100%"}),

                    dbc.Button("Ver interpretación", id="btn-explica-14", color="danger", className="mt-2"),
                    dbc.Collapse(
                        dbc.Card(
                            dbc.CardBody([
                                html.P(
                                    "Este gráfico Sunburst ofrece una visión estructurada de las combinaciones más frecuentes entre cinco directores presentes en Netflix, sus géneros predominantes y los actores con los que más han colaborado. Permite entender las conexiones clave dentro del catálogo en términos de producción y reparto."),

                                html.P(
                                    "Por ejemplo, David Dhawan colabora principalmente en géneros como 'International Movies' y 'Comedies', destacando actores recurrentes como Anupam Kher y Salman Khan. Por otro lado, Cathy Garcia-Molina se asocia especialmente con 'Dramas' e 'International Movies', junto a actores como John Lloyd Cruz y Joross Gamboa."),

                                html.P(
                                    "También se observa cómo grandes nombres como Steven Spielberg o Martin Scorsese están vinculados con géneros clásicos o documentales, reforzando su perfil más tradicional o autoral. Incluso aparecen casos curiosos como el de Bob Dylan o Allen Ginsberg en el apartado documental, lo que muestra la variedad de estilos presentes."),

                                html.P(
                                    "En definitiva, este gráfico ilustra cómo ciertos directores han construido relaciones recurrentes con actores específicos dentro de géneros determinados, creando patrones de colaboración que forman parte del ADN del catálogo de Netflix.")
                            ], className="mx-3 my-2" , style={"textAlign": "justify"})
                        ),
                        id="collapse-explica-14",
                        is_open=False,
                        className="mt-2"
                    )
                ]),
                width=12
            )
        ], className="mb-5 mx-5 scroll-section"),

    ])

# Callback para actualizar el gráfico según el periodo seleccionado, se ejecuta cuando el usuario selecciona "Año", "Mes" o "Día" en los radio buttons
@callback(
    Output("grafico-periodo", "figure"),               # El gráfico que se actualizará
    Input("radioItems-periodo", "value")               # La entrada es el valor seleccionado del RadioItems
)
def actualizar_grafico(periodo):
    # Llama a una función que genera el gráfico correspondiente según el periodo elegido
    return get_bar_plot_by_period(periodo)

@callback(
    Output("collapse-explica-1", "is_open"),           # Controla si el panel colapsable está abierto
    Output("btn-explica-1", "children"),               # Cambia el texto del botón
    Input("btn-explica-1", "n_clicks"),                # Cuando se hace clic en el botón
    State("collapse-explica-1", "is_open"),            # Estado actual del panel (abierto o cerrado)
)
def toggle_collapse_1(n, is_open):
    if n:
        nuevo_estado = not is_open                     # Cambia el estado actual
        texto = "Ocultar interpretación" if nuevo_estado else "Ver interpretación"
        return nuevo_estado, texto
    return is_open, "Ver interpretación"


@callback(
    Output("collapse-explica-2", "is_open"),
    Output("btn-explica-2", "children"),
    Input("btn-explica-2", "n_clicks"),
    State("collapse-explica-2", "is_open"),
)

def toggle_collapse_2(n, is_open):
    if n:
        nuevo_estado = not is_open
        texto = "Ocultar interpretación" if nuevo_estado else "Ver interpretación"
        return nuevo_estado, texto
    return is_open, "Ver interpretación"

@callback(
    Output("collapse-explica-3", "is_open"),
    Output("btn-explica-3", "children"),
    Input("btn-explica-3", "n_clicks"),
    State("collapse-explica-3", "is_open"),
)

def toggle_collapse_3(n, is_open):
    if n:
        nuevo_estado = not is_open
        texto = "Ocultar interpretación" if nuevo_estado else "Ver interpretación"
        return nuevo_estado, texto
    return is_open, "Ver interpretación"

@callback(
    Output("collapse-explica-4", "is_open"),
    Output("btn-explica-4", "children"),
    Input("btn-explica-4", "n_clicks"),
    State("collapse-explica-4", "is_open"),
)

def toggle_collapse_4(n, is_open):
    if n:
        nuevo_estado = not is_open
        texto = "Ocultar interpretación" if nuevo_estado else "Ver interpretación"
        return nuevo_estado, texto
    return is_open, "Ver interpretación"

@callback(
    Output("collapse-explica-5", "is_open"),
    Output("btn-explica-5", "children"),
    Input("btn-explica-5", "n_clicks"),
    State("collapse-explica-5", "is_open"),
)

def toggle_collapse_5(n, is_open):
    if n:
        nuevo_estado = not is_open
        texto = "Ocultar interpretación" if nuevo_estado else "Ver interpretación"
        return nuevo_estado, texto
    return is_open, "Ver interpretación"

@callback(
    Output("collapse-explica-6", "is_open"),
    Output("btn-explica-6", "children"),
    Input("btn-explica-6", "n_clicks"),
    State("collapse-explica-6", "is_open"),
)

def toggle_collapse_6(n, is_open):
    if n:
        nuevo_estado = not is_open
        texto = "Ocultar interpretación" if nuevo_estado else "Ver interpretación"
        return nuevo_estado, texto
    return is_open, "Ver interpretación"

@callback(
    Output("collapse-explica-7", "is_open"),
    Output("btn-explica-7", "children"),
    Input("btn-explica-7", "n_clicks"),
    State("collapse-explica-7", "is_open"),
)

def toggle_collapse_7(n, is_open):
    if n:
        nuevo_estado = not is_open
        texto = "Ocultar interpretación" if nuevo_estado else "Ver interpretación"
        return nuevo_estado, texto
    return is_open, "Ver interpretación"

@callback(
    Output("collapse-explica-8", "is_open"),
    Output("btn-explica-8", "children"),
    Input("btn-explica-8", "n_clicks"),
    State("collapse-explica-8", "is_open"),
)

def toggle_collapse_8(n, is_open):
    if n:
        nuevo_estado = not is_open
        texto = "Ocultar interpretación" if nuevo_estado else "Ver interpretación"
        return nuevo_estado, texto
    return is_open, "Ver interpretación"

@callback(
    Output("collapse-explica-9", "is_open"),
    Output("btn-explica-9", "children"),
    Input("btn-explica-9", "n_clicks"),
    State("collapse-explica-9", "is_open"),
)

def toggle_collapse_9(n, is_open):
    if n:
        nuevo_estado = not is_open
        texto = "Ocultar interpretación" if nuevo_estado else "Ver interpretación"
        return nuevo_estado, texto
    return is_open, "Ver interpretación"

@callback(
    Output("collapse-explica-10", "is_open"),
    Output("btn-explica-10", "children"),
    Input("btn-explica-10", "n_clicks"),
    State("collapse-explica-10", "is_open"),
)

def toggle_collapse_10(n, is_open):
    if n:
        nuevo_estado = not is_open
        texto = "Ocultar interpretación" if nuevo_estado else "Ver interpretación"
        return nuevo_estado, texto
    return is_open, "Ver interpretación"

@callback(
    Output("collapse-explica-11", "is_open"),
    Output("btn-explica-11", "children"),
    Input("btn-explica-11", "n_clicks"),
    State("collapse-explica-11", "is_open"),
)

def toggle_collapse_11(n, is_open):
    if n:
        nuevo_estado = not is_open
        texto = "Ocultar interpretación" if nuevo_estado else "Ver interpretación"
        return nuevo_estado, texto
    return is_open, "Ver interpretación"

@callback(
    Output("collapse-explica-12", "is_open"),
    Output("btn-explica-12", "children"),
    Input("btn-explica-12", "n_clicks"),
    State("collapse-explica-12", "is_open"),
)

def toggle_collapse_12(n, is_open):
    if n:
        nuevo_estado = not is_open
        texto = "Ocultar interpretación" if nuevo_estado else "Ver interpretación"
        return nuevo_estado, texto
    return is_open, "Ver interpretación"

@callback(
    Output("collapse-explica-13", "is_open"),
    Output("btn-explica-13", "children"),
    Input("btn-explica-13", "n_clicks"),
    State("collapse-explica-13", "is_open"),
)

def toggle_collapse_13(n, is_open):
    if n:
        nuevo_estado = not is_open
        texto = "Ocultar interpretación" if nuevo_estado else "Ver interpretación"
        return nuevo_estado, texto
    return is_open, "Ver interpretación"

@callback(
    Output("collapse-explica-14", "is_open"),
    Output("btn-explica-14", "children"),
    Input("btn-explica-14", "n_clicks"),
    State("collapse-explica-14", "is_open"),
)

def toggle_collapse_14(n, is_open):
    if n:
        nuevo_estado = not is_open
        texto = "Ocultar interpretación" if nuevo_estado else "Ver interpretación"
        return nuevo_estado, texto
    return is_open, "Ver interpretación"

