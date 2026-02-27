
numero=int(input("Digite seu numero inteiro: "))
print(numero,"segundos")
horas=numero//3600
numero=numero%3600

minutos=numero//60
numero=numero%60

segundos=numero//1
print("Quantidade correspondente em horas, minutos e segundos: ",horas,"h",minutos,"m",segundos,"s")

