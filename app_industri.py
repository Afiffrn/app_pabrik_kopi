import streamlit as st
import pandas as pd
import joblib

# Tampilan Header Dashboard Pabrik
st.title("🏭 Dashboard AI Sortir Kopi Otomatis")
st.write("Sistem Interface Produksi Massal - Model Verifikasi Industri")

st.write("---")

# Form Input Data Baru dari Sensor Pabrik
st.subheader("📥 Ambil Sampel Data Sensor Terkini:")
ukuran = st.number_input("Dimensi Ukuran Biji Kopi (mm):", min_value=1.0, max_value=20.0, value=7.5, step=0.1)
gelap = st.number_input("Tingkat Kegelapan Warna Biji (%):", min_value=1.0, max_value=100.0, value=60.0, step=1.0)

# Load Otak AI Hasil Validasi SOP 2
try:
    model_ai = joblib.load("otak_kopi_industri.joblib")
    
    # Bungkus Input ke DataFrame (Nama kolom WAJIB sama dengan nama kolom di CSV luar tadi!)
    data_input = pd.DataFrame([{
        'ukuran_mm': ukuran,
        'tingkat_gelap': gelap
    }])

    # Eksekusi Prediksi Kilat
    prediksi = model_ai.predict(data_input)[0]

    st.write("---")
    st.subheader("🤖 Keputusan Otomatis Otak AI:")
    
    if prediksi == 1:
        st.success("STATUS BIJI KOPI: **PREMIUM (Lolos Standar Ekspor! ✈️)**")
    else:
        st.warning("STATUS BIJI KOPI: **LOKAL (Alokasikan ke Gudang Domestik 🏪)**")

except FileNotFoundError:
    st.error("🚨 File 'otak_kopi_industri.joblib' belum ditemukan! Jalankan script 'latih_ai_industri.py' terlebih dahulu di terminal.")