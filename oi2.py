print("Olá esse é um programa para calcular a tabuada de um número de 1 a 10")
a = int(input('Insira um valor: '))
while a > 10 or a <= 0:
 print ('Só vale numeros entre 1 a 10')
 a = int(input('Insira outro valor, de 1 a 10: ')) 
b = 1
while a <= 10 or a > 0:
 print(a * b)
 b += 1
 if b == 11:
  print("Pronto, tá ai sua tabuada :)")
  break

