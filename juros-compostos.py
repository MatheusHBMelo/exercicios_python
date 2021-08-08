# Crie um programa que calcule a taxa de juros compostos para um emprestimo.
# Leve em consideração o montante, capital, taxa de juros e a quantidade de meses.

valor_capital = float(input('Qual o valor do capital que será investido: '))
taxa_juros = float(input('Qual a taxa de juros mensal: '))
tempo_meses = int(input('O valor será aplicado em quantos meses: '))

taxa_juros = taxa_juros / 100

montante = valor_capital * ((taxa_juros + 1) ** tempo_meses)

print("_______________________________________________\n")
print(f'Você aplicou R${valor_capital:.2f}')
print(f'Com uma taxa de {taxa_juros}% mensal')
print(f'Em um periodo de {tempo_meses} meses')
print("_______________________________________________\n")

print(f'O valor total a ser pago é de R${montante:.2f}')
