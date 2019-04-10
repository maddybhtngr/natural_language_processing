entries = nltk.corpus.cmudict.entries()
print(len(entries))

for entry in entries[10000:10025]:
    print(entry)