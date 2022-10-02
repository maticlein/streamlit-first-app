import streamlit as st
import pandas as pd
from gsheetsdb import connect
from PIL import Image

conn = connect()

@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

def main():
    st.title("First Streamlit web app")
    image = Image.open("./img/logo-innovacion-ufro.png")
    st.image(image, width = 320)
    st.write("Ejemplo de web app utilizando el framework Streamlit para mostrar las coordenadas del edificio de la Macrofacultad en el campus Andrés Bello de la Universidad de La Frontera, donde se encuentra la oficina del equipo de Innovación Curricular de la Facultad de Ingeniería y Ciencias.")
    st.markdown("## Coordenadas")   
    st.write("Ejemplo de uso de DataFrame, columnas de Streamlit, métricas y mapa.")
    macrofacultad = pd.DataFrame({
        "lat": [-38.745943943240675],
        "lon": [-72.61618078412191], 
    }) 
    macrofacultad
    col1, col2 = st.columns(2)
    col1.metric("Latitud", round(macrofacultad["lat"][0], 4))
    col2.metric("Longitud", round(macrofacultad["lon"][0], 4))
    st.markdown("## Mapa")
    st.map(macrofacultad)

    st.markdown("## Equipo Innovación Curricular FICA")
    st.write("Ejemplo de conexión con Google Sheets.")
    st.markdown("### a) Resultado de la Query:")
    st.code("SELECT * FROM sheet_url", language = "sql")
    sheet_url = st.secrets["public_gsheets_url"]
    rows = run_query(f'SELECT * FROM "{sheet_url}"')
    for row in rows:
        st.write(f"{int(row.id)}.- {row.nombre} {row.apellido}")
    
    st.markdown("### b) Resultado de la Query:")
    st.code("SELECT * FROM sheet_url WHERE id = 1", language = "sql")
    data = run_query(f'SELECT * FROM "{sheet_url}" WHERE id = 1')
    data
 
if __name__ == "__main__":
    main()