faturamentoAnual = float(input("Qual o seu faturamento anual?"))
tipoAssinatura = int(input("Qual seu tipo de assinatura? 'Basic [1], Silver [2], Gold [3] ou Platinum [4]'"))

if tipoAssinatura == 1:
     resultado = faturamentoAnual * 0.3
     print("O valor a ser pago é de: ", resultado, "Reais")
elif tipoAssinatura == 2:
    resultado = faturamentoAnual * 0.2
    print("O valor a ser pago é de: ", resultado, "Reais")
elif tipoAssinatura == 3:
    resultado = faturamentoAnual * 0.1
    print("O valor a ser paago é de: ", resultado, "Reais")
elif tipoAssinatura == 4:
    resultado = faturamentoAnual * 0.05
    print("O valor a ser pago é de: ", resultado, "Reais")

