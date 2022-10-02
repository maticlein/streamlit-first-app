import streamlit as st
import pandas as pd
from gsheetsdb import connect

conn = connect()

@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

def main():
    st.title("First Streamlit web app")
    st.write("Ejemplo de web app utilizando el framework Streamlit para mostrar las coordenadas del edificio de la Macrofacultad en el campus Andrés Bello de la Universidad de La Frontera, donde se encuentra la oficina del equipo de Innovación Curricular de la Facultad de Ingeniería y Ciencias.")
    st.markdown("## Coordenadas")   
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

    sheet_url = st.secrets["public_gsheets_url"]
    rows = run_query(f'SELECT * FROM "{sheet_url}"')
    for row in rows:
        st.write(f"{row.nombre} {row.apellido} {int(row.id)}")
 
if __name__ == "__main__":
    main()