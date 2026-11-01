def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def quilometros_para_milhas(quilometros):
    return quilometros / 1.609


def quilogramas_para_libras(quilogramas):
    return quilogramas * 2.20462

print("==============================")
print("       PYTHON CONVERTER")
print("==============================")

print("\nEscolha uma conversão:")
print("1 - Celsius para Fahrenheit")
print("2 - Quilômetros para Milhas")
print("3 - Quilogramas para Libras")

opcao = input("\nDigite sua opção: ")

if opcao == "1":
    celsius = float(input("\nDigite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"\n{celsius}°C é igual a {fahrenheit:.2f}°F")
elif opcao == "2":
    quilometros = float(input("\nDigite a distância em quilômetros: "))
    milhas = quilometros / 1.609
    print(f"\n{quilometros} km é igual a {milhas:.2f} mi")
elif opcao == "3":
    quilogramas = float(input("\nDigite o peso em quilogramas: "))
    libras = quilogramas * 2.20462
    print(f"\n{quilogramas} kg é igual a {libras:.2f} lb")
else:
    print("Opção inválida!")