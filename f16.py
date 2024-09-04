# F16 - Exit

import sys
import f14

def exit():
    # Sebelum keluar, minta konfirmasi untuk menyimpan file
    while True:
        confirm_save = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if confirm_save == 'y' or confirm_save == 'Y' or confirm_save == 'n' or confirm_save == 'N':
            break
    
    if confirm_save == 'y' or confirm_save == 'Y':
        # Jika memilih untuk menyimpan file
        f14.save()

    # Keluar dari program yang berjalan
    sys.exit()
