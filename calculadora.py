#Calculadora com While

while True:
  numero_1 = input('Digite um número: ')
  numero_2 = input('Digite outro número: ')
  operador = input('Digite o operador (+-/*): ')

  numeros_validos = None

  try:
    num_1_float = float(numero_1)
    num_2_float = float(numero_2)
    numeros_validos = True
  except:
    numeros_validos = None

  if numeros_validos is None:
    print('Digite um número válido')
    continue

  operadores_validos = '+=/*'

  if operador not in operadores_validos:
    print('Operador Inválido')
    continue

  if len(operador) > 1:
    print('Escolha apenas 1 operador')
    continue

  print('Aqui está o resultado: ')
  if operador == '+':
    print(f'{num_1_float + num_2_float}')
  
  elif operador == '-':
   print(f'{num_1_float + num_2_float}')

  elif operador == '*':
   print(f'{num_1_float * num_2_float}')

  elif operador == '/':
   print(f'{num_1_float / num_2_float}')

  sair = input('Deseja sair? [s]im: ').lower().startswith('s')

  if sair is True:
    break

