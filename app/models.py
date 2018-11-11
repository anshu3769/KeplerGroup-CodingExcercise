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
        number_of_words = len(words)

        #Generate a random number in range 0 to number_of_words-1
        word_index = random.randint(0,number_of_words-1)
        return words[word_index]


"""
#################################################
Rhyme class
#################################################
"""
class Rhyme:

    @staticmethod
    def serialize(word):
        """ Serializes a word into a dictionary """
        return {"word": word}

    @staticmethod
    def get_rhyming_words(word):
        """ Get the list of words rhyming with given word """

        #The pronouncing package provides the functionality to get
        #rhyming words from the CMU Pronouncing Dictionary for a given
        #word.
        word_list = pronouncing.rhymes(word)
        return word_list

    """
    @staticmethod
    def get_rhyming_words(word):
       
        #This method calls an API which also returns the list 
        #of rhyming words. One drawback of this method is 
        #that sometimes API call could fail.
        
        word_list = []
        URL = "https://api.datamuse.com/words?rel_rhy=" + word
        response = requests.get(url = URL)
        data = response.json()
        for rhyming_word  in data:
            word_list.append(rhyming_word['word'])
        return word_list
    """
