from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

vect = CountVectorizer(binary = True)
corpus= ["CNN is good optical character recognition","optical character recognition is significant"]
vect.fit(corpus)
print(vect.transform(corpus).toarray())

vect = TfidfVectorizer()
corpus= ["CNN is good optical character recognition","optical character recognition is significant"]
vect.fit(corpus)
print(vect.transform(corpus).toarray())

import pandas as pd
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vect.transform(["Tessaeract is an optical character recognition system","optical character recognition system is significant"]))
print(similarity)