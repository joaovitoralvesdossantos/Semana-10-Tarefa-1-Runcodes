# faz a contagem dos numeros e depois a media
def numeros_media(lista_numeros):
    soma = 0

    for numero in lista_numeros:
        soma = soma + numero
        media = soma / 100
    return media

# Função principal
def main():

    #entrada de dados
    meus_numeros = [int(input("Digite um número: ")) for i in range(100)]

    #processamento
    media = numeros_media(meus_numeros)

    #saida de dados
    print(f"A média dos números é: {media:.2f}")

# Chama a função principal
if __name__ == '__main__':
    main()