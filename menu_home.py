import streamlit as st
import pandas as pd
from datetime import datetime
#import plotly.express as px
#import plotly.graph_objs as go
#from plotly.subplots import make_subplots
#from wordcloud import WordCloud
#import matplotlib.pyplot as plt
import re
from collections import Counter
from wordcloud import WordCloud 
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style = 'whitegrid')

def display_home():
    st.markdown(f'<h1 style="font-weight:bolder;font-size:40px;color:black;text-align:center;">Analisis Sentimen Twitter</h1>', unsafe_allow_html=True)
    st.markdown(f'<h3 style="font-weight:normal;font-size:18px;color:gray;text-align:center;">Study Case: Perusahaan Telekomunikasi</h1>', unsafe_allow_html=True)

    result = pd.read_csv('/Users/anandaanugrahramadhan/Documents/Skripsi/Deploy/data/result.csv')

    text = """
    # Ringkasan

    PT. Smartfren Telecom, Tbk. merupakan salah satu layanan telekomunikasi terbesar di Indonesia. 
    Meskipun menjadi salah satu layanan telekomunikasi terbesar, tidak semua pengguna memiliki komentar positif atau bahkan negatif. 
    Kini pengguna dapat menyampaikan berbagai sentimen media, salah satunya Twitter. Media Twitter memiliki keunggulan tampilan sederhana, 
    topik terupdate, akses terbuka terhadap tweet dan menyampaikan pendapat dengan cepat. Dari berbagai komentar di Twitter, diperlukan suatu 
    teknik untuk membagi sentimen positif atau negatif. Penelitian ini menggunakan preprocessing dan klasifikasi sentimen ke dalam kelas positif, 
    negatif, dan netral dengan metode lexicon based. Sedangkan untuk modelingnya menggunakan long short-term memory (LSTM). 
    Data yang digunakan berupa sentimen tentang layanan telekomunikasi Smartfren dari media sosial Twitter yang berjumlah 400.000 (empat ratus ribu) 
    dari tahun 2019 hingga 2022, dimana setiap tahunnya dibatasi 100.000 (seratus ribu) pertahunnya. 
    Aplikasi sistem analisis sentimen telah berhasil di bangun, dengan menyajikan halaman home hasil prediksi sentimen menggunakan metode Lexicon Based 
    dan LSTM, halaman data scrapping, halaman data preparation, dan halaman modeling. 
    """

    st.markdown(text, unsafe_allow_html=True)



