
import json

json_file = "usuarios.json"

try:
    with open(json_file, "r", encoding="utf-8") as arquivo:
        usuarios = json.load(arquivo)

except (FileNotFoundError, json.JSONDecodeError):
    usuarios = []


def salvar_usuarios():
    with open(json_file, "w", encoding="utf-8") as arquivo:
        json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)


print("=== CADASTRO DE USUÁRIO ===")


opcao = input(
    "\nEscolha uma opção:\n"
    "1 - Cadastrar usuário\n"
    "2 - Listar usuários\n"
    "3 - Sair\n"
    "4 - Excluir usuário\n"
    "5 - Editar usuário\n"
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
            salvar_usuarios()
            print("\nUsuário cadastrado com sucesso!\n")

    elif opcao == "2":
        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado.\n")
        else:
            print("=== LISTA DE USUÁRIOS ===")

            for i, usuario in enumerate(usuarios, start=1):
                print(f"{i}. Nome: {usuario['nome']}, E-mail: {usuario['email']}")

            print()

    elif opcao == "3":
        break

    elif opcao == "4":
        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado.\n")
        else:
            print("=== EXCLUIR USUÁRIO ===")

            for i, usuario in enumerate(usuarios, start=1):
                print(f"{i}. Nome: {usuario['nome']}, E-mail: {usuario['email']}")

            try:
                indice = int(input("Digite o número do usuário a ser excluído: ")) - 1

                if 0 <= indice < len(usuarios):
                    del usuarios[indice]
                    salvar_usuarios()
                    print("\nUsuário excluído com sucesso!\n")
                else:
                    print("\nÍndice inválido!\n")

            except ValueError:
                print("\nPor favor, digite um número válido!\n")

    elif opcao == "5":
        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado.\n")
        else:
            print("=== EDITAR USUÁRIO ===")

            for i, usuario in enumerate(usuarios, start=1):
                print(f"{i}. Nome: {usuario['nome']}, E-mail: {usuario['email']}")

            try:
                indice = int(input("Digite o número do usuário a ser editado: ")) - 1

                if 0 <= indice < len(usuarios):
                    print(f"\nEditando usuário: {usuarios[indice]['nome']}")

                    novo_nome = input("Digite o novo nome (ou pressione Enter para manter): ")
                    novo_email = input("Digite o novo e-mail (ou pressione Enter para manter): ")
                    nova_senha = input("Digite a nova senha (ou pressione Enter para manter): ")

                    if novo_nome:
                        usuarios[indice]['nome'] = novo_nome

                    if novo_email:
                        email_existe = any(
                            u["email"] == novo_email
                            for i, u in enumerate(usuarios)
                            if i != indice
                        )

                        if email_existe:
                            print("\nE-mail já cadastrado!\n")
                        else:
                            usuarios[indice]['email'] = novo_email

                    if nova_senha:
                        usuarios[indice]['senha'] = nova_senha

                    salvar_usuarios()
                    print("\nUsuário editado com sucesso!\n")

                else:
                    print("\nÍndice inválido!\n")

            except ValueError:
                print("\nPor favor, digite um número válido!\n")

    else:
        print("Opção inválida!\n")

    opcao = input(
        "Escolha uma opção:\n"
        "1 - Cadastrar usuário\n"
        "2 - Listar usuários\n"
        "3 - Sair\n"
        "4 - Excluir usuário\n"
        "5 - Editar usuário\n"
        "Digite sua opção: "
    )

print("\nSaindo do programa. Até logo!")
