import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
keys = chars.copy()

print(f"chars: {chars}")
print(f"keys: {keys}")

random.shuffle(keys)

if __name__ == "__main__":
    is_running = True
    while is_running:
        choice = input("Enter 1 to encrypt the text and 2 to decrypt the text. Else anything to exit: \n")
        if choice == "1":
            plain_text = input("Enter the plain text.\n")
            encrypted_text = ""
            for i in plain_text:
                encrypted_text += keys[chars.index(i)]
            print(encrypted_text)
        elif choice == "2":
            encrypted_text = input("Enter the encrypted text.\n")
            plain_text = ""
            for i in encrypted_text:
                plain_text += chars[keys.index(i)]
            print(plain_text)

        else:
            is_running =False
