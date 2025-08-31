pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro ou 'fim' para encerrar: ").lower()
    if entrada == 'fim':
        break
try:
    numero = int(entrada)
    if numero % 2 == 0:
        print(f"{numero} é par.")
        pares += 1
    else:
        print(f"{numero} é ímpar.")
        impares += 1
except ValueError:
    print("Entrada inválida. Digite um número inteiro.")

print(f"Total de pares: {pares}")
print(f"Total de ímpares: {impares}")