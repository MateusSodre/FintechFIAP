NumeroRefeicoes = int (input("Quantas refeições você fez até o momento?"))

i =0
caloriasTotais = 0

#loop que vai somar as calorias e tera como limitador a quantidade de refeição indicada pela var 'NumeroRefeicoes'
while i < NumeroRefeicoes:
    i += 1
    input("O que você comeu?")
    calorias = int (input("Quantas calorias tinha nesta refeição?"))
    caloriasTotais += calorias

#escreve o total de calorias consumidas
print("O total de calorias consumidas até o momento foi de ", caloriasTotais)