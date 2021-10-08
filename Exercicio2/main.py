dias = int(input('Digite os dias: '))
horas = int(input('Digite as horas: '))
minutos = int(input('Digite os minutos: '))
segundos = int(input('Digite os segundos: '))

calculo = (dias*24*60*60) + (horas*60*60) + (minutos*60) + (segundos)

print('O valor corresponde {} segundos.' .format(calculo))