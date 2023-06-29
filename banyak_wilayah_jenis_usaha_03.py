import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = pd.read_csv('data/data.csv')

# Menghitung jumlah wilayah yang memiliki jenis usaha
count_by_wilayah = data.groupby('wilayah')['jenis_usaha'].size()

# Mengatur ukuran grafik
plt.figure(figsize=(10, 6))

# Membuat grafik batang dengan warna yang ditentukan
count_by_wilayah.plot(kind='bar', color=['#FFCE54', '#FC6E51', '#A0D468', '#4FC1E9', '#ED5565'])

# Mengatur label sumbu x dan y
plt.xlabel('Wilayah')
plt.ylabel('Jumlah Jenis Usaha')

# Memberikan judul grafik
plt.title('Jumlah Wilayah yang Memiliki Jenis Usaha di Jakarta', fontsize=14, fontweight='bold')

# Mengubah tampilan label sumbu x menjadi vertikal
plt.xticks(rotation='horizontal')

# Menampilkan grafik
plt.show()
