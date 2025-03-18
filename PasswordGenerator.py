import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    num_passwords = int(input("Masukkan jumlah password yang ingin dibuat: "))
    length = int(input("Masukkan panjang setiap password: "))
    
    print("\nGenerated Passwords:")
    for _ in range(num_passwords):
        print(generate_password(length))

if __name__ == "__main__":
    main()
