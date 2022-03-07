import socket
from _thread import *
import pickle
from game import Game

server = "10.32.41.35"
port = 1111

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.bind((server, port))
except socket.error as e:
    str(e)

sock.listen(2)
print("Waiting for a connection...")

connected = set()
games = {}
idAmount = 0


def threaded_client(conn, p, idGame):
    global idAmount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if idGame in games:
                game = games[idGame]

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

    print("Connection lost.")
    try:
        del games[idGame]
        print("Game closing...", idGame)
    except:
        pass
    idAmount -= 1
    conn.close()



while True:
    conn, addr = sock.accept()
    print("Connected to:", addr)

    idAmount += 1
    p = 0
    idGame = (idAmount - 1)//2
    if idAmount % 2 == 1:
        games[idGame] = Game(idGame)
        print("Creating new game...")
    else:
        games[idGame].ready = True
        p = 1


    start_new_thread(threaded_client, (conn, p, idGame))