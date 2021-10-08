from operator import itemgetter
##Cria a lsta e o dicionario
estoque = []
estoques = {}

##Cria um loop while, para adicionar os itens do estoque
while True:

   ##inputs para receber os dados do teclado, codigo, estoque e mínimo
   print('Digite 0 caso queira encerrar! ')
   estoques['codigo'] = int(input('Digite um numero do codigo: '))

   ##Condição if para que o programa se encerre quando digitado 0, no campo codigo
   if estoques['codigo'] == 0:
        break

   estoques['estoque'] = int(input('Digite o numero de estoque: '))
   estoques['minimo'] = int(input('Digite o minimo de produto para o estoque: '))

   ##Adiciona os dados vindo do teclado nos diconarios e listas
   estoque.append(estoques.copy())

   ##Ordena a lista, em ordem crescente pela chave codigo
   listaOrdenada = sorted(estoque, key=itemgetter('codigo'))

#Far o print da lista
print(listaOrdenada)


