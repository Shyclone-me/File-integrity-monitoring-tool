import hashlib
import os
import json
import time

path = input("ENter parh : ")
hashlist = {}

def hash_file(file_path):
    sha256 = hashlib.sha256() 
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):  
                sha256.update(chunk)       
        return sha256.hexdigest()        
    except (PermissionError, FileNotFoundError):
        return None
def stat(fullpath):
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
    
    
    
for root, dirs, files in os.walk(path):
    folderhash = {}
    for file in files:
        fullpath = os.path.join(root, file)
        size, modtime = stat(fullpath)
        
        filehash = hash_file(fullpath)
        if filehash:
            hashlist[fullpath] = {"Hash": filehash,"size": size ,"mod_time": modtime}
            print("Hashed : ",fullpath)
            


print("hash Dictionary",hashlist)

