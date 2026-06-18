import pandas as pd
import random

print("🏭 Memulai Generator Data Pabrik Kopi (100 Baris) . . .")

data_100 = {
    'ukuran_mm' : [],
    'tingkat_gelap' : [],
    'target_kualitas' : []
}

for i in range(100):
    if i % 2 == 0:
        ukuran = round(random.uniform(8.0 , 12.0), 2)
        gelap = round(random.uniform(60.0, 85.0), 2)
        target = 1
    else:
        ukuran = round(random.uniform(4.0, 7.9), 2)
        gelap = round(random.uniform(10.0, 59.0), 2)
        target = 0

    # LURUS DI SINI! (Artinya data Premium maupun Lokal sama-sama di-append)
    data_100['ukuran_mm'].append(ukuran)
    data_100['tingkat_gelap'].append(gelap)
    data_100['target_kualitas'].append(target)

# Pastikan proses simpan CSV dan Print ini berada di LUAR for-loop (paling kiri)
df = pd.DataFrame(data_100)
df.to_csv("data_kopi_pabrik.csv", index=False)

print("✅ Sukses! File 'data_kopi_pabrik.csv' sekarang berisi 100 baris data campuran seimbang!")