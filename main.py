def maior(a, b):
    if a > b:
        return a
    return b

def soma(lista, x):
    somaParcial = 0
    for i in range(len(lista)):
        somaParcial += lista[i]
    if x != None:
        somaParcial += x
    return somaParcial

def media(lista):
    somaParcial = soma(lista)
    return somaParcial/len(lista)

def valores_iguais(lista1 , lista2):
    lista3 = []
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i] == lista2[j] && lista1[i] not in lista3:
                lista3.append(lista1[i])
                break

    return lista3

def indice_prim_valor_igual(lista1,lista2):
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                return i
    
    return None


def main():
    valores1 = [random.randint(0, x + 10) for x in range(10)]
    valores2 = [random.randint(0, x + 10) for x in range(10)]
    valor_a = random.randint(0, 50)
    valor_b = random.randint(0, 50)

    print(f'Lista A: {valores1}')
    print(f'Lista B: {valores2}')
    print(f'Valor A: {valor_a}')
    print(f'Valor B: {valor_b}')
    print(f'Result: maior: {maior(valor_a, valor_b)}')
    print(f'Result: soma: {soma(valores1, valor_b)}')
    print(f'Result: media: {media(valores1)}')
    print(f'Result: valores_iguais: {valores_iguais(valores1, valores2)}')
    print(f'Result: indice_prim_valor_igual: {indice_prim_valor_igual(valores1, valores2)}')

if __name__ == '__main__':
    main()