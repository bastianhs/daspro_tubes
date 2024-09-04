# F11 - Hancurkan Candi

import data_array

def CariID(array_candi, ID):
    # Mencari keberadaan ID candi yang ingin dihancurkan
    i = 0 
    found = False
    while (i <= ID and i < data_array.n_max_candi and not found):
        if (array_candi[i][0] == ID):
            found = True
        else:
            i += 1

    return found

def hancurkancandi():
    # Dilakukan pengecekan terhadap role akun
    if data_array.current_role != "roro_jonggrang":
        # Jika rolenya bukan roro_jonggrang
        print("Hancurkan candi hanya dapat diakses oleh akun Roro Jonggrang.")
    else:
        # Jika rolenya adalah roro_jonggrang

        # Memasukkan ID candi yang ingin dihancurkan
        ID = int(input("Masukkan ID Candi: "))

        # Cek keberadaan ID candi tersebut
        if CariID(data_array.candi, ID):
            # Jika ID candi ada

            # Konfirmasi untuk menghancurkan candi
            cek = input(f"Apakah anda yakin ingin menghancurkan candi ID: {ID} (Y/N)? ")
            while cek != 'Y' and cek != 'y' and cek != 'N' and cek != 'n':
                cek = input(f"Apakah anda yakin ingin menghancurkan candi ID: {ID} (Y/N)? ")

            if cek == 'Y' or cek == 'y':
                # Jika sudah yakin
                data_array.candi[ID] = (-1, "", 0, 0, 0)
                data_array.n_candi -= 1
                print("\nCandi telah berhasil dihancurkan.")
            else:
                # Jika belum yakin
                print("\nCandi batal dihancurkan")
        else:
            # Jika ID candi tidak ada
            print("\nTidak ada candi dengan ID tersebut.")
