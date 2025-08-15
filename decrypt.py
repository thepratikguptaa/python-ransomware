# Activate virtual environment before running the script:
# source .venv/bin/activate   --- for macOS/Linux
# .venv\Scripts\activate      --- for Windows

import os
from cryptography.fernet import Fernet

# finding files
files = []
for file in os.listdir():
    if file == "the_malware.py" or file == "thekey.key" or file == "decrypt.py" or file == "README.md" or file == "requirements.txt": # process every file except the script itself, the key file, the decryption script, the README file and the requirements file
        continue
    if os.path.isfile(file): # process only files
        files.append(file)

print("Files encrypted:", files)

with open("thekey.key", "rb") as key:
    secretkey = key.read()

secretphrase = "pratik"
user_phrase = input("Say my name: ")

if user_phrase == secretphrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
    print("Files decrypted successfully.")
else:
    print("Wrong name.")
