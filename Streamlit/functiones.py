import pandas as pd
import streamlit as st
import json
import numpy as np

class Funciones(object):

    @staticmethod
    def Graphic_to_Regions():
        st.sidebar.title('Región')
        df_from_json = pd.read_json('../Json/PCR_Regional.json')
        df_from_json['positividad'] = np.where(np.isnan(df_from_json['positividad']), 0, df_from_json['positividad'])
        st.write("""
        # Comparative graph between Regions 
        """)
        region = st.sidebar.multiselect("Elegir regiones",
                                    ["Atacama", "Ñuble", "Magallanes", "Arica y Parinacota", "Aysén", "Coquimbo",
                                     "Araucanía", "Los Lagos", "Los Ríos", "Magallanes", "Tarapacá", "Valparaíso",
                                     "Biobío", "O’Higgins", "Maule", "Metropolitana","Todas las Regiones"],["Araucanía"])

        for e in range(len(region)):
            info = df_from_json[['positividad']].loc[(df_from_json['Region'] == str(region[e]))]
            info.reset_index(drop=True, inplace=True)
            info.rename(columns={'positividad': region[e]}, inplace=True)
            chart_data = pd.DataFrame(data=info,columns=region)
            #print(chart_data)
            st.line_chart(chart_data, 800, 400)

    @staticmethod
    def Graphic_to_Communs():
        df=pd.read_json('../Json/Regiones_Provincias_comunas.json')
        df_from_json = pd.read_json('../Json/PCR_Comunal.json')
        df_from_json['positividad'] = np.where(np.isnan(df_from_json['positividad']), 0, df_from_json['positividad'])
        st.sidebar.title('Comunas')
        st.write("""
        # Comparative graph between Communs
        """)
        
        options=list(df['region'])
        region=st.sidebar.selectbox("Elegir regiones",options)
        if len(region)==0:
            st.error("Por favor, ingrese una región")
        if len(region)!=0:
            if region=="Arica y Parinacota":
                comunas=st.sidebar.multiselect("Elegir Comunas",list(Funciones.ObtenerComnunas(0)))
                for e in range(len(comunas)):
                    info = df_from_json[['positividad']].loc[(df_from_json['Comuna'] == str(comunas[e]))]
                    info.reset_index(drop=True, inplace=True)
                    info.rename(columns={'positividad': comunas[e]}, inplace=True)
                    chart_data = pd.DataFrame(data=info,columns=comunas)
                    #print(chart_data)
                    st.line_chart(chart_data, 500, 200)
            if region=="Tarapacá":
                comunas=st.sidebar.multiselect("Elegir Comunas",list(Funciones.ObtenerComnunas(1)))
                for e in range(len(comunas)):
                    info = df_from_json[['positividad']].loc[(df_from_json['Comuna'] == str(comunas[e]))]
                    info.reset_index(drop=True, inplace=True)
                    info.rename(columns={'positividad': comunas[e]}, inplace=True)
                    chart_data = pd.DataFrame(data=info,columns=comunas)
                    #print(chart_data)
                    st.line_chart(chart_data, 500, 200)
            if region=="Antofagasta":
                comunas=st.sidebar.multiselect("Elegir Comunas",list(Funciones.ObtenerComnunas(2)))
                for e in range(len(comunas)):
                    info = df_from_json[['positividad']].loc[(df_from_json['Comuna'] == str(comunas[e]))]
                    info.reset_index(drop=True, inplace=True)
                    info.rename(columns={'positividad': comunas[e]}, inplace=True)
                    chart_data = pd.DataFrame(data=info,columns=comunas)
                    #print(chart_data)
                    st.line_chart(chart_data, 500, 200)
            if region=="Atacama":
                comunas=st.sidebar.multiselect("Elegir Comunas",list(Funciones.ObtenerComnunas(3)))
                for e in range(len(comunas)):
                    info = df_from_json[['positividad']].loc[(df_from_json['Comuna'] == str(comunas[e]))]
                    info.reset_index(drop=True, inplace=True)
                    info.rename(columns={'positividad': comunas[e]}, inplace=True)
                    chart_data = pd.DataFrame(data=info,columns=comunas)
                    #print(chart_data)
                    st.line_chart(chart_data,500, 200)
            if region=="Coquimbo":
                comunas=st.sidebar.multiselect("Elegir Comunas",list(Funciones.ObtenerComnunas(4)))
                for e in range(len(comunas)):
                    info = df_from_json[['positividad']].loc[(df_from_json['Comuna'] == str(comunas[e]))]
                    info.reset_index(drop=True, inplace=True)
                    info.rename(columns={'positividad': comunas[e]}, inplace=True)
                    chart_data = pd.DataFrame(data=info,columns=comunas)
                    #print(chart_data)
                    st.line_chart(chart_data, 500, 200)
            if region=="Valparaíso":
                comunas=st.sidebar.multiselect("Elegir Comunas",list(Funciones.ObtenerComnunas(5)))
                for e in range(len(comunas)):
                    info = df_from_json[['positividad']].loc[(df_from_json['Comuna'] == str(comunas[e]))]
                    info.reset_index(drop=True, inplace=True)
                    info.rename(columns={'positividad': comunas[e]}, inplace=True)
                    chart_data = pd.DataFrame(data=info,columns=comunas)
                    #print(chart_data)
                    st.line_chart(chart_data, 500, 200)
            if region=="O’Higgins":
                comunas=st.sidebar.multiselect("Elegir Comunas",list(Funciones.ObtenerComnunas(6)))
                for e in range(len(comunas)):
                    info = df_from_json[['positividad']].loc[(df_from_json['Comuna'] == str(comunas[e]))]
                    info.reset_index(drop=True, inplace=True)
                    info.rename(columns={'positividad': comunas[e]}, inplace=True)
                    chart_data = pd.DataFrame(data=info,columns=comunas)
                    #print(chart_data)
                    st.line_chart(chart_data, 500, 200)
            if region=="Maule":
                comunas=st.sidebar.multiselect("Elegir Comunas",list(Funciones.ObtenerComnunas(7)))
                for e in range(len(comunas)):
                    info = df_from_json[['positividad']].loc[(df_from_json['Comuna'] == str(comunas[e]))]
                    info.reset_index(drop=True, inplace=True)
                    info.rename(columns={'positividad': comunas[e]}, inplace=True)
                    chart_data = pd.DataFrame(data=info,columns=comunas)
                    #print(chart_data)
                    st.line_chart(chart_data, 500, 200)
            if region=="Ñuble":
                comunas=st.sidebar.multiselect("Elegir Comunas",list(Funciones.ObtenerComnunas(8)))
                for e in range(len(comunas)):
                    info = df_from_json[['positividad']].loc[(df_from_json['Comuna'] == str(comunas[e]))]
                    info.reset_index(drop=True, inplace=True)
                    info.rename(columns={'positividad': comunas[e]}, inplace=True)
                    chart_data = pd.DataFrame(data=info,columns=comunas)
                    #print(chart_data)
                    st.line_chart(chart_data, 500, 200)
            if region=="Biobío":
                comunas=st.sidebar.multiselect("Elegir Comunas",list(Funciones.ObtenerComnunas(9)))
                for e in range(len(comunas)):
                    info = df_from_json[['positividad']].loc[(df_from_json['Comuna'] == str(comunas[e]))]
                    info.reset_index(drop=True, inplace=True)
                    info.rename(columns={'positividad': comunas[e]}, inplace=True)
                    chart_data = pd.DataFrame(data=info,columns=comunas)
                    #print(chart_data)
                    st.line_chart(chart_data, 500, 200)
            if region=="Araucanía":
                comunas=st.sidebar.multiselect("Elegir Comunas",list(Funciones.ObtenerComnunas(10)))
                for e in range(len(comunas)):
                    info = df_from_json[['positividad']].loc[(df_from_json['Comuna'] == str(comunas[e]))]
                    info.reset_index(drop=True, inplace=True)
                    info.rename(columns={'positividad': comunas[e]}, inplace=True)
                    chart_data = pd.DataFrame(data=info,columns=comunas)
                    #print(chart_data)
                    st.line_chart(chart_data, 500, 200)
            if region=="Los Ríos":
                comunas=st.sidebar.multiselect("Elegir Comunas",list(Funciones.ObtenerComnunas(11)))
                for e in range(len(comunas)):
                    info = df_from_json[['positividad']].loc[(df_from_json['Comuna'] == str(comunas[e]))]
                    info.reset_index(drop=True, inplace=True)
                    info.rename(columns={'positividad': comunas[e]}, inplace=True)
                    chart_data = pd.DataFrame(data=info,columns=comunas)
                    #print(chart_data)
                    st.line_chart(chart_data, 500, 200)
            if region=="Los Lagos":
                comunas=st.sidebar.multiselect("Elegir Comunas",list(Funciones.ObtenerComnunas(12)))
                for e in range(len(comunas)):
                    info = df_from_json[['positividad']].loc[(df_from_json['Comuna'] == str(comunas[e]))]
                    info.reset_index(drop=True, inplace=True)
                    info.rename(columns={'positividad': comunas[e]}, inplace=True)
                    chart_data = pd.DataFrame(data=info,columns=comunas)
                    #print(chart_data)
                    st.line_chart(chart_data, 500, 200)
            if region=="Aysén":
                comunas=st.sidebar.multiselect("Elegir Comunas",list(Funciones.ObtenerComnunas(13)))
                for e in range(len(comunas)):
                    info = df_from_json[['positividad']].loc[(df_from_json['Comuna'] == str(comunas[e]))]
                    info.reset_index(drop=True, inplace=True)
                    info.rename(columns={'positividad': comunas[e]}, inplace=True)
                    chart_data = pd.DataFrame(data=info,columns=comunas)
                    #print(chart_data)
                    st.line_chart(chart_data, 500, 200)
            if region=="Magallanes":
                comunas=st.sidebar.multiselect("Elegir Comunas",list(Funciones.ObtenerComnunas(14)))
                for e in range(len(comunas)):
                    info = df_from_json[['positividad']].loc[(df_from_json['Comuna'] == str(comunas[e]))]
                    info.reset_index(drop=True, inplace=True)
                    info.rename(columns={'positividad': comunas[e]}, inplace=True)
                    chart_data = pd.DataFrame(data=info,columns=comunas)
                    #print(chart_data)
                    st.line_chart(chart_data, 500, 200)
            if region=="Metropolitana":
                comunas=st.sidebar.multiselect("Elegir Comunas",list(Funciones.ObtenerComnunas(15)))
                for e in range(len(comunas)):
                    info = df_from_json[['positividad']].loc[(df_from_json['Comuna'] == str(comunas[e]))]
                    info.reset_index(drop=True, inplace=True)
                    info.rename(columns={'positividad': comunas[e]}, inplace=True)
                    chart_data = pd.DataFrame(data=info,columns=comunas)
                    #print(chart_data)
                    st.line_chart(chart_data, 500, 200)


    @staticmethod        
    def ObtenerComnunas(x):
        df=pd.read_json('../Json/Regiones_Provincias_comunas.json')
        z=len(df['comunas'][x])        
        Comunas=[]
        for i in range(z):
            Comunas.append(df['comunas'][x][i]['name'])

        return Comunas