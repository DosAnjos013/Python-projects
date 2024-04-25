c0 = int(input("Digite um número, para aplicarmos a hipótese de Collatz: "))
par = 0
impar = 0
contador = 0




while c0 >= 1:
    if c0 == 1:
        print (c0,"esse é o resultado final da hipótese")
        contador += 1
        break
        
    if c0 % 2 == 1:
        print (c0 ,"é impar, então devemos multiplicar o resultado por 3 e adicionar 1 ao resultado")
        c0 = 3*c0+1
        contador += 1
        
    else:
        print (c0," é par, então devemos dividir o resultado por 2")
        c0 = c0/2
        contador += 1
        
print ("\nPara o número escolhido, foram necessárias",contador,"etapas, para o numéro chegar a 1")

        
