dinheiro = 0
pessoas = 0

while True:
    idade = input('Digite a idade: ')
    if idade == 'sair':
        break
    idade = int(idade)
    pessoas += 1

    if idade < 3:
        ingresso = 0
    else:
        if idade > 12:
            ingresso = 30

        else:
            ingresso = 15

    dinheiro += ingresso
media = dinheiro / pessoas

print('O total de ingressos  é : {}'.format(pessoas))
print('O total gasto é : {}'.format(dinheiro))
print('A média do gasto é : {}'.format(media))


