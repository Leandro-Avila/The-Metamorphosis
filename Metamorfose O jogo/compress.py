import zlib


def compress(file):

    with open(file + '.jpg', "rb") as in_file:
        compressed = zlib.compress(in_file.read())

    with open(file + '.txt', "wb") as out_file:
        out_file.write(compressed)

compress('imagens/sala')
