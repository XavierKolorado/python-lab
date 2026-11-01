nome = input("Digite seu nome: ")

nota1 = float(input("Digite a primeira nota: "))

while nota1 < 0 or nota1 > 10:
    print("Nota inválida! Digite um valor entre 0 e 10.")
    nota1 = float(input("Digite a primeira nota novamente: "))

nota2 = float(input("Digite a segunda nota: "))

while nota2 < 0 or nota2 > 10:
    print("Nota inválida! Digite um valor entre 0 e 10.")
    nota2 = float(input("Digite a segunda nota novamente: "))

nota3 = float(input("Digite a terceira nota: "))

while nota3 < 0 or nota3 > 10:
    print("Nota inválida! Digite um valor entre 0 e 10.")
    nota3 = float(input("Digite a terceira nota novamente: "))

media = (nota1 + nota2 + nota3) / 3

print(f"\n{nome}, sua média é: {media:.2f}")

if media >= 7:
    print("Parabéns! Você foi aprovado.")
else:
    print("Infelizmente, você não foi aprovado.")