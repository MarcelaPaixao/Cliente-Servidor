from jogo import *

import  socket
import threading 

def host_game(game, host, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        server.bind((host, port))
        server.listen(1)
        
        
        try:
                client, addr = server.accept()
                client_thread = threading.Thread(target=game.handle_connection, args=(client,))
                client_thread.start()
                client_thread.join()
                
        except KeyboardInterrupt:
                print("Erro de teclado")
        except Exception as e:
                print("Erro inesperado {e}")
        finally:
                server.close()
                print("Socket do servidor foi fechado.")


game = JogoDaVelha("X")
host_game(game, "localhost", 9999)