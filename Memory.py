import os
from os.path import exists
import json

class Memory(object):

    def RenameFile(self,filename, newfilename):
        f = Memory()
        file_exists = f.FileExists(filename)
        newfile_exists = f.FileExists(filename)
        if file_exists == False:
            print(f"Error: Origional file, \'{filename}\', does not exist.")
        else:
            if newfile_exists == True:
                print(f"Error: New file name, \'{newfilename}\', already exists.")
            else:
                os.rename(filename,newfilename)

    def FileExists(self,filename):
        file_exists = os.path.exists(filename)
        return file_exists

    def CreateFile(self,filename):
        f = Memory()
        file_exists = f.FileExists(filename)
        if file_exists == True:
            print(f"Error: The file, \'{filename}\', already exists.")
        else:
            open(filename,"x")
            
    def DeleteFile(self,filename):
        f = Memory()
        file_exists = f.FileExists(filename)
        if file_exists == False:
            print(f"The file you want to delete, \'{filename}\', does not exist.")
        else:
            os.remove(filename)
     
    def DeleteFolder(self,foldername):
        os.rmdir(foldername)

    def CreateFolder(self,parent_dir,foldername):
        path = os.path.join(parent_dir,foldername)
        try:
            os.mkdir(path, exist_ok = True)
            print(f"Directory '%s' sucessfully created." % foldername)
        except OSError as error:
            print("Directory '%s' can not be created." % foldername)


    def updateIntentsTxt(self, filename, tag, patterns, responses):
        # open or create new file
        f = Memory()
        file_exists = f.FileExists(filename)
        if file_exists == False:
            print(f"Error: The file you want to update, \'{filename}\', does not exist.")
        else:
            with open(filename) as f:
                data = f.readlines()
            intent = f",\n {{\"tag\": \"{tag}\", \"patterns\": [\"{patterns}\"], \"responses\": [\"{responses}\"], \"context_set\": \"\" }}"
            f.write(intent)
            f.close()

    def addIntentsJson(self,filename,tag,patterns,responses):
        new_data = {
            "tag":tag,
            "patterns":patterns,
            "responses":responses,
            "context_set":""}
        with open(filename,"r+") as f:
            data = json.load(f)
            data["intents"].append(new_data)
            f.seek(0)
            json.dump(data,f, indent = 4)

    def updateIntentsJson(self,filename,reference,json_item,new_value):
        with open(filename,'r') as f:
            data = json.load(f)
            for item in data:
                if item[json_item] in ["Shell","Type"]:
                    item[json_item] = "new value"
        with open(filename,'w') as f:
            json.dump(data,f,indent=4)

    def getIntentValue(self,filename,tag):
        data = ReadJson(filename)
        value = data["intents"][0][tag]
        return value

    def getProfileValue(self, filename, profile, name, feature):
        data = ReadJson(filename)
        value = data[profile][0][name][feature]
        return value

    
    def updateProfileValue(self,filename,profile,name,feature,newValue):
        data = ReadJson(filename)
        data[profile][0][name][feature] = newValue
        WriteJson(filename,data)

def ReadJson(filename):
    with open(filename,'r+') as f:
        data = json.load(f)
    return data

def WriteJson(filename,data):
    with open(filename,'w') as f:
        json.dump(data,f,indent=4)
        
