#Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. O programa deve continuar pedindo senhas até que uma válida
#  seja inserida ou o usuário digite 'sair'.
# # --- Verificador de senha forte ---
def senha_forte(senha):
    return len(senha) >= 8 and any(char.isdigit() for char in senha)
while True:
    senha = input("Digite uma senha forte ou 'sair' para encerrar: ").lower()
    if senha == 'sair':
        print("Encerrando verificação.")
        break
    if senha_forte(senha):
        print("Senha válida e forte!")
        break
    else:
        print("Senha fraca. Deve ter pelo menos 8 caracteres e conter ao menos um número.")