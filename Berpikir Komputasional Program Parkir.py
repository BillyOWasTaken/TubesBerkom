#https://ult.itb.ac.id/news/detail/695ed7c1-1550-461b-ba45-818fee71afd3/revisi-pemberlakuan-tarif-parkir-di-kampus-itb-jatinangor
awal = [5,6]
akhir = [22,24]

print("Pilih Area Parkir\n1. Gerbang Utama    2. Kehutanan")
park = int(input())
while park < 1 or park > 2:
    print("Area Parkir Invalid!")
    print("Pilih Area Parkir\n1. Gerbang Utama    2. Kehutanan")
    park = int(input())
    print(park)

motorparksize = int(input("Masukkan jumlah tempat parkir motor yang ada: "))
mobilparksize = int(input("Masukkan jumlah tempat parkir mobil yang ada: "))
parkirmotor = ["0" for i in range(motorparksize)];
motoroccupiedindex = 0;
parkirmobil = ["0" for i in range(mobilparksize)];
mobiloccupiedindex = 0;
sudahparkir = False;
ParkedAt = 0;


print("\n\nTARIF PARKIR")
print(f"MOBIL\nRp.2.000,-/Jam pertama\nRp.2.000,-/Jam berikutnya; maksimal Rp.10.000,- per hari")
while awal < akhir: 
   print(f"\n========={awal[park]:02}:00=========")
   jumlahvhcl = int(input("Jumlah kendaraan: "))
   for i in range(jumlahvhcl):
       print("Jenis Kendaraan\n1. Mobil    2. Motor")
       jenis = int(input("Jenis Kendaraan: "))
       plat = str(input("Plat Nomor: "))
       if jenis == 1:
           for j in range(mobilparksize):
               if parkirmobil[j][0] == plat:
                   sudahparkir = True;
                   ParkedAt = j;
           if sudahparkir == True:
               biaya = 2000*(parkirmobil[ParkedAt][1]-awal[park])+2000;
               print(f"Biaya Parkir: Rp.{biaya},-")
               print("Tempelkan kartu pembayaran")
               pembayaran = int(input())
               if pembayaran >= biaya: 
                   sudahparkir = False;
                   parkirmobil[ParkedAt]="0";
                   mobiloccupiedindex -= 1;
                   print("Pembayaran diterima. Hati - hati di jalan!")
               else:
                   print("Saldo tidak cukup")
           else:
               parkirmobil[mobiloccupiedindex]=[plat,awal[park]];
               mobiloccupiedindex += 1;
  


