import os
import sys


def file_valid():
        
    ipFile = "/../tempFiles/ipFile"

    #Checks if file exists
    if(os.path.isfile(os.getcwd() + ipFile )):
        print("IP file Exists")
        nameFile = os.getcwd() + ipFile
    else:
        print("IP file DNE")
        sys.exit()

    #If file exists, then read file and return contents
    contents = open(nameFile,'r')
    temp = contents.readlines()
    contents.close()
    
    return temp


