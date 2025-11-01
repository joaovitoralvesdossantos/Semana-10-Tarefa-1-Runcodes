# faz a contagem de 10 até 1000 separados por , e utiliza um . no final
def conta():
        lista = [i + 10 for i in range(0, 1000, 10)]
        print (*lista, sep=", ", end=".")

# Função principal
def main():

    #processamento e saida de dados
    conta()

# Chama a função principal
if __name__ == '__main__':
    main()