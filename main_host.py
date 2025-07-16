import  socket
import threading 

SIZE = 3

class JogoDaVelha:

    
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.me = "X"
        self.opponent = "O"
        self.turn = "X"
        self.winner = None
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
        
       
        for i in range (2): 
            if(int(move[i])>2 or int(move[i])<0):
                return False
        
        return (self.board[int(move[0])][int(move[1])]==" ")
    
    def handle_connection(self, client):
        while self.winner == None:
            if self.moves < 9: 
                if self.turn == self.me:
                    move = input("Onde deseja jogar no tabuleiro (linha, coluna)?")
                    if self.valid_move(move.split(',')):
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
    
    def print_board(self):
        for row in range(SIZE):
            print(" | ".join(self.board[row]))
            if row != SIZE - 1:
                print("----------")
    
    def check_for_winner(self):
        #Verifica nas linhas
        for row in range(SIZE):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != " ":
                self.winner = self.board[row][0]
                # return
        
        #Verifica nas colunas
        for col in range(SIZE):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                self.winner = self.board[0][col]
                # return

        #Verifica na diagonal 1
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            self.winner = self.board[0][0]
            
        #Verifica na diagonal 2
        elif self.board[2][0] == self.board[1][1] == self.board[0][2] != " ":
            self.winner = self.board[2][0]
        
    def apply_move(self, move, player):
        self.moves += 1
        self.board[int(move[0])][int(move[1])] = player
        
        self.print_board()
        self.check_for_winner()
        
        if self.winner == self.me:
            print("Parabéns, você venceu :)")

        elif self.winner == self.opponent:
            print("Que pena, você perdeu :(")
        
        elif self.moves == 9:
            print("Deu empate!")

game = JogoDaVelha()
game.host_game("localhost", 9998)

