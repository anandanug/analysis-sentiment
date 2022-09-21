import streamlit as st
import pandas as pd
#import plotly.express as px
#import plotly.graph_objs as go
#from plotly.subplots import make_subplots
#from wordcloud import WordCloud
#import matplotlib.pyplot as plt
import re
from collections import Counter

def display_inference():
    text = """
    # Model Inference
    Model machine learning yang sudah dilatih digunakan untuk memprediksi data baru (*inference*). Berdasarkan 
    tahap modeling, model machine learning terbaik adalah `TF-IDF SVM` dengan akurasi skor `74.60%` pada data test.

    ### Data inference
    Data baru yang digunakan untuk proses *inference* memiliki deskripsi sebagai berikut.
    """

    st.markdown(text, unsafe_allow_html=True)
    #st.markdown(f"Shape dari data inference: {df_comments.shape[0]} baris, {df_comments.shape[1]} kolom")
    #st.markdown(
        #f'Rentang waktu: `{df_comments["datetime"].min().strftime("%d %b %Y")}` sampai `{df_comments["datetime"].max().strftime("%d %b %Y")}`')
    #st.dataframe(df_comments.head(10))
    st.info('Data yang ditampilkan sudah dilakukan *preprocessing*, *masking*, dan diprediksi labelnya.')

    text = """
    ### Hasil inference
    Berikut ini adalah hasil inference model pada data baru.
    | Sentiment  | Jumlah |
    |------------|--------|
    | `neutral`  | 8718   |
    | `positive` | 3050   |
    | `negative` | 3491   |
    """

    st.markdown(text, unsafe_allow_html=True)