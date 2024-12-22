#Program Parkir Otomatis
#Kelompok 06
'''
Athar Ramadhana Dermawan 19624078
Aziza Dharma Putri 19624079
Ahmad Aditya Ar Rasyid 19624101
Billy Ontoseno Irawan 19624130
Wa Ode Amerta Lambelu 19624136
'''

import time
import cv2
import webbrowser
import math
import os
import pyqrcode
import png

vipsize = [0,0]
tarifvipawal = [0,0]
tarifvip = [0,0]
parksize = [0,0,0]
tarifawal = [0,0,0]
tarif = [0,0,0]
tarifmaks = [0,0,0]
tarifvalet = [0,0,0]

print("\n===================================  SETUP  =================================\n")
for i in range(3):
    if i == 0:
        parksize[i] = int(input("Masukkan jumlah tempat parkir mobil yang ada: "))
        vipsize[i] = int(input("Masukkan jumlah tempat parkir VIP mobil yang ada: "))
    elif i == 1:
        parksize[i] = int(input("\nMasukkan jumlah tempat parkir motor yang ada: "))
        vipsize[i] = int(input("Masukkan jumlah tempat parkir VIP motor yang ada: "))
    else:
        parksize[i] = int(input("\nMasukkan jumlah tempat parkir bus/truk yang ada: "))
        break
    tarifawal[i] = int(input("Masukkan tarif parkir reguler jam pertama: "))
    tarif[i] = int(input("Masukkan tarif parkir reguler per jam: "))
    tarifmaks[i] = int(input("Masukkan tarif parkir reguler maksimal per hari: "))
    tarifvipawal[i] = int(input("Masukkan tarif parkir VIP jam pertama: "))
    tarifvip[i] = int(input("Masukkan tarif parkir VIP per jam: "))
    tarifvalet[i] = int(input("Masukkan tarif parkir valet: "))
    
tarifmaks[2] = int(20000)
tarifawal[2]= int(input("Masukkan tarif parkir (flat): "))

print("\n=============================================================================")
os.system('cls' if os.name == 'nt' else 'clear')

#Setup parkir mobil, motor, dan bus/truk
parkir =[["0" for i in range(parksize[0])], #Parkir Mobil
         ["0" for i in range(parksize[1])], #Parkir Motor
         ["0" for i in range(parksize[2])]] #Parkir Bus/Truk

parkirvip = [["0" for i in range(vipsize[0])], #Parkir VIP Mobil
             ["0" for i in range(vipsize[1])]] #Parkir VIP Motor
           
programjalan = True

def clear():
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    
def displayParkir(jenis, tipe):
     if tipe == 1:
         # Hitung ukuran grid
         gridsize = math.ceil(math.sqrt(vipsize[jenis-1]))

         # Representasikan array dalam grid
         grid = [["" for _ in range(gridsize)] for _ in range(gridsize)]

         # Isi grid dengan data parkir
         for i, value in enumerate(parkirvip[jenis-1]):
             row = i // gridsize
             col = i % gridsize
             if value == "0":
                 grid[row][col] = "\u25A1"  # Karakter □ (□)
             else:
                 grid[row][col] = "\u25A3"  # Karakter ▣ (▣)

         # Tampilkan grid
         print("  " + " ".join(str(i+1) for i in range(gridsize)))  # Header kolom
         for i, row in enumerate(grid):
             print(chr(65 + i), " ".join(row))  # Baris dengan label alfabet
     else:
         # Hitung ukuran grid
         gridsize = math.ceil(math.sqrt(parksize[jenis-1]))

         # Representasikan array dalam grid
         grid = [["" for _ in range(gridsize)] for _ in range(gridsize)]

         # Isi grid dengan data parkir
         for i, value in enumerate(parkir[jenis-1]):
             row = i // gridsize
             col = i % gridsize
             if value == "0":
                 grid[row][col] = "\u25A1"  # Karakter □ (□)
             else:
                 grid[row][col] = "\u25A3"  # Karakter ▣ (▣)

         # Tampilkan grid
         print("  " + " ".join(str(i+1) for i in range(gridsize)))  # Header kolom
         for i, row in enumerate(grid):
             print(chr(65 + i), " ".join(row))  # Baris dengan label alfabet


def parkirkanDuluLe(plat, jenis, tempat, tipe):
    
    
    waktumasuk = time.strftime("%H%M")
    if tipe != 3:
        #Decode input posisi seperti A2 menjadi indeks array
        row = ord(tempat[0].upper()) - 65  # Konversi huruf ke indeks baris (A=0, B=1, ...)
        col = int(tempat[1:]) - 1  # Konversi angka ke indeks kolom
        gridsize = math.ceil(math.sqrt(parksize[jenis-1]))
        if tipe == 1:
            gridsize = math.ceil(math.sqrt(vipsize[jenis-1]))
        indexparkir = row * gridsize + col
    QRlink = waktumasuk + plat
    if tipe == 1:
        QRlink = QRlink + "VIP"
        if parkirvip[jenis-1][indexparkir] == "0":
            parkirvip[jenis-1][indexparkir] = QRlink
            url = pyqrcode.create(QRlink)
            url.png(f"{QRlink}.png", scale = 6)
        else:
            print(f"Tempat parkir {tempat} sudah terisi.")

    elif tipe == 2:
        QRlink = QRlink + "reg"
        if parkir[jenis-1][indexparkir] == "0":
            parkir[jenis-1][indexparkir] = QRlink
            url = pyqrcode.create(QRlink)
            url.png(f"{QRlink}.png", scale = 6)
        else:
            print(f"Tempat parkir {tempat} sudah terisi.")
    else:
      QRlink = QRlink + "val"
      for i in range(parksize[jenis-1]):
        if parkir[jenis-1][i] == "0":
            parkir[jenis-1][i] = QRlink
            url = pyqrcode.create(QRlink)
            url.png(f"{QRlink}.png", scale = 6)
            break
        

