# jogo_cliente_latencia.py
import socket
import time

def main():
    print("--- Cliente do Jogo da Velha ---")
    server_ip = input("Digite o endereço IP do servidor (host):\n> ")
    server_port = 9999

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"\nConectando a {server_ip}...")
        s.connect((server_ip, server_port))
        print("[Conexão Estabelecida]")

        ### INÍCIO DO BLOCO DE TESTE DE LATÊNCIA ###
        print("\n--- Iniciando Teste de Latência (RTT) ---")
        latencias = []
        for i in range(5):
            # Prepara para medir o tempo de ida e volta
            inicio_rtt = time.monotonic()
            
            # 1. Envia uma mensagem "ping"
            s.sendall(b'ping')
            
            # 2. Aguarda a resposta "pong" do servidor
            s.recv(1024)
            
            # Medição de tempo finalizada
            fim_rtt = time.monotonic()
            
            # Calcula a duração em milissegundos
            rtt_ms = (fim_rtt - inicio_rtt) * 1000
            latencias.append(rtt_ms)
            print(f"  - Ping {i+1}: Resposta em {rtt_ms:.2f} ms")
            time.sleep(0.5) # Pequena pausa para visualização

        # Calcula e exibe as estatísticas
        media_latencia = sum(latencias) / len(latencias)
        min_latencia = min(latencias)
        max_latencia = max(latencias)

        print("\n--- Resumo da Latência ---")
        print(f"Mínima:  {min_latencia:.2f} ms")
        print(f"Máxima:  {max_latencia:.2f} ms")
        print(f"Média:   {media_latencia:.2f} ms")
        print("--------------------------\n")
        ### FIM DO BLOCO DE TESTE DE LATÊNCIA ###

        # O jogo começa normalmente após os testes
        print("Iniciando o jogo...")
        while True:
            print("Aguardando jogada do oponente (X)...")
            data = s.recv(1024)
            if not data:
                print("O servidor desconectou. Fim de jogo.")
                break
            
            print(f"Oponente jogou em: {data.decode('utf-8')}")
            
            my_move = input("É a sua vez (O). Onde deseja jogar (linha,coluna)?\n> ")
            s.sendall(my_move.encode('utf-8'))

    except Exception as e:
        print(f"\n[ERRO] {e}")
    finally:
        s.close()
        print("\n--- Conexão Fechada ---")

if __name__ == "__main__":
    main()