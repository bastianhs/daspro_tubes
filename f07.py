# F07 - Jin Pengumpul

import random
import data_array

def kumpul():
	# Dilakukan pengecekan terhadap role akun yang dipakai
	# kumpul hanya bisa dilakukan oleh jin pengumpul
	if (data_array.current_role == "jin_pengumpul"):
		# Jika rolenya adalah jin_pengumpul

		# Melakukan random terhadap bahan bangunan yang terkumpul
		# menggunakan library random
		pasir = random.randint(0, 5)
		batu = random.randint(0, 5)
		air = random.randint(0, 5)

		# Meng-update jumlah bahan bangunan yang terkumpul oleh jin pengumpul
		data_array.bahan_bangunan[0] = (data_array.bahan_bangunan[0][0], data_array.bahan_bangunan[0][1], data_array.bahan_bangunan[0][2] + pasir)
		data_array.bahan_bangunan[1] = (data_array.bahan_bangunan[1][0], data_array.bahan_bangunan[1][1], data_array.bahan_bangunan[1][2] + batu)
		data_array.bahan_bangunan[2] = (data_array.bahan_bangunan[2][0], data_array.bahan_bangunan[2][1], data_array.bahan_bangunan[2][2] + air)

		print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air")
	else:
		# Jika rolenya bukan jin_pengumpul
		print("Kumpul hanya dapat diakses oleh akun jin pengumpul.")
