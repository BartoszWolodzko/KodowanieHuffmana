from random import randint

with open("tekst_genertaor.txt", "a") as f:
    for i in range(0, 1000000):
        f.write(chr(randint(40, 80)))
