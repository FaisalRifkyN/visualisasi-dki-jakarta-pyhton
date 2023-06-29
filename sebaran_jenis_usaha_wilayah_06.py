import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = pd.read_csv('data/data.csv')

# Menghitung jumlah jenis usaha pada setiap wilayah
count_by_wilayah_usaha = data.groupby(['wilayah', 'jenis_usaha']).size().unstack()

# Mengatur ukuran grafik
plt.figure(figsize=(10, 6))

# Mendapatkan daftar wilayah
wilayah = count_by_wilayah_usaha.index

# Mendapatkan daftar jenis usaha
jenis_usaha = count_by_wilayah_usaha.columns

# Menghitung jumlah jenis usaha pada setiap wilayah
count = len(wilayah)
width = 0.8 / len(jenis_usaha)

# Mengatur posisi x pada setiap bar
x = []
for i in range(count):
    x.append([j + width * i for j in range(len(jenis_usaha))])

# Membuat grafik bar terpisah untuk setiap jenis usaha
for i in range(count):
    plt.bar(x[i], count_by_wilayah_usaha.iloc[i], width=width, label=wilayah[i])

# Mengatur label sumbu x dan y
plt.xlabel('Jenis Usaha')
plt.ylabel('Jumlah Usaha')

# Memberikan judul grafik
plt.title('Sebaran Jenis Usaha di Setiap Wilayah di Jakarta')

# Mengatur tampilan label sumbu x menjadi vertikal
plt.xticks([j + width * (count-1) / 2 for j in range(len(jenis_usaha))], jenis_usaha, rotation='vertical')

# Mengatur ukuran sumbu y
plt.ylim(0, 150)  # Ubah batas atas sumbu y sesuai kebutuhan

# Menampilkan legenda
plt.legend(title='Wilayah')

# Menghilangkan garis di sekeliling grafik
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Menampilkan grafik
plt.show()
