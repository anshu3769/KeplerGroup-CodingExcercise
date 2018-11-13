"""
Kepler Group Coding Excercise

Paths:
-----
GET /words/random?input=<comma sepearted list of words>  - Takes list of words and returns a random word out of them
GET /words/rhyming/{word} - Takes a word and return list of words rhyming with the given word
GET /words/pig-latin/{word} - Takes a word and returns its pig-latin translation
-----
"""

import os
import sys
import logging
from flask import Response, jsonify, request, json, url_for, make_response,abort
from flask_api import status
from werkzeug.exceptions import BadRequest, NotFound, UnsupportedMediaType, InternalServerError # Exception Class

from . import app
from app.models import RandomWord, Rhyme, PigLatin

"""
######################################################################
# Error Handlers
######################################################################
"""

@app.errorhandler(400)
def bad_request(error):
    """ Handles bad requests with 400_BAD_REQUEST """
    #error = 'Required parameters not found.'
    #message = 'Please specify the input/at least two words in the input.'
    message = str(error)
    #more_info='Use something like /words/random?input=word1,word2,word3.'
    app.logger.info(error)
    return jsonify(status=400,\
                   error='Bad Request',\
                   message=message), 400


@app.errorhandler(404)
def not_found(error):
    """ Handles resources not found with 404_NOT_FOUND """
    message = str(error)
    app.logger.info(message)
    return jsonify(status=404,\
                   error='Not Found', \
                    message=message), 404



@app.errorhandler(500)
def internal_server_error(error):
    """ Handles unexpected server error with 500_SERVER_ERROR """
    message = str(error)
    app.logger.info(message)
    return jsonify(status=500,\
                   error='Internal Server Error',\
                    message=message), 500



"""
#####################################################################
GET INDEX PAGE
#####################################################################
"""
@app.route('/',methods=['GET'])
@app.route('/words',methods=['GET'])
def index():
    """ Root URL response """
    app.logger.info("WORDS REST API SERVICE")
    return jsonify(name='Words REST API Service',\
                   version='1.0',\
                   info="Home page for the API"
                  ), status.HTTP_200_OK

"""
######################################################################
# GET RANDOM WORD
######################################################################
"""
@app.route('/words/random', methods=['GET'])
def get_random_word():
    """
    This endpoint will return a word randomly selected from the
    given list of words in the query

    """
    app.logger.info("Processing random word request.")

    #Split the input list into words
    if 'input' in request.args:
        words = request.args['input'].split(",")
    else:      # Abort the request with error messgae  if the 'input' is not provided
        abort(400,'Input not provided')

    # Abort the request with error message if the number of words is less that two
    # greater than 20
    if words is None or len(words) < 2 or len(words) > 20:
        abort(400,'Length of the list is either less than 2 or greater than 20')

    # Abort the request if length of any word is greater than 45.
    #Longest word in Oxford dictionary is of length 45.
    if not valid_length_of_words(words):
        abort(400,'Length of one or more words is greater than 45')

    #Call the method from the RandomWord class to get the random word
    word = RandomWord.get_random_word(words)
    return make_response(jsonify(RandomWord.serialize(word)), status.HTTP_200_OK)




"""
######################################################################
# GET RHYMING WORDS LIST
######################################################################
"""
@app.route('/words/rhyming/<string:word>', methods=['GET'])
def get_rhyming_words(word='Kepler'):
    """
    This endpoint will return list of words rhyming with the given
    words as parameter. It will skip the words after the first comma
    if a comma separated list is provided and will return the list of
    words rhyming with the first word.

    """
    app.logger.info("Processing rhyming words request.")

    #Get the first word if a comma seperated list is provided
    input = word.split(",")[0]

    #Abort if the the word is not a valid English word
    if valid_english_word(input) is False:
        abort(400,'The word is not a valid english word')

    #Call the method from the Rhyme class to get the rhyming words list
    rhyming_words = Rhyme.get_rhyming_words(input)
    return make_response(jsonify(rhyming_words), status.HTTP_200_OK)


"""
######################################################################
# GET PIG-LATIN WORD
######################################################################
"""
@app.route('/words/pig-latin/<string:word>', methods=['GET'])
def get_pig_latin_word(word='Kepler'):
    """
    This endpoint will return pig-latin translation of the given word.
    """
    app.logger.info("Processing pig-latin word request.")

    #Get the first word if a comma seperated list is provided
    input = word.split(",")[0]

    #Abort if the the word is not a valid English word
    if valid_english_word(input) is False:
        abort(400,'The word is not a valid english word')

    #Call the method from the Rhyme class to get the rhyming words list
    pig_latin_word = PigLatin.get_pig_latin_word(input)
    return make_response(jsonify(pig_latin_word), status.HTTP_200_OK)



"""
######################################################################
# RHYMING WORDS LIST INDEX
######################################################################
"""
@app.route('/words/rhyming/', methods=['GET'])
def get_rhyming_words_empty():
    """
    This endpoint will return a response asking the user to provide
    input word.

    """
    app.logger.info("Rhyming words index.")

    return jsonify(name='Index page for Rhyming words list',\
                   message='Please provide the word whose rhyming words you want',\
                   more_info='Use something like /words/random/cat'), 200



"""
######################################################################
# Utility functions
######################################################################
"""

def initialize_logging(log_level=logging.INFO):
    """ Initialized the default logging to STDOUT """
    if not app.debug:
        print('Setting up logging...')

        # Set up default logging for submodules to use STDOUT
        fmt = '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
        logging.basicConfig(stream=sys.stdout, level=log_level, format=fmt)

        # Make a new log handler that uses STDOUT
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(logging.Formatter(fmt))
        handler.setLevel(log_level)

        # Remove the Flask default handlers and use our own
        handler_list = list(app.logger.handlers)
        for log_handler in handler_list:
            app.logger.removeHandler(log_handler)

        app.logger.addHandler(handler)
        app.logger.setLevel(log_level)
        app.logger.info('Logging handler established.')


def valid_length_of_words(word_list = []):
    """Validate if the words in the list have valid lengths"""
    for w in word_list:
        if len(w) > 45:
            return False;
    # In all other cases, the function returns true
    return True


def valid_english_word(word):
    """Validate if the word is a English word.
    The check is on the characters of the word.
    It must contain just alphabets from a-z or A-Z
    and nothing else.
    """
    return word.isalpha()
