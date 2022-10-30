import ipaddress
import socket
import sys
import threading
import time

from colorama import Fore

start_time = time.time()
ports = [80, 443, 1234]

total_open = 0
total_ips = 0


def connect(host):
    global total_open
    global total_ips
    total_ips += 1
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        result = s.connect_ex((host, port))
        if result == 0:
            print('port ' + Fore.YELLOW + str(port) + Fore.RESET + ' is ' + Fore.BLUE + ' open ' + Fore.RESET + ' for ' + host)
            total_open += 1


threads = []
for ip in ipaddress.IPv4Network(sys.argv[1]):
    thread1 = threading.Thread(target=connect, args=(str(ip),))
    thread1.start()
    threads.append(thread1)

for thread in threads:
    thread.join()
print('scan finished in ' + Fore.GREEN + str(round(time.time() - start_time, 2)) + Fore.MAGENTA + ' seconds ' + Fore.RESET + 'total open ports ' + Fore.BLUE + str(total_open) + Fore.RESET + ' total ips: ' + Fore.YELLOW + str(total_ips))
