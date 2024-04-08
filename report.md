# Laporan Proyek Predictive Analytics - I Gusti Ngurah Bagus Ferry Mahayudha
## Domain Proyek

### _Latar Belakang_
Dalam era modern ini, dengan perubahan iklim yang semakin terasa, pemahaman yang lebih baik tentang kualitas cuaca menjadi krusial untuk mengelola risiko dan mengurangi dampak negatifnya. Kualitas udara yang buruk dapat berdampak serius pada kesehatan manusia, ekonomi dan pariwisata. Partikel-partikel  kecil  dalam  udara  seperti  PM2.5 dapat  meresap  ke  dalam  paru-paru  dan  bahkan  masuk  ke  aliran  darah.  Ini dapat   menyebabkan   gangguan   pernapasan   seperti   asma,   bronkitis,   dan pneumonia[1]. Pertumbuhan ekonomi   berpengaruh   positif dan signifikan terhadap kualitas udarapada jangka pendek maupun jangka panjang[2]. Dengan memprediksi kualitas udara yang buruk, tindakan pencegahan dapat diambil untuk melindungi kesehatan masyarakat. Dengan pemahaman yang mendalam tentang prediksi kualitas cuaca, berbagai pihak dapat mengambil langkah-langkah proaktif untuk melindungi kesehatan masyarakat, menjaga keberlanjutan lingkungan, dan mengurangi dampak negatif perubahan iklim. Model prediksi machine learning dapat digunakan untuk memprediksi kualitas cuaca sehingga dengan hasil prediksi, masyarakat dapat melakukan tindakan pencegahan untuk mencegah dampak buruk yang berkelanjutan terhadap kesehatan manusia, ekonomi dan pariwisata.

### _Mengapa dan bagaimana menyelesaikan masalah tsb_
Karena kualitas udara yang buruk dapat berdampak serius pada kesehatan manusia, serta dapat menghambat pariwisata dan aktivitas ekonomi lainnya. Sehingga, diperlukan adanya model klasifikasi kualitas udara untuk mencegah dampak buruk tersebut.

