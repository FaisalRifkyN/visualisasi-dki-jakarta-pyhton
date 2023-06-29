import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = pd.read_csv('data/data.csv')

# Menghitung jumlah jenis usaha di setiap kecamatan
count_by_kecamatan = data.groupby('kecamatan')['jenis_usaha'].size()

# Mengatur ukuran grafik
plt.figure(figsize=(10, 6))

# Membuat grafik batang horizontal dengan warna yang berbeda
count_by_kecamatan.plot(kind='barh', color=['#FFCE54', '#FC6E51', '#A0D468', '#4FC1E9', '#ED5565'])

# Mengatur label sumbu x dan y
plt.xlabel('Jumlah Jenis Usaha')
plt.ylabel('Kecamatan')

# Memberikan judul grafik
plt.title('Sebaran Jenis Usaha di Setiap Kecamatan di Jakarta', fontsize=14, fontweight='bold')

# Menghilangkan garis di sekeliling grafik
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Menampilkan grafik
plt.show()
