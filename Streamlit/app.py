# -*- coding: utf-8 -*-
import pandas as pd
import streamlit as st
import json
import numpy as np

#Prueba de graficos con json
def Graficos_Mario():
    df_from_json = pd.read_json('../Json/PCR_Regional.json')
    df_from_json['positividad'] = np.where(np.isnan(df_from_json['positividad']), 0, df_from_json['positividad'])
    #print(df_from_json[['Region', 'fecha', 'positividad']])
    st.write("""
    # From Json_PCR_Regional to Streamlit Table
    """
             )
    st.write(df_from_json[['Region', 'positividad', 'fecha']])
    region = st.sidebar.multiselect("Elegir regiones",
                                    ["Atacama", "Ñuble", "Magallanes", "Arica y Parinacota", "Aysén", "Coquimbo",
                                     "Araucanía", "Los Lagos", "Los Ríos", "Magallanes", "Tarapacá", "Valparaíso",
                                     "Biobío", "O’Higgins", "Maule", "Metropolitana"],["Araucanía"])
    for e in range (len(region)):
        st.write(df_from_json[['Region','positividad','fecha']].loc[(df_from_json['Region'] ==str(region[e])) & (df_from_json['positividad']>=0)])
    chart_data = pd.DataFrame(
        np.random.randn(20, len(region)), columns=region)

    st.line_chart(chart_data)

    # Posibilida de graficar en base a un mapa pero faltaria latitud y longitud para las zonas
    # map_data = pd.DataFrame(
    #   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    #  columns=['lat', 'lon'])

    # st.map(map_data)

Graficos_Mario()

#Posibilida de graficar en base a un mapa pero faltaria latitud y longitud para las zonas
#map_data = pd.DataFrame(
 #   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
  #  columns=['lat', 'lon'])

#st.map(map_data)

