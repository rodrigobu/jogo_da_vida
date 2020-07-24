import time
import os
import random
import sys


class JogoVida():

    def limpar_console(self):
        """
        Limpa o console usando um comando do sistema baseado no sistema operacional do usuário.
        """

        if sys.platform.startswith('win'):
            os.system("cls")
        elif sys.platform.startswith('linux'):
            os.system("clear")
        else:
            print("Unable to clear terminal. Your operating system is not supported.\n\r")


    def redimensionar_console(self, linhas, cols):
        """
        Redimensiona o console para o tamanho de linhas x colunas

        : param linhas: Int - o número de linhas para o console redimensionar para
        : param cols: Int - O número de colunas para o console redimensionar para
        """

        if cols < 32:
            cols = 32

        if sys.platform.startswith('win'):
            command = "mode con: cols={0} lines={1}".format(cols + cols, linhas + 5)
            os.system(command)
        elif sys.platform.startswith('linux'):
            command = "\x1b[8;{linhas};{cols}t".format(linhas=linhas + 3, cols=cols + cols)
            sys.stdout.write(command)
        else:
            print("Não foi possível redimensionar o terminal. Seu sistema operacional não é suportado. \n\r")

    def cria_grid_inicial(self, linhas, cols):
        """
        Cria uma lista aleatória de listas que contém 1s e 0s para representar as células no Jogo da Vida de Conway.

        : param linhas: Int - O número de linhas que a grid do Jogo da Vida terá
        : param cols: Int - O número de colunas que a grid do Jogo da Vida terá
        : return: Int [] [] - Uma lista de listas contendo 1s para células vivas e 0s para células mortas
        """

        grid = []
        for linhas in range(linhas):
            grid_linhas = []
            for col in range(cols):
                # Gera um número aleatório e, com base nisso, decida se deseja adicionar uma célula viva ou morta à grid
                if random.randint(0, 7) == 0:
                    grid_linhas += [1]
                else:
                    grid_linhas += [0]
            grid += [grid_linhas]
        return grid


    def print_grid(self, linhas, cols, grid, geracao):
        """
        Imprime no console o grid do Jogo da Vida

        : param linhas: Int - O número de linhas que a grid do Jogo da Vida possui
        : param cols: Int - O número de colunas que a grid do Jogo da Vida possui
        : param grid: Int [] [] - A lista de listas que serão usadas para representar a grid do Jogo da Vida
        : param geracao: Int - A geração atual da grid do Jogo da Vida
        """

        self.limpar_console()

        output_str = ""

        # Compila a sequência de saída e imprime no console
        output_str += "Geração {0} - Para sair do programa, pressione <Ctrl-C>\n\r".format(geracao)
        for linhas in range(linhas):
            for col in range(cols):
                if grid[linhas][col] == 0:
                    output_str += ". "
                else:
                    output_str += "@ "
            output_str += "\n\r"
        print(output_str, end=" ")


    def create_next_grid(self, linhas, cols, grid, next_grid):
        """
        Analisa a geração atual da grid do Jogo da Vida e determina quais células vivem e morrem na próxima
        geração da grid do Jogo da Vida.

        : param linhas: Int - O número de linhas que a grid do Jogo da Vida possui
        : param cols: Int - O número de colunas que a grid do Jogo da Vida possui
        : param grid: Int [] [] - A lista de listas que serão usadas para representar a grid do Game of Life da geração atual
        : param next grid: Int [] [] - A lista de listas que serão usadas para representar a próxima geração do Jogo da Vida
         
        """
        for linha in range(linhas):
            for col in range(cols):
                # Verifica o número de células vivas na célula do grid [linhas] [col]
                live_neighbors = self.get_vizinhos_vivos(linha, col, linhas, cols, grid)

                # Se o número de células vivas for menor que 2 ou maior que 3, 
                # tornamos a célula do grid [linhas] [col] uma célula morta
                if live_neighbors < 2 or live_neighbors > 3:
                    next_grid[linha][col] = 0
                # Se o número de células vivas for 3 e a célula do grid [linha] [col] estiver morta anteriormente,
                # faça célula em uma célula viva
                elif live_neighbors == 3 and grid[linha][col] == 0:
                    next_grid[linha][col] = 1
                # Se o número de células vivas circundantes for 3 e a célula do grid [linha] [col] estiver viva, 
                # mantenha-a viva
                else:
                    next_grid[linha][col] = grid[linha][col]


    def get_vizinhos_vivos(self, linha, col, linhas, cols, grid):
        """
        Conta o número de células vivas ao redor de uma célula central na grid [linhas] [célula].

        : param linha: Int - As linha da célula central
        : param col: Int - a coluna da célula central
        : param linhas: Int - O número de linhas que a grid do Jogo da Vida possui
        : param cols: Int - O número de colunas que a grid do Jogo da Vida possui
        : param grid: Int [] [] - A lista de listas que serão usadas para representar o grid do Jogo da Vida
        : return: Int - O número de células vivas ao redor da célula no grid [linhas] [cell]
        """

        life_sum = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0):
                    life_sum += grid[((linha + i) % linhas)][((col + j) % cols)]
        return life_sum


    def grid_changing(self, linhas, cols, grid, next_grid):
        """
        Verifica se a grid do Jogo da vida da geração atual é a mesma da grid do Jogo da Vida da próxima geração.

         : param linhas: Int - O número de linhas que a grid do Jogo da Vida possui
         : param cols: Int - O número de colunas que a grid do Jogo da Vida possui
         : param grid: Int [] [] - A lista de listas que serão usadas para representar a grid do Game of Life da geração atual
         : param next_grid: Int [] [] - A lista de listas que serão usadas para representar a próxima geração do Jogo da Vida
         rede
         : return: Boolean - Se a grid de geração atual é igual à grid de próxima geração
        """

        for linhas in range(linhas):
            for col in range(cols):
                if not grid[linhas][col] == next_grid[linhas][col]:
                    return True
        return False


    def get_integer_value(self, prompt, low, high):
        """
        Solicita ao usuário uma entrada inteira e entre limites determinados, baixo e alto.
        :param prompt: String - Solicita uma entrada para usuário
        :param low: Int - O limite minimo em que o usuário deve permanecer
        :param high: Int - O limite máximo de que o usuário deve permanecer 
        :return: Os valores validados que usuário digitou
        """

        while True:
            try:
                value = int(input(prompt))
            except ValueError:
                print("O valor deve ser um número inteiro")
                continue
            if value < low or value > high:
                print("O valor inserido não está dentro dos limites (valor menor ou igual {0} ou valor maior ou igual {1}).".format(low, high))
            else:
                break
        return value


    def run_game(self):
        """
        Solicita ao usuário informações para configurar o Jogo da Vida para rodar por um determinado número de gerações.
        """

        self.limpar_console()

        linhas = self.get_integer_value("Digite o número de linhas (10-60): ", 10, 60)
        cols = self.get_integer_value("Digite o número de colunas (10-118): ", 10, 118)

        generations = self.get_integer_value("Digite o número de gerações (1-100000): ", 1, 100000)
        self.redimensionar_console(linhas, cols)

        current_generation = self.cria_grid_inicial(linhas, cols)
        next_generation = self.cria_grid_inicial(linhas, cols)

        # Execução do jogo
        gen = 1
        for gen in range(1, generations + 1):
            if not self.grid_changing(linhas, cols, current_generation, next_generation):
                break
            self.print_grid(linhas, cols, current_generation, gen)
            self.create_next_grid(linhas, cols, current_generation, next_generation)
            time.sleep(1 / 5.0)
            current_generation, next_generation = next_generation, current_generation

        self.print_grid(linhas, cols, current_generation, gen)
        input("Press <Enter> to exit.")


# Inicia o Jogo da Vida
JogoVida().run_game()
