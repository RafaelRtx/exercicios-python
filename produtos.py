# acrescentar 10% ao valor de cada preço no dicionádio de produtos
import copy

from dados import produtos

novos_produtos =[
 {**p, 'preco': round(p['preco'] * 1.1, 2)} 
 for p in copy.deepcopy(produtos) 
]


#ordenar produtos por nome decrescente e gerar uma deep copy dos produtos ordenados

produtos_ordenados_por_nome = sorted(
  copy.deepcopy(produtos), key=lambda p: p['nome'],
  reverse=True
)

#ordenar produtos por preço crescente e gerar uma deep copy dos produtos ordenados

produtos_ordenados_por_preco = sorted(
  copy.deepcopy(produtos), key=lambda p: p['preco'],
)

#FINAL
print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')


