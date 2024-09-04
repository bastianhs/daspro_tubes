# F05 - Ubah Tipe Jin

import data_array

def ubahjin():
    # Dilakukan pengecekan terhadap role dari akun
    # ubahjin hanya bisa dilakukan oleh role bandung_bondowoso
    if data_array.current_role == 'bandung_bondowoso':
        # Jika role adalah bandung_bondowoso

        # Memasukkan username jin yang ingin diubah tipenya
        jin = input("Masukkan username jin : ")

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
            # Jika username ditemukan dan rolenya bukan bandung_bondowoso maupun roro_jonggrang

            # Konfirmasi untuk mengubah tipe jin
            while True:
                if data_array.user[index][2] == "jin_pengumpul":
                    # Jika rolenya adalah jin_pengumpul
                    yakin = input("Jin ini bertipe \"Pengumpul\". Yakin ingin mengubah ke tipe \"Pembangun\" (Y/N)? ")
                else:
                    # Jika rolenya adalah jin_pembangun
                    yakin = input("Jin ini bertipe \"Pembangun\". Yakin ingin mengubah ke tipe \"Pengumpul\" (Y/N)? ")

                if yakin == 'Y' or yakin == 'y' or yakin == 'N' or yakin == 'n':
                    break

            if yakin == 'Y' or yakin == 'y':
                # Jika sudah yakin

                # Mengganti role jin
                if data_array.user[index][2] == "jin_pengumpul":
                    # Jika role awalnya adalah jin_pengumpul
                    data_array.user[index] = (data_array.user[index][0], data_array.user[index][1], "jin_pembangun")
                else:
                    # Jika role awalnya adalah jin_pembangun
                    data_array.user[index] = (data_array.user[index][0], data_array.user[index][1], "jin_pengumpul")

                print("\nJin telah berhasil diubah")
            else:
                # Jika belum yakin
                print("\nJin batal diubah")
        else:
            # Jika username tidak ditemukan atau rolenya bandung_bondowoso/roro_jonggrang
            print("\nTidak ada jin dengan username tersebut.")
    else:
        # Jika role bukan bandung_bondowoso
        print("\nUbah jin hanya dapat diakses oleh akun Bandung Bondowoso.") 
