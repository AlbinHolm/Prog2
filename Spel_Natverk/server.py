import socket
from _thread import *
import pickle
from game import Game

server = '10.32.41.35'
port = 5555

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    serverSocket.bind((server, port))

except socket.error as err:
    str(err)


serverSocket.listen(2)
print("Waiting for server...")

connected = set()
games = {}
idAmount = 0

def threaded_client(conn, p, gameId):
    global idAmount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()
            if gameId in games:
                game = games[gameId]
                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(p, data)
                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break
    print("Game connection lost")
    try:
        del games[gameId]
        print("Game closing...", gameId)
    except:
        pass
    idAmount -= 1
    conn.close()

while True:
    conn, addr = serverSocket.accept()
    print("Currently connected to:", addr)

    idAmount += 1
    p = 0
    gameId = (idAmount - 1)//2
    if idAmount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1


    start_new_thread(threaded_client, (conn, p, gameId))