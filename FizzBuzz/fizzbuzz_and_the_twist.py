tamanho = int(input('Tamanho da lista: '))
def create(size):
    final_list = []
    for i in range (1, size + 1):
        if i % 5 == 0 and i % 3 == 0:
            final_list.append('FizzBuzz')
        elif i % 3 == 0:
            final_list.append('Fizz')
        elif i % 5 ==0:
            final_list.append('Buzz')
        else:
            final_list.append(i)
    return final_list

print (create(tamanho))
