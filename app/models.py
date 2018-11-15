""" Kepler Group Coding Excercise


--------------------------
Model class for Words API
--------------------------

This file contains three classes - 
1. RandomWord - It contains method for generating a random
word from the given list of words
2. Rhyme - It contains method for generating rhyming words
for a given word.
3. PigLatin - It contains method for translating a word
to its pig-latin form.

In future, if persistence is required to be added to the model
,use this file to do the same.
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
    """RandomWord class contains two methods.

    1. serialize - Serialize a word into a dictionary
    2. get_random_word - Returns a word randomly from the given 
    list of words.
    """

    @staticmethod
    def serialize(word):
        """ Serialize a word into a dictionary

        input/argument - An english word
	return value - A dictionary with key/value pair for the word
        """
        return {"random_word":word}

    @staticmethod
    def get_random_word(words):
        """Get a word randomly from the given list of words

        input/argument - List of words
        return value - Word chosen randomly from the given list
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
    """ Rhyme class contains two methods -
 
    1. serialize - Serialize a word into a dictionary

    2. get_rhyming_word - Get the list of words rhyming
    with the given word. The methods makes use of Pronouncing 
    package  provided by python community to get the rhyming 
    words for a word. 
    """
    
    @staticmethod
    def serialize(word):
        """ Serialize a word into a dictionary

        input/argument - An english word
        return value - A dictionary with key/value pair for the word
        """
        return {"rhyming_word": word}

    @staticmethod
    def get_rhyming_words(word):
        """ Get the list of words rhyming with given word
 
        input/argument - An english word
        return value - List of words rhyming with the given word
        
        NOTE - The "pronouncing" package provides the functionality to
        get rhyming words from the CMU Pronouncing Dictionary for a given
        word.      
        """

        """The pronouncing package provides the functionality to get
        rhyming words from the CMU Pronouncing Dictionary for a given
        word."""
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
    """PigLatin class contains two method - 

    1. serialize - Serialize a word into a dictionary
    2. get_pig_latin_word - Get the pig-latin translation 
    of a given word.
    """
    @staticmethod
    def serialize(word):
        """ Serialize a word into a dictionary

        input/argument - An english word
        return value - A dictionary with key/value pair for the word
        """
        return {"pig_latin_word":word}

    @staticmethod
    def get_pig_latin_word(word):
        """Get the pig-latin translation of the given word

	input/argument - An english word
        return value - pig-latin transaltion of the input word

	NOTE - Pig Latin is a language used by English-speaking people, 
        especially when they want to disguise something they are saying 
        from non-Pig Latin speakers. Pig latin translation works in unique 
        way. There are some rules to convert a word into its pig-latin form.

	1. If the word starts with a vowel, add an 'ay' at the end.
        For example, 'owl' will become 'owlay' after translation.

	2. If the word starts with sh'|'gl'|'ch'|'ph'|'tr'|'br'| 
       'fr'|'bl'|'gr'|'st'|'sl'|'cl'|'pl'|'fl , remove it from the 
        begining and put at the end. Then add 'ay' at the end.
	For example, 'check' will become 'eckchay'.
	
	3. In all other cases, the first  character will be removed 
        from the begining and will be put at the end. The word will be
        appended by 'ay' after that.
        For example, 'who' will become 'howay'
        """
        #To check the words that start with this combination
        #of their first two characters
        consonant_combination_list = ['sh', 'gl', 'ch', \
                                      'ph', 'tr', 'br', 'fr', \
                                      'bl', 'gr', 'st', 'sl', \
                                      'cl', 'pl', 'fl']

 
	#Translate the word based on the rules of translation
        if word[0] in ['a', 'e', 'i', 'o', 'u']:
            word = word+'ay'
        elif word[0]+word[1] in consonant_combination_list:
            word = word[2:]+word[:2]+'ay'
        else:
            word = word[1:]+word[0]+'ay'

        return word
