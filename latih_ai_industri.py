import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

print("📥 [LANGKAH 1] Membaca Datasheet Baru dari Kopi Pabrik...")
df_pabrik = pd.read_csv("data_kopi_pabrik.csv")

# Memisahkan Fitur (X) dan Target (y)
X = df_pabrik[['ukuran_mm', 'tingkat_gelap']]
y = df_pabrik['target_kualitas']

print("🪓 [LANGKAH 2] Memotong Data (Train-Test Split) dengan Keadilan Sosial (Stratify)...")
# Di sini kuncinya! Kita potong data secara adil agar proporsi target seimbang
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2,       # 20% disimpan rapat-rapat untuk ujian
    random_state=42,     # Mengunci pola acak agar hasil konsisten
    stratify=y           # Menjaga proporsi Premium & Lokal tetap adil
)

print("🧠 [LANGKAH 3] Melatih Model Menggunakan Data Latihan (X_train)...")
model_industri = DecisionTreeClassifier(random_state=42)
model_industri.fit(X_train, y_train)

print("📊 [LANGKAH 4] Menguji Kecerdasan AI Melalui Ujian Digital...")
prediksi_ujian = model_industri.predict(X_test)

# Hitung Akurasi Asli berdasarkan data ujian murni
skor_akurasi = accuracy_score(y_test, prediksi_ujian)
print("\n==================================================")
print("📝 LAPORAN EVALUASI STANDAR INDUSTRI UNTUK ATASAN")
print("==================================================")
print(f"🎯 Tingkat Akurasi Model: {skor_akurasi * 100:.2f}%")
print("\n🔍 Tabel Analisis Detail (Classification Report):")
print(classification_report(y_test, prediksi_ujian, target_names=['Lokal', 'Premium']))
print("--------------------------------------------------\n")

# Syarat Ekstraksi: Hanya jika akurasi lolos standar (Misal minimal 70%)
if skor_akurasi >= 0.70:
    print("📦 [LANGKAH 5] Lolos Sensor! Mengekstrak Otak AI Segar ke .joblib...")
    joblib.dump(model_industri, "otak_kopi_industri.joblib")
    print("✅ SELESAI! Model teruji siap digunakan di lapangan!")
else:
    print("❌ [GAGAL] Akurasi di bawah standar. Harap periksa dataset kembali!")