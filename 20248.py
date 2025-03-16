import tkinter as tk
import random

class Game2048:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("2048")
        
        self.papan = [[0] * 4 for _ in range(4)]
        self.kanvas = tk.Canvas(self.root, width=400, height=400, bg="white")
        self.kanvas.pack()
        
        self.root.bind("<KeyPress>", self.gerakan)
        self.tambah_ubin()
        self.tambah_ubin()
        self.perbarui_tampilan()
        
        self.root.mainloop()
    
    def tambah_ubin(self):
        pilihan = [(i, j) for i in range(4) for j in range(4) if self.papan[i][j] == 0]
        if pilihan:
            baris, kolom = random.choice(pilihan)
            self.papan[baris][kolom] = random.choice([2, 4])
    
    def perbarui_tampilan(self):
        self.kanvas.delete("all")
        for i in range(4):
            for j in range(4):
                nilai = self.papan[i][j]
                warna = "#CDC1B4" if nilai == 0 else "#EEE4DA"
                self.kanvas.create_rectangle(j * 100, i * 100, (j + 1) * 100, (i + 1) * 100, fill=warna, outline="black")
                if nilai:
                    self.kanvas.create_text(j * 100 + 50, i * 100 + 50, text=str(nilai), font=("Arial", 24, "bold"))
    
    def gerakan(self, event):
        if event.keysym in ('Up', 'Down', 'Left', 'Right'):
            if self.gerak_papan(event.keysym):
                self.tambah_ubin()
                self.perbarui_tampilan()
    
    def gerak_papan(self, arah):
        papan_lama = [baris[:] for baris in self.papan]
        if arah == 'Up':
            self.papan = self.transposisi(self.papan)
            self.geser()
            self.papan = self.transposisi(self.papan)
        elif arah == 'Down':
            self.papan = self.transposisi(self.papan)
            self.balik()
            self.geser()
            self.balik()
            self.papan = self.transposisi(self.papan)
        elif arah == 'Left':
            self.geser()
        elif arah == 'Right':
            self.balik()
            self.geser()
            self.balik()
        return papan_lama != self.papan
    
    def geser(self):
        for i in range(4):
            baris = [nilai for nilai in self.papan[i] if nilai != 0]
            for j in range(len(baris) - 1):
                if baris[j] == baris[j + 1]:
                    baris[j] *= 2
                    baris[j + 1] = 0
            baris = [nilai for nilai in baris if nilai != 0]
            self.papan[i] = baris + [0] * (4 - len(baris))
    
    def transposisi(self, papan):
        return [list(baris) for baris in zip(*papan)]
    
    def balik(self):
        for i in range(4):
            self.papan[i].reverse()

if __name__ == "__main__":
    Game2048()