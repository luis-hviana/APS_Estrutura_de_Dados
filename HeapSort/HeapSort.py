import time
def heapSort(vetor):
    tamanho = len(vetor)

    for i in range(tamanho // 2 - 1, -1, -1):
        heap(vetor, tamanho, i)

    for i in range(tamanho - 1, 0, -1):
        vetor[i], vetor[0] = vetor[0], vetor[i]  # swap
        heap(vetor, i, 0)

def heap(vetor, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and vetor[i] < vetor[l]:
        largest = l

    if r < n and vetor[largest] < vetor[r]:
        largest = r

    if largest != i:
        vetor[i], vetor[largest] = vetor[largest], vetor[i]

        heap(vetor, n, largest)

if __name__ == '__main__':
    inicioAQ = time.time()
    vetor = []
    with open('10000_numbers.txt', 'r') as arquivo:
        for valor in arquivo:
            vetor.append(int(valor))
    arquivo.close()
    fimAQ = time.time()

    inicio = time.time()
    heapSort(vetor)
    fim = time.time()

    tempoDeAquisicao = fimAQ - inicioAQ
    tempoDeOrdenacao = fim - inicio
    print("Tempo total: ", tempoDeAquisicao + tempoDeOrdenacao)
    print("Tempo de aquisição: ", tempoDeAquisicao)
    print("Tempo de ordenação: ", tempoDeOrdenacao)



