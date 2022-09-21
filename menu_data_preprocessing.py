import streamlit as st
import pandas as pd


def display_data_preprocessing():
    df_raw = pd.read_csv('prep.csv', low_memory=False)
    df_result = pd.read_csv('/Users/anandaanugrahramadhan/Documents/Skripsi/Deploy/data/merge_1.csv', low_memory=False)

    text = """
    # Data Preparation
    Tahap ini adalah tahap mengubah data mentah menjadi data bersih yang dapat dijadikan informasi untuk tahap 
    elanjutnya yaitu mempersiapkan data untuk langkah-langkah yang disebut dengan preprocessing. 
    Preprocessing data terdiri dari enam tahapan yaitu, case folding, filtering, tokenizing, stopword removal, formalization dan stemming.
    """
    st.markdown(text, unsafe_allow_html=True)

    text = """
    Jika sudah memiliki data dapat melakukan upload file dibawah ini. Data akan dimasukan ke tahap data preprocessing apabila data 
    tersebut memiliki kolom seperti `date`, `tweet_id`, `text`, `username`, `verified`, `followers`, `following`, `mentioned users`, 
    `retweet`, `like` , `reply`, `media`, `language`, dan `location` atau data yang di unduh dari data scrapping.

    ## Program Data Preprocessing
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
        st.dataframe(df_result .head())
       # st.download_button('Download file', data)

