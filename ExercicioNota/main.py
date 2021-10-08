#Começo do programa, menu de cadastro de aluno e nota, caso realmente queira cadastrar.
print('Escolha uma opcao')
print('1 - Cadastrar Aluno: ')
print('2 - Sair')
opcao = int(input('Insira uma opção aqui: '))

#Depois de escolhida a opção entra no while, enquanto não digitar a opção 2 que é sair o pragra não encerra.
while opcao != 2:

    #Inputs para receber as entradas os dados de nome e nota.
    nome = input('Insira seu nome: ')
    nota = float(input('Insira sua nota: '))

    #Aqui começa as condições do conceito de acordo com as notas.
    if nota >= 0.0 and nota <= 2.9:
       conceito = 'E'
    elif nota >= 3.0 and nota <= 4.9:
       conceito = 'D'
    elif nota >= 5.0 and nota <= 6.9:
       conceito = 'C'
    elif nota >= 7.0 and nota <= 8.9:
       conceito = 'B'
    elif nota >= 9.0 and nota <= 10:
       conceito = 'A'

    #Aqui  faz o print das do nome do aludo respectivamente com sua nota e o conceito de acordo com o mesmo
    print('O aluno {} tirou nota {} e se enquadra no conceito {}. \n'.format(nome, nota, conceito))

    #Aqui imprimi o menu novamente caso o usuário queira inserir outro nome e nota ou sair do programa
    #Caso a opção seja 1, inicia novamente no while.
    print('Escolha uma opcao')
    print('1 - Cadastrar Aluno: ')
    print('2 - Sair')
    opcao = int(input('Insira uma opção aqui: '))

