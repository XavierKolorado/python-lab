import secrets
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return senha
while True:
    tamanho = int(input("Quantos caracteres sua senha deve ter? "))

    if tamanho < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
    else:
        senha = gerar_senha(tamanho)
        print(f"Sua senha gerada: {senha}")
        break