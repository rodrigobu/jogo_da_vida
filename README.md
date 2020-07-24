# Jogo da Vida
Esse algoritimo foi baseado no problema no dojopuzzle(http://dojopuzzles.com/problemas/exibe/jogo-da-vida/).

## Conjunto de regras

Usando o conjunto de regras a seguir, a grade de células evoluirá de geração em geração até atingir um estado estático de todas as células mortas ou uma mistura de células estáticas, oscilantes ou móveis

1. _ ** Subpopulação ** _ - Se uma célula viva tiver cercada por menos de dois vizinhos, ela morre e não chega à próxima geração.
2. _ ** Equilíbrio ** _ - Se uma célula viva é cercada por dois ou três vizinhos vivos, a célula permanece viva e passa para a próxima geração.
3. _ ** Superpopulação ** _ - Se uma célula viva estiver cercada por mais de três vizinhos vivos, a célula morre e não chega à próxima geração.
4. _ ** Reprodução ** _ - Se uma célula morta estiver cercada por três vizinhos vivos, a célula permanece viva e passa para a próxima geração.

## Como executar

Este projeto foi desenvolvido usando o Python 3.8 e requer que o usuário tenha pelo menos o Python 3 instalado para executar o programa. O Python 3+ pode ser instalado [aqui] (https://www.python.org/downloads/).

Para executar este projeto, o usuário deve abrir um terminal / console e navegar para a pasta do projeto e depois para o diretório de scripts. Uma vez dentro do diretório do script, simplesmente execute ** `python main.py` ** para iniciar o programa.

Uma vez iniciado o programa, o usuário será solicitado a inserir o número de ** linhas ** e ** colunas ** para criar a grade do Jogo da Vida. Após o usuário decidir sobre o formato da grade, ele deve inserir o número de ** gerações ** para executar o jogo e, em seguida, será apresentada uma grade aleatória do Game of Life que evolui continuamente até que todas as células estejam mortas, paradas ou as gerações acabaram.