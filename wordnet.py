from nltk.corpus import wordnet

print(wordnet.synsets('motorcar'))
print(wordnet.synset('car.n.01').lemma_names())