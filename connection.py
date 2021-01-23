import os
import sys
import re
import time
import paramiko

#checks if file and commands file exists
credFile = "/../tempFiles/creds"
commandFile = "/../tempFiles/commands"

if (os.path.isfile(os.getcwd() + credFile)):
    print("Creds file found")
else:
    print("No credential file")
    sys.exit()

if (os.path.isfile(os.getcwd() + commandFile)):
    print("Commands file found")
else:
    print("No commands file")
    sys.exit()


#function to connect to ssh server and send commands
def connect(ip):

    #global variables defined above
    global credFile
    global commandFile

    #attempts to connect to ssh server and prints error if failed
    try:
        #opens creds file to obtain credentials to authenticate to ssh server
        tempFile = open(os.getcwd() + credFile, 'r')
        creds = tempFile.readline()

        username = creds.split(':')[0]
        password = creds.split(':')[1].rsplit("\n")[0]

        
        #begins Paramiko
        session = paramiko.SSHClient()

        #line for testing, remove for production
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #connects and authenticates to target IP
        session.connect(ip, username = username, password = password)

        #spawns a shell
        connection = session.invoke_shell()

        #sends commands to shell
        comFile = open(os.getcwd() + commandFile, 'r')
        commands = comFile.readline()

        #for command in commands:
            #connection.send(command + "\n")
            #time.sleep(2)
        
        print(commands)
        stdInput, stdOutput, stdError = session.exec_command(commands)
        
        tempFile.close()
        comFile.close()

        #response = connection.recv(65535)
        
        outputList = stdOutput.read().split(b"\n")
        print(outputList)       

    except paramiko.AuthenticationException:
        print("There was an authentication error, Exiting...\n")



    
   
