def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while x < min or x > max:
        x = int(input(pergunta))
    return x
def fatorial(num):
    """
    CALCULA A FATORIAL
    :param num: numero fornecido pelo usuario
    :return: retorno do calculo da fatorial
    """


    fat = 1

    if num == 0:
        return fat

    for i in range(1,num+1,1):
        fat *= i
    return fat
x = valida_int('Insira um numero para fazer a fatorial: ', 0, 20)
print('A fatorial do numero {} é {}: ' .format(x, fatorial(x)))