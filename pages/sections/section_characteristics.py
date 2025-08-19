import pandas as pd
from dash import html
import dash_bootstrap_components as dbc
from pages.sections.data_loader import get_clean_data  # Importamos función de limpieza de datos

def layout():
    # Carga el dataset limpio
    df = get_clean_data()

    # Extrae tipos de dato por columna y los formatea para mostrarlos como texto
    df_types = df.dtypes.astype(str).reset_index().rename(columns={"index": "Variable", 0: "Tipo de dato"})

    # Lista de descripciones personalizadas para cada variable del dataset
    descriptions = [
        "Identificador único del contenido",
        "Tipo de contenido (Película o Serie)",
        "Título del contenido",
        "Director principal",
        "Actores involucrados",
        "País donde se produjo",
        "Fecha en la que se añadió a Netflix",
        "Año de estreno",
        "Clasificación por edad",
        "Duración original (texto)",
        "Categoría o género",
        "Descripción del contenido",
        "Duración en minutos (*)",              # Variable añadida por el usuario
        "Número de temporadas (*)"              # Variable añadida por el usuario
    ]

    # Función auxiliar para contar valores nulos o no válidos
    def contar_invalidos(serie):
        if serie.dtype == object:
            return serie.isna().sum() + serie.str.strip().isin(["", "Unknown", "unknown", "Not Available", "NA"]).sum()
        else:
            return serie.isna().sum()

    # Aplica la función a cada columna y guarda el resultado como DataFrame
    invalid_counts = pd.Series({col: contar_invalidos(df[col]) for col in df.columns}).reset_index()
    invalid_counts.columns = ["Variable", "Nulos/Inválidos"]

    # Une los tipos de dato con la cantidad de nulos/invalidos por variable
    df_types = df_types.merge(invalid_counts, on="Variable")

    # Selecciona variables numéricas para caracterización estadística
    numeric_vars = ["release_year", "duration_minutes", "duration_seasons"]

    # Calcula medidas estadísticas: media, desviación típica, mínimo y máximo
    stats = df[numeric_vars].describe().T

    # Composición del layout de la pestaña
    layout = html.Div([
        dbc.Row([
            # Columna izquierda: Información sobre las variables
            dbc.Col([
                html.H5("Características de las variables", className="text-center text-dark mb-3"),

                html.P(
                    "La siguiente tabla ofrece una descripción detallada de cada una de las variables que conforman el conjunto de datos, "
                    "incluyendo un breve resumen de su contenido, así como una especificación clara de su tipo desde una perspectiva programática, "
                    "lo cual facilita su comprensión y posterior manipulación en el análisis de datos.",
                    className="text-secondary text-center mb-4"
                ),

                # Tabla que muestra variable, descripción, tipo de dato y nº de datos inválidos
                dbc.Table(
                    [
                        html.Thead(
                            html.Tr([
                                html.Th("Variable", className="text-dark text-center"),
                                html.Th("Descripción", className="text-dark text-center"),
                                html.Th("Tipo de dato", className="text-dark text-center"),
                                html.Th("Nº de datos inválidos", className="text-dark text-center"),
                            ])
                        ),
                        html.Tbody([
                            html.Tr([
                                html.Td(variable, className="text-light text-left"),
                                html.Td(description, className="text-light text-left"),
                                html.Td(dtype, className="text-light text-left"),
                                html.Td(invalid_count, className="text-light text-left"),
                            ], className="table-secondary" if i % 2 == 0 else "table-dark")
                            for i, (variable, description, dtype, invalid_count) in enumerate(
                                zip(df_types["Variable"], descriptions, df_types["Tipo de dato"], df_types["Nulos/Inválidos"])
                            )
                        ])
                    ],
                    bordered=True,
                    hover=True,
                    responsive=True,
                    class_name="w-100"
                ),

                # Nota aclaratoria sobre variables creadas por el autor
                html.Small(
                    "* Las variables 'duration_minutes' y 'duration_seasons' no forman parte del conjunto de datos original de Netflix, "
                    "sino que han sido creadas para distinguir la duración de películas (en minutos) y series (en temporadas).",
                    className="text-muted d-block my-2 text-left"
                )
            ], width=6),  # Ocupa la mitad de la fila

            # Columna derecha: Estadísticas de variables numéricas
            dbc.Col([
                html.H5("Caracterización de variables numéricas", className="text-center text-dark mb-3"),

                html.P(
                    "A continuación, se presentan y analizan las principales medidas estadísticas descriptivas correspondientes a las variables numéricas más relevantes del conjunto de datos, "
                    "con el fin de proporcionar una visión general de su comportamiento, distribución y características fundamentales.",
                    className="text-secondary text-center mb-4"
                ),

                # Tabla con media, desviación típica, máximo y mínimo por variable
                dbc.Table(
                    [
                        html.Thead(
                            html.Tr([
                                html.Th("Variable", className="text-dark text-center"),
                                html.Th("Media", className="text-dark text-center"),
                                html.Th("Desviación típica", className="text-dark text-center"),
                                html.Th("Máximo", className="text-dark text-center"),
                                html.Th("Mínimo", className="text-dark text-center")
                            ])
                        ),
                        html.Tbody([
                            html.Tr([
                                html.Td(var, className="text-light text-left"),
                                html.Td(f"{stats.loc[var, 'mean']:.2f}", className="text-light text-center"),
                                html.Td(f"{stats.loc[var, 'std']:.2f}", className="text-light text-center"),
                                html.Td(int(stats.loc[var, 'max']), className="text-light text-center"),
                                html.Td(int(stats.loc[var, 'min']), className="text-light text-center")
                            ], className="table-secondary" if i % 2 == 0 else "table-dark")
                            for i, var in enumerate(numeric_vars)
                        ])
                    ],
                    bordered=True,
                    hover=True,
                    responsive=True,
                    class_name="w-100"
                )
            ], width=6)
        ], className="mx-3 gx-5")  # Margen y separación horizontal entre columnas
    ])

    return layout