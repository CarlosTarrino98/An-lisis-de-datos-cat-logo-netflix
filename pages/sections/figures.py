# Importación de librerías necesarias
import pandas as pd
import plotly.express as px  # Librería para gráficos interactivos
from pages.sections.data_loader import get_clean_data  # Función que carga y limpia el dataset

# Gráfico 1: Comparativa de Películas vs Series (Gráfico de pastel con estilo "dona")
def get_pie_chart_type():
    # Obtenemos el DataFrame limpio a partir del archivo CSV
    df = get_clean_data()

    # Traducimos los tipos de contenido al español para mostrarlos en el gráfico
    df["type_es"] = df["type"].map({"Movie": "Películas", "TV Show": "Series"})

    # Contamos la cantidad de cada tipo y lo convertimos en un nuevo DataFrame
    pie_data = df["type_es"].value_counts().reset_index()
    pie_data.columns = ["Tipo", "Cantidad"]  # Renombramos columnas para claridad

    # Creamos el gráfico de pastel con Plotly Express
    fig = px.pie(
        pie_data,
        names="Tipo",                       # Categoría: Películas o Series
        values="Cantidad",                  # Valor: cuántas hay de cada tipo
        color_discrete_sequence=["#E50914", "#221f1f"],  # Colores: rojo Netflix y gris oscuro
        hole=0.4                            # Añade un agujero en el centro (estilo dona)
    )

    # Mostramos tanto el porcentaje como la etiqueta en cada segmento
    fig.update_traces(textinfo="percent+label")

    # Ajustamos diseño visual del gráfico
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",       # Fondo transparente del área del gráfico
        paper_bgcolor="rgba(0,0,0,0)",      # Fondo transparente del resto
        font_color="white",                 # Texto en blanco para contraste con el fondo oscuro
        title_font_size=20,

        # Configuración de la leyenda: horizontal, centrada y sobre el gráfico
        legend=dict(
            orientation="h",
            y=1.2,
            x=0.5,
            xanchor="center",
            yanchor="bottom"
        )
    )

    # Devolvemos la figura generada
    return fig

# Gráfico 2: Clasificación por edades (Gráfico de burbujas interactivo)
def get_bubble_chart_rating():
    # Cargamos los datos limpios
    df = get_clean_data()

    # Diccionario de etiquetas explicativas para cada tipo de clasificación por edad
    rating_labels = {
        "G": "Apta para todos",
        "PG": "Supervisión sugerida",
        "PG-13": "Mayores de 13",
        "R": "Mayores de 17",
        "NC-17": "Sólo adultos",
        "TV-Y": "Niños pequeños",
        "TV-Y7": "Niños mayores",
        "TV-Y7-FV": "Violencia fantasía",
        "TV-G": "Audiencia general",
        "TV-PG": "Guía parental",
        "TV-14": "Mayores de 14",
        "TV-MA": "Adultos",
        "NR": "Sin clasificar",
        "UR": "No clasificada",
        "Unrated": "Sin calificación",
        "UNKNOWN": "Desconocida"
    }

    # Filtramos los registros que no tienen clasificación
    df_filtered = df.dropna(subset=["rating"])

    # Contamos cuántas veces aparece cada clasificación
    rating_counts = df_filtered["rating"].value_counts().reset_index()
    rating_counts.columns = ["rating", "cantidad"]

    # Añadimos una etiqueta descriptiva combinando el código y su significado
    rating_counts["rating_label"] = rating_counts["rating"].apply(
        lambda r: f"{r}\n({rating_labels[r]})" if r in rating_labels else r
    )

    # Calculamos el porcentaje que representa cada clasificación respecto al total
    total = rating_counts["cantidad"].sum()
    rating_counts["porcentaje"] = rating_counts["cantidad"] / total * 100

    # Creamos el gráfico de burbujas con Plotly Express
    fig = px.scatter(
        rating_counts,
        x="rating_label",        # Clasificación como eje X
        y="cantidad",            # Número de títulos por clasificación
        size="cantidad",         # Tamaño de la burbuja según cantidad
        color="cantidad",        # Color también según cantidad
        size_max=60,             # Tamaño máximo permitido para la burbuja
        labels={"rating_label": "Clasificación", "cantidad": "Cantidad"},
        color_continuous_scale="Reds"
    )

    # Añadimos el porcentaje como dato adicional para mostrar en el tooltip
    fig.update_traces(
        customdata=rating_counts[["porcentaje"]],
        hovertemplate="<b>%{x}</b><br>Cantidad: %{y}<br>Porcentaje: %{customdata[0]:.2f}%<extra></extra>"
    )

    # Configuración estética general del gráfico
    fig.update_layout(
        xaxis_title="Clasificaciones por edad",
        yaxis_title="Cantidad",
        plot_bgcolor="rgba(0,0,0,0)",       # Fondo transparente del gráfico
        paper_bgcolor="rgba(0,0,0,0)",      # Fondo transparente del lienzo
        font_color="white",                 # Texto blanco
        title_font_size=20,
        showlegend=False                    # Oculta la leyenda de color
    )

    # Ocultamos la barra de escala de colores
    fig.update_coloraxes(showscale=False)

    # Devolvemos la figura lista para mostrarse
    return fig

