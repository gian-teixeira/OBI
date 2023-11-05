PI = 3.14159

raio = float(input())
area = PI*raio*raio

# Para fixar 4 decimais para a resposta, e possivel
# utilizar o comando abaixo. Nele, '4f' poderia ter
# o 4 substituido por qualquer numero, como '2f'.
# Esse numero indica quantas casas decimais serao
# mostradas.

print('A={:.4f}'.format(area))