def sudahParkir(plat):
    for i in range(3):
        for j in range(parksize[i]):
            if plat == parkir[i][j][4:-3]:
                return True
    for i in range(2):
        for j in range(vipsize[i]):
            if plat == parkirvip[i][j][4:-3]:
                return True
    return False
    
def IsParkirFull(jenis, tipe):
    if tipe == 1:
        for i in range(vipsize[jenis-1]):
            if parkirvip[jenis-1][i] == "0":
                return False
        return True
    else:
        for i in range(parksize[jenis-1]):
            if parkir[jenis-1][i] == "0":
                return False
        return True

def scanQR():
    video = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    while True:
        _, frame = video.read() # Hanya perlu frame video
        data, _, _ = detector.detectAndDecode(frame)
        if data:
            return data
        
def keluar(dataparkir):
    waktukeluar = time.strftime("%H%M")
    waktukeluar = int(waktukeluar[:2])*60 + int(waktukeluar[2:])
    waktumasuk = int(dataparkir[:2])*60 + int(dataparkir[2:4])
    plat = dataparkir[4:-3]
    biaya = 0
    if sudahParkir(plat) == True:
        if dataparkir[-3:] == "VIP":
            for i in range(2):
                for j in range(vipsize[i]):
                    if parkirvip[i][j] == dataparkir:
                        biaya = tarifvipawal[i] + (math.ceil((waktukeluar-waktumasuk)/60))*tarifvip[i]
        else:
            for i in range(3):
                for j in range(parksize[i]):
                    if parkir[i][j] == dataparkir:
                        biaya = tarifawal[i] + (math.ceil((waktukeluar-waktumasuk)/60))*tarif[i]
                        if biaya > tarifmaks[i]:
                            biaya = tarifmaks[i]
                        if dataparkir[-3:] == "val":
                            biaya += tarifvalet[i]      
        print(f"Biaya Parkir: Rp.{biaya},-")
        print("Metode Pembayaran:\n[1]Kartu\n[2]Cash")
        metode = int(input("Pilih metode pembayaran:"))
        if metode == 1:
            while True:
                pembayaran= int(input("Jumlah saldo:"))
                if pembayaran >= biaya:
                    parkir[i][j] = "0"
                    print("Pembayaran diterima. Hati - hati di jalan!")
                    break
            else:
                print("Saldo tidak cukup. Tolong isi saldo Anda dan tempelkan kartu pembayaran")
        elif metode == 2:
            while True:
                pembayaran= int(input("Jumlah uang:"))
                if pembayaran >= biaya:
                    parkir[i][j] = "0"
                    print(f"Pembayaran diterima. Kembalian: Rp{pembayaran - biaya},-\nHati - hati di jalan!")
                    break
            else:
               print("Uang belum mencukupi.")
    else:
         print("Kendaraan tidak ditemukan di dalam tempat parkir")
        
while programjalan:
    print("\n\n=======================TARIF PARKIR=====================\n")
    for i in range(3):
        if i == 0:
            print("\nMOBIL")
        elif i == 1:
            print("\nMOTOR")
        else:
            print("\nBUS/TRUK")
            break
        print(f"\nREGULER\nRp.{tarifawal[i]},-/Jam pertama\nRp.{tarif[i]},-/Jam berikutnya; maksimal Rp.{tarifmaks[i]},- per hari")
        print(f"\nVIP\nRp.{tarifvipawal[i]},-/Jam pertama\nRp.{tarifvip[i]},-/Jam berikutnya")
        print(f"\nTarif Valet: Rp.{tarifvalet[i]},-")
    print(f"\nRp.{tarifawal[2]},- (flat)")
    print("\n========================================================\n")
    print("\nPilih Aksi\n[1]Masuk\n[2]Keluar\n[3]Exit Program")
    aksi = int(input("Aksi: "))
    if aksi == 1:
        print("\nJenis Kendaraan\n1. Mobil    2. Motor  3. Bus/Truk")
        jenis = int(input("Jenis Kendaraan: "))
        tipepark = 2
        if jenis !=3:
            print("\nPilih tipe parking:\n[1]VIP\n[2]Reguler\n[3]Valet")
            tipepark = int(input())
        if not IsParkirFull(jenis,tipepark):
            tempat = "A1"
            plat = input("Masukkan plat kendaraan: ")
            plat = plat.replace(" ","")
            if not sudahParkir(plat):
                if tipepark == 3:
                    parkirkanDuluLe(plat, jenis, tempat, tipepark)
                    print("Silahkan masuk")
                    clear()
                else:
                    displayParkir(jenis, tipepark)
                    tempat = input("\n\nPilih tempat parkir: ")
                    parkirkanDuluLe(plat, jenis, tempat, tipepark)
                    print("Silahkan masuk")
                    clear()
            else:
                print("Kendaraan sudah berada di dalam tempat parkir")
                clear()
        else:
            print("Maaf, tempat parkir penuh")
            clear()          
    elif aksi == 2:
        print("Tunjukkan kode QR parkir")
        dataparkir = scanQR()
        cv2.destroyAllWindows
        keluar(dataparkir)
        clear()
    elif aksi == 3:
        print("Mematikan program...")
        time.sleep(2)
        programjalan = False
        
        
