# F15 - Help

import data_array

def help():
    # Kumpulan pesan bantuan
    help_login = "     Untuk masuk menggunakan akun."
    help_logout = "     Untuk keluar dari akun yang digunakan sekarang."
    help_summonjin = "     Untuk memanggil jin.\n     Tipe jin yang tersedia adalah jin pengumpul dan jin pembangun."
    help_hapusjin = "     Untuk menghapus jin.\n     Bila jin sudah dihapus, candi yang dibuat oleh jin tersebut juga ikut terhapus."
    help_ubahjin = "     Untuk mengubah tipe jin.\n     Tipe jin yang tersedia adalah jin pengumpul dan jin pembangun."
    help_bangun = "     Untuk membangun candi."
    help_kumpul = "     Untuk mengumpulkan resource candi."
    help_batchkumpul = "     Untuk memberi perintah mengumpulkan bahan kepada seluruh jin dengan tipe pengumpul."
    help_batchbangun = "     Untuk memberi perintah membangun candi kepada seluruh jin dengan tipe pembangun."
    help_laporanjin = "     Untuk mengambil laporan kinerja para jin dan banyak material yang terkumpul."
    help_laporancandi = "     Untuk mengambil laporan banyak candi yang telah dibangun, material yang telah digunakan, dan harga candi."
    help_hancurkancandi = "     Untuk menghancurkan candi yang tersedia"
    help_ayamberkokok = "     Untuk menyelesaikan permainan dengan memalsukan pagi hari."
    help_save = "     Untuk menyimpan data permainan."
    help_exit = "     Untuk keluar dari permainan."

    print("=" * 30 + " HELP " + "=" * 30)

    # Dilakukan pengecekan role akun yang digunakan
    if data_array.current_role == "bandung_bondowoso":
        # Jika rolenya bandung_bondowoso
        print("1.   logout")
        print(help_logout)
        
        print("2.   summonjin")
        print(help_summonjin)
        
        print("3.   hapusjin")
        print(help_hapusjin)
        
        print("4.   ubahjin")
        print(help_ubahjin)
        
        print("5.   batchkumpul")
        print(help_batchkumpul)
        
        print("6.   batchbangun")
        print(help_batchbangun)
        
        print("7.   laporanjin")
        print(help_laporanjin)
        
        print("8.   laporancandi")
        print(help_laporancandi)
        
        print("9.   save")
        print(help_save)
        
        print("10.  exit")
        print(help_exit)
    elif data_array.current_role == "roro_jonggrang":
        # Jika rolenya roro_jonggrang
        print("1.   logout")
        print(help_logout)

        print("2.   hancurkancandi")
        print(help_hancurkancandi)

        print("3.   ayamberkokok")
        print(help_ayamberkokok)

        print("4.   save")
        print(help_save)

        print("5.   exit")
        print(help_exit)
    elif data_array.current_role == "jin_pengumpul":
        # Jika rolenya jin_pengumpul
        print("1.   logout")
        print(help_logout)

        print("2.   kumpul")
        print(help_kumpul)

        print("3.   save")
        print(help_save)

        print("4.   exit")
        print(help_exit)
    elif data_array.current_role == "jin_pembangun":
        # Jika rolenya jin_pembangun
        print("1.   logout")
        print(help_logout)

        print("2.   bangun")
        print(help_bangun)

        print("3.   save")
        print(help_save)

        print("4.   exit")
        print(help_exit)
    else:
        # Jika belum login
        print("1.   login")
        print(help_login)

        print("2.   save")
        print(help_save)

        print("3.   exit")
        print(help_exit)

    print("=" * 66)
