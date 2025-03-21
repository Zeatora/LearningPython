import pyautogui
import time

def auto_clicker(interval, duration):
    print("Auto Clicker dimulai! Tekan CTRL + C untuk berhenti.")
    start_time = time.time()
    
    try:
        while time.time() - start_time < duration:
            pyautogui.click()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Auto Clicker dihentikan oleh pengguna.")
    
if __name__ == "__main__":
    interval = float(input("Masukkan interval antar klik (dalam detik): "))
    duration = float(input("Masukkan durasi Auto Clicker (dalam detik): "))
    auto_clicker(interval, duration)
