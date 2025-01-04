#!/usr/bin/env python3

import os
import time
from cryptography.fernet import Fernet 

exclude = ["encrypter.py", "decrypter.py", "key.key", "README.md"]

def list_files(exclude):
    archives = [file for file in os.listdir() if os.path.isfile(file) and file not in exclude]
    return archives

def load_decryption_key(file_name="key.key"):
    with open(file_name, "rb") as key_file:
        key = key_file.read()
    return key

def get_passphrase(key, file):
    fernet = Fernet(key)
    with open(file, "rb") as pw:
        encrypted_pwd = pw.read()
    decrypted_pwd = fernet.decrypt(encrypted_pwd)
    return decrypted_pwd.decode("utf-8")

def decrypt_files(key, exclude):
    fernet = Fernet(key)
    print("\033[32mDecryption key loaded\033[0m")
    files = list_files(exclude)

    for file in files:
        with open(file, "rb") as target:
            content = target.read()
        decrypted_content = fernet.decrypt(content)

        with open(file, "wb") as target:
            target.write(decrypted_content)

def main():
    pw = get_passphrase(load_decryption_key(), "passphrase")
    password = input("\033[1;34mInsert decryption passphrase: \033[0m").strip()

    while password != pw.strip():
        password = input("\033[31mIncorrect passphrase, try again: \033[0m").strip()
    if password == pw.strip():
        print ("\033[32mCorrect password, decryption starting\033[0m")
        time.sleep(2)
        decrypt_files(load_decryption_key(), exclude)
        time.sleep(2)
        print("\033[32mDecryption completed\033[0m")
        time.sleep(1)

main()
