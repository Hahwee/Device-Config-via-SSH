import sys
import subprocess

#loops through IP list and confirms if ttargets are reachable
def reach_ip(ipList):

    for ip in ipList:
        result = subprocess.call(['ping', '-c', '2', ip], stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
        if (result == 0):
            print("Success, target reachable")
            continue
        else:
            print("Failed, target unreachable")
            sys.exit()

        
