from heap import build_heap
from readAndSaveFromFile import read_txt_file, save_to_bin, _to_Bytes


class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''


def printNodes(slownik_do_szyfrowania, node, val=''):
    newVal = val + str(node.huff)

    if node.left:
        printNodes(slownik_do_szyfrowania, node.left, newVal)
    if node.right:
        printNodes(slownik_do_szyfrowania, node.right, newVal)

    if not node.left and not node.right:
        slownik_do_szyfrowania[node.symbol] = newVal


def print_tree(node):
    if node.left:
        print_tree(node.left)
    if node.right:
        print_tree(node.right)
    print(f"{node.symbol} -> {node.huff}")


def compres_tekst(slownik_do_szyfrowania, tekst):
    code = ""
    for x in range(0, len(tekst)):
        code = code + slownik_do_szyfrowania[tekst[x]]
        print(str(x / len(tekst) * 100) + "%")
    return code


def frequency_map(data):
    freq = {}
    for char in data:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


def kompresjaHuffmana(plik_do_kompresji, plik_wynikowy):
    tekst = read_txt_file(plik_do_kompresji)

    nodes = []
    czestotliwosc_liter = frequency_map(tekst)
    for x in czestotliwosc_liter:
        nodes.append(node(czestotliwosc_liter[x], x))

    while len(nodes) > 1:
        build_heap(nodes)
        left = nodes.pop(0)
        build_heap(nodes)
        right = nodes.pop(0)
        left.huff = 0
        right.huff = 1
        newNode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        nodes.append(newNode)

    slownik_do_szyfrowania = {}
    printNodes(slownik_do_szyfrowania, nodes[0])
    # print_tree(nodes[0])

    code = compres_tekst(slownik_do_szyfrowania, tekst)

    wynik = str(slownik_do_szyfrowania)
    wynik = wynik.replace("'", "")
    wynik = wynik.replace(": ", ":")
    wynik = wynik.replace(",", "")
    slownik_binarnie = ''.join(format(ord(i), '08b') for i in wynik)

    print(_to_Bytes(slownik_binarnie + "\n" + code))
    save_to_bin(_to_Bytes(slownik_binarnie + "\n" + code), plik_wynikowy)


plik_do_kompresji = "test1.txt"
plik_wynikowy = "wynik.bin"
kompresjaHuffmana(plik_do_kompresji, plik_wynikowy)
print("done")
