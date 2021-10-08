numero1 = int(input('Insira o primeiro numero:'))
numero2 = int(input('Insira o segundo numero:'))
numero3 = int(input('Insira o terceiro numero:'))

if numero1 and numero2 and numero3 > 0:
    if numero1 + numero2 > numero3 and numero2 + numero3 > numero1 and numero1 + numero3 > numero2:
       if numero1 != numero2 and numero2 != numero3 and numero1 != numero3:
           print('Triangulo escaleno')
       else:
           if numero1 == numero2 and numero2 == numero3 and numero3 == numero1:
               print('Triangulo equilqtero')
           else:
               print('Triangulo isosceles')
    else:
        print('Você digitou um numero não valido para formar um triângulo, dgte outro numero:')
else:
    print('Você digitou um numero não valido para formar um triângulo, dgte outro numero:')


