masuk = (input("Mau Kali/Tambah/Kurang/Bagi : "))

if (masuk == "Kali"):
    Data1 = int(input("Masukkan angka 1 : "))
    Data2 = int(input("Masukkan angka 2 : "))
    Hasil1 = Data1*Data2
    print("Hasil perkalian : ", Hasil1)
elif (masuk == "Tambah"):
    Data1 = int(input("Masukkan angka 1 : "))
    Data2 = int(input("Masukkan angka 2 : "))
    Hasil2 = Data1+Data2
    print("Hasil perkalian : ", Hasil2)
elif (masuk == "Kurang"):
    Data1 = int(input("Masukkan angka 1 : "))
    Data2 = int(input("Masukkan angka 2 : "))
    Hasil3 = Data1-Data2
    print("Hasil perkurangan : ", Hasil3)
elif (masuk == "Bagi"):
    Data1 = int(input("Masukkan angka 1 : "))
    Data2 = int(input("Masukkan angka 2 : "))
    Hasil4 = Data1/Data2
    print("Hasil pembagian : ", Hasil4)
else:
    print("Mohon maaf hasil kurang sesuai")
