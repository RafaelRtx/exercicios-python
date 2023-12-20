import os

palavra_sec = 'batata'
letras_acerto=''
tentativas=0

while True:
  entrada = input('Digite uma letra: ')

  if len(entrada) > 1:
    print('Digite apenas uma letra')
    continue

  tentativas += 1

  if entrada in palavra_sec:
    letras_acerto += entrada
  
  palavra_formada = ''
  for palavra_montada in palavra_sec:
    if palavra_montada in letras_acerto:
      palavra_formada += palavra_montada
    else:
      palavra_formada += '*'

  print('Palavra formada: ', palavra_formada)

  if palavra_formada == palavra_sec:
    os.system('cls')
    print('VOCÊ GANHOU, PARABÉNS')
    print('A palavra secreta era: ',palavra_sec)
    print('Tentativas: ',tentativas)
    letras_acerto = ''
    tentativas=0  

  


  

    