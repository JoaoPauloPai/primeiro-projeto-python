import pandas as pd
import win32com.client as win32

#passo a paaso para a solução
#abrir os 6 arquivos em excel
#para cada arquivo :
#verificar se algum valor na coluna vendas naquele arquivo é maior que 55.000
#se for maior que 55.00 envia um sms com o nome mes e as vendas do vendedor

tabela_vendas = pd.read_excel('Vendas.xlsx')

pd.set_option('display.max_columns', None)

faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print('Faturamento de todas as Lojas')
print(faturamento)
#Atualizando
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print('*' * 50)
print('Quantidade de Produtos por Loja')
print(quantidade)

ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})
print('*' * 50)
print('Ticker Médio por Loja')
print(ticket_medio)

#enviar um email com o relatório
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'joaopaulopai99@gmail.com'
mail.Subject = 'Relatório de Vendas por Loja'
mail.HTMLBody = f'''

<p>Prezados,</p>

<p>Segue o Relatório de Vendas por cada Loja.</p>

<p>Faturamento:</p>

<p>Quantidade:</p>

<p>Ticket Médio:</p>

'''

mail.Send()

print("Email enviado com sucesso")