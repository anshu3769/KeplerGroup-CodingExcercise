"""
Kepler Group Coding Excercise

Paths:
-----


GET /words/randomword?input=space-seperated-words  - Takes list of words and returns a random word out of them 
GET /words/rhymingwords/{word} = one - Takes a word and return list of words rhyming with the given word


import os
import sys
import logging
from flask import Response, jsonify, request, json, url_for, make_response
from flask_api import status
from werkzeug.exceptions import BadRequest, NotFound, UnsupportedMediaType, InternalServerError # Exception Class

from . import app
from models import RandomWord, Rhyme, DataValidationError



""""

######################################################################
# GET RANDOM WORD
######################################################################
@app.route('/words/randomword', methods=['GET'])
def get_random_word():
    """
    This endpoint will return a word randomly selected from the given list of 
    words as parameter

    """
    words = request.args['input'].split(" ")
    if words is None or len(words) < 2:
        return make_response('', status.HTTP_400_BAD_REQUEST)

    word = RandomWord.get_random_word(words)
    return make_response(jsonify(word.serialize()), status.HTTP_200_OK)



######################################################################
# GET RHYMING WORDS LIST
######################################################################
@app.route('/words/rhymingwords/<string:word>', methods=['GET'])
def get_rhyming_words(word):
    """
    This endpoint will return list of words rhyming with the given 
    words as parameter. It will skip the words after the first space
    if more than one word is given as input. 
    
    """
    input = word.split(" ")[0]
    rhyming_words = Rhyme.get_rhyming_words(input)
    result = [rhyming_word.serialize() for rhyming_word in  rhyming_words]
    return make_response(jsonify(result), status.HTTP_200_OK)


