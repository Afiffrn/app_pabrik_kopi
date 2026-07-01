import pandas as pd
import numpy as np

print ("Membuat sekeranjanga data kopi kotor untuk bahan simulasi")

data_kotor = {
    'ukuran_mm': [10.2, np.nan, 8.5, -5.0, 9.0, np.nan, 11.0, 7.5, 99.0, 8.8],
    'tingkat_gelap': [70.0, 65.0, np.nan, 80.0, 75.0, 15.0, 68.0, np.nan, 72.0, 85.0],
    'target_kualitas': [1, 1, 1, 0, 1, 0, 1, 0, 0, 1] 
}

df_kotor = pd.DataFrame(data_kotor)
df_kotor.to_csv("data_kopi_kotor.csv", index = False)
print(" Sukses! File 'data_kopi_kotor.csv' yang penuh penyakit berhasil di buat !" )