# Gráfico 3: Mapa de calor que cruza tipo de contenido y clasificación por edad
def get_heatmap_type_rating():
    df = get_clean_data()

    # Traducción del tipo al español
    traduccion_type = {"Movie": "Película", "TV Show": "Serie"}
    df["type_es"] = df["type"].map(traduccion_type)

    # Diccionario con significados explicativos para cada clasificación
    rating_labels = {
        "G": "Apta para todos", "PG": "Supervisión sugerida", "PG-13": "Mayores de 13",
        "R": "Mayores de 17", "NC-17": "Sólo adultos", "TV-Y": "Niños pequeños",
        "TV-Y7": "Niños mayores", "TV-Y7-FV": "Violencia fantasía", "TV-G": "Audiencia general",
        "TV-PG": "Guía parental", "TV-14": "Mayores de 14", "TV-MA": "Adultos",
        "NR": "Sin clasificar", "UR": "No clasificada", "Unrated": "Sin calificación", "UNKNOWN": "Desconocida"
    }

    # Añadimos la etiqueta completa: código + significado
    df["rating_label"] = df["rating"].apply(
        lambda r: f"{r}\n({rating_labels[r]})" if r in rating_labels else r
    )

    # Agrupamos por tipo y clasificación
    heatmap_data = df.groupby(["type_es", "rating_label"]).size().reset_index(name="Cantidad")

    # Creamos el heatmap
    fig = px.density_heatmap(
        heatmap_data,
        x="rating_label",
        y="type_es",
        z="Cantidad",
        color_continuous_scale="Reds",
        text_auto=True
    )

    # Estilo visual
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        xaxis_title="Clasificación por edad",
        yaxis_title="Tipo de contenido",
        coloraxis_colorbar=dict(title="Cantidad"),
        margin=dict(t=30, l=30, r=30, b=30),
    )

    # Tooltip personalizado
    fig.update_traces(
        hovertemplate="<b>Tipo:</b> %{y}<br><b>Clasificación:</b> %{x}<br><b>Cantidad:</b> %{z}<extra></extra>"
    )

    return fig

# Gráfico 4: Cantidad de estrenos por año, mes o día de la semana
def get_bar_plot_by_period(periodo="año"):
    df = get_clean_data()
    df = df.dropna(subset=["date_added"]).copy()

    df["date_added"] = pd.to_datetime(df["date_added"])

    # Configuramos según el periodo seleccionado
    if periodo == "año":
        datos = df["release_year"].value_counts().sort_index()
        titulo = "Cantidad de estrenos por año"
        etiqueta_x = "Año"
    elif periodo == "mes":
        datos = df["date_added"].dt.month_name().value_counts().reindex([
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ])
        titulo = "Cantidad de estrenos por mes"
        etiqueta_x = "Mes"
    elif periodo == "día":
        datos = df["date_added"].dt.day_name().value_counts().reindex([
            "Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"
        ])
        titulo = "Cantidad de estrenos por día de la semana"
        etiqueta_x = "Día"

    # Creamos el gráfico de barras
    fig = px.bar(
        x=datos.index,
        y=datos.values,
        labels={"x": etiqueta_x, "y": "Cantidad"},
        color_discrete_sequence=["#E50914"]
    )

    # Estilo
    fig.update_layout(
        title=titulo,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
    )

    return fig

