# Tugas-Pak-Teguh

Soal Nomor 1

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


JAWABAN NOMOR 1

PERBANDINGAN NILAI ANDI DAN DIMAS SECARA MANUAL

Nilai Andi

Total nilai = (tugas x 30%) + (uts x 30%) + (uas x 40%)

Tugas = 80
UTS = 70
UAS = 90

Total nilai = (80 x 30%) + (70 x 30%) + (90 x 40%)
Total nilai = 24 + 21 + 36
Total nilai =81

Nilai akhir Andi adalah 81, sehingga masuk kategori nilai huruf B dan dinyatakan Lulus.


Nilai Dimas

Total nilai = (tugas x 30%) + (uts x 30%) + (uas x 40%)

Tugas = 75
UTS = 80
UAS = 65

Total nilai = (75 x 30%) + (80 x 30%) + (65 x 40%)
Total nilai = 22,5 + 24 + 26
Total nilai = 72,5

Nilai akhir Dimas adalah 72,5, sehingga masuk kategori nilai huruf B dan dinyatakan Lulus.


PERBANDINGAN DENGAN OUTPUT PYTHON

Nama	Nilai Akhir	Nilai Huruf	Status
Andi	81.0	B	Lulus
Dimas	72.5	B	Lulus

PS E:\FE 25\Folder Tugas\Algoritma pemrograman dasar\Kumpulan Tugas> & 'C:\Users\Divine Diva\AppData\Local\Programs\Python\Python314\python.exe' '"e:/FE 25/Folder Tugas/Algoritma pemrograman dasar/Kumpulan Tugas/Tugas 1/Jawaban Soal 1/Soal 1.py"'
nama nilai_akhir nilai_huruf status
Andi 81.0BLulus
Bunga 87.7ALulus
Citra 51.5DTidak Lulus
Dimas 72.5BLulus
Eka 35.0ETidak Lulus
--------------------------------------------------
Rata-rata nilai kelas : 65.54
Jumlah mahasiswa lulus: 3
Nilai tertinggi diperoleh oleh: Bunga 
Nilai akhirnya: 87.70
PS E:\FE 25\Folder Tugas\Algoritma pemrograman dasar\Kumpulan Tugas>



TABEL RANCANGAN FUNGSI NOMOR 1

<img width="1046" height="162" alt="image" src="https://github.com/user-attachments/assets/78f7f1cf-f02c-4d0c-a280-24c1e3abc65a" />



