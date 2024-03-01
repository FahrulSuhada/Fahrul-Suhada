class kalkulator:
    def tambah(self,a,b,o):
        hasil = a+b
        return hasil
    def kurang(self,a,b,o):
        hasil = a-b
        print(f"Hasil pengurangan dari {a} {o} {b} adalah {hasil} ")
    def kali(self,a,b,o):
        hasil = a*b
        print(f"Hasil perkalian dari {a} {o} {b} adalah {hasil} ")
    def bagi(self,a,b,o):
        if b == 0:
            print("Tidak dapat dibagi 0")
        else:
            hasil = a/b
            print(f"Hasil pembagian dari {a} : {b} adalah {hasil} ")

kalkulator = kalkulator()

while True:
    print('-'*46)
    print('>>'*5, "Aplikasi Fahrul Suhada", '<<'*6)
    print('-'*46)
    print('>>'*7, "SELAMAT DATANG", '<<'*8)
    print('-'*46)
    print("1.Lanjut ke aplikasi kalkulator\n2.Exit")
    pilihan = input("Pilih salah satu dari pilihan diatas (1/2) : ")
    print('-'*46)
    if pilihan == '1':
        print('>>'*6,"APLIKASI KALKULATOR",'<<'*6)
        print('-'*46)
        try:
            a = int(input(">> Silahkan masukan angka pertama : "))
            b = int(input(">> Silahkan masukan angka kedua : "))
        except ValueError:
            print("Undefined!.Tidak dapat kosong atau berisi selain angka!")
        print('-'*46)
        print('>>'*6,"APLIKASI KALKULATOR",'<<'*6)
        print('-'*46)
        print("Penjumlahan =>(+)\nPengurangan =>(-)\nPerkalian =>(*)\nPembagian =>(:)")
        o = str(input("Silahkan pilih satu operasi dari (+,-,*,:) : "))
        print('-'*46)
        if o == '+':
            plus = kalkulator.tambah(a,b,o)
            print(f"Hasil penjumlahan dari {a} {o} {b} adalah {plus} ")
        elif o == '-':
            kalkulator.kurang(a,b,o)
        elif o == '*':
            kalkulator.kali(a,b,o)
        elif o == ':':
            kalkulator.bagi(a,b,o)
        else:
            print("Undefined!. Pilih salah satu dari (+,-,*,:)")
    elif pilihan == '2':
        print("Terimakasih")
        break
    else:
        print("Undefined!\nHanya dapat memlih 1/2!")