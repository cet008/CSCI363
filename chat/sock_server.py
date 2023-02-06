import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

# check if port number provided
if len(sys.argv) != 2:
    print("Correct usage: include port number")
    exit()
 
#UDP_IP = str(sys.argv[1])
UDP_IP = "127.0.0.1"
UDP_PORT = int(sys.argv[1])

s.bind((UDP_IP, UDP_PORT))

clients = {}

# send message
def sendMsg(msg):
    # format as name: msg
    fullMsg = (clients[addr] + ": " + msg)
    print(fullMsg)

    # send message to all connected clients
    for client in clients:
        # do not send message to yourself
        if addr[1] != client[1]:
            s.sendto(fullMsg.encode(), (client[0], client[1]))

while True:
    # maximum clients
    if(len(clients) < 100):
        # receive message from client
        data, addr = s.recvfrom(1024)

        # set nickname as anonymous if new client
        if addr not in clients:
            clients[addr] = "anonymous"
        msg = data.decode()

        # if no message provided, ignore
        if len(msg) == 0:
            continue

        # nick command
        elif msg.split()[0] == "/nick":

            # if no nickname provided, ignore
            if len(msg.split()) == 1:
                continue
            else:
                # set nickname in dict
                clients[addr] = msg.split()[1]

        # list command
        elif msg.split()[0] == "/list":
            s.sendto(str(clients).encode(), (addr[0], addr[1]))

        # quit command
        elif msg.split()[0] == "/quit":
            # send quit message to all clients
            sendMsg(str(clients[addr]) + " has quit")

            # disconnect
            del clients[addr]

        # send message to all clients
        else:
            sendMsg(msg)
    else:
        print("Maximum clients reached")