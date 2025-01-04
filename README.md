### ransomware-DIO-Cybersecurity
A ransomware malware created for learning means as part of DIO Cybersecurity Bootcamp

### Warning: Be careful while running these scripts
It is recommended that you run these scripts on a virtualized sandbox environment (Virtual Machine).
Be very careful for not letting it affect your personal important information.
Never use it for hurting others.

### encrypter.py
Running "python3 encrypter.py" will encrypt all files encountered in the same directory of the script being run, excluding encrypter.py, decrypter.py and the encryption key that will be generated in the execution. Files file1, file2 and file3 are present for testing.

### decrypter.py and passphrase
passphrase file must contain the password that will be used to decrypt the files. The passphrase file will also be encrypted in the encryption proccess, so the password is not accessible after the encryption. 

Running "python3 decrypter.py" will ask for a password, which is the one set in the passphrase file before it's encryption. By passing the correct password, the files are decrypted.

### running encrypter.py twice in a row will make decryption impossible
Each time encrypter is run, it generates a different encryption key. Running it twice will make the first key be lost. Also, after the first decryption, the decryption process will consider the files decrypted and refuse to decrypt it again.
