import pandas as pd
import os
from functools import lru_cache

# Decorador que permite cachear el resultado para no recargar el dataset en cada llamada
@lru_cache(maxsize=1)
def get_clean_data():
    """
    Carga y limpia el dataset de Netflix desde 'data/netflix.csv'.
    Devuelve un DataFrame procesado, listo para análisis y visualización.
    """

    # Ruta relativa al archivo CSV
    csv_path = "data/netflix.csv"

    # Comprobación de que el archivo existe, lanza un error si no está
    if not os.path.exists(csv_path):
        raise FileNotFoundError("No se encontró el archivo 'netflix.csv' en la carpeta 'data/'")

    # Carga inicial del CSV en un DataFrame de pandas
    df = pd.read_csv(csv_path)

    # Conversión de la columna 'date_added' al tipo datetime (fechas)
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

    # Lista de valores considerados inválidos o no informativos
    invalid_values = {"", "Unknown", "unknown", "Not Available", "No cast", "nan", "NaN", "N/A"}

    # Limpieza general de columnas clave (relleno de nulos, conversión a texto, eliminación de espacios)
    for col in ['director', 'cast', 'country', 'rating']:
        df[col] = (
            df[col]
            .fillna("Unknown")                # Sustituye nulos
            .astype(str)                      # Asegura tipo texto
            .str.strip()                      # Elimina espacios al inicio/fin
            .replace(invalid_values, "Unknown")  # Sustituye valores basura
        )

    # Normalización de valores en la columna 'rating' (para evitar duplicados mal escritos)
    df['rating'] = df['rating'].str.upper().str.replace(".", "", regex=False)

    # Limpieza de la columna 'country' para evitar comas sobrantes al final
    df['country'] = df['country'].str.replace(r",\s*$", "", regex=True)

    # Creación de nuevas columnas numéricas:
    # - duración en minutos para películas
    df['duration_minutes'] = df['duration'].apply(
        lambda x: int(x.split()[0]) if pd.notnull(x) and 'min' in x else None
    )

    # - duración en número de temporadas para series
    df['duration_seasons'] = df['duration'].apply(
        lambda x: int(x.split()[0]) if pd.notnull(x) and 'Season' in x else None
    )

    # Eliminación de filas duplicadas
    df.drop_duplicates(inplace=True)

    # Limpieza extra de columnas de texto (elimina espacios en títulos, descripciones, etc.)
    text_columns = ['title', 'director', 'cast', 'country', 'rating', 'listed_in', 'description']
    for col in text_columns:
        df[col] = df[col].astype(str).str.strip()

    # Devuelve el DataFrame limpio y listo para usar
    return df
