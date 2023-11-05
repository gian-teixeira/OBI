# Esse codigo tem o mesmo resultado do codigo 'area.py',
# mas utiliza uma biblioteca (conjunto de comandos) de
# matemática disponivel para python

# Importando (indicado que vou utilizar) a biblioteca,
# chamada 'math'
import math

PI = 3.14159

raio = float(input())

# Em vez de fazer 'area = PI*raio*raio', posso usar a
# funcao (comando) math.pow() para fazer a potenciacao.
# Neste caso, estou fazendo raio^2 (raio elevado ao quadrado)
area = PI*pow(raio,2)

# Para fixar 4 decimais para a resposta, e possivel
# utilizar o comando abaixo. Nele, '4f' poderia ter
# o 4 substituido por qualquer numero, como '2f'.
# Esse numero indica quantas casas decimais serao
# mostradas.

print('A={:.4f}'.format(area))