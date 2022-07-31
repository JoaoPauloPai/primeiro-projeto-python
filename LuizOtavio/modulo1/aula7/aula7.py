"""
iniciar com letra, pode conter números, separar _, letras maiúsculas
"""
nome = 'joão Paulo'
idade = 52  # int
altura = 1.70  # float
e_maior = idade > 18  # bool
peso = 83
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos e seu IMC é: {imc:.2f}')
