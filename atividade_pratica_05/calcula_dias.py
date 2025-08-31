#Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.

from datetime import date

def calcular_idade_em_dias(dia, mes, ano):
   
    try:
        data_nascimento = date(ano, mes, dia)
        data_atual = date.today()
        
        # Verifica se a data de nascimento não é futura
        if data_nascimento > data_atual:
            print("Erro: A data de nascimento não pode ser no futuro.")
            return -1
        
        diferenca = data_atual - data_nascimento
        return diferenca.days
    except ValueError:
        print("Erro: Data de nascimento inválida. Por favor, insira uma data válida.")
        return -1

# Exemplo de uso
dia_nasc = int(input ("Entre com o dia do seu nascimento:"))
mes_nasc = int(input ("Entre com o mes do seu nascimento:"))
ano_nasc = int(input("Entre com o ano do seu nascimento:"))

idade_dias = calcular_idade_em_dias(dia_nasc, mes_nasc, ano_nasc)

if idade_dias != -1:
    print(f"A idade é de {idade_dias} dias.")