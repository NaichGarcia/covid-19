# -*- coding: utf-8 -*-
import sys
sys.path.insert(1,'/covid-19/Conexión')
#from Conexion import DataBase
#import pymongo as pym
import pandas as pd
import streamlit as st

st.sidebar.title("-Dashboard-Covid-19")
datos = st.sidebar.radio(
    "",
    ("Indicadores", "Positividad Test PCR(%)", "Comparacion Entre Comunas o Regiones")
)
#Si selecciona Indicadores
if datos == "Indicadores":
    #script.main()
    st.sidebar.title("Indicadores")

#Si selecciona Positividad Test PCR(%)
if datos == "Positividad Test PCR(%)":
    #script.main()
    st.sidebar.title("Positividad Test PCR(%)")

#Si selecciona Comparacion Entre Comunas o Regiones
if datos == "Comparacion Entre Comunas o Regiones":
    #script.main()
    st.sidebar.title("Comparacion Entre Comunas o Regiones")

