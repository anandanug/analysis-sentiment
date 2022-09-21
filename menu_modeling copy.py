import streamlit as st
from PIL import Image

def display_modeling():
    text = """
    # Modeling
    Tahap ini melakukan training model *machine learning* dari masukan data yang sudah dilakukan 
    klasifikasi dengan metode lexicon-based.
    """
    st.markdown(text, unsafe_allow_html=True)
    st.info("Data untuk training yang digunakan sebanyak `267826 data` dan data untuk testing sebanyak `66957 data`")

    text = """
    ## Long Short-Term Memory
    ### Deskripsi
    Long Short-Term Memory (LSTM) merupakan model varian dari Recurrent Neural Network (RNN) yang dapat mengingat informasi jangka 
    panjang (*long term dependency*). Model LSTM dirancang sebagai solusi dari masalah *vanishing gradient* yang ditemui pada RNN 
    konvensional [1]. Dalam LSTM terdapat tiga gerbang yaitu *input gate*, *forget gate*, dan *output gate*. Sel memori dan tiga gerbang 
    dirancang untuk dapat membaca, menyimpan, dan memperbarui informasi terdahulu.
    """
    st.markdown(text, unsafe_allow_html=True)
    lstm = Image.open('/Users/anandaanugrahramadhan/Documents/Skripsi/Deploy/image/LSTM3-chain.png')
    st.image(lstm, caption='Struktur LSTM, source dari colah.github.io', width=600)

    text = """
    Kelebihan:
    - LSTM tepat digunakan untuk data yang berbentuk *sequence*.
    - LSTM memiliki *performance* yang lebih baik pada *sentiment classification* ketika jumlah training data lebih banyak [2].
    - LSTM lebih baik dalam mempelajari *context-sensitive* daripada RNN [3].
    Kekurangan:
    - LSTM membutuhkan waktu lebih lama dan lebih banyak memori untuk dilatih.
    - Dropout jauh lebih sulit untuk diterapkan di LSTM.
    - LSTM sensitif terhadap inisialisasi bobot acak yang berbeda.
    ---
    Referensi:
    1. Hochreiter, S., & Schmidhuber, J. (1997). Long Short-Term Memory. 
    2. Murthy, D., Allu, S., Andhavarapu, B., Bagadi, M., & Belusont, M. (2020). Text based sentiment analysis using LSTM. 
    3. Gers, F. A., & Schmidhuber, J. (2001). LSTM recurrent networks learn simple context free and context sensitive languages.
    ### Modeling dengan LSTM
    Pada research ini, dilakukan training model LSTM dengan input data berbeda, yaitu hasil feature extraction menggunakan 
    TF-IDF dan hasil feature extraction menggunakan Word2Vec.
    Untuk meningkatkan performa model, dilakukan hyperparameter tuning menggunakan `Keras Tuner` untuk mendapatkan nilai 
    *hyperparameter* pada model. Berikut ini adalah tabel *hyperparameter*.

    | Hyperparameter   | Kombinasi            |
    |------------------|----------------------|
    | `lstm_out`       | `[32, 48, 64]`       |
    | `dropout`        | `[0.2, 0.5, 0.8]`    |
    | `learning_rate`  | `[0.1, 0.01, 0.001]` |



    Setelah dilakukan *tuning*, nilai akurasi **meningkat 2.41%** pada data test. Hasil akurasi skor dapat 
    dilihat pada tabel Accuracy Score LSTM di bawah.
    """
    st.markdown(text, unsafe_allow_html=True)
    lstm_acc = Image.open('/Users/anandaanugrahramadhan/Documents/Skripsi/Deploy/image/LSTM Accuracy.png')
    st.image(lstm_acc, caption='Accuracy Score LSTM', width=400)

    text = """
    ### Pembahasan
    Berdasarkan hasil training dan testing model, dapat kita ketahui: 
    - Model terbaik adalah **model TF-IDF LSTM** setelah dilakukan *tuning hyperparameter* dengan **akurasi 71.94%** pada data test.
    - Model dengan *feature extraction* TF-IDF memiliki hasil akurasi lebih baik dari Word2Vec karena terdapat beberapa kata yang  *out-of-vocabulary* (oov) dari *vocabulary pre-trained* FastText. 
    - Hasil akurasi pada model TF-IDF LSTM dan Word2Vec LSTM memiliki akurasi cukup baik sekitar 70%, menunjukkan LSTM mampu melakukan analisis sentimen dengan cukup baik. 
    """
    st.markdown(text, unsafe_allow_html=True)