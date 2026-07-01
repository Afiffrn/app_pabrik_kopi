import pandas as pd
from sklearn.model_selection import train_test_split
# KODE BARU: Kita impor pawang Hutan Acak dari Scikit-Learn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

print("📥 [LANGKAH 1] Membaca Datasheet SUCI Hasil Bedah Dokter Data...")
# Kita gunakan file hasil pembersihan dokter_data.py kemarin
df_pabrik = pd.read_csv("data_kopi_pabrik.csv")

X = df_pabrik[['ukuran_mm', 'tingkat_gelap']]
y = df_pabrik['target_kualitas']

print("🪓 [LANGKAH 2] Memotong Data (Train-Test Split) secara Adil...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2, 
    random_state=42, 
    stratify=y
)

print("🌲 [LANGKAH 3] Melatih Model RANDOM FOREST (Hutan Cerita) di Area Latihan...")
# KODE BARU: Memanggil RandomForestClassifier dengan 100 pohon (n_estimators=100)
model_industri = RandomForestClassifier(
    n_estimators=100,    # Jumlah total dokter/pohon di dalam forum voting
    random_state=42      # Mengunci keacakan pola agar hasil konsisten
)
model_industri.fit(X_train, y_train)

print("📊 [LANGKAH 4] Menguji Kecerdasan Hutan AI Melalui Ujian Digital...")
prediksi_ujian = model_industri.predict(X_test)

skor_akurasi = accuracy_score(y_test, prediksi_ujian)
print("\n==================================================")
print("📝 LAPORAN EVALUASI MODEL RANDOM FOREST UNTUK BOS")
print("==================================================")
print(f"🎯 Tingkat Akurasi Hutan AI: {skor_akurasi * 100:.2f}%")
print("\n🔍 Tabel Analisis Detail (Precision & Recall):")
print(classification_report(y_test, prediksi_ujian, target_names=['Lokal', 'Premium']))
print("--------------------------------------------------\n")

if skor_akurasi >= 0.70:
    print("📦 [LANGKAH 5] Mengekstrak Otak Hutan AI Baru ke .joblib...")
    # File eksternal ini otomatis akan berisi memori kolektif dari 100 pohon!
    joblib.dump(model_industri, "otak_kopi_industri.joblib")
    print("✅ SELESAI! Model Hutan Acak siap digunakan di website Streamlit!")
else:
    print("❌ [GAGAL] Akurasi di bawah standar pabrik!")