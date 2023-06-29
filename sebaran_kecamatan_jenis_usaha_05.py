import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = pd.read_csv('data/data.csv')

# Menghitung jumlah kecamatan yang memiliki jenis usaha pada setiap wilayah
count_by_wilayah_kecamatan = data.groupby(['wilayah', 'kecamatan'])['jenis_usaha'].size().reset_index()

# Mengatur ukuran grafik
plt.figure(figsize=(10, 6))

# Membuat grafik bar terpisah untuk setiap kecamatan
for wilayah in count_by_wilayah_kecamatan['wilayah'].unique():
    kecamatan_data = count_by_wilayah_kecamatan[count_by_wilayah_kecamatan['wilayah'] == wilayah]
    plt.bar(kecamatan_data['kecamatan'], kecamatan_data['jenis_usaha'], label=wilayah)

# Mengatur label sumbu x dan y
plt.xlabel('Kecamatan')
plt.ylabel('Jumlah Usaha')

# Memberikan judul grafik
plt.title('Sebaran Usaha pada Setiap Kecamatan di Jakarta', fontsize=14, fontweight='bold')

# Mengubah tampilan label sumbu x menjadi vertikal
plt.xticks(rotation='vertical')

# Menampilkan legenda
plt.legend(title='Wilayah')

# Menghilangkan garis di sekeliling grafik
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Menampilkan grafik
plt.show()
