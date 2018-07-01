import zlib


def decompress(file):
    out_file = open (file + '.txt', "rb")
    decompressed = zlib.decompress(out_file.read())

    dec_file = open (file + '.jpg', "wb")
    dec_file.write(decompressed)
