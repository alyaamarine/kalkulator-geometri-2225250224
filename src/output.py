import os

def tampilkan_dan_simpan_hasil(sisi, luas, keliling):
    """Menampilkan hasil ke terminal dan mencatatnya ke file log data"""
    output_teks = f"Persegi [Sisi={sisi}] -> Luas: {luas}, Keliling: {keliling}"
    print("\n" + "="*40)
    print(output_teks)
    print("="*40 + "\n")
    
    # Menyimpan otomatis ke folder data sesuai panduan
    path_file = "data/riwayat_hitung.txt"
    os.makedirs(os.path.dirname(path_file), exist_ok=True)
    with open(path_file, "a") as file:
        file.write(output_teks + "\n")