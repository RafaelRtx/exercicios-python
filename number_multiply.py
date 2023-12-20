

def createMultiplicador(multiplicador):
  def multiplicar(numero):
    return numero * multiplicador
  return multiplicar

duplicar = createMultiplicador(2)
triplicar = createMultiplicador(3)

print(duplicar(5))
print(triplicar(10))
  