idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Você é menor de idade.")
elif idade < 65:
    print("Você é adulto.")
else:
    print("Você é idoso.")
