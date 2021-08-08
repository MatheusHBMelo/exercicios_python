# Altere o programa anterior de modo que a escada seja invertida.

name = input('Digite o seu nome: ').upper()
for n in range(0, len(name) + 1):
    print(name[:-n])