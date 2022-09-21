import streamlit as st
from PIL import Image
import pandas as pd

def display_modeling():
    df_lex = pd.read_csv('lexicon.csv', low_memory=False)
    df_lstm = pd.read_csv('lstm.csv', low_memory=False)
    text = """
    # Modeling
    """
    st.markdown(text, unsafe_allow_html=True)

    text = """
    ## Klasifikasi Lexicon Based

    Klasifikasi sentimen dengan lexicon based adalah klasifikasi berdasarkan kata positif, negatif, dan netral 
    yang ada pada tweet yang telah melakukan tahap preprocessing. Klasifikasi ini telah dicocokkan dengan kata-kata yang terdapat
    dalam Lexicon Bahasa Indoesia. Tweet yang memiliki kata positif, maka akan digolongkan pada sentimen positif, jika tweet 
    memiliki kata negatif maka akan digolongkan menjadi sentimen negatif, 
    jika bukan kata positif ataupun negatif maka akan digolongkan menjadi sentimen netral.
    """
    st.markdown(text, unsafe_allow_html=True)

    text = """
    Jika sudah memiliki data dapat melakukan upload file dibawah ini. Data akan dimasukan ke tahap klasifikasi lexicon-based apabila data 
    tersebut memiliki kolom seperti `text`, `preprocessing`, atau data yang diunduh dari tahap data preprocessing.

    ### Program Lexicon Based
    """
    st.markdown(text, unsafe_allow_html=True)

    upl = st.file_uploader('Upload file')
    if upl:
        df = pd.read_csv(upl)
        st.write(df.head(5))

    text = """
    Jika sudah upload data lakukan data preprocessing dengan menekan tombol dibawah ini dan langsung di download.
    """
    st.markdown(text, unsafe_allow_html=True)

    if st.button('Proses'):
        st.dataframe(df_lex.head())
       # st.download_button('Download file', data)

    text = """
    ## LSTM

    Algoritma Long Short-Term Memory (LSTM) memiliki memori yang sangat besar, sehingga sangat cocok digunakan untuk data yang berbentuk sequence. 
    Modeling data dengan LSTM yaitu tahap memodelkan apakah data yang akan diuji termasuk kedalam sentimen positif, negatif, atau netral dan 
    mendapatkan akurasi.
    """
    st.markdown(text, unsafe_allow_html=True)

    text = """
    Jika sudah memiliki data dapat melakukan upload file dibawah ini. Data akan dimasukan ke tahap modelingd apabila data 
    tersebut memiliki kolom seperti `text`, `preprocessing`,  `polarity_score`, `polarity` atau data yang diunduh dari tahap data klasifikasi lexicon-based.

    ### Program LSTM
    """
    st.markdown(text, unsafe_allow_html=True)

    upl2 = st.file_uploader('Upload file', key=2)
    if upl2:
        df2 = pd.read_csv(upl2)
        st.write(df2.head(5))

    text = """
    Jika sudah upload data lakukan data preprocessing dengan menekan tombol dibawah ini dan langsung di download.
    """
    st.markdown(text, unsafe_allow_html=True)

    if st.button('Proses', key=3):
        st.dataframe(df_lstm.head())
       # st.download_button('Download file', data)