# Gráfico 5: Número de contenidos añadidos a Netflix por año de subida
def get_line_chart_date_added():
    df = get_clean_data()

    # Convertimos a datetime por seguridad
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

    # Extraemos el año de subida
    df['year_added'] = df['date_added'].dt.year

    # Contamos los añadidos por año
    year_counts = df['year_added'].value_counts().sort_index()

    # Creamos el gráfico de línea
    fig = px.line(
        x=year_counts.index,
        y=year_counts.values,
        labels={"x": "Año de subida", "y": "Número de contenidos"},
        markers=True
    )

    # Estilo de la línea y diseño general
    fig.update_traces(line_color="#E50914")
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        title_font_size=20,
    )

    return fig

# Gráfico 6: Histograma de duración de películas (en minutos)
def get_histogram_duration_movies():
    df = get_clean_data()

    # Creamos un histograma para la duración en minutos
    fig = px.histogram(
        df,
        x="duration_minutes",             # Duración en el eje X
        nbins=50,                         # Número de divisiones (bins)
        labels={"duration_minutes": "Duración (minutos)", "count": "Cantidad"}
    )

    # Personalización del color y estilo
    fig.update_traces(marker_color="#FAF0E6")
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",      # Fondo del gráfico transparente
        paper_bgcolor="rgba(0,0,0,0)",     # Fondo del lienzo transparente
        font_color="white",               # Texto blanco
        title_font_size=20,
        xaxis_title="Duración (minutos)",
        yaxis_title="Cantidad"
    )

    return fig

# Gráfico 7: Histograma de número de temporadas en series
def get_histogram_duration_series():
    df = get_clean_data()

    # Creamos un histograma para el número de temporadas
    fig = px.histogram(
        df,
        x="duration_seasons",
        nbins=15,  # Número de divisiones
        labels={"duration_seasons": "Número de temporadas", "count": "Cantidad"}
    )

    # Personalización del gráfico
    fig.update_traces(marker_color="#FAF0E6")
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        title_font_size=20,
        xaxis_title="Número de temporadas",
        yaxis_title="Cantidad"
    )

    return fig

# Gráfico 8: Cantidad de contenidos por país (Top 20)
def get_bar_chart_country():
    df = get_clean_data()

    # Dividimos y contamos países (algunos registros contienen varios separados por coma)
    country_counts = (
        df["country"]
        .dropna()
        .str.split(", ")
        .explode()
        .value_counts()
        .nlargest(20)  # Top 20 países
        .reset_index()
    )
    country_counts.columns = ["Country", "Count"]

    # Creamos un gráfico de barras horizontales
    fig = px.bar(
        country_counts,
        x="Count",
        y="Country",
        orientation="h",
        color_discrete_sequence=["#E50914"]  # Color rojo Netflix
    )

    # Personalización visual
    fig.update_layout(
        yaxis_title="País",
        xaxis_title="Cantidad",
        font_color="white",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)"
    )

    return fig

