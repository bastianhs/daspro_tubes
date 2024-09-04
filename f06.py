# F06 - Jin Pembangun

import data_array
import random

def bangun():
    # Dilakukan pengecekan role akun terlebih dahulu
    if data_array.current_role != "jin_pembangun":
        # Jika rolenya bukan jin_pembangun
        print("Bangun hanya dapat diakses oleh akun jin pembangun.")
    else:
        # Jika rolenya adalah jin_pembangun

        # Generate pasir, batu, dan air yang diperlukan untuk membangun candi
        pasir = random.randint(1, 5)
        batu = random.randint(1, 5)
        air = random.randint(1, 5)

        # Mengecek ketersediaan bahan bangunan
        if pasir > data_array.bahan_bangunan[0][2] or batu > data_array.bahan_bangunan[1][2] or air > data_array.bahan_bangunan[2][2]:
            # Jika stok bahan bangunan tidak cukup
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")
        else:
            # Jika stok bahan bangunan cukup

            # Mengurangi stok bahan bangunan yang dimiliki
            data_array.bahan_bangunan[0] = (data_array.bahan_bangunan[0][0], data_array.bahan_bangunan[0][1], data_array.bahan_bangunan[0][2] - pasir)
            data_array.bahan_bangunan[1] = (data_array.bahan_bangunan[1][0], data_array.bahan_bangunan[1][1], data_array.bahan_bangunan[1][2] - batu)
            data_array.bahan_bangunan[2] = (data_array.bahan_bangunan[2][0], data_array.bahan_bangunan[2][1], data_array.bahan_bangunan[2][2] - air)

            # Cek jumlah candi yang telah dibangun
            if data_array.n_candi < 100:
                # Jika jumlahnya belum 100, candi akan tercatat
 
                # Mencari id candi terkecil yang kosong
                empty_id = 0
                while empty_id == data_array.candi[empty_id][0]:
                    empty_id += 1

                # Meng-update jumlah candi
                data_array.n_candi += 1

                # Mencatat data id, pembuat, pasir, batu, dan air dari candi yang dibangun
                data_array.candi[empty_id] = (empty_id, data_array.current_username, pasir, batu, air)

            print("Candi berhasil dibangun.")
            print("Sisa candi yang perlu dibangun: " + str(data_array.n_max_candi - data_array.n_candi))
