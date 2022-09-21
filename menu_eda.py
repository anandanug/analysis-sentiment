import streamlit as st
import pandas as pd
#import plotly.express as px
#import plotly.graph_objs as go
#from plotly.subplots import make_subplots
#from wordcloud import WordCloud
#import matplotlib.pyplot as plt
import re
from collections import Counter

def display_eda():
    text = '''
    # Exploratory Data Analysis (EDA)
    Data yang dilakukan eksplorasi adalah tipe data `data development` yang akan digunakan untuk membentuk model sentiment analysis.

    '''
    st.markdown(text, unsafe_allow_html=True)

    #df = pd.read_csv("data/data_complete_masked.csv")
    #data = df[df.data_type == 'development']
    #temp = data.copy()
    #temp['datetime'] = pd.to_datetime(temp['datetime'])

    st.markdown("### Data development")
    #st.markdown(f"Shape dari data development: {data.shape[0]} baris, {data.shape[1]} kolom")
    #st.markdown(f'Rentang waktu: `{temp["datetime"].min().strftime("%d %b %Y")}` sampai `{temp["datetime"].max().strftime("%d %b %Y")}`')
    #st.dataframe(data)

    st.markdown("Keterangan untuk tiap kolom data:")
    text = """
    | Column      | Keterangan                                                                                                                                                                                                                                                                                                                                                                              |
    |-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | `text`      | Komentar-komentar dari user Instagram                                                                                                                                                                                                                                                                                                                                                   |
    | `label`     | Sentiment label berupa `neutral`, `positive`, dan `negative`                                                                                                                                                                                                                                                                                                                            |
    | `username`  | Username Instagram (sudah dilakukan masking untuk menjaga kerahasiaan user)                                                                                                                                                                                                                                                                                                             |
    | `likes`     | Jumlah like dari komentar                                                                                                                                                                                                                                                                                                                                                               |
    | `datetime`  | Tanggal dari komentar dibuat                                                                                                                                                                                                                                                                                                                                                            |
    | `data_type` | Tipe data dibedakan menjadi: <br>- data `development` adalah data komentar yang digunakan untuk membuat model dengan rentang waktu `3 Mar 2021` - `7 Jul 2021` dengan `label` dari hasil anotasi. <br>- data `inference` adalah data komentar yang diambil dari `8 Jul 2021` - `14 Nov 2021` dengan `label` didapatkan dari prediksi model terbaik yang dilatih menggunakan data `development`. |
    """
    st.markdown(text, unsafe_allow_html=True)
    st.markdown(f"<br>", unsafe_allow_html=True)
    st.info("Data yang digunakan EDA dibawah semuanya sudah dilakukan preprocessing. Untuk detail proses preprocessing dapat dilihat pada menu Data Preprocessing.")
