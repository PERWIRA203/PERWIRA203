import math

print("Ini program menghitung akar persamaan kuadrat > AX^2 + BX + C = 0")

A = int(input("Masukkan nilai A : "))
B = int(input("Masukkan nilai B : "))
C = int(input("Masukkan nilai C : "))

def diskri(A, B, C):    
    D = B*B - 4 * A * C

    if (D > 0):
        X3 = (-B + math.sqrt(D))/(2 * A)
        X4 = (-B - math.sqrt(D))/(2 * A)
        print("Nilai D = ", D)
        print("Nilai akar 1 = ", X3)
        print("Nilai akar 2 = ", X4)
        print("Grafik memotong sumbu x di 2 titik yang berbeda")

    elif (D == 0):
        X5 = (-B)/(2 * A)
        print("Nilai D = ", D)
        print("Nilai akar = ", X5)
        print("Grafik menyinggung sumbu X")

    elif (D < 0):
        print("Akar imaginer")
        print("Grafik tidak memotong sumbu X")

print(diskri(A, B, C))

Jawab = str(input("Anda ingin mengulang ? y/t :  "))

if (Jawab == 'y'):
    while(Jawab == 'y'):
        A = int(input("Masukkan nilai A : "))
        B = int(input("Masukkan nilai B : "))
        C = int(input("Masukkan nilai C : "))
        print(diskri(A, B, C))
        Jawab = input("Anda ingin mengulang ? y/t :  ")
        if Jawab == 't':
            print("Terima kasih telah menggunakan program saya")
            break

elif (Jawab == 't'):
    print("Terima kasih telah menggunakan program saya")

else:
    print("Mohon maaf hanya menerima y/t")
    








