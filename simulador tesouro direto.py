while True:
    print("------------------------")
    print("  Seja bem-vindo(a) ao  ")
    print("       Tesouro Direto   ")
    print("------------------------")

    print("Tesouro prefixado 2024")
    print("Tesouro prefixado 2026")

    escolha = input("Qual investimento você gostaria de simular? a para 2024 e b para 2026:")

    if escolha == 'a':
            valor1 = int(input("Qual o valor que você deseja investir?:"))
            valor2 = int(input("Se você for investir todo mês, qual o valor desejado?:"))

            valorT = (valor2 * 32) + valor1
            porcIR = (valorT * 15) /100
            valorIR = (valorT - porcIR)
            valorB3 = (valorT * 1.5) /100
            valorLU = (valorT * 0.1081)
            valorB = (valorT + valorLU)

            valorLI = (valorT - (valorIR + valorB3))


            print("------------------------")
            print("-       Resultado da   -")
            print("-        simulação     -")
            print("------------------------")

            print("------------------------------------")
            print("Valor incial investido:", valor1)
            print("Aportes de ",valor2,"por 32 meses")
            print("Valor total inevestido:", valorT)
            print("------------------------------------")

            print("-------------------------")
            print("Valor bruto:", valorB)
            print("I.R.:", porcIR)
            print("Taxa da B3:", valorB3)
            print("-------------------------")

            denovo = str(input("Deseja realizar outra simulação? s/n:"))

    else:

            valor1= int(input("Qual o valor que você deseja investir?:"))
            valor2 = int(input("Se você for investir todo mês, qual o valor desejado?:"))

            valorT = (valor2 * 50) + valor1
            porcIR = (valorT * 15) /100
            valorIR = (valorT - porcIR)
            valorB3 = (valorT * 2.5) /100
            valorLU = (valorT * 0.1081)
            valorB = (valorT + valorLU)

            valorLI = (valorT - (valorIR + valorB3))

            print("-----------------------")
            print("-       Resultado da  -")
            print("-        simulação    -")
            print("-----------------------")

            print("------------------------------------")
            print("Valor incial investido:", valor1)
            print("Aportes de ",valor2,"por 50 meses")
            print("Valor total inevestido:", valorT)
            print("-----------------------------------")

            print("-------------------------")
            print("Valor bruto:", valorB)
            print("I.R.:", porcIR)
            print("Taxa da B3:", valorB3)
            print("-------------------------")
 
    denovo = str(input("Deseja realizar outra simulação? s/n: "))

    if denovo == 'n':
        break

print("Programa encerrado")

