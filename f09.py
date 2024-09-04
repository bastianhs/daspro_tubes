# F09 - Ambil Laporan Jin

import data_array

def laporanjin() :
    # Dilakukan pengecekan terhadap role akun yang dipakai
    # laporanjin hanya bisa dilakukan oleh Bandung Bondowoso
    if (data_array.current_role == "bandung_bondowoso"):
        # Jika role adalah bandung_bondowoso

        # Menentukan jumlah jin dan jumlah setiap tipe jin
        count_jin = 0
        count_pengumpul = 0
        count_pembangun = 0
        for i in range(2, data_array.n_max_user) :
            if (data_array.user[i][2] == "jin_pengumpul"):
                # jika role user adalah jin pengumpul
                count_jin += 1
                count_pengumpul += 1
            elif (data_array.user[i][2] == "jin_pembangun"):
                # jika role user adalah jin pembangun
                count_jin += 1
                count_pembangun += 1

        print(f"Total Jin: {count_jin}")
        print(f"Total Jin Pengumpul: {count_pengumpul}")
        print(f"Total Jin Pembangun: {count_pembangun}")

        # Mencari jin terajin dan termalas
        if data_array.n_candi == 0:
            # Jika tidak ada candi yang berdiri,
            # jin terajin dan termalas dikosongkan/tidak terdefinisi
            terajin = "-"
            termalas = "-"
        else:
            # Jika ada candi yang berdiri, jin terajin dan termalas terdefinisi
            # jin_pengumpul mungkin menjadi jin terajin atau termalas

            # Membuat dan mengisi array dengan username semua jin
            n_max_jin = data_array.n_max_user - 2
            username_setiap_jin = ["" for i in range(n_max_jin)]
            for i in range(2, data_array.n_max_user):
                if data_array.user[i][0] != "":
                    username_setiap_jin[i - 2] = data_array.user[i][0]

            # Membuat dan mengisi array dengan jumlah candi yang dibangun tiap jin
            candi_per_jin = [0 for i in range(n_max_jin)]
            for i in range(n_max_jin):
                for j in range(data_array.n_max_candi):
                    if username_setiap_jin[i] != "" and username_setiap_jin[i] == data_array.candi[j][1]:
                        candi_per_jin[i] += 1

            # Menghapus data username jin
            # dengan kondisi jin: rolenya jin_pengumpul dan tidak ada candi yang dibangun
            # dilakukan agar jin dengan kondisi tersebut tidak dijadikan jin termalas
            for i in range(n_max_jin):
                for j in range(2, data_array.n_max_user):
                    if username_setiap_jin[i] == data_array.user[j][0]:
                        role_jin = data_array.user[j][2]

                if role_jin == "jin_pengumpul" and candi_per_jin[i] == 0:
                    username_setiap_jin[i] = ""

            # Menentukan jin terajin
            # Jin terajin pasti punya candi yang masih berdiri
            # karena jika jin terajin tidak punya candi yang masih berdiri,
            # berarti jumlah candi yang masih berdiri adalah 0
            # Jika jumlah candi = 0, kasus yang berlaku adalah jin terajin dan termalas tidak terdefinisi
            index_terajin = 0
            for index_jin in range(1, n_max_jin):
                if candi_per_jin[index_jin] > candi_per_jin[index_terajin]:
                    index_terajin = index_jin
                elif candi_per_jin[index_jin] == candi_per_jin[index_terajin]:
                    if username_setiap_jin[index_jin] < username_setiap_jin[index_terajin]:
                        index_terajin = index_jin

            terajin = username_setiap_jin[index_terajin]

            # Menentukan jin termalas
            # Jin termalas mungkin tidak punya candi yang masih berdiri
            index_termalas = index_terajin
            for index_jin in range(0, n_max_jin):
                if username_setiap_jin[index_jin] != "":
                    if candi_per_jin[index_jin] < candi_per_jin[index_termalas]:
                        index_termalas = index_jin
                    elif candi_per_jin[index_jin] == candi_per_jin[index_termalas]:
                        if username_setiap_jin[index_jin] > username_setiap_jin[index_termalas]:
                            index_termalas = index_jin

            termalas = username_setiap_jin[index_termalas]

        print(f"Jin Terajin: {terajin}")
        print(f"Jin Termalas: {termalas}")

        # Mengambil data jumlah pasir, batu, dan air
        jumlah_pasir = data_array.bahan_bangunan[0][2]
        jumlah_batu = data_array.bahan_bangunan[1][2]
        jumlah_air = data_array.bahan_bangunan[2][2]
        print(f"Jumlah Pasir: {jumlah_pasir} unit")
        print(f"Jumlah Batu: {jumlah_batu} unit")
        print(f"Jumlah Air: {jumlah_air} unit")
    else:
        # Jika role bukan bandung_bondowoso
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
