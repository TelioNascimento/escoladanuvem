def palindromo(frase):
    #Remover os espacos e convertendo para minusculo
    texto_limpo = ''.join(char.lower()
                          for char in frase
                          if char.isalnum()
                          )
    return texto_limpo == texto_limpo[::-1] # comparando o texto limpo a sua versão invertida

texto = input("Digite a expressão ou palavra:")
resultado = palindromo(texto)

if resultado == True:
    resposta = "Sim"
else:
    resposta = "Não"

print(f"'{texto}' é um palindromo? {resposta}")