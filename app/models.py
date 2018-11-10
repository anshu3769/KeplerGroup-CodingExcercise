"""
Model for Kepler Group Coding Excercise 

In future, if any model needs to be added to the application,
it can be added in this file.
Currently, it contains two classes namely
1. RandomWord - which contains method for generating a random 
word given a list of words
2. Rhyme - which contains method for generating rhyming words
for a given  word
"""

import os
import json
import random
import requests


#######################
RandomWord class
#######################
class RandomWord:

    @staticmethod
    def serialize(word):
        """ Serializes a word into a dictionary """
        return {"randomWord":word}

    @staticmethod
    def get_random_word(words):
        """ Select a word randomly from the given list of words and return it """
        string_length = len(words)
        word_index = random.randint(0,string_length)
        return words[word_index]



#######################
Rhyme class
#######################
class Rhyme:
   
    @staticmethod
    def serialize(word):
        """ Serializes a word into a dictionary """
        return {"word": word}

    @staticmethod
    def get_rhyming_words(word):
        """ Get the list of words rhyming with given word """
        word_list = []
        url = "https://api.datamuse.com/words?rel_rhy=" + word
        response = requests.get(url = URL)
        data = response.json()
        for rhyming_word  in data:
            word_list.append(rhyming_word['word'])
         return word_list
