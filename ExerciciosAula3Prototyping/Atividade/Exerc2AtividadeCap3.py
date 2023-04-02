votosSegunda = int (input("Quantos votos segunda-feira teve?"))
votosTerca = int (input("Quantos votos terça-feira teve?"))
votosQuarta = int (input("Quantos votos quarta-feira teve?"))
votosQuinta = int (input("Quantos votos quinta-feira teve?"))
votosSexta = int (input("Quantos votos sexta-feira teve?"))

maior = votosSegunda
escolhido = "segunda-feira"

if votosTerca > maior:
    maior = votosTerca
    escolhido = "terca-feira"
    if votosQuarta > maior:
        maior = votosQuarta
        escolhido = "quarta-feira"
        if votosQuinta > maior:
            maior = votosQuinta
            escolhido = "quinta-feira"
            if votosSexta > maior:
                maior = votosSexta
                escolhido = "sexta-feira"

print("O dia ganhador da eleição foi: ", escolhido, "com o total de: ", maior, " votos")

