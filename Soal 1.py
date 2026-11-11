"""
Seorang dosen ingin merekap nilai mahasiswa. Nilai akhir dihitung dari tugas (bobot 30%),
UTS (bobot 30%), dan UAS (bobot 40%), semuanya dalam skala 0–100. Nilai huruf ditentukan
sebagai berikut.

Nilai akhir Nilai huruf
≥ 85                A
70 s.d. < 85        B
55 s.d. < 70        C
40 s.d. < 55        D
< 40                E



Mahasiswa dinyatakan lulus jika memperoleh nilai huruf minimal C. Data lima mahasiswa
disimpan dalam daftar berikut pada program Anda.
Nama Tugas UTS UAS
Andi  80   70  90
Bunga 90   85  88
Citra 60   45  50
Dimas 75   80  65
Eka   30   40  35




(a)Tulislah program yang menampilkan tabel rekap berisi nama, nilai akhir, nilai huruf, dan
keterangan lulus atau tidak lulus untuk setiap mahasiswa. Setelah tabel, tampilkan ratarata
nilai akhir kelas dan banyaknya mahasiswa yang lulus.
(b)Program Anda harus memiliki sedikitnya empat fungsi selain main(), dengan sedikitnya
satu fungsi void dan satu fungsi non-void. Buatlah tabel rancangan fungsi dengan kolom:
nama fungsi, parameter, mengembalikan nilai atau tidak, dan tugas yang dikerjakan.
(c)Tentukan secara manual nilai akhir dan nilai huruf untuk Andi dan Dimas, lalu bandingkan
dengan keluaran program Anda.
(d)Dosen meminta tambahan fitur: menampilkan nama mahasiswa dengan nilai akhir tertinggi.
Jelaskan fungsi apa saja yang perlu Anda tambah atau ubah, dan fungsi mana yang
tidak perlu disentuh sama sekali. Kaitkan jawaban Anda dengan cara Anda mengelompokkan
kode pada bagian (b)



"""

#Definisi rekap untuk menampilkan tabel rekap berisi nama, nilai akhir, nilai huruf, dan status kelulusan masing masing mahasiswa
def rekap (data):
    print(f"{'nama'} {'nilai_akhir'} {'nilai_huruf'} {'status'}")
    for mahasiswa in data:
        print(f"{mahasiswa['nama']}" f"{mahasiswa['nilai_akhir']}" f"{mahasiswa['huruf']}" f"{mahasiswa['status']}")


def hitung_nilai_akhir (tugas, uts, uas):
    return (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)



def nilai_huruf (nilai_akhir):
    if nilai_akhir >= 85:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 55:
        return "C"
    elif nilai_akhir >= 40:
        return "D"
    else:
        return "E"


def penentu_lulus (nilai_huruf):
    if nilai_huruf in ["A", "B", "C"]:
        return "Lulus"
    else:
        return "Tidak Lulus"


def hitung_rata_rata (total, jumlah):
    return total / jumlah


def jumlah_mahasiswa_lulus (data):
    jumlah = 0
    for mahasiswa in data:
        if mahasiswa["status"] == "Lulus":
            jumlah += 1
    return jumlah


#Untuk bagian (d)(cukup menambahkan definisi baru untuk menentukan nilai tertinggi dari seluruh data nilai mahasiswa yang terbaca di dalam variabel data dari hasil perhitungan nilai akhir 3 parameter bobot penilaian)
def cari_nilai_tertinggi(data):
    nilai_mahasiswa_tertinggi = max(
        data,
        key=lambda mahasiswa: mahasiswa["nilai_akhir"]
    )
    return nilai_mahasiswa_tertinggi


def main():
    data = [
        {"nama": "Andi ", "tugas": 80, "uts": 70, "uas": 90},
        {"nama": "Bunga ", "tugas": 90, "uts": 85, "uas": 88},
        {"nama": "Citra ", "tugas": 60, "uts": 45, "uas": 50},
        {"nama": "Dimas ", "tugas": 75, "uts": 80, "uas": 65},
        {"nama": "Eka ", "tugas": 30, "uts": 40, "uas": 35},
        {"nama": "Orang 1 ", "tugas": 78, "uts": 67, "uas": 76},
        {"nama": "Orang 2 ", "tugas": 50, "uts": 56, "uas": 98},
        {"nama": "Orang 3 ", "tugas": 80, "uts": 84, "uas": 67},
        {"nama": "Orang 4 ", "tugas": 70, "uts": 94, "uas": 79},
        {"nama": "Anonimus", "tugas": 100, "uts": 100, "uas": 100}
    ]


    total_nilai = 0

    for mahasiswa in data:
        nilai = hitung_nilai_akhir(
            mahasiswa["tugas"],
            mahasiswa["uts"],
            mahasiswa["uas"]
        )

        huruf = nilai_huruf(nilai)
        status = penentu_lulus(huruf)

        mahasiswa["nilai_akhir"] = nilai
        mahasiswa["huruf"] = huruf
        mahasiswa["status"] = status

        total_nilai += nilai

    # Menampilkan hasil rekap
    rekap(data)

    rata_rata = hitung_rata_rata (total_nilai, len(data))
    jumlah_lulus = jumlah_mahasiswa_lulus(data)

    print("-" * 50)
    print(f"Rata-rata nilai kelas : {rata_rata:.2f}")
    print(f"Jumlah mahasiswa lulus: {jumlah_lulus}")

    # Mencari mahasiswa dengan nilai tertinggi (bagian(d))(cukup menambahkan pemanggilan dari fungsi definisi nilai tertinggi, tidak perlu mengubah kode lainnya)
    nilai_mahasiswa_tertinggi = cari_nilai_tertinggi(data)
    
    print(f"Nilai tertinggi diperoleh oleh: {nilai_mahasiswa_tertinggi['nama']}")
    print(f"Nilai akhirnya: {nilai_mahasiswa_tertinggi['nilai_akhir']:.2f}")



if __name__ == "__main__":
    main()