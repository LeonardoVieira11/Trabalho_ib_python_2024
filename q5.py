horario = int(input("Digite um horário: "))
if (horario)<=11:
  print("É de manhã")
elif (horario)>11 and (horario)<=18:
  print("É de tarde")
else:
  print("É de noite")