# Studi Kasus 2 — Streaming Data Sensor IoT Hemat Memori

## Masalah yang Diselesaikan
Stasiun cuaca mengirim ribuan bacaan suhu per jam. Memuat semuanya ke satu
list akan menguras RAM. Program ini memproduksi dan memproses data **satu per
satu** secara streaming, lalu mengategorikan tiap suhu:
Dingin (< 20°C), Normal (20–30°C), Panas (> 30°C).

## Konsep Python yang Digunakan
- **Generator Function & `yield`** — menghasilkan data suhu secara bertahap.
- **Iterator Pattern** — konsumsi data dengan `for` / `next()`.
- **Efisiensi Memori** — tidak ada list raksasa; data hidup hanya saat diproses.

## Cara Menjalankan
```bash
cd case-02-iot-generator
python main.py
```

## Bukti Eksekusi
![Output program](output.png)
