dias_aluguel = float(input('Digite os dias que deseja alugar o carro: '))
quant_km = float(input('Digite a quantidade de km: '))

valor_aluguel = (dias_aluguel*60) + (quant_km*0.15)

print('O valor do aluguel é:{}' .format(valor_aluguel))