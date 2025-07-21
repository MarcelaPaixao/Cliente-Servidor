from jogo import *

import  socket
import threading 

TOKENS_VALIDOS = {
        "user1@@@" : "user1",
        "abc123" : "user2",
}

def host_game(game, host, port):
        
        try:
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
                server.bind((host, port))
                server.listen(1)
                client, addr = server.accept()

                token = client.recv(1024).decode()
                if token in TOKENS_VALIDOS:
                        name = TOKENS_VALIDOS[token]
                        print(f"Token válido. Usuário: {name}")
                        client.send("Sucesso".encode())

                        client_thread = threading.Thread(target=game.handle_connection, args=(client,))
                        client_thread.start()
                        client_thread.join()
                
                else:
                        print("Token inválido.")
                        client.send("Falha".encode())
                        client.close()
                
        except KeyboardInterrupt:
                print("Erro de teclado")
        except Exception as e:
                print("Erro inesperado {e}")
        finally:
                server.close()
                print("Socket do servidor foi fechado.")


game = JogoDaVelha("X")
host_game(game, "localhost", 9999)