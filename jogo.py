#adicionar bibliotecas que forem necessárias

class jogo_da_velha:
    def __init__(self):
        self.board = [[" ", " ", " "], 
                      [" ", " ", " "], 
                      [" ", " ", " "]]
        self.player1 = "X"
        self.player2 = "O"
        self.turn = "X" #sempre vai começar com X
        self.winner = None
        self.game_over = False
        self.plays_count = 0

    def print_board(self):
        for row in range(3):
            print(" | ".join(self.board[row]))
            if row != 2:
                print("----------")

    def is_valid_move(self, move):
        if move[0] > 2 or move[0] < 0 or move[1] > 2 or move[1] < 0:
            return False
        return self.board[int(move[0])][int(move[1])] == " "

    def check_for_winner(self):
        #Verificar se ganhou na linha
        #Verificar se ganhou na coluna
        #Verificar se ganhou na diagonal 1
        #Verificar se ganhou na diagonal 2
        print("blabla")

