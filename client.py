from jogo import *

import  socket
import threading 

def connect_opponent(game, host, port): 
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        
        try:
                client_thread = threading.Thread(target=game.handle_connection, args=(client,))
                client_thread.start()
                client_thread.join()
                
        except KeyboardInterrupt:
                print("Erro de teclado")      
        except Exception as e:
                print("Erro de conexão")
       

game = JogoDaVelha("O")
connect_opponent(game, "localhost", 9999)