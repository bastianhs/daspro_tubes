# F14 - Save

import os
import data_array
import f13

def save():
    # Memasukkan nama folder yang akan diisi file penyimpanan .csv
    input_folder = input("Masukkan nama folder: ")

    print("Saving...")

    # Menggabungkan path antara parent folder dengan input folder dari user
    relative_folder_path = os.path.join(f13.parent_folder, input_folder)

    # Pengecekan keberadaan input folder dari user dalam storage komputer
    if (not os.path.exists(relative_folder_path)):
        # Jika input folder tidak ditemukan, cek dulu keberadaan parent folder
        if (not os.path.exists(f13.parent_folder)):
            # Jika parent folder tidak ditemukan, parent folder dibuat terlebih dahulu
            print("Membuat folder " + f13.parent_folder + "...")
            os.makedirs(f13.parent_folder)

        # Jika belum ada, input folder dari user akan dibuat
        print("Membuat folder " + relative_folder_path + "...")
        os.makedirs(relative_folder_path)

    # Setelah input folder dari user ada di dalam storage komputer,
    # dilakukan save file .csv untuk bahan bangunan, candi, dan user ke dalam folder tersebut
    save_bahan_bangunan(relative_folder_path)
    save_candi(relative_folder_path)
    save_user(relative_folder_path)

    print("Berhasil menyimpan data di folder " + relative_folder_path + '!')

def save_bahan_bangunan(folder_path):
    # Melakukan save pada file bahan_bangunan.csv
    with open(os.path.join(folder_path, "bahan_bangunan.csv"), 'w') as file_bahan_bangunan:
        file_bahan_bangunan.write(f13.headers_bahan_bangunan)
        for index_row in range(data_array.n_max_bahan_bangunan):
            for index_column in range(3):
                file_bahan_bangunan.write(str(data_array.bahan_bangunan[index_row][index_column]))
                if index_column < 2: # (nama, deskripsi)
                    file_bahan_bangunan.write(';')
                else: # index_column = 2 (jumlah)
                    file_bahan_bangunan.write('\n')

def save_candi(folder_path):
    # Melakukan save pada file candi.csv
    with open(os.path.join(folder_path, "candi.csv"), 'w') as file_candi:
        file_candi.write(f13.headers_candi)
        for index_row in range(data_array.n_max_candi):
            if data_array.candi[index_row][0] != -1:
                for index_column in range(5):
                    file_candi.write(str(data_array.candi[index_row][index_column]))
                    if index_column < 4: # (id, pembuat, pasir, batu)
                        file_candi.write(';')
                    else: # index_column = 4 (air)
                        file_candi.write('\n')

def save_user(folder_path):
    # Melakukan save pada file user.csv
    with open(os.path.join(folder_path, "user.csv"), 'w') as file_user:
        file_user.write(f13.headers_user)
        for index_row in range(data_array.n_max_user):
            if data_array.user[index_row][0] != "":
                for index_column in range(3):
                    file_user.write(str(data_array.user[index_row][index_column]))
                    if index_column < 2: # (username, password)
                        file_user.write(';')
                    else: # index_column = 2 (role)
                        file_user.write('\n')
