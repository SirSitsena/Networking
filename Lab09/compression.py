from math import log2
import random
import zlib


def makeHisto(byteArr):
    histo = []
    for i in range(0, 255):
        c = 0.0
        for j in byteArr:
            if i == j:
                c += 1.
        histo.append(c)
    return histo


def makeProb(histo):
    sum = 0.0
    for i in histo:
        sum += i
    for i in range(len(histo)):
        histo[i] = histo[i] / sum
    return histo


def entropi(prob):
    sum = 0.0
    for p in prob:
        if p != 0:
            sum += p * log2(1./p)
    return sum

# utf-8
with open('exempeltext.txt') as file:

    # -----------------------------------TEXT-START
    print("")
    print("------------The Text")
    print("")
    txt = file.read(-1)
    byteArr = bytearray(txt, "utf-8")
    print("The text has: " + str(len(txt)) + " symbols")
    print("The text is: " + str(len(byteArr)) + " bytes long")
    print("The Texts Entropy is: " + str(entropi(makeProb(makeHisto(byteArr)))) + " bit/symbol")
    # -----------------------------------TEXT-END

    # -----------------------------------COPY - START
    print("")
    print("------------The Copy")
    print("")
    theCopy = byteArr.copy()
    random.shuffle(theCopy)

    print("The Copy's Entropy is: " + str(entropi(makeProb(makeHisto(theCopy)))))

    #--------------------------------Zip Algorithm
    zippedShuffledCode = zlib.compress(theCopy)
    print("The zipped Copy has: " + str(len(zippedShuffledCode)) + " bytes")
    print("The zipped Copy has: " + str(8*len(zippedShuffledCode)) + " bits")
    print("The zipped Copy's Entropy is: " + str(entropi(makeProb(makeHisto(zippedShuffledCode)))) + " bit/symbol")
    print("The zip algo compressed the data to: " + str(100-len(zippedShuffledCode)/len(byteArr)*100) + " % from origin(TEXT)")
    print("The zip algo compressed the data to: " + str(len(zippedShuffledCode)/len(byteArr)*8) + " more bit\symbol")
    #--------------------------------End Zip Algorithm

    # -----------------------------------COPY - END

    # -----------------------------------Unshuffled byteArr - START
    print("")
    print("------------byteARR ZIP")
    print("")
    zipbyteArr = zlib.compress(byteArr)
    print("The zipped Unshuffled byteArr has: " + str(len(zipbyteArr)) + "bytes")
    print("The zipped Unshuffled byteArr's Entropy is: " + str(entropi(makeProb(makeHisto(zipbyteArr)))) + " bit/symbol")
    print("The zip algo compressed the data to: " + str(100-len(zipbyteArr)/len(byteArr)*100) + " % from origin(TEXT)")
    print("The zip algo compressed the data to: " + str(len(zipbyteArr)/len(byteArr)*8) + " more bit\symbol")
    # -----------------------------------Unshuffled byteArr - END


    # --------------------------------Repetitive text
    print("")
    print("----------------------------Repetitive text")
    print("")
    t1 = """I hope this lab never ends because
    it is so incredibly thrilling!"""
    print("The t1 has: " + str(len(t1)) + " symbols")
    bytePrint = bytearray(t1, "utf-8")
    print("The t1 is: " + str(len(bytePrint)) + " bytes long")
    t1Zip = zlib.compress(bytePrint)
    print("The zipped t1 has: " + str(len(t1Zip)) + " bytes")
    print("The zipped t1's Entropy is: " + str(entropi(makeProb(makeHisto(t1Zip)))) + " bit/symbol")
    print("The zip algo compressed the data to: " + str(100-len(t1Zip)/len(bytePrint)*100) + " % from origin(t1)")

    print("")
    t10 = 10 * t1
    print("The t10 has: " + str(len(t10)) + " symbols")
    print("The t10 has: " + str(len(bytearray(t10, "utf-8"))) + " bytes")
    t10Zip = zlib.compress(bytearray(t10, "utf-8"))
    print("The zipped t10 has: " + str(len(t10Zip)) + " bytes")
    print("The zipped t10's Entropy is: " + str(entropi(makeProb(makeHisto(t10Zip)))) + " bit/symbol")
    print("The zip algo compressed the data to: " + str(100-len(t10Zip)/len(bytearray(t10, "utf-8"))*100) + " % from origin(t1)")
    # --------------------------------End Repetitive text

# 9.2 - 1.c
# 	The string contains 29091 symbols and the bytearray has 30491 bytes. This has to do with how the UTF-8 interprets the Swedish “ÅÄÖ”. The “ÅÄÖ” in UTF-8 take 2 bytes each instead of 1 byte.

# 9.2 - 2.d
# 	Using an optimal encoding we can not achieve a better compression with an entropy with less than 4.6285 bit/symbol without exploiting the statistical redundancy.

# 9.2 - 4.e
# The data source’s entropy is the smallest one.
# The zlib-encoding of theCopy has the highest entropy.
# The compressed data in the zip requires less bits to store the same data like the data source, which leads to a higher entropy (bit/symbol) plus the compressed data is shuffled randomly which increases the entropy when compressed.

# 9.2 - 5.b
# The first string got compressed down to 70(69 before?????) bytes.
# The second string got compressed down to 79 bytes.

# 9.2 - 5.c
# The zip algorithm searches for patterns in the text before compressing it which allows it to effectively compress the data without the need to store repeated stuff.

