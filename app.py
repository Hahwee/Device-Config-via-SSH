import sys
from connection import connect
from fileValid import file_valid
from ipValid import valid_ip_check
from reachable import reach_ip
from threads import connect_threads


if __name__ == '__main__':
    
    ipList = file_valid()

    valid_ip_check(ipList)

    reach_ip(ipList)

    connect_threads(ipList, connect)
