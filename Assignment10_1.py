###############################################################################
#
# Author:  Mamata Anil Parab                           
# Project: Automation program to find file in directory with particular extension      
# Input:   "Mamata",".txt"                                  
# Output:  P1.txt
#          P2.txt
###############################################################################

from sys import *;
import os;


def DirectoryFileSearch(path,FileExt):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
    exists = os.path.isdir(path)

    if exists:
        for folderName, SubFolder, FileName in os.walk(path):
            for File in FileName:
                if File.endswith(FileExt):
                    print(File)
            print('')
    else:
        print("Invalid Path");


def main():
    if (len(argv)<2):
        print("Error");
    try:
        DirectoryFileSearch(argv[1], argv[2])

    except Exception:
        print("Error: invalid input");


if __name__ == "__main__":
    main();

