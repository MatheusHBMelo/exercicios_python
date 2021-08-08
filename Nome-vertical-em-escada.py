# Modifique o programa anterior de forma a mostrar o nome em formato de escada.

name = input('Digite o seu nome: ').upper()
for n in range(0, len(name) + 1):
    print(name[:n])