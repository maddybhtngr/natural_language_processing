from nltk.tokenize import TweetTokenizer
text = 'Dude! The party was so lit brooo, omg :D #funtimes'
twtkn = TweetTokenizer()
print(twtkn.tokenize(text))
