nome = input("Digite o seu nome: ") 
disciplina = input("Digite sua disciplina: ") 
nota1 = int(input("Digite sua primeira nota: "))
nota2 = int(input("Digite sua segunda nota: ")) 
m = (nota1 + nota2)/2
if (m)>5:
    print(f"Você {nome} está aprovado em {disciplina} com média {m}")
else:
    print(f"Você {nome} está reprovado em {disciplina} com média {m}")