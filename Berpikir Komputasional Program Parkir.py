#Program Parkir Otomatis
#Kelompok 06
'''
Athar Ramadhana Dermawan 19624078
Aziza Dharma Putri 19624079
Ahmad Aditya Ar Rasyid 19624101
Billy Ontoseno Irawan 19624130
Wa Ode Amerta Lambelu 19624136
'''


print("\n===================================  SETUP  =================================\n")
mobilparksize = int(input("Masukkan jumlah tempat parkir mobil yang ada: "))
motorparksize = int(input("\nMasukkan jumlah tempat parkir motor yang ada: "))
parkirmotor = ["0" for i in range(motorparksize)] #Setup parkir motor
parkirmobil = ["0" for i in range(mobilparksize)] #Setup parkir mobil
programjalan = True
print("\n=============================================================================")

print("\n\n=======================TARIF PARKIR=====================\n")
print("\nMOBIL\nRp.2000,-/Jam pertama\nRp.2000,-/Jam berikutnya; maksimal Rp.10.000,- per hari")
print("\nMOTOR\nRp.1000,-/Jam pertama\nRp.1000,-/Jam berikutnya; maksimal Rp.2000,- per hari")
print("\n========================================================")
while programjalan:
    print("\nPilih Aksi\n[1]Masuk\n[2]Keluar\n[3]Exit Program")
    aksi = int(input("Aksi: "))
    if aksi == 1:
        print("\nJenis Kendaraan\n1. Mobil    2. Motor")
        jenis = int(input("Jenis Kendaraan: "))
        if jenis == 1:  #Mobil
            parkirpenuh = True
            for j in range(mobilparksize):
                if parkirmobil[j] == "0" and parkirpenuh:
                    parkirpenuh = False
            if parkirpenuh == False:
                plat = str(input("Plat Nomor: "))
                # Cari apakah mobil sudah ada di tempat parkir berdasarkan plat nomor
                sudahparkir = False
                for j in range(mobilparksize):
                    if  parkirmobil[j][0] == plat:
                        sudahparkir = True
                if sudahparkir:
                    print("Mobil sudah berada di dalam tempat parkir")
                else:
                    awal = input("Masukkan waktu masuk kendaraan dalam format 24-jam (contoh: 0830) : ")
                    jamawal = int(awal[:2])  # Ambil 2 digit pertama sebagai jam
                    menitawal = int(awal[2:])  # Ambil 2 digit berikutnya sebagai menit
                    while menitawal > 59 or jamawal > 23:
                        awal = input("Waktu Invalid. Tolong input ulang waktu masuk: ")
                        jamawal = int(awal[:2])  # Ambil 2 digit pertama sebagai jam
                        menitawal = int(awal[2:])  # Ambil 2 digit berikutnya sebagai menit
                    # Cari tempat parkir kosong pertama untuk mobil baru
                    parked = False
                    for j in range(mobilparksize):
                        if parkirmobil[j] == "0" and not parked:
                            parkirmobil[j] = [plat, jamawal*60+menitawal]  # Simpan plat nomor dan waktu masuk
                            parked = True
                            print("\nSilahkan masuk")
            else:
                 print("Maaf, tempat parkir mobil penuh.")           
        elif jenis == 2:  #Motor
            parkirpenuh = True
            for j in range(motorparksize):
                if parkirmotor[j] == "0" and parkirpenuh:
                    parkirpenuh = False
            if parkirpenuh == False:
                plat = str(input("Plat Nomor: "))
                # Cari apakah motor sudah ada di tempat parkir berdasarkan plat nomor
                sudahparkir = False
                for j in range(motorparksize):
                    if  parkirmotor[j][0] == plat:
                        sudahparkir = True
                if sudahparkir:
                    print("Motor sudah berada di dalam tempat parkir")
                else:
                    awal = input("Masukkan waktu masuk kendaraan dalam format 24-jam (contoh: 0830) : ")
                    jamawal = int(awal[:2])  # Ambil 2 digit pertama sebagai jam
                    menitawal = int(awal[2:])  # Ambil 2 digit berikutnya sebagai menit
                    while menitawal > 59 or jamawal > 23:
                        awal = input("Waktu Invalid. Tolong input ulang waktu masuk: ")
                        jamawal = int(awal[:2])  # Ambil 2 digit pertama sebagai jam
                        menitawal = int(awal[2:])  # Ambil 2 digit berikutnya sebagai menit
                    # Cari tempat parkir kosong pertama untuk motor baru
                    parked = False
                    for j in range(mobilparksize):
                        if parkirmobil[j] == "0" and not parked:
                            parkirmotor[j] = [plat, jamawal]  # Simpan plat nomor dan waktu masuk
                            parked = True
                            print("Silahkan masuk")
            else:
                 print("Maaf, tempat parkir motor penuh.")
                 
    elif aksi == 2:
        print("\nJenis Kendaraan\n1. Mobil    2. Motor")
        jenis = int(input("Jenis Kendaraan: "))
        if jenis == 1:  #Mobil
                plat = str(input("Plat Nomor: "))
                # Cari apakah mobil sudah ada di tempat parkir berdasarkan plat nomor
                sudahparkir = False
                sudahbayar = False
                ParkedAt = 0 #Variabel untuk menyimpan lokasi parkir kendaraan
                for j in range(mobilparksize):
                    if  parkirmobil[j][0] == plat:
                        sudahparkir = True
                        ParkedAt = j
                if sudahparkir:
                    akhir = input("Masukkan waktu keluar kendaraan dalam format 24-jam (contoh: 1500) : ")
                    jamakhir = int(akhir[:2])  # Ambil 2 digit pertama sebagai jam
                    menitakhir = int(akhir[2:])  # Ambil 2 digit berikutnya sebagai menit
                    while menitakhir > 59 or jamakhir > 23:
                        akhir = input("Waktu Invalid. Tolong input ulang waktu keluar: ")
                        jamakhir = int(akhir[:2])  # Ambil 2 digit pertama sebagai jam
                        menitakhir = int(akhir[2:])  # Ambil 2 digit berikutnya sebagai menit
                    # Jika mobil sudah parkir, hitung biaya parkir dan keluarkan mobil
                    biaya = 2000 if((jamakhir*60+menitakhir - parkirmobil[ParkedAt][1])//60) <= 1 else 2000 * ((jamakhir*60+menitakhir - parkirmobil[ParkedAt][1])//60)
                    if biaya > 10000:
                        biaya = 10000
                        print(f"Biaya Parkir: Rp.{biaya},-")
                    else:
                        print(f"Biaya Parkir: Rp.{biaya},-")
                    print("Tempelkan kartu pembayaran")
                    while not sudahbayar: #Selama pembayaran belum terpenuhi, mobil tidak bisa keluar
                        pembayaran = int(input("Jumlah saldo: "))
                        if pembayaran >= biaya: 
                            parkirmotor[ParkedAt] = "0"  # Kosongkan tempat parkir
                            print("Pembayaran diterima. Hati - hati di jalan!")
                            sudahbayar = True
                        else:
                            print("Saldo tidak cukup. Tolong isi saldo Anda dan tempelkan kartu pembayaran")
                else:
                    print("Mobil tidak ada di dalam tempat parkir")
                       
        elif jenis == 2:  #Motor
                plat = str(input("Plat Nomor: "))
                # Cari apakah motor sudah ada di tempat parkir berdasarkan plat nomor
                sudahparkir = False
                sudahbayar = False
                ParkedAt = 0 #Variabel untuk menyimpan lokasi parkir kendaraan
                for j in range(motorparksize):
                    if  parkirmotor[j][0] == plat:
                        sudahparkir = True
                        ParkedAt = j
                if sudahparkir:
                    akhir = input("Masukkan waktu keluar kendaraan dalam format 24-jam (contoh: 1500) : ")
                    jamakhir = int(akhir[:2])  # Ambil 2 digit pertama sebagai jam
                    menitakhir = int(akhir[2:])  # Ambil 2 digit berikutnya sebagai menit
                    while menitakhir > 59 or jamakhir > 23:
                        akhir = input("Waktu Invalid. Tolong input ulang waktu keluar: ")
                        jamakhir = int(akhir[:2])  # Ambil 2 digit pertama sebagai jam
                        menitakhir = int(akhir[2:])  # Ambil 2 digit berikutnya sebagai menit
                    # Jika motor sudah parkir, hitung biaya parkir dan keluarkan motor
                    biaya = 1000 if((jamakhir*60+menitakhir - parkirmotor[ParkedAt][1])//60) <= 1 else 1000 * ((jamakhir*60+menitakhir - parkirmotor[ParkedAt][1])//60)
                    if biaya > 2000:
                        biaya = 2000
                        print(f"Biaya Parkir: Rp.{biaya},-")
                    else:
                        print(f"Biaya Parkir: Rp.{biaya},-")
                    print("Tempelkan kartu pembayaran")
                    while not sudahbayar: #Selama pembayaran belum terpenuhi, motor tidak bisa keluar
                        pembayaran = int(input("Jumlah saldo: "))
                        if pembayaran >= biaya: 
                            parkirmotor[ParkedAt] = "0"  # Kosongkan tempat parkir
                            print("Pembayaran diterima. Hati - hati di jalan!")
                            sudahbayar = True
                        else:
                            print("Saldo tidak cukup. Tolong isi saldo Anda dan tempelkan kartu pembayaran")
                else:
                    print("Motor tidak ada di dalam tempat parkir")
    elif aksi == 3:
        programjalan = False
