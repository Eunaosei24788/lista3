print("Este programa serve para calcular a média entre duas notas de 0 a 10")
a = int(input("Insira a primeira nota: "))

while a > 10 or a < 0:
 print("Este número não é valido")
 a = int(input("Insira uma outra nota: "))

b = int(input("Insira a segunda nota: "))

while b > 10 or b < 0:
 print("Este número não é valido")
 b = int(input("Insira uma outra nota: "))

c = a + b
print("Sua média é: ")
print(c / 2)

print("Deseja fazer outro cálculo?")

d = str(input("Digite sim, ou não: "))

if d == "não":
 print("Tchau")

while d == "sim":
  a = int(input("Insira a primeira nota: "))
  while a > 10 or a < 0:
   print("Este número não é valido")
   a = int(input("Insira uma outra nota: "))
  b = int(input("Insira a segunda nota: "))
  while b > 10 or b < 0:
   print("Este número não é valido")
   b = int(input("Insira uma outra nota: "))    
  c = 0
  c = a + b
  print("Sua média é: ")
  print(c / 2)
  print("Deseja fazer outro cálculo?")
  d = str(input("Digite sim, ou não: "))
  if d == "não":
   print("Tchau")
   break



