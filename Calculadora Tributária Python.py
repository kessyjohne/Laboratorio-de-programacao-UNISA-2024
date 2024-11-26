print ('=========Calculadora Tributária=========')

valorCalcular = float(input('Digite o valor a ser calculado R$: '))

aliquota_icms = float(input("Digite a alíquota do ICMS (%): "))
aliquota_iss = float(input("Digite a alíquota do ISS (%): "))
aliquota_pis = float(input("Digite a alíquota do PIS (%): "))
aliquota_cofins = float(input("Digite a alíquota do COFINS (%): "))

valor_icms = valorCalcular * (aliquota_icms / 100)
valor_iss = valorCalcular * (aliquota_iss / 100)
valor_pis = valorCalcular * (aliquota_pis / 100)
valor_cofins = valorCalcular * (aliquota_cofins / 100)

print ('==========Resultado dos calculos==========')

print(f"ICMS: R$ {valor_icms:.2f}")
print(f"ISS: R$ {valor_iss:.2f}")
print(f"PIS: R$ {valor_pis:.2f}")
print(f"COFINS: R$ {valor_cofins:.2f}")

total_tributos = valor_icms + valor_iss + valor_pis + valor_cofins
print (f'O total de imposto a ser pago será R$ {total_tributos}')