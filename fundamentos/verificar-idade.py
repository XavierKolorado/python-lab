nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

while idade < 0:
    print("Idade inválida! Digite um valor maior ou igual a 0.")
    idade = int(input("Digite sua idade novamente: "))

if idade >= 18:
    print(f"{nome}, você é maior de idade.")
else:
    print(f"{nome}, você não é maior de idade.")