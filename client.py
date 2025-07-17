from jogo import *

import  socket
import threading 

def connect_opponent(game, host, port): 
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        threading.Thread(target=game.handle_connection, args=(client,)).start()

game = JogoDaVelha("O")
connect_opponent(game, "localhost", 9998)