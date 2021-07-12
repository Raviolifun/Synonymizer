
# Internal imports
import random

# External imports
import nltk
from nltk.corpus import wordnet


def download():
    nltk.download('popular')


def synoantonym_file(file_name, excluded_words, synonym):
    # It kept trying to replace it with IT or information technology lol
    similar = synonym

    with open(file_name) as input_file, open(file_name[:-4] + "_output.txt", "w+") as output_file:
        for line in input_file:

            line = line.strip(" \n")
            if not line == "":
                words = line.split()

                for i in range(len(words)):
                    word = words[i]

                    filtered_word = ""
                    special = ".?!\","
                    start_of_word = True
                    start_special = ""
                    end_special = ""
                    for char in word:
                        if char in special:
                            if start_of_word:
                                start_special = start_special + char
                            else:
                                end_special = end_special + char
                        else:
                            filtered_word = filtered_word + char
                            start_of_word = False

                    word = filtered_word

                    if not word.lower() in excluded_words:

                        new_val = ""
                        synonyms = []
                        antonyms = []

                        for syn in wordnet.synsets(word):
                            for l in syn.lemmas():
                                synonyms.append(l.name())
                                if l.antonyms():
                                    antonyms.append(l.antonyms()[0].name())

                        synonyms = set(synonyms)
                        antonyms = set(antonyms)

                        syn_len = len(synonyms)
                        ant_len = len(antonyms)

                        if similar:
                            if syn_len == 0:
                                new_val = word
                            else:
                                new_val = list(synonyms)[random.randint(0, syn_len - 1)]
                        else:
                            if ant_len == 0:
                                new_val = word
                            else:
                                new_val = list(antonyms)[random.randint(0, ant_len - 1)]

                        new_val = new_val.replace("_", " ")
                        new_val = start_special + new_val + end_special

                        words[i] = new_val

                line = " ".join(words)
                output_file.write(line + "\n")

            else:
                output_file.write("\n")
