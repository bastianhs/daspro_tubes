# F08 - Batch Kumpul/Bangun

import random
import data_array

def batchkumpul():
    # Dilakukan pengecekan terhadap role akun yang dipakai
    # batchkumpul hanya bisa dilakukan oleh Bandung Bondowoso
    if (data_array.current_role == "bandung_bondowoso"):
        # Jika role-nya adalah bandung_bondowoso

        # Menghitung banyak jin pengumpul
        count_pengumpul = 0
        for i in range (2, data_array.n_max_user):
            if (data_array.user[i][2] == "jin_pengumpul"):
                # Jika role suatu akun adalah jin pengumpul,
                # jumlah jin pengumpul bertambah 1
                count_pengumpul = count_pengumpul + 1

        # Mengecek banyaknya jin pengumpul
        if count_pengumpul == 0:
            # Jika tidak ada jin bertipe pengumpul
            print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
        else:
            # Jika ada jin bertipe pengumpul, setiap jin akan mengumpulkan bahan
            # Jumlah bahan bangunan yang dikumpulkan tiap jin bisa berbeda

            print(f"Mengerahkan {count_pengumpul} jin untuk mengumpulkan bahan.")

            total_pasir = 0
            total_batu = 0
            total_air = 0
            for i in range(count_pengumpul):
                # Melakukan random terhadap bahan bangunan yang terkumpul
                # menggunakan library random
                total_pasir += random.randint(0, 5)
                total_batu += random.randint(0, 5)
                total_air += random.randint(0, 5)

            # Meng-update jumlah bahan bangunan yang terkumpul oleh seluruh jin pengumpul
            data_array.bahan_bangunan[0] = (data_array.bahan_bangunan[0][0], data_array.bahan_bangunan[0][1], data_array.bahan_bangunan[0][2] + total_pasir)
            data_array.bahan_bangunan[1] = (data_array.bahan_bangunan[1][0], data_array.bahan_bangunan[1][1], data_array.bahan_bangunan[1][2] + total_batu)
            data_array.bahan_bangunan[2] = (data_array.bahan_bangunan[2][0], data_array.bahan_bangunan[2][1], data_array.bahan_bangunan[2][2] + total_air)

            print(f"Jin menemukan total {total_pasir} pasir, {total_batu} batu, dan {total_air} air.")
    else:
        # Jika role-nya bukan bandung_bondowoso
        print("Batch kumpul hanya dapat diakses oleh akun Bandung Bondowoso.")

