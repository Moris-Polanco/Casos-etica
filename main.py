import streamlit as st
import gateway

def header():
    st.header('Generador de casos de ética')
    st.markdown("##### Genera casos originales de ética.")
    st.text('version 0 - Last update 08/08/2022')

def instert_text():
    txt = st.text_area("Ingrese palabras clave, separadas por coma y con punto al final.")
    colum1, colum2,colum3,colum4,colum5 = st.columns([1,1,1,1,1])

    if colum1.button("Genere Caso"):
        with st.spinner(text='en progreso'):
            
            new_txt, status = gateway.conect_gerador_casos_etica(txt)
            status = 200
            
            if status == 200:
                st.text_area(label="Generador de casos de ética :", value=new_txt, height=250)
                st.success("Sucess!")  
            else:
                st.text_area(label="Error:", value=new_txt["Error"])
                st.error(new_txt["Error"]) 
    
    if colum2.button("Limpie"):
        st.info("cleaning")

st.sidebar.markdown("# Generador de casos de ética ❄️")
header()
instert_text()
