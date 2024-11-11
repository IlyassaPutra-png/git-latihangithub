'''
Nama: Ilyassa Putra
Nim: 2402741
Kelas: 1-C RPL
TUGAS lOGIN
'''

username = "Daspro2023"
password ="Latihan"
kesempatan_login = 3
batas = 0
print("\nSelamat datang di sistem login Admin |0_0|")
print(f"Dengan Username: {username}")
print("Anda memiliki 3 kesempatan untuk memasukkan password yang benar.\n")

while batas < kesempatan_login:
    a = input("Masukan Password yang sudah tersimpan: ")
    
    if a  == password:
        print("Login berhasil!!!! selamat datang admin |0_0|")
        break
    else:
        batas+= 1
        if batas < kesempatan_login:
            print(f"Login Salah! Kesempatan Anda {kesempatan_login- batas}x kali lagi.")
        else:
            print("Anda tidak diperkenankan mengakses aplikasi ini.")

