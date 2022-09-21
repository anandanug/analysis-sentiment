import streamlit as st

def display_data_preprocessing():
    text = """
    # Data Preprocessing
    Tahap ini adalah tahap mengubah data mentah menjadi data bersih yang dapat dijadikan informasi untuk tahap 
    elanjutnya yaitu mempersiapkan data untuk langkah-langkah yang disebut dengan preprocessing. 
    Preprocessing data terdiri dari enam tahapan yaitu, case folding, filtering, tokenizing, stopword removal, formalization dan stemming.

    ### Step 1: Case folding text
    Tahap ini membersihkan teks secara umum, meliputi:
    Berikut ini adalah proses yang terjadi.
    Sebelum dilakukan `casefoldingtext`:
    ```
    @Chanieyazxa smartfren wish nya bisa masuk sma favorit aamiin
    ```
    Setelah dilakukan `casefoldingText`:
    ```
    @chanieyazxa smartfren wish nya bisa masuk sma favorit aamiin
    ```
    ### Step 2: Filtering text
    Tahap ini membersihkan teks secara umum, meliputi:
    Berikut ini adalah proses yang terjadi.
    Sebelum dilakukan `filteringText`:
    ```
    @chanieyazxa smartfren, wish nya bisa masuk sma favorit amin
    ```
    Setelah dilakukan `cleansing text`:
    ```
    chanieyazxa smartfren, wish nya bisa masuk sma favorit amin
    ``` 
    ### Step 3: Tokenizing text
    Tahap ini membersihkan teks secara umum, meliputi:
    Berikut ini adalah proses yang terjadi.
    Sebelum dilakukan `tokenizingText`:
    ```
    chanieyazxa smartfren wish nya bisa masuk sma favorit amin
    ```
    Setelah dilakukan `tokenizing text`:
    ```
    ['chanieyazxa', 'smartfren', 'wish', 'nya', 'bisa', 'masuk', 'sma', 'favorit', amin]
    ```
    ### Step 4: Remove stopwords
    Tahap ini menghapus kata-kata yang termasuk *stop words*. *Stop words* adalah kata-kata yang tidak
    memiliki makna atau arti jika dia berdiri sendiri. Misalnya: apa, kenapa, saya, yang.
    Daftar *stop words* yang digunakan gabungan dari beberapa referensi, yaitu:
    - [Stop words oleh Sastrawi](https://raw.githubusercontent.com/onlyphantom/elangdev/master/elang/word2vec/utils/stopwords-list/sastrawi-stopwords.txt)
    - Stop words oleh NLTK
    - Tambahan *stop words*: `admin`, `mimin`, `min`, `minkes`, `kalo`, `nya`, `username` 
        
    Berikut ini adalah proses yang terjadi.
    Sebelum dilakukan `remove stopwords`:
    ```
    ['chanieyazxa', 'smartfren', 'wish', 'nya', 'bisa', 'masuk', 'sma', 'favorit', amin]
    ```
    Setelah dilakukan `remove stopwords`:
    ```
    ['chanieyazxa', 'smartfren', 'wish', 'masuk', 'sma', 'favorit', amin]
    ```
    ### Step 5: Tokenization
    Tahap ini merubah kalimat menjadi token-token kata. Proses pemisahan menjadi token kata berdasarkan spasi.
    Sebelum dilakukan `tokenization`:
    ```
    terima kasih infonya ayo lengah semangat pandemi ikuti protokol kesehatan tangan_berdoa 
    tangan_berdoa tangan_berdoa
    ```
    Setelah dilakukan `tokenization`:
    ```
    [terima, kasih, infonya, ayo, lengah, semangat, pandemi, ikuti, protokol, kesehatan, 
    tangan_berdoa, tangan_berdoa, tangan_berdoa]
    ```
    ## Split data into data train and data test
    Tahap ini membagi dataset menjadi data `train` dan data `test`.
    - Data `train` digunakan untuk melatih model machine learning.
    - Data `test` digunakan untuk mengetahui performa model machine learning terhadap data baru.
    Pembagian dataset `train` : `test` = 80% : 20%.
    ```python 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    print(X_train.shape, y_train.shape)
    print(X_test.shape, y_test.shape)
    ```
    Hasilnya setelah dataset dibagi:
    - `train`: 267826 baris, 927 kolom
    - `test`: 66957 baris, 927 kolom
    """
    st.markdown(text, unsafe_allow_html=True)

    st.file_uploader('Upload a CSV')

    st.button('Refresh') #jelasin fungsi tombol refresh