# Entity Relationship Diagram


## Deskripsi Database

Database digunakan untuk menyimpan data historis pengunjung dan hasil prediksi jumlah pengunjung.


# Entity 1: Visitor History


| Field | Type | Key | Deskripsi |
|-|-|-|-|
| id | Integer | PK | Identitas data |
| visit_date | Date | - | Tanggal kunjungan |
| visit_day | String | - | Hari kunjungan |
| visitor_total | Integer | - | Jumlah pengunjung aktual |



# Entity 2: Prediction Result


| Field | Type | Key | Deskripsi |
|-|-|-|-|
| id | Integer | PK | Identitas prediksi |
| visitor_history_id | Integer | FK | Referensi data historis |
| visit_day | String | - | Hari yang diprediksi |
| prediction_value | Integer | - | Hasil prediksi |
| created_at | Datetime | - | Waktu prediksi |



# Relasi Antar Entity


Visitor History

memiliki banyak

Prediction Result



Relasi:

Visitor History (1) ---- (N) Prediction Result



# ERD Diagram


```mermaid

erDiagram


VISITOR_HISTORY ||--o{ PREDICTION_RESULT : menghasilkan


VISITOR_HISTORY {

int id PK

date visit_date

string visit_day

int visitor_total

}



PREDICTION_RESULT {

int id PK

int visitor_history_id FK

string visit_day

int prediction_value

datetime created_at

}
