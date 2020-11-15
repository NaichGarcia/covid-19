# -*- coding: utf-8 -*-
from Conexion import Database as db
import pymongo as pym
import pandas as pd
import streamlit as st
import json

#Inicializar nuestra conexión
db.initialize('covid')
#DataFrame
df = pd.read_json('../Templates/CollectionQuerry.json',encoding='UTF-8',)
df=df.drop(['_id'],axis='columns')#Borra la columna _id (creada por el Mongo)


print(df)
st.dataframe(df)#Crea una tabla en streamlit dataframe
st.table(df.style.highlight_min())#Crea una tabla estatica en streamlit y le da un colocr a los maximos valores
df2=pd.read_json('../Json/Regiones_Provincias_comunas.json',orient='records')
st.dataframe(df2)
print(df2)
with open('../Json/Regiones_Provincias_comunas.json', encoding='utf-8') as f:
  data = json.load(f)
st.json(data)#->Jorge esto es para ti, ahí resolví el problema que tenias de leer archivos json en codeados en utf-8


