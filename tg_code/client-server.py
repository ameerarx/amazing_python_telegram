import socket
import sys 

def server():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(("127.0.0.1",5500))
    print("listenning at {}".format(s.getsockname()))
    while True:
        data,address = s.recvfrom(1024)
        print("Client at {} says {}".format(address,data))
        s.sendto(data,address)
def client(): 
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    msg = input("enter your message :").encode("ascii")
    s.sendto(msg,("127.0.0.1",5500)) 
    data,address = s.recvfrom(1024)
    print("Server Says : {}".format(data))
if __name__ == "__main__":
    if '-s' in sys.argv:
        server()
    else:
        client()               