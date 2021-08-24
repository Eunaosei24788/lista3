from random import randint
c = randint(1,10)
print ('você tem 3 tentativas para acertar um numero gerado aleatoriamente entre 1 a 10, ele não muda nunca.')
adv = int(input("coloca um numero de 1 a 10 pfv: "))
while adv > 10 or adv <= 0:
    print()
    print("pode só numero de 1 a 10")
    adv = int(input("coloca um numero de 1 a 10, por favor mano: "))
t = 2
while t > 0 and adv != c:
    t = t - 1
    print()
    adv = int(input("coloca dnv pfv, vc errou: "))
    while adv > 10 or adv <= 0:
        print()
        print("pode só numero de 1 a 10")
        adv = int(input("coloca um numero de 1 a 10, por favor mano: "))
if adv == c:
    print("acertou dale dale dele doli")
else:
    print("perdeu")
print("o valor sorteado é", c)