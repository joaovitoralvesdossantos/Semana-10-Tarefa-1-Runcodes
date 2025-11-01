# procura o maior numero em uma lista de 100 numeros positivos
def numeros_positivos(lista_numeros):
    maior = lista_numeros[0]

    for numero_atual in lista_numeros: 
        if numero_atual > maior:
            maior = numero_atual  
    return maior

# Função principal
def main():

    #entrada de dados
    meus_numeros = [int(input("Digite um número: ")) for i in range(100)]

    #processamento
    maior = numeros_positivos(meus_numeros)

    #saida de dados
    print(f"O maior número da lista é: {maior}")

# Chama a função principal
if __name__ == '__main__':
    main()