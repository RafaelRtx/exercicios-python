#Inserir, apagar e listar itens em uma lista
import os

lista = []

while True:
  print('Selecione uma opção')
  opcao = input('[i]nserir, [a]pagar, [l]istar: ')

  if opcao == 'i':
    os.system('cls')
    valor = input('Insira o item : ')
    lista.append(valor)
  elif opcao == 'a':
    indice_str = input('Escolha um índice para apagar: ')

    try:
      indice = int(indice_str)
      del lista[indice]
    except ValueError:
      print('Erro: digite um número válido')
    except IndexError:
      print('Erro: índice não encontrado')
  elif opcao == 'l':
    os.system('cls')
    if len(lista) == 0:
      print('nada para listar')
    
    for i, valor in enumerate(lista):
      print(i, valor)
      
  else:
    print('Por favor, escolha "i", "l" ou "a" ')    