from nltk.stem import PorterStemmer
stemmerporter = PorterStemmer()
#works for

print('Porter Stemmer')
print("Works for")
print(stemmerporter.stem('Working'))
print(stemmerporter.stem('singing'))
print(stemmerporter.stem('truthfulness'))
print(stemmerporter.stem('napping'))
print(stemmerporter.stem('dying'))
print(stemmerporter.stem("beforehand"))

print("--------------------------------------------")

print("Doesn't Work for")
#does not work for
print(stemmerporter.stem('Happiness'))
print(stemmerporter.stem('gratitude'))
print(stemmerporter.stem('gratituous'))
print(stemmerporter.stem('swinger'))
print(stemmerporter.stem('Dying'))
print(stemmerporter.stem("restaurant"))


print("====================================")
print("====================================")


print("Lancaster Stemmer")

from nltk.stem import LancasterStemmer
stemmerLan = LancasterStemmer()
print("Works with")
print(stemmerLan.stem('working'))
print(stemmerLan.stem('Happiness'))
print(stemmerLan.stem('swinger'))
print(stemmerLan.stem('Dying'))
print(stemmerLan.stem('Truthfulness'))
print(stemmerLan.stem("singing"))
print(stemmerLan.stem("apple"))
print(stemmerLan.stem("applause"))
print(stemmerLan.stem("tries"))


print("--------------------------------------------")


print("Doesn't work with")
print(stemmerLan.stem('gratitude'))
print(stemmerLan.stem('gratituous'))
print(stemmerLan.stem("restaurant"))
print(stemmerLan.stem("restaurant"))
print(stemmerLan.stem("enter"))
print(stemmerLan.stem("pacman"))




from nltk.stem import RegexpStemmer
stemmerRgx = RegexpStemmer('ing')
print(stemmerRgx.stem("working"))
print(stemmerRgx.stem("sing"))
print(stemmerRgx.stem("singing"))

from nltk.stem import SnowballStemmer
stemmerSnow = SnowballStemmer('french')
print(stemmerSnow.stem("manger"))