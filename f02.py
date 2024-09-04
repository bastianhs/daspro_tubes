# F02 - Logout

import data_array

def logout() :
    # Status login dicek terlebih dahulu
    if data_array.current_username == "":
        # Jika belum login, logout akan gagal
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    else:
        # Jika sudah login, logout dapat dilakukan
        data_array.current_username = ""
        data_array.current_role = ""
        print("Logout berhasil!")
