###############################################################################
#
# Author:  Mamata Anil Parab                           
# Project: Automation to replace file extensions in directory       
# Input:   "Mamata", ".txt" , ".exe"                                
# Output:  "p1.txt" => "p1.exe"
#
###############################################################################

import os
from sys import*
from os.path import splitext

def DirectoryName(path,fileExt1,fileExt2):
    flag=os.path.isabs(path)
    if flag==False:
        path=os.path.abspath(path)
    exists=os.path.isdir(path)
    if exists:
        for FolderName, SubFolderName, FileName in os.walk(path):
            for File in FileName:
                if fileExt1==splitext(File)[1]:
                    newFile=File.replace(fileExt1,fileExt2)
                    print(newFile)
                   # os.rename(os.join(FileName,File),os.join(FileName,newFile))

def main():

    if len(argv)<3:
        print("Error: Invalid number of input arguments")

    if(argv[1]=="-u" or argv[1]=="-U"):
        print("usage: ApplicationName AbsolutePath_Of_Directory Extension1 Extension2")

    if(argv[1]=="-h" or argv[1]=="-H"):
        print("This script is used to change file extension")

    print("Application name: ",argv[0]);

    try:
        DirectoryName(argv[1],argv[2],argv[3])

    except ValueError:
        print("Error:Invalid datatype of input");
        
    except Exception:
        print("Error: Invalid input");


if __name__=="__main__":
    main()
        
