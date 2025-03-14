import random

def lempar_dadu():
    print("Selamat datang di permainan Lempar Dadu!")
    
    while True:
        input("Tekan ENTER untuk melempar dadu (atau ketik 'keluar' untuk berhenti): ")
        hasil = random.randint(1, 6)
        print(f"Hasil lemparan: {hasil}")
        
        keluar = input("Ingin melempar lagi? (ya/tidak): ").lower()
        if keluar == "tidak":
            print("Terima kasih telah bermain!")
            break

if __name__ == "__main__":
    lempar_dadu()