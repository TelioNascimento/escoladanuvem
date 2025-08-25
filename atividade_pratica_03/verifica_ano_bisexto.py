# Escola da Nuvem
# Atividade Pratica 03
# Editado por Telio Mauricio
# Exercicio 05
# Verificador Ano Bissexto
ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")