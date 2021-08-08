# Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

string_um = input('Digite a primeira string: ')
string_dois = input('Digite a segunda string: ')

print(f'O tamanho da string {string_um} é de {len(string_um)} caracteres.')
print(f'O tamanho da string {string_dois} é de {len(string_dois)} caracteres.')

if len(string_um) == len(string_dois):
    print('As duas strings são de tamanhos iguais.')
else:
    print('As duas strings são de tamanhos diferentes.')

if string_um == string_dois:
    print('As duas strings são iguais.')
else:
    print('As duas strings são diferentes.')

