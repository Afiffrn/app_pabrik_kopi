import pandas as pd
import random

print("🏭 Memulai Generator Data Pabrik Kopi Versi Pintar (100 Baris) . . .")

data_100 = {
    'ukuran_mm' : [],
    'tingkat_gelap' : [],
    'target_kualitas' : []
}

for i in range(100):
    # 25% Data Premium Murni (Besar & Gelap)
    if i < 25:
        ukuran = round(random.uniform(8.0, 12.0), 2)
        gelap = round(random.uniform(60.0, 85.0), 2)
        target = 1
    # 25% Data Lokal Murni (Kecil & Terang)
    elif i < 50:
        ukuran = round(random.uniform(4.0, 7.9), 2)
        gelap = round(random.uniform(10.0, 59.0), 2)
        target = 0
    # 25% Data Anomali A: Ukuran KECIL tapi warna GELAP (Kopi gosong - Wajib Lokal!)
    elif i < 75:
        ukuran = round(random.uniform(4.0, 7.9), 2)
        gelap = round(random.uniform(60.0, 85.0), 2)
        target = 0  # <--- HUKUM JADI LOKAL
    # 25% Data Anomali B: Ukuran BESAR tapi warna TERANG (Kopi mentah - Wajib Lokal!)
    else:
        ukuran = round(random.uniform(8.0, 12.0), 2)
        gelap = round(random.uniform(10.0, 59.0), 2)
        target = 0  # <--- HUKUM JADI LOKAL

    data_100['ukuran_mm'].append(ukuran)
    data_100['tingkat_gelap'].append(gelap)
    data_100['target_kualitas'].append(target)

df = pd.DataFrame(data_100)
df.to_csv("data_kopi_pabrik.csv", index=False)

print("✅ Sukses! Datasheet baru dengan 4 variasi kelas industri berhasil dibuat!")