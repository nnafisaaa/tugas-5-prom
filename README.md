# Tugas PTM-05 REST API Design

## Proyek

Penerapan Algoritma XGBoost dengan Optimasi Grid Search untuk Prediksi Jumlah Pengunjung Berdasarkan Hari Kunjungan pada Wisata Religi Makam Gus Dur.


## Deskripsi Sistem

Sistem ini merupakan aplikasi berbasis website yang digunakan untuk melakukan prediksi jumlah pengunjung pada Wisata Religi Makam Gus Dur berdasarkan hari kunjungan.

Sistem menggunakan algoritma XGBoost sebagai model machine learning dengan optimasi Grid Search untuk menentukan kombinasi parameter model terbaik.


## Tujuan Sistem

Tujuan perancangan sistem:

- Membuat desain REST API untuk layanan prediksi.
- Membuat rancangan struktur data.
- Membuat rancangan database.
- Mendokumentasikan kontrak API.


## Teknologi

- Website
- REST API
- Python
- Pydantic
- XGBoost
- Grid Search


## Struktur File

| File | Fungsi |
|---|---|
| openapi.yaml | Spesifikasi endpoint REST API |
| erd.md | Rancangan Entity Relationship Diagram |
| models.py | Skema data Pydantic |
| api-contract.md | Dokumentasi desain API |
| ptm-05-prompt-log.md | Dokumentasi penggunaan AI |


## Endpoint Utama

POST /api/predict


Endpoint digunakan untuk menerima hari kunjungan dan menghasilkan prediksi jumlah pengunjung.


## Alur Sistem

User

↓

Frontend Website

↓

Backend API

↓

Prediction Service

↓

XGBoost Model

↓

Hasil Prediksi


## Pengembang

Nama:

NIM: