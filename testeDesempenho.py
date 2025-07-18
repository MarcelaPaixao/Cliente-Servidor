# jogo_servidor_latencia.py
import socket
import threading

SIZE = 3

class JogoDaVelha:
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.turn = "X"
        self.me = "X"
        self.opponent = "O"
        self.winner = None
        self.moves = 0

    def print_board(self):
        print("-------------")
        for row in range(SIZE):
            print(f"| {self.board[row][0]} | {self.board[row][1]} | {self.board[row][2]} |")
            if row != SIZE - 1:
                print("-------------")
        print("-------------")
    
    def host_game(self, host, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(1)
        print(f"--- Servidor de Teste de Latência ---")
        print(f"Aguardando oponente na porta {port}...")
        
        client, addr = server.accept()
        print(f"\n[Conexão Estabelecida] Oponente conectado de {addr}")
        
        threading.Thread(target=self.handle_connection, args=(client,)).start()

    def handle_connection(self, client):
        ### INÍCIO DO BLOCO DE TESTE DE LATÊNCIA ###
        try:
            print("\nExecutando teste de latência pré-jogo...")
            # O servidor apenas responderá a 5 pings do cliente
            for _ in range(5):
                ping_data = client.recv(1024)
                if not ping_data:
                    raise ConnectionError("Cliente desconectou durante o teste.")
                # Apenas envia de volta o que recebeu (echo/pong)
                client.sendall(ping_data)
            print("Teste de latência finalizado. Iniciando o jogo.\n")
        except Exception as e:
            print(f"[ERRO] Falha no teste de latência: {e}")
            client.close()
            return
        ### FIM DO BLOCO DE TESTE DE LATÊNCIA ###
            
        # O resto do código do jogo continua normalmente
        while self.winner is None and self.moves < 9:
            if self.turn == self.me:
                move = input("É a sua vez (X). Onde deseja jogar (linha,coluna)? Ex: 1,1\n> ")
                if self.is_valid_move(move):
                    client.send(move.encode('utf-8'))
                    self.apply_move(move, self.me)
                    self.turn = self.opponent
                else:
                    print("Jogada inválida. Tente novamente.")
            else: 
                try:
                    print("Aguardando jogada do oponente (O)...")
                    data = client.recv(1024)
                    if not data:
                        print("O oponente desconectou.")
                        break
                    
                    move = data.decode('utf-8')
                    if self.is_valid_move(move):
                        self.apply_move(move, self.opponent)
                        self.turn = self.me
                except ConnectionResetError:
                    print("O oponente desconectou.")
                    break
        client.close()
        print("--- Fim de Jogo ---")

    def is_valid_move(self, move_str):
        try:
            parts = move_str.split(',')
            if len(parts) != 2: return False
            row, col = int(parts[0]), int(parts[1])
            if not (0 <= row < SIZE and 0 <= col < SIZE): return False
            if self.board[row][col] != " ": return False
            return True
        except (ValueError, IndexError):
            return False

    def apply_move(self, move_str, player):
        self.moves += 1
        parts = move_str.split(',')
        row, col = int(parts[0]), int(parts[1])
        self.board[row][col] = player
        
        print("\nO tabuleiro agora está assim:")
        self.print_board()
        self.check_for_winner()
        
        if self.winner:
            print(f"\n{self.winner} venceu!")
        elif self.moves == 9:
            print("\nDeu empate!")

    def check_for_winner(self):
        for i in range(SIZE):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ": self.winner = self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ": self.winner = self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ": self.winner = self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ": self.winner = self.board[0][2]

game = JogoDaVelha()
game.host_game("0.0.0.0", 9999)