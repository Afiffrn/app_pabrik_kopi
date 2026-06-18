import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

print(" 1. Membaca Datasheet Eksternal menggunakan Pandas")

df_pabrik = pd.read_csv("data_kopi_pabrik.csv")

print("\n--- Isi 5 data teratas dari CSV")
print(df_pabrik.head())
print("-=================================-")

X = df_pabrik[['ukuran_mm', "tingkat_gelap"]]
y = df_pabrik['target_kualitas']

print(" Melatih Model otak AI (Decision Tree)")
model_industri = DecisionTreeClassifier()
model_industri.fit(X, y)

print("Mengekstrak Model AI menjadi file Eksternal (.joblib)")

joblib.dump(model_industri, "otak_kopi_industri.joblib")

print("Selesai File 'otak_kopi_industri.joblib' sukses menetas dari data CSV !")

