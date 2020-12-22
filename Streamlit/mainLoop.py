# -*- coding: utf-8 -*-
import sys
from functiones import Funciones as fns
import pymongo as pym
import pandas as pd
import streamlit as st
st.beta_set_page_config(
    page_title="Covid-19 Chile",
 	layout="centered",
 	initial_sidebar_state="expanded",
)


st.sidebar.title(" Dashboard Covid-19")
datos = st.sidebar.radio(
    "",
    ( "Comparación Regiones","Comparacion entre Comunas")
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
if datos == "Comparación Regiones":
    #script.main()
    fns.Graphic_to_Regions()
if datos=="Comparacion entre Comunas":
    fns.Graphic_to_Communs()

