"""
Soal 2: Struk Pengiriman Toko Daring
Sebuah toko daring menentukan ongkos kirim berdasarkan berat paket (bilangan bulat, dalam
kg) dan jarak pengiriman (dalam km).
• Biaya berat: Rp10.000 untuk paket hingga 2 kg. Untuk setiap kg selebihnya ditambah
Rp4.000.
• Biaya jarak: tidak ada biaya tambahan jika jarak tidak lebih dari 20 km, dan Rp5.000 jika
jarak lebih dari 20 km.
• Ongkos kirim adalah jumlah biaya berat dan biaya jarak. Pelanggan yang berstatus anggota
mendapat potongan 10% dari ongkos kirim.
Toko memiliki daftar pesanan hari ini sebagai berikut.
Pelanggan Berat (kg) Jarak (km) Anggota
Rina        1           10       Bukan
Sari        5           25       Bukan
Tono        5           25        Ya
Umar        2           30        Ya
Vina        8           15       Bukan



(a)Tulislah program yang mencetak struk untuk setiap pesanan, berisi nama pelanggan, biaya
berat, biaya jarak, potongan (jika ada), dan ongkos kirim akhir. Setelah semua struk, cetak
total pendapatan ongkos kirim hari ini.
(b)Rancang pembagian program ke dalam fungsi-fungsi. Seperti pada Soal 1, sertakan tabel
rancangan fungsi (nama fungsi, parameter, mengembalikan nilai atau tidak, tugas yang
dikerjakan). Terdapat sedikitnya satu fungsi void dan satu fungsi non-void.
(c)Tentukan secara manual ongkos kirim akhir untuk pesanan Sari, Tono, dan Umar, lalu
buktikan bahwa program Anda memberikan hasil yang sama.
(d)Toko mengubah kebijakan: batas jarak menjadi 15 km dan biaya tambahan jarak menjadi
Rp7.000. Tunjukkan bagian kode yang harus Anda ubah. Jika Anda harus mengubah
lebih dari satu tempat untuk satu perubahan aturan, jelaskan bagaimana pengelompokan
kode dapat diperbaiki.

"""
# Mata uang (Rupiah(Rp))
biaya_dasar = 10_000

# Satuan berat (Kilogram(kg))
batas_berat_dasar = 2 

# Mata uang (Rupiah(Rp))
biaya_lanjutan_per_kilo = 4_000

# Satuan jarak (Kilometer(Km))(Untuk bagian d variabel ini yang menentukan batas gratis untuk jarak nominal kebawah)
batas_gratis_jarak_maximum = 20

# Mata uang (Rupiah(Rp))(Untuk bagian d variabel ini yang mengatur nominal harga yang ditentukan setelah melewati  batas gratis untuk jarak nominal kebawah)
biaya_jarak_lanjutan = 5_000

# Diskom langganan Keanggotaan
diskon_anggota = 0.10

def hitung_biaya_berat(berat):
    if berat <= batas_berat_dasar:
        return biaya_dasar
    else:
        return biaya_dasar + ((berat - batas_berat_dasar) * biaya_lanjutan_per_kilo)



def hitung_biaya_jarak(jarak):
    if jarak <= batas_gratis_jarak_maximum:
        return 0
    else:
        return biaya_jarak_lanjutan

def hitung_ongkir(berat, jarak, anggota):
    biaya_berat = hitung_biaya_berat(berat)
    biaya_jarak = hitung_biaya_jarak(jarak)

    subtotal = biaya_berat + biaya_jarak

    if anggota == "Ya":
        potongan = subtotal * diskon_anggota
    else:
        potongan = 0

    total = subtotal - potongan

    return biaya_berat, biaya_jarak, potongan, total

def cetak_struk(nama, berat, jarak, anggota):
    biaya_berat, biaya_jarak, potongan, total = hitung_ongkir(
        berat, jarak, anggota
    )

    print("\n========== STRUK PENGIRIMAN ==========")
    print("Nama Pelanggan :", nama)
    print("Berat Paket    :", berat, "kg")
    print("Jarak          :", jarak, "km")
    print("Biaya Berat    : Rp", format(biaya_berat, ","))
    print("Biaya Jarak    : Rp", format(biaya_jarak, ","))
    print("Potongan       : Rp", format(potongan, ","))
    print("Ongkir Akhir   : Rp", format(total, ","))
    print("======================================")

def main():
    pesanan = [
        ("Rina", 1, 10, "Bukan"),
        ("Sari", 5, 25, "Bukan"),
        ("Tono", 5, 25, "Ya"),
        ("Umar", 2, 30, "Ya"),
        ("Vina", 8, 15, "Bukan")
    ]
    
    total_pendapatan = 0

    for nama, berat, jarak, anggota in pesanan:
        cetak_struk(nama, berat, jarak, anggota)

        hasil = hitung_ongkir(berat, jarak, anggota)
        total_pendapatan += hasil[3]

    print("\nTOTAL PENDAPATAN HARI INI")
    print("Rp", format(total_pendapatan, ","))





if __name__ == "__main__":
    main()


