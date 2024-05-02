print("\nO algoritmo receberá o nome dos alunos, as notas do alunos, e exibirá a média ponderada ou aritmética das notas.\n\n")

tipoMedia = ["Média ponderada","Média aritimética","Ambas"]
opcao = 0
while ((opcao < 1) or (opcao > 3)):
    print("+----------------------+")
    print("|        Opções        |")
    print("|1. " + tipoMedia[0] + "    |")
    print("|2. " + tipoMedia[1] + "  |")
    print("|3. " + tipoMedia[2] + "              |")
    print("+----------------------+")
    opcao = int(input("\nSelecione a opção desejada: "))
    
    if ((opcao < 1) or (opcao > 3)):
        print("Opção invalida!!\nTente novamente!!!\n")
print("\n+-------------------------------------------------------------+\n")

peso = []
pessoas = []
notas = []
mediaA = []
mediaP = []


#Recebe o peso das notas
if ((opcao == 1) or (opcao == 3)):
    print("\nDe acordo com a opção desejada defina o peso das notas.")
    for i in range(4):
        print("\n",i+1,"° nota")
        peso.append(int(input("Qual é o peso: ")))
print("\n+-------------------------------------------------------------+\n")

#Recebe a quantidade de pessoas a seram avaliadas
quantidade = int(input("Qual é a quantidade de avaliados?: "))
print("\n+-------------------------------------------------------------+\n")

#Recebe o nome dos avaliados e os guarda em uma lista
print("\nAgora vamos listar os avaliados...")
for i in range(quantidade):
    print("\n", i + 1,"° avaliado!")
    pessoas.append(input("Digite o nome: "))
print("\n+-------------------------------------------------------------+\n")


#recebe as notas
for i in range(quantidade):
    for j in range(4):
        print("\n", j + 1,"° nota de ", pessoas[i])
        notas.append(float(input("Digite a nota: ")))
    mediaA.append((notas[0] + notas[1] + notas[2] + notas[3]) / 4)
    mediaP.append(((notas[0] * peso[0]) + (notas[1] * peso[1]) + (notas[2] * peso[2]) + (notas[3] * peso[3]))/10)
    notas.clear()
    print("\n+-------------------------------------------------------------+\n")


#imprime as notas
print("\n\nNotas:")
if (opcao == 1):
    for i in range (quantidade):
        print("\n",pessoas[i]," - Média ponderada:",round(mediaP[i],2))
elif (opcao == 2):
    for i in range (quantidade):
        print("\n",pessoas[i]," - Média ponderada:",round(mediaA[i],2))
elif (opcao == 3):
    for i in range (quantidade):
        print("\n",pessoas[i]," - Média ponderada:",round(mediaP[i],2)," | Média aritimética: ",round(mediaA[i],2))