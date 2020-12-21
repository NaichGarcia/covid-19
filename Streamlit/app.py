# -*- coding: utf-8 -*-
import pandas as pd
import streamlit as st
import json
import numpy as np

#Prueba de graficos con json
def Graficos_Pcr_Nacional():
    #DAtos para graficos con info real
    aRegion = []
    st.sidebar.title('Navegación')
    df_from_json = pd.read_json('../Json/PCR_Regional.json')
    df_from_json['positividad'] = np.where(np.isnan(df_from_json['positividad']), 0, df_from_json['positividad'])
    #print(df_from_json[['Region', 'fecha', 'positividad']])
    st.write("""
    # From Json_PCR_Regional to Streamlit Table
    """
             )
    region = st.sidebar.multiselect("Elegir regiones",
                                    ["Atacama", "Ñuble", "Magallanes", "Arica y Parinacota", "Aysén", "Coquimbo",
                                     "Araucanía", "Los Lagos", "Los Ríos", "Magallanes", "Tarapacá", "Valparaíso",
                                     "Biobío", "O’Higgins", "Maule", "Metropolitana","Todas las Regiones"],["Araucanía"])

    for e in range(len(region)):
        info = df_from_json[['positividad']].loc[
            (df_from_json['Region'] == str(region[e]))]
        info.reset_index(drop=True, inplace=True)
        info.rename(columns={'positividad': region[e]}, inplace=True)

        chart_data = pd.DataFrame(
            data=info,
            columns=region
        )

        st.line_chart(chart_data, 800, 400)

    # Posibilida de graficar en base a un mapa pero faltaria latitud y longitud para las zonas
    # map_data = pd.DataFrame(
    #   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    #  columns=['lat', 'lon'])

    # st.map(map_data)

Graficos_Pcr_Nacional()




#Posibilida de graficar en base a un mapa pero faltaria latitud y longitud para las zonas
#map_data = pd.DataFrame(
 #   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
  #  columns=['lat', 'lon'])

#st.map(map_data)

