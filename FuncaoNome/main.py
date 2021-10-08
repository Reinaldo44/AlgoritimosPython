def funcaoMudaNome(nome, sobreNome, raUninter):

    primeiraLetra = nome[0].lower()
    email = '@algoritmos.com.br'
    concatena = primeiraLetra + sobreNome.lower() + raUninter + email

    return concatena

nome = input('Insira seu primeiro nome: ')
sobreNome = input('Insira seu primeiro sobrenome: ')
ruUninter = input('Digite os dois ultimos digitos do seu RA: ')

print('Seu nome é {} {} e seu email é: {}'.format(nome, sobreNome, funcaoMudaNome(nome,sobreNome,ruUninter)))