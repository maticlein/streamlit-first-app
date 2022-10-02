import streamlit as st
import numpy as np
import pandas as pd

def main():
    st.title("First Streamlit web app")
    st.write("Ejemplo de web app utilizando el framework Streamlit para mostrar las coordenadas del edificio de la Macrofacultad en el campus Andrés Bello de la Universidad de La Frontera.")
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
 
if __name__ == "__main__":
    main()