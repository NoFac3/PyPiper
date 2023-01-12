import os
from os.path import exists
import json

def RenameFile(filename, newfilename):
    file_exists = FileExists(filename)
    newfile_exists = FileExists(newfilename)
    if file_exists == False:
        print(f"Error: Origional file, \'{filename}\', does not exist.")
    else:
        if newfile_exists == True:
            print(f"Error: New file name, \'{newfilename}\', already exists.")
        else:
            os.rename(filename,newfilename)

def FileExists(filename):
    file_exists = os.path.exists(filename)
    return file_exists

def CreateFile(filename):
    file_exists = FileExists(filename)
    if file_exists == True:
        print(f"Error: The file, \'{filename}\', already exists.")
    else:
        open(filename,"w")

def DeleteFile(filename):
    file_exists = FileExists(filename)
    if file_exists == False:
        print(f"The file you want to delete, \'{filename}\', does not exist.")
    else:
        os.remove(filename)
     
def DeleteFolder(foldername):
    os.rmdir(foldername)

def CreateFolder(parent_dir,foldername):
    path = os.path.join(parent_dir,foldername)
    try:
        os.mkdir(path, exist_ok = True)
        print(f"Directory {foldername} sucessfully created.")
    except OSError as error:
        print(f"Directory {foldername} can not be created.")

def addIntentsJson(filename,tag,patterns,responses):
    new_data = {
            "tag":tag,
            "patterns":patterns,
            "responses":responses,
            "context_set":""}
    data = ReadJson(filename)
    data["intents"].append(new_data)
    WriteJson(filename,data)

def setJsonValue(new_value,filename,key,tag,subkey):
    data = ReadJson(filename)
    keys = data.keys()
    for k in keys:
        if k == key:
            if tag=="":
                data[k] = new_value
            elif tag!="":
                if len(subkey)==0:
                    data[k][0][tag] = new_value
                elif len(subkey)==1:
                    data[k][0][tag][subkey[0]] = new_value
                else:
                    data[k][0][tag][subkey[0]][subkey[1]] = new_value
        WriteJson(filename,data)
                
def getJsonValue(filename,key,tag,subkey):
    value = ""
    data = ReadJson(filename)
    keys = data.keys()
    for k in keys:
        if k == key:
            if tag=="":
                value = data[k]
            elif tag!="":
                if len(subkey)==0:
                    value = data[k][0][tag]
                elif len(subkey)==1:
                    value = data[k][0][tag][subkey[0]]
                else:
                    value = data[k][0][tag][subkey[0]][subkey[1]]
    return value

def ReadJson(filename):
    with open(filename,'r+') as f:
        data = json.load(f)
    return data

def WriteJson(filename,data):
    with open(filename,'w') as f:
        f.seek(0)
        json.dump(data,f,indent=4)



