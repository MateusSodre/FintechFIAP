#calcular a nota
numeroAluno = 1
media = 0
somaNotas = 0

#loop para inserir a nota dos alunos impares
for i in range (1,50,2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS IMPARES")
    notas = int(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}".format(numeroAluno)))
    somaNotas += notas
    numeroAluno += 2

#variavel que faz o calculo da média
media = (somaNotas / 25)
print(media)

#Reatribui valores nas variáveis, esta correto? que outra maneira poderia fazer isso?
numeroAluno = 2
media = 0
somaNotas = 0

#loop para inserir a nota dos alunos pares
for i in range (1,50,2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
    notas = int(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}".format(numeroAluno)))
    somaNotas += notas
    numeroAluno += 2

media = (somaNotas / 25)
print(media)