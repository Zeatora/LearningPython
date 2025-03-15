from threading import Timer
import time
import tkinter as tk
from tkinter import *
from datetime import datetime
import winsound
from win10toast import ToastNotifier

window = Tk()
window.geometry('600x600')
window.title('Simple Hitungan Mundur Python')

head = Label(window, text="Jam Hitungan Mundur dan Pengatur Waktu", font=("Fredoka"))
head.pack(pady=20)

Label(window, text="Enter time in HH:MM:SS", font=("bold")).pack()

jam = StringVar()
menit = StringVar()
detik = StringVar()
hitungan = IntVar()
cek = BooleanVar()

Entry(window, textvariable=jam, width=30).pack()
Entry(window, textvariable=menit, width=30).pack()
Entry(window, textvariable=detik, width=30).pack()

Checkbutton(window, text='Cek Musik', onvalue=True, variable=cek).pack()

label = Label(window, text="00:00", font=("Fredoka", 20))
label.pack()

def countdown():
    try:
        h = int(jam.get()) if jam.get() else 0
        m = int(menit.get()) if menit.get() else 0
        s = int(detik.get()) if detik.get() else 0
        t = h * 3600 + m * 60 + s

        def update():
            nonlocal t
            if t > 0:
                mins, secs = divmod(t, 60)
                display = '{:02d}:{:02d}'.format(mins, secs)
                label.config(text=display)
                t -= 1
                window.after(1000, update)
            else:
                label.config(text="Waktu Habis")
                if cek.get():  
                    winsound.Beep(440, 1000)

        update()

    except ValueError:
        label.config(text="Input tidak valid")

Button(window, text="Set Hitungan Mundur", command=countdown, bg='green').place(x=260, y=230)

now = datetime.now()
currentTime = now.strftime("%H:%M:%S")
Label(window, text=currentTime).pack()

toast = ToastNotifier()
toast.show_toast("Notifikasi", "Timer dimatikan", duration=5, threaded=True)

window.mainloop()
