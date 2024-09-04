# F03 - Summon Jin

import data_array

def summonjin():
    if data_array.n_user >= 102:
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    else:
        print("Jenis jin yang dapat dipanggil:")
        print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(" (2) Pembangun - Bertugas membangun candi")

        # Memilih nomor jenis jin
        # validasi menggunakan pengulangan iterate-stop
        while True:
            nomor_jenis = input("\nMasukkan nomor jenis jin yang ingin dipanggil: ")
            if nomor_jenis == '1' or nomor_jenis == '2':
                break
            print(f"\nTidak ada jenis jin bernomor \"{nomor_jenis}\"!")

        if nomor_jenis == '1':
            print("\nMemilih jin \"Pengumpul\".")
            input_role = "jin_pengumpul"
        else:
            print("\nMemilih jin \"Pembangun\".")
            input_role = "jin_pembangun"

        # Membuat username akun jin
        # validasi menggunakan pengulangan iterate-stop
        while True:
            input_username = input("\nMasukkan username jin: ")
            if input_username != "" and not username_jin_exist(input_username, data_array.user, data_array.n_user):
                break
            if username_jin_exist(input_username, data_array.user, data_array.n_user):
                print(f"\nUsername \"{input_username}\" sudah diambil!")

        # Membuat password akun jin
        # validasi menggunakan pengulangan iterate-stop
        while True:
            input_password = input("\nMasukkan password jin: ")
            if 5 <= len(input_password) <= 25:
                break
            print("\nPassword panjangnya harus 5-25 karakter!")

        print("\nMengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...")

        # Mencari posisi user dalam array yang kosong
        index = 2
        while data_array.user[index][0] != "":
            index += 1

        # Meng-update data akun jin
        data_array.n_user += 1
        data_array.user[index] = (input_username, input_password, input_role)

        print(f"\nJin {input_username} berhasil dipanggil!")

def username_jin_exist(username, array_user, n_user):
    index = 2
    found = False
    while index < n_user and not found and username != "":
        if array_user[index][0] == username:
            found = True
        else:
            index += 1

    return found
