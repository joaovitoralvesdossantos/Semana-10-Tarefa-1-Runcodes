# faz a contagem de numeros pares e impares do numero 100
def numeros_pares(lista_numeros):

    total_pares = 0
    total_impares = 0

    for numero in lista_numeros:
     if numero % 2 == 0:
        total_pares += 1
     else:
        total_impares += 1
     
    return total_pares, total_impares

# Função principal
def main():

    #entrada de dados
    meus_numeros = [int(input("Digite um número: ")) for i in range(100)]

    #processamento
    pares, impares = numeros_pares(meus_numeros)

    #saida de dados
    print(f"A lista possuí {pares} números pares e {impares} números ímpares.")

# Chama a função principal
if __name__ == '__main__':
    main()