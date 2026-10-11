# Studi Kasus 3 — Sistem Keamanan Akun & Audit Log Login

## Masalah yang Diselesaikan
Login harus memenuhi aturan format ketat dan setiap percobaan (berhasil/gagal)
tercatat otomatis tanpa mengotori logika utama.

**Aturan:**
- Username: minimal 5 karakter, hanya huruf dan angka.
- Password: minimal 8 karakter dan memuat minimal satu angka.

## Konsep Python yang Digunakan
- **RegEx (`re`)** — validasi format username dan password.
- **Decorator & Closure** — `audit_log` membungkus fungsi `login` untuk mencatat
  timestamp, username, dan status (BERHASIL / DITOLAK + alasan).
- **`@property`** — enkapsulasi atribut `username` dan `password` pada class `User`.

## Skenario Pengujian (di `main.py`)
1. Gagal: format username tidak sesuai.
2. Gagal: password terlalu pendek / tanpa angka.
3. Berhasil: semua kriteria terpenuhi.

## Cara Menjalankan
```bash
cd case-03-login-security
python main.py
```

## Bukti Eksekusi
![Output program](output.png)
