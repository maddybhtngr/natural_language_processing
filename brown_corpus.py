import nltk

from nltk.corpus import brown
print(brown.categories())
print(brown.words(categories="adventure")[:20])
