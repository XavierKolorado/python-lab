print("=== CADASTRO DE USUÁRIO ===")

usuarios = []

opcao = input(
    "\nEscolha uma opção:\n"
    "1 - Cadastrar usuário\n"
    "2 - Listar usuários\n"
    "3 - Sair\n"
    "Digite sua opção: "
)

while opcao != "3":

    if opcao == "1":
        nome = input("Digite o nome do usuário: ")
        email = input("Digite o e-mail do usuário: ")
        senha = input("Digite a senha do usuário: ")

        usuario = {
            "nome": nome,
            "email": email,
            "senha": senha
        }

        if any(u["email"] == email for u in usuarios):
            print("\nE-mail já cadastrado!\n")
        else:
            usuarios.append(usuario)
            print("\nUsuário cadastrado com sucesso!\n")

    elif opcao == "2":
        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado.\n")
        else:
            print("=== LISTA DE USUÁRIOS ===")

            for i, usuario in enumerate(usuarios, start=1):
                print(f"{i}. Nome: {usuario['nome']}, E-mail: {usuario['email']}")

            print()

    else:
        print("Opção inválida!\n")

    opcao = input(
        "Escolha uma opção:\n"
        "1 - Cadastrar usuário\n"
        "2 - Listar usuários\n"
        "3 - Sair\n"
        "Digite sua opção: "
    )

print("\nSaindo do programa. Até logo!")