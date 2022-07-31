"""
iniciar com letra, pode conter números, separar _, letras maiúsculas
"""
nome = 'João Paulo'
ano_atual = 2022
ano_nascimento = 1967
idade = ano_atual - ano_nascimento  # int
altura = 1.70  # float
e_maior = idade > 18  # bool
peso = 83
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura:.2f} de altura e pesa {peso}.')
print(f'O IMC de {nome} é: {imc:.2f}.')
print(f'{nome} nasceu em: {ano_nascimento}.')
