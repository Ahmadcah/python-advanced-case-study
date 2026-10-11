"""Studi Kasus 2 - Streaming Data Sensor IoT Hemat Memori."""

import random

SUHU_MIN = 15.0
SUHU_MAX = 38.0
JUMLAH_BACAAN = 10  # minimal 10


def sensor_suhu(jumlah):
    """Generator: hasilkan `jumlah` suhu acak antara SUHU_MIN dan SUHU_MAX.

    Hint: gunakan `yield` di dalam loop, jangan simpan ke list.
    """
    for _ in range(jumlah):
        yield round(random.uniform(SUHU_MIN, SUHU_MAX), 2)


def kategori_suhu(suhu):
    """Kembalikan 'Dingin' (<20), 'Normal' (20-30), atau 'Panas' (>30)."""
    if suhu < 20:
        return "Dingin"
    if suhu <= 30:
        return "Normal"
    return "Panas"


def main():
    # TODO:
    # 1. buat generator: pembaca = sensor_suhu(JUMLAH_BACAAN)
    # 2. konsumsi satu per satu (for loop atas generator ATAU next(pembaca))
    # 3. cetak: nomor bacaan | suhu | kategori, dengan format rapi
    # Bonus: tunjukkan next() manual sekali, dan tangkap StopIteration
    pembaca = sensor_suhu(JUMLAH_BACAAN)

    print("--- Streaming Data Sensor IoT ---")
    try:
        suhu_awal = next(pembaca)
        print(f"Bacaan manual: {suhu_awal:.2f} | {kategori_suhu(suhu_awal)}")
    except StopIteration:
        print("Generator sudah habis.")
        return

    print("{:<10} {:>8} {:>10}".format("No", "Suhu", "Kategori"))
    print(f"{1:<10} {suhu_awal:>8.2f} {kategori_suhu(suhu_awal):>10}")
    for nomor, suhu in enumerate(pembaca, start=2):
        print(f"{nomor:<10} {suhu:>8.2f} {kategori_suhu(suhu):>10}")


if __name__ == "__main__":
    main()
