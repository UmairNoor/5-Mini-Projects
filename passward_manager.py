from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user , pwd = data.split()
            print("User:" , user , "| Passwords:" , pwd)
def add():
    name = input("Account Name : ")
    pwd = input("passward : ")

    with open('passwords.txt' , 'a') as f:
        f.write(name + "|" + pwd + "\n")


while True : 
    mode = input("Would you like to add new passward or existing ones (add,view) or press q to quit : ")
    if mode == "q":
        break
    elif mode == "view" :
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. ")
        continue 