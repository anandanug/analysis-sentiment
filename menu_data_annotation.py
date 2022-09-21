import streamlit as st
import pandas as pd
#import plotly.express as px
from PIL import Image

def display_data_annotation():
    text = '''
    # Data Annotation
    Tahap ini melakukan anotasi label data menjadi `neutral`, `positive`, dan `negative` dari data yang didapatkan pada proses crawling.
    '''
    st.markdown(text, unsafe_allow_html=True)
    st.info("Note: data yang dilakukan anotasi hanya pada tahun `2019`, `2020`, `2021`, dan `2022`")
        
    text = '''
    Sehingga setelah difilter berdasarkan rentang waktu, didapatkan data sebanyak `400.000 data`.
    ### Metode pelabelan
    Pelabelan dilakukan oleh semua anggota team dengan masing-masing anggota melakukan anotasi sebanyak kurang lebih `1991 data`.
    Untuk panduan pelabelan `neutral`, `positive`, dan `negative` mengacu pada metode/aturan berikut:
    - Positive
        * Terdapat _keyword_ yang bermakna positif, seperti: ucapan syukur, doa, kata-kata semangat.
        * Terdapat emoticon yang memiliki konteks positif, seperti: 🥰, 😄, 🙏.
        * Komentar apapun yang memiliki konteks positif.
    - Negative
        * Terdapat _keyword_ yang bermakna negatif, seperti: kecewa, sedih, kekesalan.
        * Terdapat emoticon yang memiliki konteks negatif, seperti: 😢, 😭, 😡.
        * Komentar apapun yang memiliki konteks negatif, seperti: sindiran, ketidakpuasan dengan kebijakan, keluhan.
    - Neutral
        * Tidak bisa masuk kategori positive atau negative.
        * Komentar yang bersifat pertanyaan misalnya ingin mengetahui suatu informasi.
    '''
    st.markdown(text, unsafe_allow_html=True)