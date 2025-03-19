import random

def bola_ajaib():
    respons = [
        "Ya, pasti!",
        "Gak tau!",
        "Kemungkinan.",
        "Tanyakan lagi nanti...",
        "Gak Peduli.",
        "Jangan terlalu berharap.",
        "Tidak.",
        "meragukan."
    ]
    
    print("Selamat datang di Bola Ajaib!")
    while True:
        pertanyaan = input("Ajukan pertanyaan ya/tidak (atau ketik 'keluar' untuk berhenti): ")
        if pertanyaan.lower() == 'keluar':
            print("Sampai jumpa!")
            break
        print("Bola Ajaib berkata:", random.choice(respons), "\n")

if __name__ == "__main__":
    bola_ajaib()