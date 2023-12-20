
def multiplica(*args):
  total = 1
  for numero in args:
    total *= numero
  return total  

print(multiplica(1,2,3,4,5,6))

def paridade(n):
  if n%2 == 0:
    return print('o Número é par')
  else:
    return print('O número é ímpar')

paridade(1)


