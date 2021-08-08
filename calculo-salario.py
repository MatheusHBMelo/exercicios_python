# Matheus possui um salário de R$3.500 fixo e um adicional de R$55.00 por clientes atendidos. 
# De quanto será o seu salário no mês que ele atendeu 7 pessoas.

qtd_clientes = int(input('Quantos clientes você atendeu no mes: '))

salario_fixo = 3500
salario_add = 55

salario_final = float(salario_fixo + (salario_add * qtd_clientes))

print("_______________________________________________\n")
print(f'Você recebe por padrão um salário fixo de R${salario_fixo:.2f}')
print(f'Você recebe por padrão um salário adicional de R${salario_add:.2f}')
print(f'No atual mês você atendeu {qtd_clientes} clientes')
print("_______________________________________________\n")

print(f'O seu salário nesse mês será de R${salario_final:.2f}')