# 🧠 Prediksi Kolektibilitas Nasabah (Machine Learning + FastAPI)

Aplikasi ini digunakan untuk melakukan **prediksi kolektibilitas nasabah** menggunakan model Machine Learning yang telah dilatih.  
Frontend dibuat dengan HTML/JavaScript, dan backend menggunakan FastAPI.

---

## 📌 1. Cara Menjalankan Backend (FastAPI)

### **1️⃣ Install semua dependensi**
Pastikan sudah install Python 3.9+

```bash
pip install fastapi uvicorn joblib numpy pydantic
```

### **2️⃣ Letakkan file model**
Pastikan file berikut ada di satu folder:
- `model_kolektibilitas.pkl`
- `feature_columns.pkl`
- `main.py` (backend)

### **3️⃣ Jalankan server FastAPI**
```bash
uvicorn main:app --reload
```

Jika berhasil, muncul:
```
API is running at http://127.0.0.1:8000
```

---

## 📌 2. Cara Menjalankan Frontend (index.html)

### **1️⃣ Buka file `index.html` secara langsung**
Cukup klik dua kali → file akan terbuka di browser.

### **2️⃣ Masukkan nilai fitur**
Isi seluruh kolom pada form:
- TOTAL POKOK  
- OS POKOK  
- TUNGGAKAN POKOK  
- JUMLAH HARI TUNGGAKAN  
- EIR  
- TUNGGAKAN BUNGA  
- UTILIZE RATE  
- STAGE_Stage 2  
- STAGE_Stage 3  

Setelah itu klik:

```
Prediksi Sekarang
```

---

## 📌 3. Contoh Input Data (Untuk Testing)

Gunakan data berikut untuk mencoba prediksi:

```
TOTAL POKOK: 10000000  
OS POKOK: 5000000  
TUNGGAKAN POKOK: 200000  
JUMLAH HARI TUNGGAKAN: 15  
EIR: 18.5  
TUNGGAKAN BUNGA: 75000  
UTILIZE RATE: 0.82  
STAGE_Stage 2: 0  
STAGE_Stage 3: 0  
```

---

## 📌 4. Endpoint API

### **POST /predict**

**Request Body:**
```json
{
  "data": {
    "TOTAL POKOK": 10000000,
    "OS POKOK": 5000000,
    "TUNGGAKAN POKOK": 200000,
    "JUMLAH HARI TUNGGAKAN": 15,
    "EIR": 18.5,
    "TUNGGAKAN BUNGA": 75000,
    "UTILIZE RATE": 0.82,
    "STAGE_Stage 2": 0,
    "STAGE_Stage 3": 0
  }
}
```

**Response:**
```json
{
  "prediction": 3
}
```

---

## 📌 5. Arti Nilai Prediksi (1–5)

| Nilai | Arti Kolektibilitas |
|------|----------------------|
| **1** | Lancar (pembayaran aman) |
| **2** | Dalam perhatian khusus |
| **3** | Kurang lancar |
| **4** | Diragukan |
| **5** | Macet / Risiko tinggi |

---

## 📌 6. Struktur Folder

```
project/
│── main.py
│── model_kolektibilitas.pkl
│── feature_columns.pkl
│── index.html
│── penjelasan.html
└── README.md
```

---

## 📌 7. Catatan

- Pastikan backend **sudah berjalan** sebelum halaman HTML dipakai.
- Jika frontend error CORS, jalankan FastAPI dengan CORS aktif.

---

Jika mau, gue bisa bikinin:
✅ README versi English  
✅ README lengkap dengan screenshot  
✅ README dengan badge GitHub

Tinggal bilang aja! 🚀🔥
