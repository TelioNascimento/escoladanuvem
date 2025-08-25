# Escola da Nuvem
# Atividade Pratica 03
# Editado por Telio Mauricio
# Exercicio 06
# Calculadora de Comissao
nome_vendedor = input()
salario_fixo = float(input())
total_vendas = float(input())
comissao = total_vendas * 0.15
salario_final = salario_fixo + comissao

print(f"TOTAL = R$ {salario_final:.2f}")