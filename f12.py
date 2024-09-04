# F12 - Ayam Berkokok

import sys
import data_array

def ayamberkokok():
    # Dilakukan pengecekan terhadap role akun yang digunakan
    if data_array.current_role != "roro_jonggrang":
        # Jika rolenya bukan roro_jonggrang
        print("Ayam berkokok hanya dapat diakses oleh akun Roro Jonggrang.")
    else:
        # Jika rolenya adalah roro_jonggrang

        print("Kukuruyuk.. Kukuruyuk..\n")
        print(f"Jumlah Candi: {data_array.n_candi}\n")

        # Cek jumlah candi yang sudah dibangun
        if data_array.n_candi < 100:
            # Jika jumlahnya belum 100
            print("Selamat, Roro Jonggrang memenangkan permainan!\n")
            print("*Bandung Bondowoso angry noise*")
            print("Roro Jonggrang dikutuk menjadi candi.")
        else:
            # Jika sudah mencapai 100
            print("Yah, Bandung Bondowoso memenangkan permainan!")

        # Keluar dari program yang berjalan
        sys.exit()
