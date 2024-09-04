# DATA BAHAN BANGUNAN
n_max_bahan_bangunan = 3 # banyaknya jenis bahan bangunan maksimum dalam array
# Array bahan bangunan
# tipe data BahanBangunan diimplementasikan dalam bentuk tuple
# (nama, deskripsi, jumlah)
bahan_bangunan = [("", "", 0) for i in range(n_max_bahan_bangunan)]


# DATA CANDI
n_max_candi = 100 # banyak candi maksimum dalam array
n_candi = 0 # banyak candi dalam array
# Array candi
# tipe data Candi diimplementasikan dalam bentuk tuple
# (id, pembuat, pasir, batu, air)
# tuple candi yang belum dibangun atau hancur adalah (-1, "", 0, 0, 0)
candi = [(-1, "", 0, 0, 0) for i in range(n_max_candi)]


# DATA USER
n_max_user = 102 # banyak user maksimum dalam array
n_user = 0 # banyak user dalam array
# Array user
# tipe data User diimplementasikan dalam bentuk tuple
# (username, password, role)
# tuple user yang belum ada atau dihapus adalah ("", "", "")
user = [("", "", "") for i in range((n_max_user))]


# Data akun yang sedang login
# jika tidak login, akan diisi string kosong
current_username = "" # username
current_role = "" # role
