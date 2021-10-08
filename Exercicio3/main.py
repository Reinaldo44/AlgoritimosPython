produto = float(input('Digite o valor do produto: '))
desconto = float(input('Digite o valor do desconto: '))


desconto = produto * (desconto/100)
produto_desconto = produto - desconto

print('Você obteve um desconto de {} reais, o preço final do seu produto é: {}' .format(desconto, produto_desconto))