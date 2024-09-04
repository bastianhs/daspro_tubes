# F10 - Ambil Laporan Candi

import data_array
            
def BahanCandi(array_candi):
    # Mencari total bahan bangunan yang digunakan
    pasir = 0
    batu = 0
    air = 0
    for i in range(data_array.n_max_candi):
        if array_candi[i][0] != -1:
            pasir += array_candi[i][2]
            batu += array_candi[i][3]
            air += array_candi[i][4]

    return pasir, batu, air

def CandiTermahal(array_candi):
    # Mencari candi termahal yang telah dibangun
    hargacandi = 0 # harga candi >= 32.500
    id = -1
    for i in range (data_array.n_max_candi):
        if array_candi[i][0] != -1:
            hargapasir = 10000 * (array_candi[i][2])
            hargabatu = 15000 * (array_candi[i][3])
            hargaair = 7500 * (array_candi[i][4])        
            harga = hargapasir + hargabatu + hargaair

            if harga > hargacandi:
                hargacandi = harga
                id = array_candi[i][0]

    return id, hargacandi

def CandiTermurah(array_candi):
    # Mencari candi termurah yang telah dibangun
    hargacandi = 165000 # harga candi <= 162.500
    id = -1
    for i in range (data_array.n_max_candi):
        if array_candi[i][0] != -1:
            hargapasir = 10000 * (array_candi[i][2])
            hargabatu = 15000 * (array_candi[i][3])
            hargaair = 7500 * (array_candi[i][4])
            harga = hargapasir + hargabatu + hargaair

            if harga < hargacandi:
                hargacandi = harga
                id = array_candi[i][0]

    return id, hargacandi

def ThousandSeparator(value):
    # Memisahkan 3 digit terakhir dengan banyak digit sisanya dengan simbol '.'
    # Batasan nilai yang dimasukkan: 32500 - 162500
    n_digits = len(str(value))
    value_formatted = ""
    for i in range(n_digits):
        value_formatted += str(value)[i]
        if (n_digits == 5 and i == 1) or (n_digits == 6 and i == 2):
            value_formatted += "."

    return value_formatted

def laporancandi():
    # Dilakukan pengecekan terhadap role akun
    if data_array.current_role != "bandung_bondowoso":
        # Jika rolenya bukan bandung_bondowoso
        print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        # Jika rolenya adalah bandung_bondowoso
        print(f"Total Candi: {data_array.n_candi}")
        print(f"Total Pasir yang digunakan: {BahanCandi(data_array.candi)[0]}")
        print(f"Total Batu yang digunakan: {BahanCandi(data_array.candi)[1]}")
        print(f"Total Air yang digunakan: {BahanCandi(data_array.candi)[2]}")
        if data_array.n_candi == 0:
            print("ID Candi Termahal: -")
            print("ID Candi Termurah: -")
        else:
            print(f"ID Candi Termahal: {CandiTermahal(data_array.candi)[0]} (Rp {ThousandSeparator(CandiTermahal(data_array.candi)[1])})")
            print(f"ID Candi Termurah: {CandiTermurah(data_array.candi)[0]} (Rp {ThousandSeparator(CandiTermurah(data_array.candi)[1])})")
