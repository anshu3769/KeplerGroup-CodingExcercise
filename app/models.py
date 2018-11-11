"""
Kepler Group Coding Excercise


--------------------------
Model class for Words API
--------------------------

This file contains two classes namely
1. RandomWord - which contains method for generating a random
word given a list of words
2. Rhyme - which contains method for generating rhyming words
for a given  word.

In future, if there occurs any requiement to add database to
the service, the corresponding models could be added in this file

"""

import os
import json
import random
import requests

"""
###############################################
RandomWord class
###############################################
"""
class RandomWord:

    @staticmethod
    def serialize(word):
        """ Serializes a word into a dictionary """
        return {"randomWord":word}

    @staticmethod
    def get_random_word(words):
        """
        Select a word randomly from the given list of words
        and return it

        """
        #Calculate the length of the list
        string_length = len(words)

        #Generate a random number in range 0 to string_length-1
        word_index = random.randint(0,string_length-1)
        return words[word_index]


"""
#######################
Rhyme class
#######################
"""
class Rhyme:

    @staticmethod
    def serialize(word):
        """ Serializes a word into a dictionary """
        return {"word": word}

    @staticmethod
    def get_rhyming_words(word):
        """ Get the list of words rhyming with given word """

        #The pronouncing package provides the functionality to rhyming
        #words from the CMU Pronouncing Dictionary
        word_list = pronouncing.rhymes(word)
        return word_list

    """
    @staticmethod
    def get_rhyming_words(word):
        #Get the list of words rhyming with given word
        word_list = []
        URL = "https://api.datamuse.com/words?rel_rhy=" + word
        response = requests.get(url = URL)
        data = response.json()
        for rhyming_word  in data:
            word_list.append(rhyming_word['word'])
        return word_list
    """
