import random
def funcaoCadastra(nome, nomeMulti,listaSorteio):

    for i in range(nomeMulti):

       listaSorteio.append(nome)

    return listaSorteio

lista = []

print('Digite 1 para cadastra doação ou 2 para finalizar!')
opcao = int(input('Digite a sua opção: '))

while opcao == 1:

   nome = input('Insira seu nome: ')
   valor = float(input('Insira o valor doado: '))
   nomeMulti = int(valor // 10)

   funcaoCadastra(nome, nomeMulti, lista)

   print('Digite 1 para cadastra doação ou 2 para finalizar!')
   opcao = int(input('Digite a sua opção: '))

print('Lista de pessos a serem sorteadas: {}'.format(lista))
random.shuffle(lista)
sorteado = random.choice(lista)

print('O sorteado foi: {}'.format(sorteado))



