def heapify(arr, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] < arr[smallest]:
        smallest = l
    if r < n and arr[r] < arr[smallest]:
        smallest = r
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)


def heapify_node(arr, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l].freq < arr[smallest].freq:
        smallest = l
    if r < n and arr[r].freq < arr[smallest].freq:
        smallest = r
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify_node(arr, n, smallest)


def build_heap(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify_node(arr, n, i)