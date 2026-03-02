tempo_destino=float(input("Digite o tempo gasto ( em horas ) para chegar ao destino: "))
velocidade_media=float(input("Digite a velocidade media (em km/h) : "))
distancia=velocidade_media*tempo_destino
consumo=distancia/12
print(f"A distância percorrida foi de {distancia:.2f} km")
print(f"O consumo do veículo foi de {consumo:.2f} litros de gasolina")

