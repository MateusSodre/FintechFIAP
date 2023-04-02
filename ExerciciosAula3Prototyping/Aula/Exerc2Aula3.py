NumeroTransacoes = int(input("Quantas trannsações você realizou?"))

#loop que soma o valor das transações,
i = 0
ValorFinal = 0
while i < NumeroTransacoes:
    i += 1
    ValorTransacao = float(input("Qual o valor da transação ?"))
    ValorFinal += ValorTransacao

#exibe o valor final das transações em reais
print("O valor total de transações realizadas foi de: ", ValorFinal, " Reais")
#exibe a media do valor das transacoes
MediaTransacoes = ValorFinal / NumeroTransacoes
print("A media do valor das transações foi de: ", MediaTransacoes , "Reais")