def read_txt_file(file_name):
    with open(file_name, "r") as f:
        tekst = f.read()
    return tekst


def save_to_bin(tekst, file):
    with open(file, "wb") as f:
        f.write(tekst)


def _to_Bytes(data):
    b = bytearray()
    for i in range(0, len(data), 8):
        b.append(int(data[i:i + 8], 2))
    return bytes(b)
