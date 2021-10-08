def mudaLetra(mudanome, mudasobrenome):
    primeiraletra = mudanome[0]
    nomecompleto = primeiraletra + mudasobrenome
    return nomecompleto

#programaprincipal
nome = input('Insira o seu nome: ')
sobrenome = input('Insira o segundo nome: ')
algoritimos = '@algoritmos.com.br'
concatena = mudaLetra(nome, sobrenome) + algoritimos

print('O seu nome é {} {} e seu email é {}'.format(nome, sobrenome, concatena))