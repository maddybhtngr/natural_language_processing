from nltk.corpus import inaugural
for i in inaugural.fileids():
    print(i)
print(inaugural.words(fileids="2009-Obama.txt")[:100])