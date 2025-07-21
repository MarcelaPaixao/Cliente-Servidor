import os
import platform
import time
SIZE = 3

def clean_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

class JogoDaVelha:
    
    def __init__(self, simbol):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.me = simbol
        if simbol == "X":
            self.opponent = "O"
        else:
            self.opponent = "X"
        self.turn = "X"
        self.winner = None
        self.moves = 0

    def valid_move(self, move):
        if(len(move)<2):
            return False
        for i in range (2): 
            if(int(move[i])>2 or int(move[i])<0):
                return False
        return (self.board[int(move[0])][int(move[1])]==" ")
    
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
            self.winner = "E"
            print("Deu empate!")
    
    def run_latency_test(self, connection):
       
        """Executa um teste de 'ping-pong' para medir a latência da rede."""
        print("\n--- Iniciando Teste de Latência (RTT) ---")
        
       
        if self.me == "O": 
            latencias = []
            for i in range(5):
                inicio_rtt = time.monotonic()
                connection.sendall(b'ping')
                connection.recv(1024)
                fim_rtt = time.monotonic()
                
                rtt_ms = (fim_rtt - inicio_rtt) * 1000
                latencias.append(rtt_ms)
                print(f"  - Ping {i+1}: Resposta em {rtt_ms:.2f} ms")
                time.sleep(0.5)

            media = sum(latencias) / len(latencias)
            minimo = min(latencias)
            maximo = max(latencias)

            print("\n--- Resumo da Latência ---")
            print(f"Mínima:  {minimo:.2f} ms")
            print(f"Máxima:  {maximo:.2f} ms")
            print(f"Média:   {media:.2f} ms")
            print("--------------------------\n")

        else: 
            for _ in range(5):
                data = connection.recv(1024)
                if not data: break
                connection.sendall(data)
        
        print("Teste de latência finalizado. Iniciando o jogo.")

    def handle_connection(self, client):
        
        #self.run_latency_test(client)
        
        while self.winner == None:
            if self.moves < 9: 
                if self.turn == self.me:
                    move = input(f"Onde deseja jogar o '{self.me}' no tabuleiro (linha, coluna)?")
    
                    if self.valid_move(move.split(',')):
                          
                            moveEncoded = move.encode('utf-8')
                            client.sendall(moveEncoded)
                            
                            self.apply_move(move,self.me)
                            self.turn = self.opponent
                        
                    else:
                            print(f"Jogada inválida.")
                    
                else:
                    print("Vez do oponente!")
                    data = client.recv(1024) 
                    if not data: 
                        print("O oponente desconectou.")
                        break
                        
                    self.apply_move(data.decode('utf-8'), self.opponent)
                    self.turn = self.me
               

        
        client.close()   
                        
        