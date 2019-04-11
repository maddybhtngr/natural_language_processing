from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

vect = CountVectorizer(binary = True)
corpus= ["""in February, the month of love as endowed by our great gifting industrial complex. 
we are wrestling with what 'love for travel' means in tangible, life affecting terms. 
The early throes of discovering travel might not be too dissimilar to the beginnings of a feverish affair A fleeting 
scene. sound or feeling that at first arouses, then enchants and eventually. lures us into a hypnotic state. 
evoking woolly-eyed reveries about what could be. This world. however. is not the most conducive for long-term 
passion, the kind that demands unflinching sustenance in the midst of distractions from a thousand notifications, 
Passion has many rivals to contend with. And in flippantly announcing travel as our first love, we are not fully 
considering the influence our other paramours (work, relationships or money) exert on us, Travellers for life are 
compulsive.","rekindles his passion for the German thinker while tracing picturesque hiking trails in the mountains 
of Switzerland it's a near-precise rendering of the lrmeicgue as a self-help book A young Kaag was an avowed Nietzsche 
acolyte but given the ravages of responsibilities and adulthood the witer put his affinity to test by undertaking 
physically enduring hikesthrough the alps, revisiting haunts that the philosopher escaped to in search of solitude 
and salve The journey's demands. Coupled with his own inner turmoil, are catnip for anybody feeling at cross purposes 
with their own life"""]
corp=vect.fit(corpus)
print(vect.transform(corpus).toarray())

print()

vect1 = TfidfVectorizer()
corpus= ["""in February, the month of love as endowed by our great gifting industrial complex. 
we are wrestling with what 'love for travel' means in tangible, life affecting terms. The early 
throes of discovering travel might not be too dissimilar to the beginnings of a feverish affair 
A fleeting scene. sound or feeling that at first arouses, then enchants and eventually. lures us 
into a hypnotic state. evoking woolly-eyed reveries about what could be. This world. however. is
 not the most conducive for long-term passion, the kind that demands unflinching sustenance in 
 the midst of distractions from a thousand notifications, Passion has many rivals to contend with. 
 And in flippantly announcing travel as our first love, we are not fully considering the influence 
 our other paramours (work, relationships or money) exert on us, Travellers for life are compulsive.
 ""","""rekindles his passion for the German thinker while tracing picturesque hiking trails in the 
 mountains of Switzerland it's a near-precise rendering of the lrmeicgue as a self-help book A young 
 Kaag was an avowed Nietzsche acolyte but given the ravages of responsibilities and adulthood the witer
  put his affinity to test by undertaking physically enduring hikesthrough the alps, revisiting haunts 
  that the philosopher escaped to in search of solitude and salve The journey's demands. Coupled with his 
  own inner turmoil, are catnip for anybody feeling at cross purposes with their own life"""]
vect1.fit(corpus)
print(vect1.transform(corpus).toarray())

print()

import pandas as pd
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vect.transform(corpus))
print(similarity)

print()

from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vect1.transform(corpus))
print(abs(similarity))