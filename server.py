from jogo import *

import  socket
import threading 

def host_game(game, host, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(1)
        
        client, addr = server.accept()
        threading.Thread(target=game.handle_connection, args=(client,)).start()
        server.close()

game = JogoDaVelha("X")
host_game(game, "localhost", 9998)