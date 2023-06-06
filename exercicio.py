frase = 'Absence of Evidence does not mean Evidence of Absence'

i=0
qtd_mais_vezes= 0
letra_mais_vezes= ''

while i < len(frase):
    letra_atual = frase[i]
    maior_current = frase.count(letra_atual)

    if qtd_mais_vezes < maior_current:
        qtd_mais_vezes = maior_current
        letra_mais_vezes = letra_atual

    i+=1
print('A letra que apareceu mais vezes foi '
f'"{letra_mais_vezes}" que apareceu {qtd_mais_vezes}x')