from nltk.corpus import names

def gender_features(word):
    return {'last Letter':word[-1]}

label = ([(name,'male') for name in names.words('male.txt')]+
         [(name,'female') for name in names.words('female.txt')])

import random
random.shuffle(label)

featureSet = [(gender_features(n),gender) for (n,gender) in label]

train,test = featureSet[500:],featureSet[:500]

import nltk
classifier = nltk.NaiveBayesClassifier.train(train)
print(classifier.classify(gender_features('willy')))
print(nltk.classify.accuracy(classifier,test))