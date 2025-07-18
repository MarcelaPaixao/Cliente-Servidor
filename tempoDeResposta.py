# Em jogo_cliente.py, dentro do loop principal

# ... (código anterior) ...

# Turno do Cliente (O)
my_move = input("É a sua vez (O). Onde deseja jogar (linha,coluna)? Ex: 0,2\n> ")

# MEDIR O TEMPO DE RESPOSTA DA JOGADA
start_move_response = time.monotonic()

s.sendall(my_move.encode('utf-8'))

# O "fim" da medição é quando recebemos a próxima jogada do servidor,
# que serve como confirmação de que nossa jogada foi recebida e processada.
data = s.recv(1024) 
# ... (o resto do código que processa a jogada do servidor)

end_move_response = time.monotonic()
move_response_time = (end_move_response - start_move_response) * 1000
print(f"--- (Info Desempenho) Tempo de resposta da jogada: {move_response_time:.2f} ms ---")

# ... (continua o loop)