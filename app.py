import streamlit as st
from PIL import Image
from menu_home import display_home
from menu_data_collection import display_data_collection
from menu_data_annotation import display_data_annotation
from menu_eda import display_eda
from menu_data_preprocessing import display_data_preprocessing
#from menu_feature_extraction import display_feature_extraction
from menu_modeling import display_modeling
from menu_inference import display_inference


st.set_page_config(layout="wide")

# menu sidebar
list_menu = ['Home', 'Data Understanding', 'Data Preparation', 
             'Modeling']
menu_choice = st.sidebar.selectbox("Select a menu", list_menu)

link = '[Demo Sentiment Analysis 🚀](#)'

st.sidebar.markdown(link, unsafe_allow_html=True)

st.sidebar.title('Skripsi')
text = """
Analisis Sentimen
---
"""
st.sidebar.markdown(text, unsafe_allow_html=True)

#doccano = Image.open('images/dsi_logo.png')
#st.sidebar.image(doccano, caption='', width=100)
text = """
Ananda Anugrah Ramadhan
"""
st.sidebar.markdown(text, unsafe_allow_html=True)

### MENU: HOME ###
if menu_choice == 'Home':
    display_home()
    
### MENU: DATA COLLECTION ###
if menu_choice == 'Data Understanding':
    display_data_collection()

### MENU: DATA PREPROCESSING ###
if menu_choice == 'Data Preparation':
    display_data_preprocessing()

### MENU: FEATURE EXTRACTION ###
#if menu_choice == 'Feature Extraction':
#    display_feature_extraction()

### MENU: MODELING ###
if menu_choice == 'Modeling':
    display_modeling()