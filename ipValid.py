import sys

def valid_ip_check(ipList):

    #loops through each IP individually, removes newline char, and splits IP address into 4 octets
    for ip in ipList:
        ip.rstrip("\n")
        octetIP = ip.split(".")

        #Checks validity of IP address and that it is not a reserved IP such as loopback addresses, multicast/broadcast (224 or higher), DHCP for Windows (169 or 254), 
        if (len(octetIP) == 4) and (1 <= int(octetIP[0]) <= 223) and (int(octetIP[0]) != 127) and (int(octetIP[0]) != 169 or int(octetIP[0]) != 254) and (int(octetIP[1]) <= 255) and (int(octetIP[2]) <= 255) and (int(octetIP[3]) <= 255):
            continue
        else:
            print("Invalid IP detected\n")
            sys.exit()
        
