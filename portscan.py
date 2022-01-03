import socket
from IPy import IP


def scan(ipaddr,port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ipaddr,port))
        print('[+]'+str(port) + ' is open')
    except:
        print('[-]' +str(port) +' is closed')

ipaddr = input('[+] enter btarget to scan:')

for port in range(79,82):
    scan(ipaddr,port)



