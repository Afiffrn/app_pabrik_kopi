import pandas as pd

print("📥 1. Membaca data kotor dari mesin sensor...")
df = pd.read_csv("data_kopi_kotor.csv")
print("=== ISI DATA MENTAH ===")
print(df)
print("=======================\n")

print("🪓 2. URUTAN BARU: Karantina & Buang Data Rusak (Outliers) Terlebih Dahulu!")
# Kita saring di awal: Hanya ambil ukuran yang masuk akal (0 s.d. 20) ATAU yang masih bolong (NaN)
# Catatan: df['ukuran_mm'].isna() wajib dimasukkan agar data bolong tidak ikut terbuang di fase ini
df_filter = df[((df['ukuran_mm'] > 0) & (df['ukuran_mm'] < 20)) | (df['ukuran_mm'].isna())]
print("✅ Data rusak (-5.0 dan 99.0) berhasil ditendang dari laboratorium!")
print("-------------------------------------------------------\n")

print("🩹 3. Menghitung Rata-rata dari Data Yang Benar-Benar Sehat...")
# Sekarang kita hitung mean dari data yang sudah bersih dari angka ekstrim 99.0
rata_ukuran_sehat = df_filter['ukuran_mm'].mean()
rata_gelap_sehat = df_filter['tingkat_gelap'].mean()

print(f"💡 Nilai Tambal Ukuran Baru (Murni): {rata_ukuran_sehat:.3f} mm (Bukan 18.625 lagi!)")
print(f"💡 Nilai Tambal Gelap Baru (Murni): {rata_gelap_sehat:.3f}%")
print("-------------------------------------------------------\n")

print("🩹 4. Menambal Data Bolong Menggunakan Nilai Murni...")
# Selesaikan penambalan menggunakan nilai rata-rata murni yang logis
df_filter['ukuran_mm'] = df_filter['ukuran_mm'].fillna(rata_ukuran_sehat)
df_filter['tingkat_gelap'] = df_filter['tingkat_gelap'].fillna(rata_gelap_sehat)
print("✅ Selesai ditambal dengan angka realistis!")
print("-------------------------------------------------------\n")

print("=== ISI DATA AKHIR SIAP LATIH ===")
# Karena baris indeks 1 dan 5 yang tadinya NaN sekarang ditambal angka murni, kita bersihkan sisa karatnya
df_bersih_total = df_filter.dropna() # Memastikan tidak ada NaN tersisa di kolom lain
print(df_bersih_total)
print("=================================\n")

df_bersih_total.to_csv("data_kopi_siap_latih.csv", index=False)
print("🚀 Selesai! File 'data_kopi_siap_latih.csv' versi REFORMASI LOGIKA siap digunakan AI!")