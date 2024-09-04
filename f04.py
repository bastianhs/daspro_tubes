# F04 - Hilangkan Jin

import data_array

def hapusjin():
    # Dilakukan pengecekan terhadap role dari akun
    # hapusjin hanya bisa dilakukan oleh akun dengan role bandung_bondowoso
    if data_array.current_role == 'bandung_bondowoso':
        # Jika role adalah bandung_bondowoso

        # Memasukkan username jin yang akan dihapus
        jin = str(input("Masukkan username jin : "))

        # Mencari keberadaan username jin tersebut
        index = 0
        found = False
        while index < data_array.n_user and not found:
            username = data_array.user[index][0]
            role = data_array.user[index][2]
            if username == jin and role != "bandung_bondowoso" and role != "roro_jonggrang":
                found = True
            else:
                index += 1

        if found:
            # Jika username jin ditemukan

            # Konfirmasi untuk menghapus jin
            while True:
                yakin = input("Apakah anda yakin ingin menghapus jin dengan username " + str(jin) + " (Y/N)? ")
                if yakin == 'Y' or yakin == 'y' or yakin == 'N' or yakin == 'n':
                    break

            if yakin == 'Y' or yakin == 'y':
                # Jika sudah yakin

                # Menghapus jin dari data user
                data_array.n_user -= 1
                data_array.user[index] = ("", "", "")

                # Menghapus candi yang dibangun oleh jin tersebut
                for i in range(data_array.n_candi):
                    if data_array.candi[i][1] == jin:
                        data_array.n_candi -= 1
                        data_array.candi[i] = (-1, "", 0, 0, 0)

                print("\nJin telah berhasil dihapus dari alam gaib.")
            else:
                # Jika belum yakin
                print("\nJin batal dihapus")
        else:
            # Jika username jin tidak ditemukan
            print("\nTidak ada jin dengan username tersebut.")
    else:
        # Jika role bukan bandung_bondowoso
        print("\nHapus jin hanya dapat diakses oleh akun Bandung Bondowoso.")
