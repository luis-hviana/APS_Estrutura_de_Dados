import time
def SelectionSort(vetor):

    for index in range(0, len(vetor)):
        min_index = index

        for right in range(index + 1, len(vetor)):
            if vetor[right] < vetor[min_index]:
                min_index = right

        vetor[index], vetor[min_index] = vetor[min_index], vetor[index]

if __name__ == '__main__':
    inicioAQ = time.time()
    vetor = []
    with open('10000_numbers.txt', 'r') as arquivo:
        for valor in arquivo:
            vetor.append(int(valor))
    arquivo.close()
    fimAQ = time.time()

    inicio = time.time()
    SelectionSort(vetor)
    fim = time.time()

    tempoDeAquisicao = fimAQ - inicioAQ
    tempoDeOrdenacao = fim - inicio
    print("Tempo total: ", tempoDeAquisicao + tempoDeOrdenacao)
    print("Tempo de aquisição: ", tempoDeAquisicao)
    print("Tempo de ordenação: ", tempoDeOrdenacao)
