#recebe os minutos atuais
minutos = int(input("Quais são os minutos da sua máquina? "))
fatorial = 1

#loop para conseguir o fatorial dos minutos informados
for i in range (1, minutos + 1):
    fatorial *= i

print("LIBERDADE{}".format(fatorial))