'''
This is a simple password manager that is not meant to be used for any serious passwords
This project is just a way to practice my developing python skills

program will still work with the wrong master password, however
incorrect results will be developed as encryption and decryption 
process need the correct master password
'''

from cryptography.fernet import Fernet

# Uncomment this function if you need to generate a new key
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, encrypted_password = data.split(" | ")
                try:
                    password = fer.decrypt(encrypted_password.encode()).decode()
                except Exception as e:
                    print(f"Error decrypting password for {user}: {e}")
                    password = "Decryption error"
                print(f"User: {user}\nPassword: {password}\n")
    except FileNotFoundError:
        print("No passwords file found. Please add a password first.")

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()

    # 'with' will automatically open and close the file
    with open('passwords.txt', 'a') as f:
        f.write(name + " | " + encrypted_pwd + "\n")

while True:
    mode = input("Would you like to add a new password or view existing passwords (view, add) press q to quit\n").lower()
    if mode == "q":
        quit()
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
