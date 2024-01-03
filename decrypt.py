from cryptography.fernet import Fernet
import os
import file_path

def  decrypt(items,clef):
    f=Fernet(clef)
    for item in items:
        with open(item,"rb") as File :
            file_data=File.read()
        decrypted_data=f.decrypt(file_data)
        with open(item,"wb") as File :
            File.write(decrypted_data)

def lire_clef():
    return open("clef.key","rb").read()

def decode() :
    clef=lire_clef()
    path=file_path.get_path()
    items=os.listdir(path)
    chemin = [path+"/"+item for item in items]
    decrypt(chemin,clef)
    os.remove("clef.key")
