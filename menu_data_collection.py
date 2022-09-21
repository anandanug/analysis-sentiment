import streamlit as st
import pandas as pd

def display_data_collection():
    text = """  
    # Data Understanding
    Data diambil pada sosial media twitter berdasarkan kata kunci “Smartfren”, “@Smartfrenworld”, dan “@smartfencare” 
    baik berupa pendapat, saran, atau kritik. Pada bahasa pemrograman python tersedia package snscrape yang berfungsi 
    untuk mengambil data tweet dari twitter. Data yang diambil dalam penelitian ini sebanyak 400.000 (empat ratus ribu) dari tahun 2019 hingga 2022 dengan data tersebut dibatasi 100.000 (seratus ribu) pertahunnya. Terdapat perbedaan pemrosesan selama penarikan data. 
    """
    st.markdown(text, unsafe_allow_html=True)

    #st.markdown(f'<br>', unsafe_allow_html=True)

    df_raw = pd.read_csv('scrapping_2019.csv', low_memory=False)

    text = """
    ## Menjalankan Program

    Isi formulir untuk mendapatkan data yang di inginkan.
    """
    st.markdown(text, unsafe_allow_html=True)

    with st.form("my_form"):
        st.text_input('Kata Kunci')
        st.date_input('Sejak')
        st.date_input('Akhir')
        st.number_input('Jumlah Data',0, 10)

        if st.form_submit_button('Proses'):
            st.dataframe(df_raw.head())
       # st.download_button('Download file', data)


