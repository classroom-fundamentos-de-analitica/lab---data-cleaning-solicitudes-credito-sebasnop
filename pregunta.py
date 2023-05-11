"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


PATH = r"solicitudes_credito.csv"


def clean_sexo(dataframe):
    """
    Correcciones de la columna "sexo" para el DataFrame.
    - Transforma el texto a minúscula
    - Establece los datos como categorías.
    """
    df = dataframe.copy()
    
    # Modificaciones
    df.sexo = df.sexo.str.lower()
    df.sexo = df.sexo.astype('category')

    return df

def clean_emprendimiento(dataframe):
    """
    Correcciones de la columna "tipo_de_emprendimiento" para el DataFrame.
    - Transforma el texto a minúscula
    - Establece los datos como categorías.
    """
    df = dataframe.copy()
    
    # Modificaciones
    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()
    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.astype('category')

    return df

def clean_idea(dataframe):
    """
    Correcciones de la columna "idea_negocio" para el DataFrame.
    - Transforma el texto a minúscula
    - Reemplaza los guiones por espacios
    - Remueve los espacios laterales
    """
    df = dataframe.copy()

    df.idea_negocio = df.idea_negocio.str.lower()
    df.idea_negocio = df.idea_negocio.str.replace("-", " ")
    df.idea_negocio = df.idea_negocio.str.replace("_", " ")
    df.idea_negocio = df.idea_negocio.str.strip()
    
    return df

def clean_barrio(dataframe):
    """
    Correcciones de la columna "barrio" para el DataFrame.
    - Transforma el texto a minúscula
    - Reemplaza los guiones por espacios

    Se pensó en aplicar la función str.strip()
    pero no coincidía con los resultados esperados
    """
    df = dataframe.copy()
    df.barrio = df.barrio.str.lower()
    df.barrio = df.barrio.str.replace("-", " ")
    df.barrio = df.barrio.str.replace("_", " ")
    # df.barrio = df.barrio.astype('category')

    return df

def clean_comuna(dataframe):
    """
    Correcciones de la columna "comuna_ciudadano" para el DataFrame.
    - Transforma los números float a int.
    - Establece los datos como categorías.
    """
    df = dataframe.copy()
    
    df.comuna_ciudadano = df.comuna_ciudadano.astype(int)
    df.comuna_ciudadano = df.comuna_ciudadano.astype('category')
    
    return df

def clean_fecha(dataframe):

    """
    Correcciones de la columna "fecha_de_beneficio" para el DataFrame.
    - Lee los textos como fechas.
    """
    df = dataframe.copy()

    df.fecha_de_beneficio = pd.to_datetime(
        df.fecha_de_beneficio,
        infer_datetime_format=True,
        format="mixed",
        dayfirst=True,
        errors="raise",
    )

    return df

def clean_monto(dataframe):
    """
    Correcciones de la columna "monto_del_credito" para el DataFrame.
    - Remueve los caracteres especiales financieros
    - Remueve los espacios laterales
    - Establece los montos como números enteros
    """
    df = dataframe.copy()
    df.monto_del_credito = df.monto_del_credito.str.replace(r"\$", "", regex=True)
    df.monto_del_credito = df.monto_del_credito.str.replace(",", "")
    df.monto_del_credito = df.monto_del_credito.str.strip()
    df.monto_del_credito = df.monto_del_credito.astype(float)
    df.monto_del_credito = df.monto_del_credito.astype(int)

    return df

def clean_linea(dataframe):
    """
    Correcciones de la columna "línea_credito" para el DataFrame.
    - Transforma el texto a minúscula
    - Reemplaza los guiones por espacios
    - Remueve los espacios laterales
    """
    df = dataframe.copy()
    df.línea_credito = df.línea_credito.str.lower()
    df.línea_credito = df.línea_credito.str.replace("-", " ")
    df.línea_credito = df.línea_credito.str.replace("_", " ")
    df.línea_credito = df.línea_credito.str.strip()

    return df


def clean_data():

    """
    Limpiando dataset del archivo "solicitudes_credito.csv"
    """

    df = pd.read_csv(PATH, sep=";", index_col=0)

    df.dropna(inplace=True)

    df = clean_sexo(df)
    df = clean_emprendimiento(df)
    df = clean_idea(df)
    df = clean_barrio(df)
    df = clean_comuna(df)
    df = clean_fecha(df)
    df = clean_monto(df)
    df = clean_linea(df)

    df.drop_duplicates(inplace=True)

    return df
