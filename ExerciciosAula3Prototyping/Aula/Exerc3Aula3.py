resposta = int(input("digite um numero"))
anterior1 = 1
anterior2 = 0

for n_elemento in range(1, resposta + 1, 1):
    atual  = anterior1 + anterior2
    anterior1 = anterior2
    anterior2= atual
    if resposta == atual:
        print("Ação bem sucedida!")
        break
    elif resposta < atual:
        print("Ação falhou...")
        break