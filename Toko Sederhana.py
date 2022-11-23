import os

Barang = []
Kuantitas = []
Harga = []
barangBeli = []
kuantitasBeli = []

def halamanLogin():
    os.system('cls')
    print("====== NineThirteen ======\n")
    print("1. Penjual")
    print("2. Pembeli")
    pilihLogin = int(input("\nMasuk Sebagai : "))
    login(pilihLogin)

def halamanPenjual():
    os.system('cls')
    print("====== NineThirteen ======\n")
    print("1. List Barang")
    print("2. Input Barang")
    print("3. Delete Barang")
    print("4. Update Barang")
    print("5. Back")
    pilihMenu = int(input("\nPilih Menu : "))
    menuPenjual(pilihMenu)

def halamanPembeli():
    os.system('cls')
    List(2)
    Back()
    halamanLogin()

def login(pilih):
    if pilih == 1:
        os.system('cls')
        halamanPenjual()
    elif pilih == 2:
        os.system('cls')
        halamanPembeli()
    else:
        print("Pilihan Tidak Tersedia")
        Back()
        halamanLogin()

def Back():
    back = input("Press any to continue")

def List(user):
    os.system('cls')
    print("\t\t     ====== NineThirteen ======\n")
    print("===================================================================")
    print("No\tNama Barang\t\tJumlah Stock\t\tHarga")
    print("===================================================================")
    if user == 1:
        for i in range(len(Kuantitas)):
            print(str(i+1) +".\t"+ Barang[i] +"\t\t\t"+ str(Kuantitas[i]) +"\t\t\tRp "+ str(Harga[i]))
    elif user == 2:
        menuBeli(Barang,Kuantitas,Harga)      

def menuBeli(Barang,Kuantitas,Harga):
    newBarang = []
    newKuantitas = []
    newHarga = []
    for i in range(len(Barang)):
        if Kuantitas[i] != 0:
            newBarang.append(Barang[i])
            newKuantitas.append(Kuantitas[i])
            newHarga.append(Harga[i])
    for i in range(len(newBarang)):
        print(str(i+1) +".\t"+ newBarang[i] +"\t\t\t"+ str(newKuantitas[i]) +"\t\t\tRp "+ str(newHarga[i]))
    pilihBarang = int(input("\nPilih Barang : ")) - 1
    for i in range(len(Barang)):
        if pilihBarang+1 > len(Barang):
            print("Barang Tidak Ditemukan")
            Back()
            List(2)
        elif Barang[i] == newBarang[pilihBarang]:
            Pembayaran(i)
  
def menuPenjual(pilih):
    if pilih == 1:
        os.system('cls')
        List(1)
        Back()
        halamanPenjual()

    elif pilih == 2:
        Lanjut = True
        while(Lanjut):
            barangBaru =  input("Nama Barang  : ")
            KuantitasBaru = int(input("Jumlah Barang: "))
            HargaBaru =   int(input("Harga Barang : "))
            inputBarang(barangBaru, KuantitasBaru, HargaBaru)
            tambah = input("Ingin Menambahkan? (y/t): ")
            if(tambah == "t"): 
                Lanjut = False
        os.system('cls')
        halamanPenjual()

    elif pilih == 3:
        os.system('cls')
        if len(Barang) == 0:
            print("Barang Tidak Tesedia")
            Back()
            halamanPenjual()
        else:
            List(1)
            pilihUser = int(input("Pilih Barang untuk Dihapus: "))-1
            deleteBarang(pilihUser)

    elif pilih == 4:
        os.system('cls')
        if len(Barang) == 0:
            print("Barang Tidak Tesedia")
            Back()
            halamanPenjual()
        else:
            List(1)
            pilihUser = int(input("Pilih Barang untuk Diupdate: "))-1
            KuantitasBaru = int(input("Jumlah Baru: "))
            HargaBaru =   int(input("Harga Baru : "))
            updateBarang(pilihUser, KuantitasBaru, HargaBaru)
    
    elif pilih == 5:
        os.system('cls')
        halamanLogin()

    else:
        print("Pilihan Tidak Tersedia")
        Back()
        halamanPenjual()

def Beli(pilih):
    Hasil = Kuantitas[pilih] - 1
    Kuantitas[pilih] = Hasil

def Pembayaran(pilih):
    bayar = int(input("Masukkan Jumlah Uang : Rp "))
    if bayar < Harga[pilih]:
        print("Uang Anda Tidak Cukup")
        Pembayaran(pilih)
    else:
        Beli(pilih)
        harga = Harga[pilih]
        kembali = lambda harga,bayar : bayar - harga
        print("Kembalian Anda : Rp " + str(kembali(harga, bayar)))
        HoF(pilih, riwayatPembelian)    

def HoF(pilih, tampil):
    return tampil(pilih)

def riwayatPembelian(pilih):
    if len(barangBeli) == 0:
        barangBeli.append(Barang[pilih])
        kuantitasBeli.append(1)
    else:
        for i in range(len(barangBeli)):
            if barangBeli[i] == Barang[pilih]:
                jumlah = kuantitasBeli[i] + 1
                kuantitasBeli[i] = jumlah
            elif barangBeli[i] != Barang[pilih]:
                barangBeli.append(Barang[pilih])
                kuantitasBeli.append(1)
    print("Riwayat Pembelian Anda : ")
    for i in range(len(barangBeli)):
        print(str(i+1) +". "+ barangBeli[i] +" = "+ str(kuantitasBeli[i]))

def inputBarang(barangBaru, KuantitasBaru, HargaBaru):
    Barang.append(barangBaru)
    Kuantitas.append(KuantitasBaru)
    Harga.append(HargaBaru)

def deleteBarang(pilihUser):
    if(pilihUser+1 > len(Barang)):
        print("Barang Tidak Ditemukan")
        Back()
        halamanPenjual()
    else:
        for i in range(len(Barang)):
            if(pilihUser == i):
                del Barang[pilihUser]
                del Kuantitas[pilihUser]
                del Harga[pilihUser]
                os.system('CLS')
                halamanPenjual()

def updateBarang(pilihUser, KuantitasBaru, HargaBaru):
    if(pilihUser+1 > len(Barang)):
        print("Barang Tidak Ditemukan")
        Back()
        halamanPenjual()
    else:
        for i in range(len(Barang)):
            if(pilihUser == i):
                Kuantitas[pilihUser] = KuantitasBaru
                Harga[pilihUser] = HargaBaru
                os.system('CLS')
                halamanPenjual()

halamanLogin()