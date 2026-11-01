# Dokumentasi Pengujian Proyek Akhir - Pertemuan 15

Berikut adalah tabel pelaporan hasil eksekusi pengujian fungsional pada aplikasi Kalkulator Geometri:

| ID | Fitur | Input / Kondisi | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| TC01 | Hitung Persegi | Sisi = 5 | Luas = 25, Keliling = 20 | Luas = 25.0, Keliling = 20.0 | **PASS** |
| TC02 | Batas Input | Sisi = 0 | Tampil pesan kesalahan | Pesan error validasi muncul | **PASS** |
| TC03 | Invalid Angka | Sisi = -5 | Tampil pesan kesalahan | Pesan error validasi muncul | **PASS** |
| TC04 | Invalid Tipe | Sisi = "abc" | Error handled via except | ValueError berhasil ditangani | **PASS** |
| TC05 | File I/O Tulis | Menyimpan log data | File riwayat_hitung.txt terbuat | File otomatis tercatat di folder data | **PASS** |