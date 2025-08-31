#Crie uma função que calcule a gorjeta a ser deixada em um restaurante,
# baseada no valor total da conta e na porcentagem de gorjeta desejada.
# Calcule o valor da gorjeta baseado no total da conta e na porcentagem desejada.


def calcula_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta/100)
    return gorjeta
valor_conta = float(input("Digite o valor total da conta: "))
porcentagem_gorjeta = float(input("Insira a porcentagem da gorjeta: "))
gorjeta = calcula_gorjeta(valor_conta, porcentagem_gorjeta)
print(gorjeta)