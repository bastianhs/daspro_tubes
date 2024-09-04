# F13 - Load

import os, sys, argparse
import data_array

# Parent folder ditentukan di awal dan bersifat tetap
parent_folder = "saves"

# Headers file .csv
headers_bahan_bangunan = "nama;deskripsi;jumlah\n"
headers_candi = "id;pembuat;pasir;batu;air\n"
headers_user = "username;password;role\n"

def load():
    # Menerima input nama folder yang sudah berisi file penyimpanan berekstensi .csv
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", help="folder's name of the external csv files", nargs='?', default="")
    arguments = parser.parse_args()

    # Menggabungkan path antara parent folder dengan input folder dari user
    relative_folder_path = os.path.join(parent_folder, arguments.folder)

    # Pengecekan keberadaan folder
    if arguments.folder == "":
        # Jika input folder tidak diberikan, dikeluarkan suatu pesan
        sys.exit("Tidak ada nama folder yang diberikan!\n\nUsage: python main.py <nama_folder>")
    elif not os.path.exists(relative_folder_path):
        # Jika input folder tidak ada dalam storage komputer, dikeluarkan suatu pesan
        sys.exit("Folder \"" + arguments.folder + "\" tidak ditemukan.")
    else:
        # Jika input folder ditemukan dalam storage komputer, dilakukan proses load
        print("Loading...")

        # Melakukan load file .csv untuk bahan bangunan, candi, dan user
        load_bahan_bangunan(relative_folder_path)
        load_candi(relative_folder_path)
        load_user(relative_folder_path)

        print("Selamat datang di program \"Manajerial Candi\"")
        print("Masukkan command \"login\" untuk masuk ke akun Anda.")
        print("Masukkan command \"help\" untuk melihat daftar command yang dapat dipanggil.")

def load_bahan_bangunan(folder_path):
    # Melakukan read pada file bahan_bangunan.csv
    with open(os.path.join(folder_path, "bahan_bangunan.csv"), 'r') as file_bahan_bangunan:
        index_row = 0
        for line in file_bahan_bangunan:
            if line != headers_bahan_bangunan: # Header tidak akan dibaca
                i = 0
                index_column = 0
                while line[i] != '\n':
                    content = ""
                    while line[i] != ';' and line[i] != '\n':
                        content += line[i]
                        i += 1

                    if index_column == 0:
                        nama = content
                    elif index_column == 1:
                        deskripsi = content
                    else: # index_column = 2
                        jumlah = int(content)

                    if line[i] == ';':
                        i += 1
                        index_column += 1

                data_array.bahan_bangunan[index_row] = (nama, deskripsi, jumlah)
                index_row += 1

def load_candi(folder_path):
    # Melakukan read pada file candi.csv
    with open(os.path.join(folder_path, "candi.csv"), 'r') as file_candi:
        n_candi = 0
        for line in file_candi:
            if line != headers_candi: # Header tidak akan dibaca
                i = 0
                index_column = 0
                while line[i] != '\n':
                    content = ""
                    while line[i] != ';' and line[i] != '\n':
                        content += line[i]
                        i += 1

                    if index_column == 0:
                        id = int(content)
                    elif index_column == 1:
                        pembuat = content
                    elif index_column == 2:
                        pasir = int(content)
                    elif index_column == 3:
                        batu = int(content)
                    else: # index_column = 4
                        air = int(content)

                    if line[i] == ';':
                        i += 1
                        index_column += 1

                data_array.candi[id] = (id, pembuat, pasir, batu, air)
                n_candi += 1

    data_array.n_candi = n_candi

def load_user(folder_path):
    # Melakukan read pada file user.csv
    with open(os.path.join(folder_path, "user.csv"), 'r') as file_user:
        index_row = 0
        for line in file_user:
            if line != headers_user: # Header tidak akan dibaca
                i = 0
                index_column = 0
                while line[i] != '\n':
                    content = ""
                    while line[i] != ';' and line[i] != '\n':
                        content += line[i]
                        i += 1

                    if index_column == 0:
                        username = content
                    elif index_column == 1:
                        password = content
                    else: # index_column = 2
                        role = content

                    if line[i] == ';':
                        i += 1
                        index_column += 1

                data_array.user[index_row] = (username, password, role)
                index_row += 1

    data_array.n_user = index_row
