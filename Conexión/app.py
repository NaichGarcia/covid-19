
from Conexion import Database as db
import pymongo as pym
import pandas as pd
import streamlit as st
import numpy as np

def get_data():
	df = pd.read_json('CollectionQuerry.json')
	df = df.sort_index()
	return df


#Inicializar nuestra conexión
db.initialize('covid')
df = get_data()
df = df.drop(['_id','Region','Codigo comuna','Codigo region'],axis=1) # Borra las columnas
df['positividad'] = np.where(np.isnan(df['positividad']), 0, df['positividad']) # Cambia los nan por el float 0.0
#df = pd.to_numeric('positividad', downcast='float')
print(df)
st.line_chart(df)



