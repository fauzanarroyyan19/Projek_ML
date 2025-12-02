📘 README – Aplikasi Prediksi Kolektibilitas Nasabah (Machine Learning)

Aplikasi ini digunakan untuk melakukan prediksi tingkat kolektibilitas nasabah (1–5) menggunakan model Machine Learning yang telah dilatih sebelumnya.
Pengguna cukup memasukkan data keuangan nasabah, lalu aplikasi akan menghasilkan prediksi kolektibilitas secara otomatis.

🚀 Cara Menjalankan Aplikasi
1️⃣ Install Dependensi

Pastikan sudah menginstal Python 3.10+
Lalu install modul yang dibutuhkan:

pip install fastapi uvicorn joblib numpy pydantic

2️⃣ Jalankan API Machine Learning

Pastikan file berikut berada satu folder:

main.py → file API FastAPI

model_kolektibilitas.pkl → model ML

feature_columns.pkl → daftar fitur

Lalu jalankan:

uvicorn main:app --reload


API akan berjalan di:

http://127.0.0.1:8000


Endpoint utama untuk prediksi:

POST /predict

3️⃣ Cara Mengirim Data untuk Prediksi

Gunakan aplikasi frontend (index.html) atau bisa juga uji manual seperti berikut:

Contoh JSON:
{
  "data": {
    "TOTAL POKOK": 10000000,
    "OS POKOK": 5000000,
    "TUNGGAKAN POKOK": 0,
    "JUMLAH HARI TUNGGAKAN": 5,
    "EIR": 12.5,
    "TUNGGAKAN BUNGA": 0,
    "UTILIZE RATE": 60,
    "STAGE_Stage 2": 0,
    "STAGE_Stage 3": 0
  }
}

🖥️ Cara Menggunakan Website (Frontend)

Buka file index.html di browser.

Masukkan semua nilai input sesuai form:

TOTAL POKOK

OS POKOK

TUNGGAKAN POKOK

JUMLAH HARI TUNGGAKAN

EIR

TUNGGAKAN BUNGA

UTILIZE RATE

STAGE 2

STAGE 3

Klik Prediksi Sekarang.

Hasil prediksi → muncul angka 1 sampai 5.

🎯 Makna Hasil Prediksi
Nilai	Arti Kolektibilitas
1	Lancar
2	Dalam Perhatian Khusus
3	Kurang Lancar
4	Diragukan
5	Macet

Model mengembalikan angka yang menunjukkan tingkat risiko.
Semakin tinggi angka → semakin berisiko.

📄 Struktur Folder
project-folder/
│── main.py
│── index.html
│── model_kolektibilitas.pkl
│── feature_columns.pkl
│── README.md

🙌 Selesai!
