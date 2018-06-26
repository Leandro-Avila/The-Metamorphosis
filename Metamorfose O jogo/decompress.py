import zlib


def decompress(file):

    with open(file + '.txt', "rb") as out_file:
        decompressed = zlib.decompress(out_file.read())

    with open(file + '.jpg', "wb") as dec_file:
        dec_file.write(decompressed)
