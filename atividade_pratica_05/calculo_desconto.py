def calcular_desconto(preco, percentual_desconto):
    desconto = preco * (percentual_desconto /100)
    preco_final = preco - desconto
    return preco_final

while True:
    try:
        preco = float(input("Digite o preço do produto (Ex: 250.754): R$"))
        percentual_desconto = float(input("Digite o percentual de desconto (Ex: 10%): "))
        break
    except ValueError:
        print("Por favor insira um valor numérico.")

preco_com_desconto = calcular_desconto(preco, percentual_desconto)
print(f"O preco final com desconto de R$ {percentual_desconto}% é: R$ {preco_com_desconto:.2f}")