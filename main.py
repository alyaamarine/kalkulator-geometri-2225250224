from src.input_data import input_dimensi_persegi
from src.proses import hitung_luas_persegi, hitung_keliling_persegi
from src.output import tampilkan_dan_simpan_hasil

def main():
    print("=== KALKULATOR GEOMETRI BANGUN DATAR INDIVIDU ===")
    print("1. Hitung Geometri Persegi")
    print("2. Keluar")
    
    pilihan = input("Pilih opsi menu (1/2): ")
    
    if pilihan == "1":
        is_valid, hasil_input = input_dimensi_persegi()
        if is_valid:
            sisi = hasil_input
            luas = hitung_luas_persegi(sisi)
            keliling = hitung_keliling_persegi(sisi)
            tampilkan_dan_simpan_hasil(sisi, luas, keliling)
        else:
            print(f"Error Validasi: {hasil_input}")
    elif pilihan == "2":
        print("Program selesai. Terima kasih!")
    else:
        print("Menu tidak valid!")

if __name__ == "__main__":
    main()