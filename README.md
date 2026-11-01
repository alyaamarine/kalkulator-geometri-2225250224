# Proyek Akhir Algoritma & Pemrograman - Kalkulator Geometri Bangun Datar

Aplikasi berbasis terminal (CLI) menggunakan Python yang dirancang untuk menghitung luas dan keliling bangun datar secara otomatis serta menyimpan riwayat perhitungannya ke dalam berkas teks.

**Nama:** Alya Mutiara Marine  
**NIM:** 2225250224  
**Kelas:** 3A  
**Dosen Pengampu:** Dr. Aan Hendrayana, S.Si., M.Pd.  

---

## 1. Deskripsi Program
Program Kalkulator Geometri Bangun Datar merupakan aplikasi sederhana berbasis *Command Line Interface* (CLI) yang dibuat untuk membantu siswa dan guru sekolah dalam memvalidasi hasil perhitungan matematis bangun datar secara cepat, akurat, dan konsisten. Program ini mengimplementasikan konsep koding modular, validasi input, dan penanganan file I/O.

## 2. Fitur Utama
* **Fitur 1 (Kalkulasi Otomatis):** Menghitung Luas dan Keliling Bangun Datar secara instan (Persegi).
* **Fitur 2 (Validasi Input Berlapis):** Mencegah program crash dengan mendeteksi input bernilai negatif, nol, atau karakter huruf (invalid string).
* **Fitur 3 (Penyimpanan Otomatis):** Menuliskan setiap hasil kalkulasi yang sukses ke dalam file riwayat teks secara permanen.

## 3. Persyaratan Sistem
* Python 3.x (Direkomendasikan Python 3.10 ke atas)
* Lingkungan kerja VS Code

## 4. Cara Menjalankan Program
1. Buka aplikasi **VS Code** dan aktifkan terminal terintegrasi (`Ctrl + ~`).
2. Jalankan aplikasi dengan mengetikkan perintah berikut pada terminal:
   ```bash
   python main.py
   ```

## 5. Struktur Folder Proyek
Susunan komponen berkas proyek dirancang secara modular sebagai berikut:
* `main.py` - Mengatur jalannya menu utama dan logika alur aplikasi (di luar folder `src`).
* `src/__init__.py` - Berkas kosong penanda paket modul Python.
* `src/input_data.py` - Menangani fungsi penangkapan dan validasi input dari pengguna.
* `src/proses.py` - Menyimpan fungsi rumus matematika kalkulasi luas & keliling persegi.
* `src/output.py` - Menangani pencetakan hasil ke layar terminal dan penulisan log berkas luar.
* `data/contoh_data.txt` - Menyimpan berkas data mentah atau contoh masukan nilai.
* `tests/test_case.md` - Dokumen tabel skenario pengujian program.
* `docs/screenshot/` - Folder penyimpanan bukti tangkapan layar jalannya program.

## 6. Tabel Hasil Pengujian (Test Case)

| ID | Fitur | Input / Kondisi | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| TC01 | Hitung Persegi | Sisi = 5 | Luas = 25, Keliling = 20 | Luas = 25.0, Keliling = 20.0 | **PASS** |
| TC02 | Batas Input | Sisi = 0 | Pesan kesalahan validasi | Pesan error validasi muncul | **PASS** |
| TC03 | Invalid Angka | Sisi = -5 | Pesan kesalahan validasi | Pesan error validasi muncul | **PASS** |
| TC04 | Invalid Tipe | Sisi = "abc" | Pesan error ditangani | Pesan error ditangani, tidak crash | **PASS** |
| TC05 | File I/O | Menyimpan log data | File riwayat_hitung.txt terbuat | File terbuat otomatis di folder data | **PASS** |

## 7. Known Issues (Masalah yang Diketahui)
* Program saat ini baru mendukung perhitungan untuk bangun datar persegi secara penuh. Pengembangan untuk penambahan menu bangun datar lain (seperti segitiga dan lingkaran) akan diintegrasikan pada fase rilis berikutnya.

## 8. Referensi & Bantuan
* RPS dan Modul Bahan Ajar Algoritma dan Pemrograman OBE Untirta 2026/2027 Ganjil.
* Python 3.x Official Documentation (Fungsi `try-except` dan File Handling).