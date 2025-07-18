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



   
Funcionalidades Implementadas:

- Estabelecimento de conexão entre dois jogadores

Possíveis Melhorias Futuras:

- Possibilitar que os participantes joguem múltiplas partidas;
- Possibilitar um placar entre jogadores;
- Chat entre jogadores;
- Fazer uma interface mais bonita;

