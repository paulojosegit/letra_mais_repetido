
print('\n')

print('****** QUAL LETRA APARECE MAIS NA FRASE QUE VOCÊ ESCRECEU? ****** \n')

frase = input('Digite uma frase >>: ')

largura_frase_digitada = len(frase)
contador = 0


print('\n')

print(f'Sua frase tem {largura_frase_digitada} caracteres... \n')

while contador <= (largura_frase_digitada - 1):

    caractere = frase[contador]
    caractere_anterior = frase[contador - 1]
    caractere_mais_repetido = 0

    if frase.count(caractere_anterior) > frase.count(caractere):
        caractere_mais_repetido = caractere_anterior
        print(f'O Caractere mais repetido é: {caractere_mais_repetido} e apareceu {frase.count(caractere_mais_repetido)}')
    else:
        ...

    contador += 1

print('FIM DO PROGRAMA')
