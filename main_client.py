import  socket
import threading 

import os
import platform

SIZE = 3

def clean_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

class JogoDaVelha:

    
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.me = "O"
        self.opponent = "X"
        self.turn = "X"
        self.winner = None
        self.moves = 0
    
    def connect_opponent(self, host, port): 
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        
        # MARCELA: pra que servem essas linhas? me e opponent já foram inicializados
        # self.me = "O"
        # self.opponent = "X"
        threading.Thread(target=self.handle_connection, args=(client,)).start()
    
    def valid_move(self, move):
        
        for i in range (2): 
            if(int(move[i])>2 or int(move[i])<0):
                return False
        
        return (self.board[int(move[0])][int(move[1])]==" ")
    
    def handle_connection(self, client):
        while self.winner == None:
            if self.moves < 9: 
                if self.turn == self.me:
                    move = input(f"Onde deseja jogar o '{self.me}' no tabuleiro (linha, coluna)?")
                    if self.valid_move(move.split(',')):
                        moveEncoded = move.encode('utf-8')
                        client.send(moveEncoded)
                        self.apply_move(move,self.me)
                        self.turn = self.opponent
                        
                    else:
                        print("Jogada inválida")
                
                else:
                    print("Vez do oponente!")
                    data = client.recv(1024)
                    if not data:
                        print("O oponente desconectou")
                        break
                                        
                    self.apply_move(data.decode('utf-8'), self.opponent)
                    self.turn = self.me

                    
        client.close()
  
    
    def print_board(self):
        for row in range(SIZE):
            print(" | ".join(self.board[row]))
            if row != SIZE - 1:
                print("---------")
    
    def check_for_winner(self):
        #Verifica nas linhas
        for row in range(SIZE):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != " ":
                self.winner = self.board[row][0]
        
        #Verifica nas colunas
        for col in range(SIZE):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                self.winner = self.board[0][col]

        #Verifica na diagonal 1
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            self.winner = self.board[0][0]
            
        #Verifica na diagonal 2
        elif self.board[2][0] == self.board[1][1] == self.board[0][2] != " ":
            self.winner = self.board[2][0]
        
    def apply_move(self, move, player):
        move = move.split(',')
        self.moves += 1
        self.board[int(move[0])][int(move[1])] = player
        
        clean_screen()

        self.print_board()
        self.check_for_winner()

        if self.winner == self.me:
            print(f"Parabéns '{self.winner}', você venceu :)")

        elif self.winner == self.opponent:
            print(f"Que pena '{self.me}', você perdeu :(")
        
        elif self.moves == 9:
            print("Deu empate!")




game = JogoDaVelha()
game.connect_opponent("localhost", 9999)