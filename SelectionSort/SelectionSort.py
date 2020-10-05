def SelectionSort(vetor):

    for index in range(0, len(vetor)):
        min_index = index

        for right in range(index + 1, len(vetor)):
            if vetor[right] < vetor[min_index]:
                min_index = right

        vetor[index], vetor[min_index] = vetor[min_index], vetor[index]

if __name__ == '__main__':
    vetor = []
    with open('1000_numbers.txt', 'r') as arquivo:
        for valor in arquivo:
            vetor.append(int(valor))
    arquivo.close()
    print("Vetor antes", vetor)
    SelectionSort(vetor)
    print("Vetor depois", vetor)