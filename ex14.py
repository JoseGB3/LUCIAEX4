salario=1500
carros_vendido=int(input("Digite o número de carros vendindos pelo funionário: "))
valor_vendido=float(input("Digite o valor total vendido pelo funcionário: "))
valor_total_vendas=carros_vendido*valor_vendido
comissao=200*carros_vendido
adc=1.5*valor_vendido
total_comissao=comissao+adc
total=salario+comissao+adc
print(f"Salário base: ,{salario:.2f}","R$")
print(f"Total de vendas: ,{valor_vendido:.2f}","R$")
print(f"Total de comissão: ,{total_comissao:.2f}","R$")
print(f"Total de adicional de 5%: ,{adc:.2f}","R$")
print(f"Salário a receber: ,{total:.2f}","R$")