### _Artikel Terkait_
1. [Dampak Buruk Polusi Udara Bagi Kesehatan Dan Cara Meminimalkan Risikonya](https://e-journal.unmas.ac.id/index.php/jeco/article/view/7035) 
- Author : Shinta Maharani, Prof. Redi Aryanta
- Tahun : 2023
2. [Pengaruh Pertumbuhan Ekonomi dan Pertumbuhhan Penduduk terhadap Kualitas Udara di Kawasan Gerbangkertosusila](https://jurnal.unimor.ac.id/JEP/article/view/1305)
- Author : Prisella Ayu Dio Oktavia, Duwi Yunitasari, Lilis Yuliati
- Tahun : 2022

## Business Understanding
### _Rumusan masalah_
1. Bagaimana cara membuat model yang dapat menangani data dengan sebaran data yang tidak seimbang ?
2. Apakah perlu dilakukan pengembangan model sehingga performa model meningkat ?
3. Apakah hanya perlu satu metrik untuk mengukur performa model secara akurat ?
4. Berapa banyak data entry yang diperlukan agar pelatihan model tidak mengalami underfitting ?

### _Tujuan proyek_
1. Untuk memprediksi kualitas udara dengan membuat model yang memiliki performa yang baik dalam memprediksi kualitas udara.
2. Untuk membuat model yang dapat memprediksi kualitas udara dengan akurasi, precision dan recall yang tinggi, yaitu diatas 80%.
3. Untuk mengetahui cara mengukur performa model.
4. Untuk mengetahui rasio data yang cukup untuk melatih model.

### _Solusi permasalahan_
1. Membuat 4 model yang sering digunakan untuk melakukan klasifikasi, yaitu _KNN_, _Decision Tree_, _Random Forest_ dan _Gaussian Naive Bayes_.
2. Memilih salah satu yang terbaik diantara keempat model untuk dilakukan pengembangan model dengan melakukan evaluasi menggunakan metrik akurasi.
3. Melakukan peningkatan performa model terbaik dengan metode _randomized_ _search_ Cross-Validation terhadap kumpulan parameter yang disediakan dalam hyperparameter tuning.
4. Menyimpan model hasil tuning yang sudah dievaluasi ulang.

## Data Understanding
### _Sumber data_
- [ISPU DKI Jakarta 2010](https://katalog.data.go.id/dataset/indeks-standar-pencemaran-udara-ispu-tahun-20101)
- [ISPU DKI Jakarta 2014](https://katalog.data.go.id/dataset/indeks-standar-pencemaran-udara-ispu-tahun-20141)
- [ISPU DKI Jakarta 2016](https://katalog.data.go.id/dataset/indeks-standar-pencemaran-udara-ispu-tahun-20161)
- [ISPU DKI Jakarta 2017](https://katalog.data.go.id/dataset/indeks-standar-pencemaran-udara-ispu-tahun-20171)
- [ISPU DKI Jakarta 2018](https://katalog.data.go.id/dataset/indeks-standar-pencemaran-udara-ispu-tahun-20181)
- [ISPU DKI Jakarta 2021](https://katalog.data.go.id/dataset/indeks-standar-pencemaran-udara-ispu-tahun-20211)

### _Detail data_
Terdapat 1517 entries untuk data yang sudah dibersihkan.
Total kolom pada data berjumlah 8 kolom dengan detail sebagai berikut :

Tabel 1. Detail Data

| Column     | Non-Null Count | Dtype     |
| :---       |    :----:      |      ---: |
| stasiun    | 1335 non-null  | float64   |
| pm25       | 1335 non-null  | float64   |
| pm10       | 1335 non-null  | float64   |
| so2        | 1335 non-null  | float64   |
| co         | 1335 non-null  | float64   |
| o3         | 1335 non-null  | float64   |
| no2        | 1335 non-null  | float64   |
| categori   | 1335 non-null  | object    |

dengan tipe data float64 6 kolom, object 2 kolom, penggunaan memori
106.7+ KB.

### _Fitur yang akan digunakan_
Variabel Fitur : `pm25`, `pm10`, `so2`, `co`, `o3`, `no2`.

### _Exploratory Data Analysis_
Tahapan dalam EDA yang dilakukan adalah :

1. Univariative Data Analysis
Dalam tahap ini, sebaran data untuk masing-masing stasiun dan kategori divisualisasikan dengan **plot()** dengan **kind='bar'** dengan pengambilan data yaitu **df['nama_kolom'].value_counts()**. Visualisasi histogram juga dilakukan untuk melihat persebaran data numerik pada tiap kolom dengan data numerik dengan **df.hist()** dengan **bins=50** dan **figsize=(20,15)**.

Berikut merupakan visulasisasi dari analisis eda yang dilakukan :

Gambar 1. Jumlah data yang ada pada tiap stasiun\
![Station](/vis/univar/1.png "Jumlah data yang ada pada tiap stasiun")\
Gambar 2. Jumlah data untuk tiap kategori\
![Category](/vis/univar/2.png "Jumlah data untuk tiap kategori")\
Gambar 3. Skewness tiap data numerik\
![Skewness](/vis/univar/3.png "Skewness tiap data numerik")

2. Multivariative Data Analysis
Dalam tahap ini, rata-rata data numerik diambil menggunakan fungsi **groupby()** dan disambung dengan **agg()** dengan argumen dictionary **dict(zip([semua_kolom_numerik], ['mean' for i in range(6)]))**. Lalu, rata-rata data numerik untuk masing-masing stasiun dan kategori divisualisasikan langsung dari dataframe dengan **df.plot.bar()** dengan **y='nama_kolom_numerik'** dan untuk pewarnaan yang berbeda yaitu 3 warna untuk kategori dan 5 warna untuk stasiun.

Berikut merupakan visualisasi dari analisis eda yang dilakukan :
Gambar 4. Rata-rata pm25 pada tiap kategori\
![AirCategory](/vis/multivar/1.png "Rata-rata pm25 pada tiap kategori")\
Gambar 5. Rata-rata pm10 pada tiap kategori\
![AirCategory](/vis/multivar/2.png "Rata-rata pm10 pada tiap kategori")\
Gambar 6. Rata-rata so2 pada tiap kategori\
![AirCategory](/vis/multivar/3.png "Rata-rata so2 pada tiap kategori")\
Gambar 7. Rata-rata co pada tiap kategori\
![AirCategory](/vis/multivar/4.png "Rata-rata co pada tiap kategori")\
Gambar 8. Rata-rata o3 pada tiap kategori\
![AirCategory](/vis/multivar/5.png "Rata-rata o3 pada tiap kategori")\
Gambar 9. Rata-rata no2 pada tiap kategori\
![AirCategory](/vis/multivar/6.png "Rata-rata no2 pada tiap kategori")\

Gambar 10. Rata-rata pm25 pada tiap stasiun\
![AirStation](/vis/multivar/7.png "Rata-rata pm25 pada tiap stasiun")\
Gambar 11. Rata-rata pm10 pada tiap stasiun\
![AirStation](/vis/multivar/8.png "Rata-rata pm10 pada tiap stasiun")\
Gambar 12. Rata-rata so2 pada tiap stasiun\
![AirStation](/vis/multivar/9.png "Rata-rata so2 pada tiap stasiun")\
Gambar 13. Rata-rata co pada tiap stasiun\
![AirStation](/vis/multivar/10.png "Rata-rata co pada tiap stasiun")\
Gambar 14. Rata-rata o3 pada tiap stasiun\
![AirStation](/vis/multivar/11.png "Rata-rata o3 pada tiap stasiun")\
Gambar 15. Rata-rata no2 pada tiap stasiun\
![AirStation](/vis/multivar/12.png "Rata-rata no2 pada tiap stasiun")\

## Data Preparation
Teknik-teknik yang digunakan dengan penjelasannya adalah sebagai berikut:
1. Menghilangkan missing value dan outliers
Dalam tahap ini, yang dilakukan adalah menghilangkan seluruh data Null dengan fungsi **dropna()** dengan **inplace=True**. Untuk visualisasi outliers, digunakan visualisasi langsung dari dataframe dengan **df.boxplot()** dengan nilai **y='nama_kolom'**. Lalu untuk pembersihan outlier, digunakan gabungan operator sebagai berikut :
**~((df < (q1 - 1.5 * iqr)) | (df > (q3 + 1.5 * iqr))).any(axis=1)**.

2. Menghilangkan kolom "stasiun"
Pada tahap ini, dilakukan data wrangling untuk memperbaiki format data sehingga pelatihan model bisa dilakukan. Hal ini dilakukan untuk menghilangkan fitur yang tidak diperlukan untuk klasifikasi.

3. Normalisasi data numerik
Pada tahap ini, dilakukan normalisasi data numerik dengan **MinMaxScaler()** dari library scikit-learn. Data lama diolah dengan formulasi/metrik sebagai berikut agar menjadi data baru.
$$\text{x' = $\dfrac{x-min(X)}{max(X) - min(X)}$ }$$
x' = data baru
x = data lama
X = seluruh data pada fitur/kolom
Hal ini dilakukan untuk meringankan beban komputasi dan mengurangi range tiap data sehingga dapat meningkatkan performa model.

4. Membagi data menjadi data latih dan data uji
Pada tahap ini, dilakukan pemecahan data menjadi data latih dan data uji dengan **train_test_split()** dari library scikit-learn dengan **test_size=0.2** dan **random_state=20** yang dimana perbandingan antara data latih dan data uji adalah **4:1** dan diacak sebanyak 20 kali.
Hal ini dilakukan agar bisa melakukan pengujian terhadap model dengan data uji yang telah disiapkan dengan perbandingan jumlah data yang cukup. 

## Modeling
Model machine learning yang digunakan ada empat, yaitu _KNN_, _Decision Tree_, _Random Forest_ dan _Gaussian Naive Bayes_.

### _Kelebihan_
- _KNN_ memiliki kemudahan dalam implementasi, tidak memerlukan tuning parameter, fleksibilitas dalam pemilihan metrik jarak, dan tidak sensitif terhadap outlier.
- _Decision Tree_ memiliki kemampuan untuk mengendalikan overfitting, tidak terpengaruh outlier, mampu menangani data campuran berupa numerik dan kategori, tidak memerlukan bantuan scaling data.
- _Random Forest_ kemampuan untuk mennangani outlier dan noise, tahan overfitting, stabil terhadap perubahan dataset, dan dapat mengukur pentingnya fitur.
- _Gaussian Naive Bayes_ memiliki performa yang baik pada data dengan fitur yang banyak, kemudahan dalam komputasi, robust terhadap data yang tidak seimbang dan tidak memerlukan tuning parameter yang rumit.

### _Kekurangan_
- _KNN_ memiliki kinerja buruk pada data dengan fitur yang banyak, kesulitan dalam menangani data kategori, dan tidak bisa optimal pada distribusi kelas yang tidak seimbang.
- _Decision Tree_ memiliki biaya komputasi yang tinggi, tidak cocok pada data dengan dimensi tinggi, rentan terhadap perubahan kecil pada dataset (tidak stabil).
- _Random Forest_ memiliki kompleksitas model yang tinggi dan pemrosesan data yang cukup rumit.
- _Gaussian Naive Bayes_ memiliki sensitivitas pada data 0, tidak bisa menangani data null dengan baik, kinerja buruk pada data kategori, dan memerlukan fitur yang sangat independen satu sama lain.

### _K Nearest Neighbors_
**Cara kerja :** 
1. Memilih Jumlah Tetangga (K): Menentukan jumlah tetangga terdekat yang akan digunakan untuk membuat prediksi. Nilai K ini biasanya ditentukan oleh pengguna berdasarkan kebutuhan aplikasi.

2. Menghitung Jarak: Setelah jumlah tetangga (K) ditentukan, langkah selanjutnya adalah menghitung jarak antara titik data yang akan diklasifikasikan dengan setiap titik data dalam set pelatihan. Jarak ini biasanya dihitung menggunakan metrik seperti jarak Euclidean, jarak Manhattan, atau jarak Minkowski.

3. Memilih Tetangga Terdekat: Setelah jarak dihitung, _KNN_ akan memilih K titik data terdekat (tetangga) dengan titik data yang akan diklasifikasikan.

4. Voting: Langkah selanjutnya adalah menentukan kelas mayoritas dari tetangga tersebut.  Prediksi dilakukan dengan cara melakukan voting mayoritas dari kelas-kelas tetangga.

5. Mengklasifikasikan: Setelah voting mayoritas dilakukan, titik data yang akan diklasifikasikan akan diberikan label kelas yang paling sering muncul di antara tetangga terdekatnya.

**Formula yang digunakan**
1. Formula Minkowski distance untuk dua vektor u dan v dengan panjang yang sama n adalah sebagai berikut:
$$\mathrm{Minkowski(u, v, p)} = (\sum_{i=1}^{n} [u_i - v_i])^{1/p}$$
Di sini, p adalah parameter yang menentukan tipe jarak. Ketika p=1
p=1, kita mendapatkan jarak Manhattan, dan ketika p=2, kita mendapatkan jarak Euclidean. Secara umum, semakin besar nilai p, semakin sensitif jarak terhadap perbedaan nilai yang besar dalam salah satu dimensi.

### _Decision Tree_
**Cara kerja :**
1. Pemilihan Fitur: Pada setiap langkah dalam pembuatan _Decision Tree_, algoritma memilih fitur yang paling baik untuk membagi dataset menjadi subset yang lebih kecil. 

2. Pembagian Dataset: Setelah fitur yang dipilih, dataset dibagi menjadi subset berdasarkan nilai fitur tersebut. 

3. Pembentukan Node: Setiap subset yang dihasilkan akan menjadi node dalam _Decision Tree_. Proses ini terus berlanjut untuk setiap node hingga kriteria berhenti terpenuhi. misalnya jika semua data dalam subset telah terklasifikasi dengan benar, atau jika batas kedalaman tree telah tercapai.

4. Prediksi: Setelah _Decision Tree_ dibangun, pengklasifikasi dapat menggunakan struktur pohon untuk memprediksi label kelas untuk data baru.

**Formula yang digunakan :**
1. Gini Impurity: Untuk masing-masing node dalam pohon keputusan dan untuk dataset S, Gini Impurity dihitung dengan formula:
$$\mathrm{Gini(S)} = 1 - \sum_{i=1}^{c} \mathrm{p}_{i}^{2}$$
dimana c adalah jumlah kelas yang berbeda dalam dataset S, dan $$\mathrm{p}_{i}$$ adalah proporsi dari instance dalam kelas ke-i dalam dataset S.

2. Gini Impurity untuk pemisahan berdasarkan atribut A didefinisikan sebagai:
$$\mathrm{Gini(S, A)} = 1 - \sum_{u \in V} \dfrac{[S_u]}{[S]} \mathrm{Gini(S_u)}$$
Pemilihan atribut berdasarkan Gini Impurity dilakukan dengan memilih atribut yang memiliki nilai Gini Impurity yang paling rendah. Semakin kecil nilai Gini Impurity, semakin baik atribut tersebut dalam memisahkan dataset.

3. Entropi dari sebuah dataset didefinisikan sebagai:
$$\mathrm{Entropy(S)} = -\sum_{i=1}^{c} p_ilog_2(p_i)$$
dimana c adalah jumlah kelas yang berbeda dalam dataset S, dan $$\mathrm{p_i}$$ adalah proporsi dari instance dalam kelas ke-i dalam dataset S.

4. Information Gain untuk atribut 
$$\mathrm{IG(S,A)} = \mathrm{Entropy(S)} - \sum_{u \in V} \dfrac{[S_u]}{[S]} \mathrm{Entropy(S_u)}$$
IG adalah perbedaan antara entropi sebelum dan setelah pembagian berdasarkan atribut A. Semakin tinggi nilai Information Gain, semakin baik atribut A dalam memisahkan dataset.

### _Random Forest_
**Cara kerja :** 
1. _Bootstrap Sampling_: _Random Forest_ menggunakan teknik _bootstrap sampling_ untuk membuat sampel data acak dari dataset pelatihan. Teknik ini memungkinkan beberapa data untuk muncul beberapa kali dalam sampel dan beberapa data mungkin tidak muncul sama sekali.

2. Pembuatan Pohon Keputusan : _Random Forest_ terdiri dari sejumlah besar pohon keputusan yang dibangun secara acak. Setiap pohon keputusan dibangun menggunakan subset acak dari data pelatihan dan subset acak dari fitur (kolom) yang tersedia.

3. Pembentukan Pohon: Setiap pohon keputusan dibangun secara rekursif dengan cara membagi dataset menjadi dua berdasarkan fitur-fitur yang dipilih secara acak. Pemilihan fitur ini dilakukan berulang kali sampai tercapai kriteria penghentian, misalnya mencapai kedalaman maksimum atau membagi node tidak meningkatkan kehomogenan kelas.

3. Pemilihan Prediksi : Setelah semua pohon dibuat, mereka melakukan prediksi atas kasus baru. Untuk klasifikasi, ini melibatkan voting mayoritas di antara semua pohon. Untuk regresi, hasil dari semua pohon diambil rata-ratanya.

**Formula yang digunakan :**
1. Gini Impurity: Untuk masing-masing node dalam pohon keputusan dan untuk dataset S, Gini Impurity dihitung dengan formula:
$$\mathrm{Gini(S)} = 1 - \sum_{i=1}^{c} \mathrm{p}_{i}^{2}$$
dimana c adalah jumlah kelas yang berbeda dalam dataset S, dan $$\mathrm{p}_{i}$$ adalah proporsi dari instance dalam kelas ke-i dalam dataset S.

2. Gini Impurity untuk pemisahan berdasarkan atribut A didefinisikan sebagai:
$$\mathrm{Gini(S, A)} = 1 - \sum_{u \in V} \dfrac{[S_u]}{[S]} \mathrm{Gini(S_u)}$$
Pemilihan atribut berdasarkan Gini Impurity dilakukan dengan memilih atribut yang memiliki nilai Gini Impurity yang paling rendah. Semakin kecil nilai Gini Impurity, semakin baik atribut tersebut dalam memisahkan dataset.

3. Entropi dari sebuah dataset didefinisikan sebagai:
$$\mathrm{Entropy(S)} = -\sum_{i=1}^{c} p_ilog_2(p_i)$$
dimana c adalah jumlah kelas yang berbeda dalam dataset S, dan $$\mathrm{p_i}$$ adalah proporsi dari instance dalam kelas ke-i dalam dataset S.

4. Information Gain untuk atribut 
$$\mathrm{IG(S,A)} = \mathrm{Entropy(S)} - \sum_{u \in V} \dfrac{[S_u]}{[S]} \mathrm{Entropy(S_u)}$$
IG adalah perbedaan antara entropi sebelum dan setelah pembagian berdasarkan atribut A. Semakin tinggi nilai Information Gain, semakin baik atribut A dalam memisahkan dataset.

Model terbaik yang dipilih adalah _Random Forest_ dikarenakan memiliki akurasi yang paling tinggi yaitu 98,8%. Pada tahap ini, model juga diupgrade dari segi parameter dengan menggunakan _randomized_ _search_ cross-validation. Cross-validation yang dilakukan adalah memilih parameter secara acak dan menguji kinerja model dengan metode cross-validation.

### _Gaussian Naive Bayes_
**Cara kerja:**
1. Pemilihan Model: Pertama, Anda harus memilih model _Gaussian Naive Bayes_ yang sesuai dengan tipe dataset yang Anda miliki, yakni dataset dengan fitur-fitur numerik yang mengikuti distribusi normal.

2. Pemisahan Kelas: Selanjutnya, pisahkan dataset ke dalam kelas-kelas yang berbeda. Setiap kelas akan memiliki distribusi Gaussian yang berbeda untuk setiap fitur numerik.

3. Estimasi Parameter: Hitung parameter-parameter statistik untuk setiap kelas, yaitu rata-rata (mean) dan varians (variance) dari setiap fitur pada setiap kelas.

4. Pemodelan Distribusi: Model distribusi Gaussian digunakan untuk mengestimasi probabilitas kelas dengan menggunakan fitur-fitur dari instance yang akan diprediksi.

5. Prediksi: Dalam melakukan prediksi, dilakukan perhitungan probabilitas dari setiap kelas menggunakan Teorema Bayes dan asumsi bahwa fitur-fitur yang ada dalam datasetnya bersifat independen. Kelas dengan probabilitas tertinggi akan dipilih sebagai prediksi.

**Formula yang digunakan:**
1. Fungsi Probabilitas Gaussian
$$\mathrm{P(x|C_i)} = \dfrac{1}{\sqrt{2\pi\sigma^2}}e^{-\dfrac{(x - \mu)}{2\sigma^2}}$$
Di sini, $$P(x|C_i)$$ adalah probabilitas nilai diberikan kelas μ adalah rata-rata dari fitur pada kelas tersebut, σ adalah simpangan baku (standar deviation), dan e adalah konstanta Euler

2. Teorema Bayes
$$\mathrm{P(C_i|x)} = \dfrac{\mathrm{P(x|C_i)}\mathrm{P(C_i)}}{\mathrm{P(x)}}$$
Di mana $$P(C_i|x)$$ adalah probabilitas kelas $$C_i$$ diberikan nilai fitur x, $$P(x|C_i)$$ adalah probabilitas nilai fitur x diberikan kelas $$C_i$$, $$P(Ci)$$ adalah probabilitas prior kelas $$C_i$$ dan $$P(x)$$ adalah probabilitas dari nilai fitur x.

### _Tahapan Pemodelan_
**1. Menguji akurasi dari keempat model**\
Keempat model yang dipilih diuji dengan metrik akurasi, precision, dan recall dengan data uji sebanyak 20% dari keseluruhan data bersih. Cuplikan hasil akurasi dari keempat model yang didapat adalah sebagai berikut:

Tabel 2. Hasil Akurasi Keempat Model
| Model              |  Accuracy  | 
| :---               |  :------:  | 
| _Random Forest_    |  0.988764  |  
| _Decision Tree_    |  0.981273  |  
| _KNN_              |  0.917603  | 
| _Gaussian NB_      |  0.910112  | 

**2. Peng-upgrade-an model dengan akumulasi nilai metrik tertinggi**\
Model yang memenuhi kriteria tersebut adalah model _Random Forest_. Model tsb akan di-tune dengan metode randomized _search_ _cross validation_ dengan mempertimbangkan parameter dari _Random Forest_ yaitu : `n_estimators`, `min_sample_split`, `min_sample_leaf`, `max_feature`, `max_depth`, dan `bootstrap`. Hasil yang diperoleh dari metode validasi silang ini adalah beberapa nilai parameter sebagai berikut :

Tabel 3. Nilai dari Parameter yang Didapat
| Parameter           |  Nilai  | 
| :---                |  ----:  | 
| n_estimators        |  600    |  
| min_sample_split    |  5      |  
| min_sample_leaf     |  1      | 
| max_feature         |  'sqrt' | 
| max_depth           |  60     | 
| bootstrap           |  False  | 


## Evaluation
Metrik yang digunakan dalam tahap evaluasi model adalah accuracy. 
 Dalam notasi matematis:

$$\text{Accuracy = $\dfrac{TP + TN}{TP + TN + FP + FN}$ }$$

Di mana:
- TP adalah True Positives (instansi data positif yang diprediksi dengan benar),
- TN adalah True Negatives (instansi data negatif yang diprediksi dengan benar),
- FP adalah False Positives (instansi data negatif yang salah diprediksi sebagai positif), dan
- FN adalah False Negatives (instansi data positif yang salah diprediksi sebagai negatif).
 
### _Hasil Proyek_
Berikut merupakan hasil evaluasi keempat model dengan metrik accuracy, precision dan recall

| Model            |  Accuracy  |  Precision |   Recall  |
| :---             |  :------:  |  :------:  |  :------: |
| _Random Forest_    |  0.988764  |  0.989121  |  0.988764 |
| _Decision Tree_    |  0.981273  |  0.983263  |  0.981273 |
| KNN              |  0.917603  |  0.915193  |  0.917603 |
| _Gaussian NB_      |  0.910112  |  0.929939  |  0.910112 |

Gambar 16. Evaluasi keempat model dengan 3 metrik\
![Evaluation](/vis/eval/acc.png "Evaluasi keempat model dengan 3 metrik")

Analisis ini menunjukkan bahwa _Random Forest_ dan _Decision Tree_ adalah model terbaik berdasarkan performa yang diberikan pada dataset ini, namun _Random Forest_ sedikit unggul dalam hal akurasi. Namun, keputusan akhir dalam pemilihan model harus mempertimbangkan tidak hanya performa, tetapi juga kebutuhan spesifik dari aplikasi atau kasus penggunaan yang diperlukan.

Dengan demikian, model yang dipilih adalah _Random Forest_ dan dari hasil upgrade model, model menghasilkan akurasi sebesar 99,6% dimana ini sudah melebihi ekspektasi untuk memenuhi salah satu tujuan proyek.

## Referensi
### _Data_
[1] https://katalog.data.go.id/dataset/indeks-standar-pencemaran-udara-ispu-tahun-20101\
[2] https://katalog.data.go.id/dataset/indeks-standar-pencemaran-udara-ispu-tahun-20141\
[3] https://katalog.data.go.id/dataset/indeks-standar-pencemaran-udara-ispu-tahun-20161\
[4] https://katalog.data.go.id/dataset/indeks-standar-pencemaran-udara-ispu-tahun-20171\
[5] https://katalog.data.go.id/dataset/indeks-standar-pencemaran-udara-ispu-tahun-20181\
[6] https://katalog.data.go.id/dataset/indeks-standar-pencemaran-udara-ispu-tahun-20211

### _Jurnal_
[1] [P. A. D. Oktavia, D. Yunitasari, L. Yuliati, "Pengaruh Pertumbuhan Ekonomi dan Pertumbuhhan Penduduk terhadap Kualitas Udara di Kawasan Gerbangkertosusila", ekopem, vol. 4, no. 4, pp. 1-9, Jul. 2022.]()\
[2] [S. Maharani and W. R. Aryanta, “Dampak Buruk Polusi Udara Bagi Kesehatan Dan Cara Meminimalkan Risikonya”, jeco, vol. 3, no. 2, pp. 47–58, Aug. 2023.](https://e-journal.unmas.ac.id/index.php/jeco/article/view/7035/5538)

