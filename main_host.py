import  socket
import threading 

class JogoDaVelha:

    
    def init_game(self):
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.me = "X"
        self.opponent = "O"
        self.turn = "X"
        self.winner = ""
        self.moves = 0


    
    def host_game(self, host, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(1)
        
        client, addr = server.accept()

        self.me = "X"
        self.opponent = "O"
        threading.Thread(target=self.handle_connection, args=(client,)).start()
        server.close()

    def valid_move(self, move):
        
        move.split(',')
        for i in range (2): 
            if(int(move[i])>2 or int(move[i])<0):
                return False
        
        return (self.board[int(move[0])][int(move[1])]=="")



    def connect_opponent(self, host, port): 
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect = ((host, port))
        
        self.me = "O"
        self.opponent = "X"
        threading.Thread(target=self.handle_connection, args=(client,)).start()
    
    def handle_connection(self, client):
        while self.winner == "":
            if self.moves < 9: 
                if self.turn == self.me:
                    move = input("Onde deseja colocar o seu %s no tabuleiro (linha, coluna)?", self.me)
                    if not self.valid_move(move):
                        client.send(move.encode('utf-8'))
                        self.apply_move(move.split(','),self.me)
                        self.turn = self.opponent
                else:
                    print("Jogada inválida")
                
            else:
                data = client.recv(1024)
                if not data:
                    break
                else:
                    self.apply_move(data.decode('utf-8').split(','), self.opponent)
                    self.turn = self.me

                    
        client.close()