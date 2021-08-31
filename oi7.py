print("Esse programa serve para desenhar um quadrado em #")
lado = int(input("Insira o número de cada lado: "))
while lado <= 0:
    print("insira apenas números positivos")
    lado = int(input("Insira o número de cada lado: "))
for quadrado in range(lado):
    print(" # "*lado)




