número = int(input("Digite um número para que apareça sua tabuada:"))
for i in range (1,11):
    resultado = número * i
    print(f"{número} * {i}: {resultado}")