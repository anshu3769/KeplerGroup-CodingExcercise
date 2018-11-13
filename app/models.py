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
import pronouncing

"""
###############################################
RandomWord class
###############################################
"""
class RandomWord:

    @staticmethod
    def serialize(word):
        """ Serializes a word into a dictionary """
        return {"random_word":word}

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
        return {"rhyming_word": word}

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

"""
###############################################
PigLatin class
###############################################
"""
class PigLatin:

    @staticmethod
    def serialize(word):
        """ Serializes a word into a dictionary """
        return {"pig_latin_word":word}

    @staticmethod
    def get_pig_latin_word(word):
        """
        Return the pig-latin translation of the given word

        """
        consonant_combination_list = ['sh', 'gl', 'ch', \
                                      'ph', 'tr', 'br', 'fr', \
                                      'bl', 'gr', 'st', 'sl', \
                                      'cl', 'pl', 'fl']


        if word[0] in ['a', 'e', 'i', 'o', 'u']:
            word = word+'ay'
        elif word[0]+word[1] in consonant_combination_list:
            word = word[2:]+word[:2]+'ay'
        else:
            word = word[1:]+word[0]+'ay'

        return word
