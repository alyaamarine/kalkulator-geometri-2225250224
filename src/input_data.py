def input_dimensi_persegi():
    """Mengambil input sisi dari pengguna dan memvalidasinya"""
    sisi_input = input("Masukkan panjang sisi persegi: ")
    try:
        angka = float(sisi_input)
        if angka > 0:
            return True, angka
        else:
            return False, "Nilai sisi harus lebih besar dari 0!"
    except ValueError:
        return False, "Input harus berupa angka!"