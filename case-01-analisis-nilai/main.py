"""Studi Kasus 1 - Analisis Nilai Mahasiswa."""

BOBOT_TUGAS = 0.30
BOBOT_UTS = 0.30
BOBOT_UAS = 0.40
BATAS_PRESTASI = 80

data_mahasiswa = [
    {"nama": "Aisyah", "nim": "230101", "tugas": 85, "uts": 80, "uas": 88},
    {"nama": "Budi", "nim": "230102", "tugas": 70, "uts": 65, "uas": 75},
    {"nama": "Cantika", "nim": "230103", "tugas": 90, "uts": 85, "uas": 92},
    {"nama": "Dewi", "nim": "230104", "tugas": 78, "uts": 82, "uas": 80},
    {"nama": "Edo", "nim": "230105", "tugas": 95, "uts": 90, "uas": 93},
]


def hitung_nilai_akhir(data):
    """Kembalikan list baru: tiap dict ditambah key 'nilai_akhir'.

    Hint: list comprehension + {**mhs, "nilai_akhir": ...}
    """
    return [
        {
            **mahasiswa,
            "nilai_akhir": (
                mahasiswa["tugas"] * BOBOT_TUGAS
                + mahasiswa["uts"] * BOBOT_UTS
                + mahasiswa["uas"] * BOBOT_UAS
            ),
        }
        for mahasiswa in data
    ]


def filter_berprestasi(data):
    """Mahasiswa dengan nilai_akhir > BATAS_PRESTASI.

    Hint: list comprehension dengan kondisi `if`, atau filter() + lambda.
    """
    return [mahasiswa for mahasiswa in data if mahasiswa["nilai_akhir"] > BATAS_PRESTASI]


def buat_ranking(data):
    """Urutkan dari nilai_akhir tertinggi ke terendah.

    Hint: sorted(..., key=lambda m: ..., reverse=True)
    """
    return sorted(data, key=lambda mahasiswa: mahasiswa["nilai_akhir"], reverse=True)


def main():
    # TODO: panggil fungsi di atas lalu cetak hasilnya dengan rapi:
    # 1. tabel nilai akhir semua mahasiswa
    # 2. daftar mahasiswa berprestasi
    # 3. ranking
    # 4. mahasiswa terbaik (nama, NIM, nilai tugas/uts/uas, nilai akhir)
    data_nilai = hitung_nilai_akhir(data_mahasiswa)
    mahasiswa_berprestasi = filter_berprestasi(data_nilai)
    ranking = buat_ranking(data_nilai)
    mahasiswa_terbaik = max(ranking, key=lambda m: m["nilai_akhir"])

    print("Case 1 - Tabel Nilai Akhir Mahasiswa")
    print("{:<8} {:<8} {:>8} {:>8} {:>8} {:>12}".format(
        "NAMA", "NIM", "TUGAS", "UTS", "UAS", "NILAI AKHIR"
    ))
    for mahasiswa in data_nilai:
        print("{:<8} {:<8} {:>8} {:>8} {:>8} {:>12.2f}".format(
            mahasiswa["nama"],
            mahasiswa["nim"],
            mahasiswa["tugas"],
            mahasiswa["uts"],
            mahasiswa["uas"],
            mahasiswa["nilai_akhir"],
        ))

    print("\nCase 2 - Daftar Mahasiswa Berprestasi")
    if mahasiswa_berprestasi:
        for mahasiswa in mahasiswa_berprestasi:
            print(f"{mahasiswa['nama']} ({mahasiswa['nim']}): {mahasiswa['nilai_akhir']:.2f}")
    else:
        print("Tidak ada mahasiswa yang berprestasi.")

    print("\nCase 3 - Ranking Mahasiswa")
    for index, mahasiswa in enumerate(ranking, start=1):
        print(f"{index}. {mahasiswa['nama']} ({mahasiswa['nim']}): {mahasiswa['nilai_akhir']:.2f}")

    print("\nMahasiswa Terbaik")
    print(
        f"Nama: {mahasiswa_terbaik['nama']}\n"
        f"NIM: {mahasiswa_terbaik['nim']}\n"
        f"Nilai Tugas: {mahasiswa_terbaik['tugas']}\n"
        f"Nilai UTS: {mahasiswa_terbaik['uts']}\n"
        f"Nilai UAS: {mahasiswa_terbaik['uas']}\n"
        f"Nilai Akhir: {mahasiswa_terbaik['nilai_akhir']:.2f}"
    )


if __name__ == "__main__":
    main()
