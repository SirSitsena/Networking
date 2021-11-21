from math import log2
import random
import zlib


def makeHisto(byteArr):
    histo = []
    for i in range(0, 255):
        c = 0
        for j in byteArr:
            if i == j:
                c += 1
        histo.append(c)
    return histo


def makeProb(histo):
    sum = 0
    for i in histo:
        sum += i
    for i in range(len(histo)):
        histo[i] = histo[i] / sum
    return histo


def entropi(prob):
    sum = 0
    for p in prob:
        if p != 0:
            sum += p * log2(1./p)
    return sum


with open('exempeltext.txt') as file:
    txt = file.read(-1)
    byteArr = bytearray(txt, "utf-8")
    print(len(txt))  # 29091 symbols
    print(len(byteArr))  # 30491 bytes

    print(entropi(makeProb(makeHisto(byteArr))))

    theCopy = byteArr.copy()
    print(theCopy)
    random.shuffle(theCopy)

    print(entropi(makeProb(makeHisto(theCopy))))

    #--------------------------------Zip Algorithm
    print("----------------------------ZIP THE COPY")
    code = zlib.compress(theCopy)
    print(len(code))  # ~19926 bytes    -------->    # ~19926*8 = 159408 bit
    print(entropi(makeProb(makeHisto(code))))   # ~7.981177235034273 bit/symbol
    #--------------------------------End Zip Algorithm

    # --------------------------------Unshuffled byteArr
    print("----------------------------byteARR ZIP")
    zipbyteArr = zlib.compress(byteArr)
    print(len(zipbyteArr))
    print(entropi(makeProb(makeHisto(zipbyteArr))))
    # --------------------------------End Unshuffled byteArr

    # --------------------------------Repetitive text
    print("----------------------------Repetitive text")
    t1 = """I hope this lab never ends because
    it is so incredibly thrilling!"""
    print(len(t1))
    t1Zip = zlib.compress(bytearray(t1, "utf-8"))
    print(len(t1))
    print(entropi(makeProb(makeHisto(t1Zip))))

    t10 = 10 * t1
    print(len(t10))
    t10Zip = zlib.compress(bytearray(t10, "utf-8"))
    print(len(t10Zip))
    print(entropi(makeProb(makeHisto(t10Zip))))
    # --------------------------------End Repetitive text