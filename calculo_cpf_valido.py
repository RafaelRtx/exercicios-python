"""
Calculo do segundo dígito do CPF (Do 1º digito pegue os 9 primeiros números e use uma contagem regressiva de 10 ao invés de 11)
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

cpf= '46619661807'
nove_dig= cpf[:9]
cont_reg = 10
resultado = 0

for digito in nove_dig:
    resultado += (int(digito) * cont_reg)
    cont_reg-=1
digito1 = ((resultado*10) % 10)
digito1 = digito1 if digito1 <=9 else 0
#O o primeiro Digito dos últimos 2 digitos desse CPF é 0.

dez_digitos = nove_dig + str(digito1)
cont_reg_2 = 0
resultado_dig_2 = 11
for digito in dez_digitos:
    resultado_dig_2 += int(digito) * cont_reg_2
    cont_reg_2 -=1

digito_2 =  (resultado_dig_2 * 10) %11
digito_2 = digito_2 if digito_2 <= 9 else 0

novo_cpf = f'{nove_dig}{digito1}{digito_2}'
print(novo_cpf)

#verifica se CPF é válido
if cpf == novo_cpf:
    print(f'{cpf} é válido')
else:
    print('CPF inválido')

