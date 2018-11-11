"""
Kepler Group Coding Excercise

Paths:
-----
GET /words/randomword?input=<comma sepearted list of words>  - Takes list of words and returns a random word out of them
GET /words/rhymingwords/{word} - Takes a word and return list of words rhyming with the given word
-----
"""

import os
import sys
import logging
from flask import Response, jsonify, request, json, url_for, make_response
from flask_api import status
from werkzeug.exceptions import BadRequest, NotFound, UnsupportedMediaType, InternalServerError # Exception Class

from . import app
from app.models import RandomWord, Rhyme


"""
#####################################################################
GET INDEX PAGE
#####################################################################
"""
@app.route('/',methods=['GET'])
def index():
    """ Root URL response """
    print("WORDS REST API SERVICE")
    return jsonify(name='Words REST API Service',
                   version='1.0'
                  ), status.HTTP_200_OK

"""
######################################################################
# GET RANDOM WORD
######################################################################
"""
@app.route('/words/randomword', methods=['GET'])
def get_random_word():
    """
    This endpoint will return a word randomly selected from the 
    given list of words in the query

    """
    print("GET_RANDOM_WORD")

    #Split the input list into words
    if 'input' in request.args:
        words = request.args['input'].split(",")
    else:      # Return detailed error message if the 'input' is not provided
        return jsonify(status=404,error='Required parameters not found.',\
                        message='Please specify the input',\
                        more_info='Use something like /words/randomword?input=word1,word2,word3'), 404

    # Return detailed error message if the number of words is less that two
    if words is None or len(words) < 2:
        return jsonify(status=404,error='Required number of parameters not found.',\
                        message='Please input atleast two or more words',\
                        more_info='Use something like /words/randomword?input=word1,word2,word3'), 404

    #Call the method from the RandomWord class to get the random word
    word = RandomWord.get_random_word(words)
    return make_response(jsonify(RandomWord.serialize(word)), status.HTTP_200_OK)




"""
######################################################################
# GET RHYMING WORDS LIST
######################################################################
"""
@app.route('/words/rhymingwords/<string:word>', methods=['GET'])
def get_rhyming_words(word='Kepler'):
    """
    This endpoint will return list of words rhyming with the given
    words as parameter. It will skip the words after the first comma
    if a comma separated list is provided and will return the list of
    words rhyming with the first word.

    """
    print("GET_RHYMING_WORDS")

    #Get the first word if a comma seperated list is provided
    input = word.split(",")[0]

    #Call the method from the Rhyme class to get the rhyming words list
    rhyming_words = Rhyme.get_rhyming_words(input)
    return make_response(jsonify(rhyming_words), status.HTTP_200_OK)


"""
######################################################################
# RHYMING WORDS LIST ROUTE INDEX
######################################################################
"""
@app.route('/words/rhymingwords/', methods=['GET'])
def get_rhyming_words_empty():
    """
    This endpoint will return a response asking the user to provide
    input word.

    """
    print("GET_RHYMING_WORDS_EMPTY")

    return jsonify(status=404,error='Input parameter is missing.',\
                    message='Please provide the word whose rhyming words you want',\
                    more_info='Use something like /words/randomword/cat'), 404
