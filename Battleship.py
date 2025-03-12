import random

def buat_papan(ukuran):
    return [['O' for _ in range(ukuran)] for _ in range(ukuran)]

def cetak_papan(papan):
    for baris in papan:
        print(" ".join(baris))

def tempatkan_kapal(papan):
    ukuran = len(papan)
    return random.randint(0, ukuran - 1), random.randint(0, ukuran - 1)

def dapatkan_tebakan_pemain():
    baris = int(input("Masukkan baris: "))
    kolom = int(input("Masukkan kolom: "))
    return baris, kolom

def permainan_battleship():
    ukuran = 5
    papan = buat_papan(ukuran)
    kapal_baris, kapal_kolom = tempatkan_kapal(papan)
    percobaan = 5
    
    print("Selamat datang di Battleship!")
    cetak_papan(papan)
    
    for percobaan_ke in range(percobaan):
        print(f"Percobaan {percobaan_ke + 1} dari {percobaan}")
        tebakan_baris, tebakan_kolom = dapatkan_tebakan_pemain()
        
        if (tebakan_baris, tebakan_kolom) == (kapal_baris, kapal_kolom):
            print("Selamat! Anda menenggelamkan kapal musuh!")
            return
        else:
            if 0 <= tebakan_baris < ukuran and 0 <= tebakan_kolom < ukuran:
                papan[tebakan_baris][tebakan_kolom] = "X"
                print("Meleset! Coba lagi.")
            else:
                print("Di luar batas! Coba lagi.")
        cetak_papan(papan)
    
    print("Permainan selesai! Kapal berada di:", kapal_baris, kapal_kolom)

if __name__ == "__main__":
    permainan_battleship()
