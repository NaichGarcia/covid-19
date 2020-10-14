from Conexion import Database as db
import pymongo as pym
import pandas as pd
import streamlit as st
import time
import numpy as np

#Inicializar nuestra conexión 
db.initialize('covid')
collection='test1'
#Obtener datos de Database
z= db.Get_Data_from_database(collection)
#print(z)
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)
for i in range(1,5):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()
print("separador ------")
# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")