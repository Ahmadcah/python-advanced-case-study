# Studi Kasus 1 — Analisis Nilai Mahasiswa

## Masalah yang Diselesaikan
Bagian akademik menerima data nilai mahasiswa dalam bentuk list of dictionary.
Program ini menghitung nilai akhir (Tugas 30%, UTS 30%, UAS 40%), menyaring
mahasiswa berprestasi (nilai akhir > 80), membuat ranking, dan mengumumkan
mahasiswa terbaik — tanpa perulangan `for` bertingkat.

## Konsep Python yang Digunakan
- **List Comprehension** — menghitung nilai akhir dan memfilter data secara ringkas.
- **Lambda Function** — sebagai `key` pada `sorted()`.
- **Filtering & Sorting** — `sorted(..., key=lambda ..., reverse=True)` untuk ranking.

## Cara Menjalankan
```bash
cd case-01-analisis-nilai
python main.py
```

## Bukti Eksekusi
![Output program](output.png)
