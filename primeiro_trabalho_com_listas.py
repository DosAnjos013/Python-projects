#Cenário
#Era uma vez um chapéu. O chapéu não continha coelhos, mas uma lista de cinco números: 1, 2, 3, 4 e 5.

#Sua tarefa:

#escreva uma linha de código que solicite que o usuário substitua o número do meio na lista por um número inteiro inserido pelo usuário (Etapa 1)
#escreva uma linha de código que remova o último elemento da lista (Etapa 2)
#escreva uma linha de código que imprima o comprimento da lista atual (Etapa 3).

hatList= [1,2,3,4,5]
print ("A lista atual contém a sequência", hatList)
modificador = int(input("\nDigite um número, para substituir o número da terceira posição da lista: "))
hatList[2] = modificador
print ("\nA nova sequência é:", hatList)
print("\nO comprimento da lista é:", len(hatList))
