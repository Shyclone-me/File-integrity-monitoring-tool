import os
import hashlib
import time
import json

def Banner(banner):        
    print()

def stats(fullpath):
    stat = os.stat(fullpath)
    size = stat.st_size
    modtime = stat.st_mtime
    
    for i in ['B','KB','MB','GB']:
        if size < 1024: 
            realsize = f"{size:.2f} {i}"
            break
        size /= 1024 
    
    real_time = time.ctime(modtime)
    
    return realsize, real_time

def baseline(path):
    hashlist={}
    def hash_calculator(secondpath):
        sha256=hashlib.sha256()
        try:
            with open(secondpath, "rb") as f:
                while chunk := f.read(4096):
                    sha256.update(chunk)
            return sha256.hexdigest()
        except (FileNotFoundError, PermissionError):
            return None
    for roots,dirs,files in os.walk(path):
        for file in files:
            secondpath = os.path.join(roots,file)
            size , modtime = stats(secondpath) 
            filehash = hash_calculator(secondpath)
            if filehash:
                hashlist[secondpath] = {"HASH ":filehash,"SIZE ": size, "LASTmodificationTIME ": modtime}
                print("hashed : ", secondpath)
    return hashlist
            

def jsonm(path,hashlist):    
    jsonname = input("Enter a name to save as : ")   
    with open(f"hashfolder/{jsonname}.json", "w") as json_file:
        json.dump(hashlist,json_file,indent=4)
    return True


def verify(path):
    print()

def auto(path):
    print()
    

def userchoice():
    Banner("front")
    path = input("Enter file location: ")
    if os.path.exists(path):
        choice = int(input("Enter your choice: "))
        if choice == 1:
            hashlsit= baseline(path)
            if jsonm(path, hashlsit):
                print(f"Hashlist is saved in json sucessfully with name {path}.json")
            
        elif choice == 2:
            verify(path)
        elif choice == 3:
            auto(path)
        elif choice == 4:
            print(exit)
        else:
            print("Enter a valid choice: ")    
    else:
        print("path doesnot exists")
userchoice()