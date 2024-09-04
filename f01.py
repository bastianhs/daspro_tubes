# F01 - Login

import data_array

def login():
    # Pertama, status login dicek
    if data_array.current_username != "":
        # Jika sudah login, login akan gagal
        print("Login gagal!")
        print("Anda telah login dengan username " + data_array.current_username + ", silahkan lakukan \"logout\" sebelum melakukan login kembali.")
    else:
        # Input username dan password
        username = str(input("Username: "))
        password = str(input("Password: "))

        # Mencari keberadaan username
        idxfound = 0
        while data_array.user[idxfound][0] != username and idxfound < (data_array.n_max_user - 1):
            idxfound += 1

        if data_array.user[idxfound][0] != username:
            # Jika username tidak ditemukan
            print("Username tidak terdaftar!")
        else:
            # Jika username ditemukan, dilakukan pengecekan password
            if password == data_array.user[idxfound][1]:
                # Jika password benar
                data_array.current_username = username
                data_array.current_role = data_array.user[idxfound][2]
                print("Selamat datang, " + username + "!")
                print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil.")
            else:
                # Jika password salah
                print("Password salah!")
