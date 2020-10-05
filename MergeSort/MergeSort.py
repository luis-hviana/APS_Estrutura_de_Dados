def mergeSort(vetor):
    if len(vetor)>1:
        mid = len(vetor)//2
        lefthalf = vetor[:mid]
        righthalf = vetor[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                vetor[k]=lefthalf[i]
                i=i+1
            else:
                vetor[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            vetor[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            vetor[k]=righthalf[j]
            j=j+1
            k=k+1

if __name__ == '__main__':
    vetor = []
    with open('10000_numbers.txt', 'r') as arquivo:
        for valor in arquivo:
            vetor.append(int(valor))
    arquivo.close()
    print("Vetor antes", vetor)
    mergeSort(vetor)
    print("Vetor depois", vetor)
