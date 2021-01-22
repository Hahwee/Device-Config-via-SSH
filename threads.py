import threading

#function to allow for multiple ssh connections
def connect_threads(ipList,function):

    threads = []

    for ip in ipList:
        thread = threading.Thread(target = function, args = (ip,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
