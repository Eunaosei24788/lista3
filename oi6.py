print("Olá esse programa serve para mostrar os números pares entre 1 e o número escolhido por você.")
n = int(input("Insira seu número: "))
u = 0
while n <= 0:
    print("Este número não é permitido")
    n = int(input("Insira outro número: "))
while u <= n:
    print(u)
    u += 2
    