def batchbangun():
    # Cek role akun yang dipakai
    if data_array.current_role != "bandung_bondowoso":
        # Jika role-nya bukan bandung_bondowoso
        print("Batch bangun hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        # Jika role-nya adalah bandung_bondowoso

        # Menghitung jumlah jin pembangun dalam batchbangun
        n_pembangun_batch = 0
        for i in range(2, data_array.n_max_user):
            if data_array.user[i][2] == "jin_pembangun":
                n_pembangun_batch += 1

        # Menentukan keberhasilan batchbangun
        if n_pembangun_batch == 0:
            # Jika tidak punya jin pembangun
            print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
        else:
            # Jika punya jin pembangun

            # Mengambil seluruh username jin pembangun
            # dan mengurutkannya dari urutan leksikografis terkecil
            username_pembangun_batch = ["" for i in range(n_pembangun_batch)]
            index_pembangun = 0
            for i in range(2, data_array.n_max_user):
                if data_array.user[i][2] == "jin_pembangun":
                    username_pembangun_batch[index_pembangun] = data_array.user[i][0]
                    index_pembangun += 1

            for i in range(n_pembangun_batch - 1):
                index_username_terkecil = i
                for j in range(i + 1, n_pembangun_batch):
                    if username_pembangun_batch[j] < username_pembangun_batch[index_username_terkecil]:
                        index_username_terkecil = j

                temp = username_pembangun_batch[index_username_terkecil]
                username_pembangun_batch[index_username_terkecil] = username_pembangun_batch[i]
                username_pembangun_batch[i] = temp

            # Membuat catatan sementara candi
            # Awalnya diisi dengan candi yang sudah ada
            candi_batch = [(-1, "", 0, 0, 0) for i in range(data_array.n_max_candi)]
            for i in range(data_array.n_max_candi):
                if data_array.candi[i][0] != -1:
                    candi_batch[i] = data_array.candi[i]

            # Generate candi yang dibangun oleh setiap jin pembangun
            total_pasir = 0
            total_batu = 0
            total_air = 0
            for i in range(n_pembangun_batch):
                # Mengambil username jin pembangun
                username_pembangun = username_pembangun_batch[i]

                # Mencari id candi terkecil yang kosong
                j = 0
                while j < data_array.n_max_candi - 1 and candi_batch[j][0] != -1:
                    j += 1

                if candi_batch[j][0] == -1:
                    empty_id = j
                else:
                    empty_id = -1

                # Menentukan jumlah pasir, batu, dan air yang dibutuhkan secara acak
                pasir = random.randint(1, 5)
                batu = random.randint(1, 5)
                air = random.randint(1, 5)

                # Mencatat candi yang dibangun ke dalam catatan sementara
                # dilakukan jika id candi yang kosong ditemukan
                if empty_id != -1:
                    candi_batch[empty_id] = (empty_id, username_pembangun, pasir, batu, air)

                # Meng-update total bahan bangunan yang dibutuhkan
                total_pasir += pasir
                total_batu += batu
                total_air += air

            print(f"Mengerahkan {n_pembangun_batch} jin untuk membangun candi dengan total bahan {total_pasir} pasir, {total_batu} batu, dan {total_air} air.")

            # Cek stok bahan bangunan
            if data_array.bahan_bangunan[0][2] < total_pasir or data_array.bahan_bangunan[1][2] < total_batu or data_array.bahan_bangunan[2][2] < total_air:
                # Jika bahan bangunan kurang, tidak ada candi yang berhasil dibangun

                # Menghitung kekurangan pasir
                if data_array.bahan_bangunan[0][2] < total_pasir:
                    pasir_kurang = total_pasir - data_array.bahan_bangunan[0][2]
                else:
                    pasir_kurang = 0

                # Menghitung kekurangan batu
                if data_array.bahan_bangunan[1][2] < total_batu:
                    batu_kurang = total_batu - data_array.bahan_bangunan[1][2]
                else:
                    batu_kurang = 0

                # Menghitung kekurangan air
                if data_array.bahan_bangunan[2][2] < total_air:
                    air_kurang = total_air - data_array.bahan_bangunan[2][2]
                else:
                    air_kurang = 0

                print(f"Bangun gagal. Kurang {pasir_kurang} pasir, {batu_kurang} batu, dan {air_kurang} air.")
            else:
                # Jika bahan bangunan cukup

                # Mengurangi stok bahan bangunan
                data_array.bahan_bangunan[0] = (data_array.bahan_bangunan[0][0], data_array.bahan_bangunan[0][1], data_array.bahan_bangunan[0][2] - total_pasir)
                data_array.bahan_bangunan[1] = (data_array.bahan_bangunan[1][0], data_array.bahan_bangunan[1][1], data_array.bahan_bangunan[1][2] - total_batu)
                data_array.bahan_bangunan[2] = (data_array.bahan_bangunan[2][0], data_array.bahan_bangunan[2][1], data_array.bahan_bangunan[2][2] - total_air)

                # Meng-update data candi dengan data dari catatan sementara
                for i in range(data_array.n_max_candi):
                    if data_array.candi[i][0] == -1 and candi_batch[i][0] != -1:
                        data_array.n_candi += 1
                        data_array.candi[i] = candi_batch[i]

                print(f"Jin berhasil membangun total {n_pembangun_batch} candi.")
