

# passo a passo para a solutes
# abrir os arquivos em exel
# para cada arquivo verficar na coluna vendas 
# se for maior que 55 mil enviar um sms 
# nome e valor para o numero cadastrado.
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

tabelas_vendas = pd.read_excel('janeiro.xlsx')

print(tabelas_vendas)