# Gráfico 9: Muestra la evolución temporal de contenidos añadidos por país en un mapa animado
def get_animated_choropleth_map():
    df = get_clean_data()

    # Filtramos los registros válidos con fecha y país
    df = df.dropna(subset=["country", "date_added"]).copy()
    df["date_added"] = pd.to_datetime(df["date_added"])
    df["Año"] = df["date_added"].dt.year  # Extraemos el año de subida

    # Algunos títulos tienen varios países separados por coma
    df["country"] = df["country"].str.split(", ")
    df = df.explode("country").reset_index(drop=True)
    df.rename(columns={"country": "País"}, inplace=True)

    # Agrupamos por año y país
    df_grouped = df.groupby(["Año", "País"]).size().reset_index(name="Cantidad")

    # Creamos el mapa animado (choropleth)
    fig = px.choropleth(
        df_grouped,
        locations="País",
        locationmode="country names",
        color="Cantidad",
        animation_frame="Año",
        hover_name="País",
        hover_data={"País": False, "Cantidad": True, "Año": True},
        color_continuous_scale=px.colors.sequential.Reds
    )

    # Tooltip personalizado
    fig.update_traces(
        hovertemplate="<b>%{hovertext}</b><br>Año: %{customdata[1]}<br>Cantidad: %{z}<extra></extra>"
    )

    # Estilo visual
    fig.update_layout(
        coloraxis_colorbar=dict(title="Cantidad"),
        geo=dict(
            showframe=False,
            showcoastlines=False,
            bgcolor="rgba(0,0,0,0)"
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white"
    )

    return fig

# Gráfico 10: Muestra la distribución de géneros del catálogo en un treemap
def get_treemap_genres():
    df = get_clean_data()

    # Contamos cuántas veces aparece cada género
    genre_counts = (
        df["listed_in"]
        .dropna()
        .str.split(", ")
        .explode()
        .value_counts()
        .reset_index()
    )
    genre_counts.columns = ["Género", "Cantidad"]

    # Calculamos el porcentaje respecto al total
    total = genre_counts["Cantidad"].sum()
    genre_counts["Porcentaje"] = (genre_counts["Cantidad"] / total * 100).round(2)

    # Preparamos las columnas necesarias para el treemap
    genre_counts["parent"] = "Géneros"  # Nodo raíz
    genre_counts["custom_label"] = genre_counts["Género"]
    genre_counts["custom_count"] = genre_counts["Cantidad"]
    genre_counts["custom_percentage"] = genre_counts["Porcentaje"]

    # Añadimos el nodo raíz
    root = pd.DataFrame({
        "Género": ["Géneros"],
        "Cantidad": [0],
        "parent": [""],
        "custom_label": [""],
        "custom_count": [""],
        "custom_percentage": [""]
    })

    # Combinamos raíz + hijos
    df_treemap = pd.concat([root, genre_counts], ignore_index=True)

    # Creamos el treemap
    fig = px.treemap(
        df_treemap,
        names="Género",
        parents="parent",
        values="Cantidad",
        color="Cantidad",
        color_continuous_scale=px.colors.sequential.Reds,
        custom_data=["custom_label", "custom_count", "custom_percentage"]
    )

    # Tooltip personalizado
    fig.update_traces(
        hovertemplate=[
            "" if label == "Géneros"
            else "<b>%{customdata[0]}</b><br>Cantidad: %{customdata[1]}<br>Porcentaje: %{customdata[2]}%<extra></extra>"
            for label in df_treemap["Género"]
        ]
    )

    # Estilo visual
    fig.update_layout(
        margin=dict(t=10, l=0, r=0, b=10),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white"
    )

    return fig

# Gráfico 11: Muestra el género más frecuente por país en formato mapa
def get_choropleth_dominant_genre():
    df = get_clean_data()

    # Filtramos nulos y separamos múltiples países y géneros
    df = df.dropna(subset=["country", "listed_in"])
    df["country"] = df["country"].str.split(", ")
    df["listed_in"] = df["listed_in"].str.split(", ")
    df = df.explode("country").explode("listed_in")

    # Contamos cuántas veces aparece cada género en cada país
    genre_counts = df.groupby(["country", "listed_in"]).size().reset_index(name="count")

    # Seleccionamos el género más frecuente por país
    dominant_genres = genre_counts.loc[genre_counts.groupby("country")["count"].idxmax()].reset_index(drop=True)
    dominant_genres.columns = ["País", "Género predominante", "Cantidad"]

    # Creamos un mapa tipo choropleth coloreado por género
    fig = px.choropleth(
        dominant_genres,
        locations="País",
        locationmode="country names",
        color="Género predominante",
        hover_name="País",
        hover_data={"Género predominante": True, "Cantidad": True, "País": False},
        color_discrete_sequence=px.colors.qualitative.Set3
    )

    # Estilo visual
    fig.update_layout(
        title=None,
        geo=dict(
            showframe=False,
            showcoastlines=False,
            bgcolor="rgba(0,0,0,0)"
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        legend_title_text="Género predominante"
    )

    return fig

# Gráfico 12: Muestra los 20 actores que más veces aparecen en el catálogo
def get_bar_chart_top_actors():
    df = get_clean_data()

    # Separamos los actores de cada contenido
    cast_series = df["cast"].dropna().str.split(", ").explode()

    # Excluimos valores no informativos
    exclude = {"unknown", "Unknown", "Not Available", "No cast", ""}
    cast_series = cast_series[~cast_series.isin(exclude)]

    # Obtenemos los 20 actores con más apariciones
    top_actors = cast_series.value_counts().nlargest(20).reset_index()
    top_actors.columns = ["Actor", "Apariciones"]

    # Gráfico de barras horizontales
    fig = px.bar(
        top_actors,
        x="Apariciones",
        y="Actor",
        orientation="h",
        color="Apariciones",
        color_continuous_scale=px.colors.sequential.Reds,
    )

    # Estilo
    fig.update_layout(
        yaxis=dict(autorange="reversed"),  # Actores más frecuentes arriba
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        xaxis_title="Número de apariciones",
        yaxis_title="Actor"
    )
    fig.update_coloraxes(showscale=False)

    return fig

# Gráfico 13: Muestra los 20 directores más frecuentes en el catálogo
def get_bar_chart_top_directors():
    df = get_clean_data()

    # Separamos los nombres de directores
    director_series = df["director"].dropna().str.split(", ").explode()

    # Excluimos valores no válidos
    exclude = {"unknown", "Unknown", "Not Available", "No director", ""}
    director_series = director_series[~director_series.isin(exclude)]

    # Top 20 directores más frecuentes
    top_directors = director_series.value_counts().nlargest(20).reset_index()
    top_directors.columns = ["Director", "Apariciones"]

    # Gráfico de barras horizontales
    fig = px.bar(
        top_directors,
        x="Apariciones",
        y="Director",
        orientation="h",
        color="Apariciones",
        color_continuous_scale=px.colors.sequential.Reds,
    )

    # Estilo visual
    fig.update_layout(
        yaxis=dict(autorange="reversed"),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        xaxis_title="Número de apariciones",
        yaxis_title="Director"
    )
    fig.update_coloraxes(showscale=False)

    return fig

# Gráfico 14: Muestra la relación jerárquica entre los directores más frecuentes, los géneros que más trabajan y sus actores más habituales
def get_sunburst_director_genre_actor():
    df = get_clean_data()

    # Eliminamos registros con datos faltantes en las columnas clave
    df = df.dropna(subset=["director", "cast", "listed_in"])

    # Convertimos las cadenas separadas por comas a listas
    df["director"] = df["director"].str.split(", ")
    df["cast"] = df["cast"].str.split(", ")
    df["listed_in"] = df["listed_in"].str.split(", ")

    # Expandimos para tener un registro por combinación de director, género y actor
    df = df.explode("director").explode("listed_in").explode("cast")

    # Filtramos valores no informativos
    exclude = {"unknown", "Unknown", "Not Available", "No cast", ""}
    df = df[~df["director"].isin(exclude)]
    df = df[~df["cast"].isin(exclude)]

    # Nos quedamos con los 5 directores más frecuentes
    top_directors = df["director"].value_counts().nlargest(5).index
    df = df[df["director"].isin(top_directors)]

    # Agrupamos por director, género y actor contando ocurrencias
    grouped = df.groupby(["director", "listed_in", "cast"]).size().reset_index(name="count")

    # Filtrado jerárquico: para cada director, mostramos solo sus 3 géneros más trabajados y, por cada uno, sus 2 actores más frecuentes
    filtered_data = []
    for director, df_dir in grouped.groupby("director"):
        # Seleccionamos los 3 géneros más frecuentes para ese director
        top_genres = df_dir.groupby("listed_in")["count"].sum().nlargest(3).index
        df_dir = df_dir[df_dir["listed_in"].isin(top_genres)]

        for genre, df_genre in df_dir.groupby("listed_in"):
            # Seleccionamos los 2 actores más frecuentes dentro de ese género para ese director
            top_actors = df_genre.nlargest(2, "count")
            filtered_data.append(top_actors)

    # Concatenamos todos los registros filtrados
    df_final = pd.concat(filtered_data)

    # Creamos el gráfico Sunburst
    fig = px.sunburst(
        df_final,
        path=["director", "listed_in", "cast"],  # Jerarquía: Director > Género > Actor
        values="count",
        color="count",
        color_continuous_scale="Reds",
        hover_data={"count": True}
    )

    # Personalizamos el tooltip
    fig.update_traces(
        hovertemplate='<b>%{label}</b><br>Recuentos: %{value}<extra></extra>'
    )

    # Estilo del gráfico
    fig.update_layout(
        margin=dict(t=10, l=0, r=0, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white"
    )

    # Ocultamos la barra lateral de color
    fig.update_coloraxes(showscale=False)

    return fig