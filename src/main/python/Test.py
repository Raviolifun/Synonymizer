# External imports
import nltk
from nltk.corpus import wordnet

nltk.download('popular')

word = 'results'
synonyms = []
antonyms = []

for syn in wordnet.synsets(word):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))