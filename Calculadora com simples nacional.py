print('=========Calculadora Tributária=========')

opcao_simples = input('Deseja calcular um serviço ? (Digite serviço) ou \
deseja calcular sua Receita Bruta pelo Simples nacional ? (Digite simples): ')

if opcao_simples == 'simples':

    receita_bruta = float(input('Digite a receita bruta acumulada nos últimos 12 meses R$: '))
    
    if receita_bruta <= 180000.00:
        aliquota_simples = 4.00
    elif receita_bruta <= 360000.00:
        aliquota_simples = 7.30
    elif receita_bruta <= 720000.00:
        aliquota_simples = 9.50
    else:
        aliquota_simples = 11.50
    
    valor_simples = receita_bruta * (aliquota_simples / 100)

    print(f'Alíquota do Simples Nacional para essa faixa de receita: {aliquota_simples:.2f}%')

    print(f'Valor do imposto a ser pago com base no Simples Nacional: R$ {valor_simples:.2f}')

    print('==========Fim da Calculadora==========')

else:

    valorCalcular = float(input('Digite o valor do serviço a ser calculado R$: '))

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

    print('==========Fim da Calculadora==========')