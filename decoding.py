def read_txt_file(file_name):
    with open(file_name, "rb") as f:
        tekst = f.read()
    return tekst

plik = read_txt_file("test_z_zajec.bin")
slownik,kod = plik.split(b'end')

slownik = slownik.decode("utf-8")
dictionary = {}
print(slownik)
for i in slownik.split(" "):
    wartosc,klucz = i.split(":")
    dictionary[klucz] = wartosc

tmp = 0

print(kod)
code=""
for i in kod:
    code = code+bin(i).split("b")[1]

tmp = ""
for i in code:
    tmp = tmp+i
    if tmp in dictionary:
        print(dictionary[tmp],end="")
        tmp = ""




print()
print(dictionary)