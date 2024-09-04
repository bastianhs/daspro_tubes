import f01, f02, f03, f04, f05, f06, f07, f08, f09, f10, f11, f12, f13, f14, f15, f16

# Load program
f13.load()

# Program utama
while True:
    input_user = input(">>> ")
    if input_user == "login":
        f01.login()
    elif input_user == "logout":
        f02.logout()
    elif input_user == "summonjin":
        f03.summonjin()
    elif input_user == "hapusjin":
        f04.hapusjin()
    elif input_user == "ubahjin":
        f05.ubahjin()
    elif input_user == "bangun":
        f06.bangun()
    elif input_user == "kumpul":
        f07.kumpul()
    elif input_user == "batchkumpul":
        f08.batchkumpul()
    elif input_user == "batchbangun":
        f08.batchbangun()
    elif input_user == "laporanjin":
        f09.laporanjin()
    elif input_user == "laporancandi":
        f10.laporancandi()
    elif input_user == "hancurkancandi":
        f11.hancurkancandi()
    elif input_user == "ayamberkokok":
        f12.ayamberkokok()
    elif input_user == "save":
        f14.save()
    elif input_user == "help":
        f15.help()
    elif input_user == "exit":
        f16.exit()
    else:
        print("Command tidak dikenal. Untuk melihat daftar command, silakan masukkan command \"help\".")
