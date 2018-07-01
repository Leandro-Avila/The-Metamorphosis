import zlib


def compress(file):
    in_file = open (file + '.jpg', "rb")
    compressed = zlib.compress(in_file.read())

    out_file = open (file + '.txt', "wb")
    out_file.write(compressed)

