##################################################################################################
#
# Author:  Mamata Anil Parab                           
# Project: Automation to copy files of specified type from one directory into another directory       
# Input:   "Mamata", "Demo"                              
# Output:  "Files are copied"
#
###################################################################################################
import os
from sys import *
import shutil

def DirectoryCopy(path,destination,FileExt):
    flag=os.path.isabs(path)
    if flag==False:
        path=os.path.abspath(path)
   
    exists=os.path.isdir(path)
    if exists:
       # destination=os.mkdir(path,"w");
        for FolderName,SubFolderName,FileName in os.walk(path):
            for item in os.listdir(FolderName):
                print(item)
            for file in FileName:
                if file.endswith(FileExt):
                     shutil.copy(file,destination)
                     #print(file)

                

def main():

    if len(argv)<3:
        print("Error: Invalid number of input arguments")

    if(argv[1]=="-u" or argv[1]=="-U"):
        print("usage: ApplicationName AbsolutePath_Of_Directory Extension1 Extension2")

    if(argv[1]=="-h" or argv[1]=="-H"):
        print("This script is used to change file extension")

    print("Application name: ",argv[0]);

    try:
        DirectoryCopy(argv[1],argv[2],argv[3])

    except ValueError:
        print("Error:Invalid datatype of input");
        
    except Exception:
        print("Error: Invalid input");


if __name__=="__main__":
    main()
        
