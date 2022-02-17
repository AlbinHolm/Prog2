import socket
from _thread import *
import sys

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = '10.32.41.35'  #IP to run server on
port = 5555

server_ip = socket.gethostbyname(server)

try:
    serverSocket.bind((server, port))

except socket.error as e:
    print(str(e))

serverSocket.listen(2)
print("Waiting for a connection")

currentId = "0"
pos = ["0:50,50", "1:50,200"]
def threaded_client(conn):
    global currentId, pos
    conn.send(str.encode(currentId))
    currentId = "1"