import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = pd.read_csv('data/data.csv')

# Menghitung jumlah jenis usaha
counts = data.groupby('jenis_usaha').size()

# Mengatur ukuran grafik
plt.figure(figsize=(10, 6))

# Menentukan warna yang akan digunakan pada grafik
colors = ['#FFCE54', '#FC6E51', '#A0D468', '#4FC1E9', '#ED5565']

# Membuat grafik pie chart
counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=colors, wedgeprops={'linewidth': 2, 'edgecolor': 'white'})

# Memberikan judul grafik
plt.title('Jenis Usaha di Jakarta', fontweight='bold')

# Mengubah tulisan label menjadi vertikal
plt.xticks(rotation='vertical')

# Mengatur font size label
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Menghilangkan kotak spines di sekitar grafik
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.gca().spines['left'].set_visible(False)

# Menampilkan grafik
plt.show()
