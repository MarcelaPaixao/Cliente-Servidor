# Cliente-Servidor

Jogo da Velha

Neste projeto, executamos o clássico jogo da velha via terminal atráves da conexão de sockets.Na sua implementação, utilizamos a linguagem python e as suas bibliotecas de socket, threading, os e plataform.

Como Executar: 

1.Clone o repositório:
    git clone <https://github.com/MarcelaPaixao/Cliente-Servidor.git>

2.Execute o servidor:
    python server.py

3.Execute o cliente:
    python client.py
4.Dê os comandos no formato: linha,coluna. Até o final do jogo.


Como Testar Estabilidade: 

-Teste de Desconexão Abrupta

    Objetivo: Garantir que o servidor detecta a desconexão, encerra a partida daquele jogador de forma limpa e não trava, ficando pronto para um próximo jogador (se o modificarmos para isso).

    Como Simular:

    1.Rode python jogo_servidor.py em uma máquina.

    2.Em outra máquina (ou terminal), rode python jogo_cliente.py e conecte-se.

    3.Faça uma ou duas jogadas.

    4.No terminal do cliente, pressione Ctrl + C ou simplesmente feche a janela do terminal.

    5.Volte ao terminal do servidor.

    O que Esperar (Resultado Correto):

    -O terminal do servidor deve imprimir uma mensagem como: "O oponente desconectou."

Teste de "Input" Inválido


    Objetivo: Garantir que o servidor não quebre ao tentar processar dados que não são coordenadas válidas.

    Como Simular:
    
    1.Rode python jogo_servidor.py em uma máquina.

    2.Em outra máquina (ou terminal), rode python jogo_cliente.py e conecte-se.

    3.Faça uma jogada inválida, por exemplo, com indices maiores que a matriz ou sem virgula.

    O que Esperar (Resultado Correto):

    -O terminal do servidor deve imprimir uma mensagem como: "Jogada inválida."

Teste de desempenho: 
    1.Tempo de latência: 
    Execução:

    1.Descomente os trechos de testes dos códigos e rode-os normalmente
    
    O que esperar:
    
    -A primeira coisa que você verá no terminal do cliente será o resultado do teste de latência, com os tempos mínimo, máximo e médio para a troca de mensagens.
    
    2.Tempo de Resposta da Jogada:


    Este novo valor lhe dirá quanto tempo, em milissegundos, você esperou desde o envio da sua jogada até receber a próxima ação do servidor.


   
Funcionalidades Implementadas:
    
-Server.py: Este script atua como o anfitrião (host) da partida. Ele instancia um objeto de socket (socket.AF_INET, socket.SOCK_STREAM) e o vincula a um endereço e uma porta. O servidor então aguarda e aceita uma única conexão de um cliente para iniciar o jogo. A opção SO_REUSEADDR é utilizada para permitir a rápida reutilização do endereço do socket após o término da partida.

-Client.py: Este script funciona como o cliente que se junta a uma partida existente. Ele cria um socket e estabelece uma conexão com o servidor no endereço e porta especificados.

Toda a lógica, regras e estado do jogo estão encapsulados na classe JogoDaVelha, contida no arquivo jogo.py. 
Esta classe é instanciada tanto pelo servidor quanto pelo cliente, garantindo que ambos compartilhem a mesma estrutura de jogo.

-Inicialização e Estado (init): Cria um tabuleiro 3x3, define os símbolos ("X" e "O"), inicia com "X" e gerencia o número de jogadas e o vencedor.
    
-Exibição do Tabuleiro (print_board): Mostra o estado atual do jogo na tela.
    
-Validação de Movimentos (valid_move): Este método assegura a integridade das jogadas. Ele verifica se as coordenadas fornecidas estão dentro dos limites da matriz e se a célula alvo está desocupada.
    
-Aplicação de Movimentos (apply_move): Atualiza o tabuleiro com o símbolo do jogador, limpa o console e verifica se há vencedor.
    
-Detecção de Fim de Jogo (check_for_winner): Após cada jogada, o sistema verifica se a partida terminou. Ocorre uma busca nas linhas, colunas e diagonais por 3 simbolos iguais. Se não houver vitória após 9 jogadas, declara empate.
    
-Gerenciamento da Sessão de Jogo (handle_connection): Este método controla a interação e a troca de turnos entre os jogadores. Ele funciona em um ciclo que continua até que um vencedor seja definido:
        *No turno do jogador local: Ele aguarda a inserção da jogada, a envia para o oponente pela rede e atualiza o próprio tabuleiro.
        *No turno do oponente: Ele aguarda o recebimento dos dados da jogada pela rede, decodifica-os e então atualiza o tabuleiro localmente.  
Essa comunicação garante que ambos os jogadores tenham uma visão sincronizada do jogo, respeitando a ordem das jogadas até o final da partida.



Possíveis Melhorias Futuras:

    - Possibilitar que os participantes joguem múltiplas partidas;
    - Possibilitar um placar entre jogadores;
    - Chat entre jogadores;
    - Fazer uma interface mais bonita;

