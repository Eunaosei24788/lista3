print("Olá este programa serve para dividir um primeiro número, por um segundo número")
a = float(input("Insira o primeiro número: "))
while a == 0: 
 print("Este número não é valido")
 a = float(input("Insira um outro número: "))
b = float(input("Insira um segundo número: "))
while b == 0: 
 print("Este número não é valido")
 b = float(input("Insira um outro número: "))
print("O resultado desta divisão é: ")
print (a / b)