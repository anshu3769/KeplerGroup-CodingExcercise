#  Code documentation 
  This document was created using python docstring. Below are the details when help command is 
  run on the modules of the project. 
  
  
## 1. run.py
   ## Description
    Application starts running from this module.
    It also initializes logging for the application.  
    As a user, you will be running "python3 run.py"
    to start the application.
    
## 2. app

   ## Description
    Package: app
    Package for the application models and services.
    It contains the definition of the "words" flask API.

   ## Package Contents
    models
    service

    
## 3. app/models.py
   ## Description
    
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

   ## Classes
        PigLatin
        RandomWord
        Rhyme
    
   ## class PigLatin(builtins.object)
     |  PigLatin class contains two method - 
     |  
     |  1. serialize - Serialize a word into a dictionary
     |  2. get_pig_latin_word - Get the pig-latin translation 
     |  of a given word.
     |  
     |  get_pig_latin_word(word)
     |      Get the pig-latin translation of the given word
     |      
     |       input/argument - An english word
     |       return value - pig-latin transaltion of the input word
     |      
     |       NOTE - Pig Latin is a language used by English-speaking people, 
     |       especially when they want to disguise something they are saying 
     |       from non-Pig Latin speakers. Pig latin translation works in unique 
     |       way. There are some rules to convert a word into its pig-latin form.
     |      
     |       1. If the word starts with a vowel, add an 'ay' at the end.
     |       For example, 'owl' will become 'owlay' after translation.
     |      
     |       2. If the word starts with sh'|'gl'|'ch'|'ph'|'tr'|'br'| 
     |      'fr'|'bl'|'gr'|'st'|'sl'|'cl'|'pl'|'fl , remove it from the 
     |       begining and put at the end. Then add 'ay' at the end.
     |       For example, 'check' will become 'eckchay'.
     |       
     |       3. In all other cases, the first  character will be removed 
     |       from the begining and will be put at the end. The word will be
     |       appended by 'ay' after that.
     |       For example, 'who' will become 'howay'
     |  
     |  serialize(word)
     |      Serialize a word into a dictionary
     |      
     |      input/argument - An english word
     |      return value - A dictionary with key/value pair for the word
     |  
     |  ----------------------------------------------------------------------
     | 
    
   ## class RandomWord(builtins.object)
     |  RandomWord class contains two methods.
     |  
     |  1. serialize - Serialize a word into a dictionary
     |  2. get_random_word - Returns a word randomly from the given 
     |  list of words.
     |  
     |  
     |  get_random_word(words)
     |      Get a word randomly from the given list of words
     |      
     |      input/argument - List of words
     |      return value - Word chosen randomly from the given list
     |  
     |  serialize(word)
     |      Serialize a word into a dictionary
     |      
     |      input/argument - An english word
     |      return value - A dictionary with key/value pair for the word
       ----------------------------------------------------------------------
     
   ## class Rhyme(builtins.object)
     |  Rhyme class contains two methods -
     |  
     |  1. serialize - Serialize a word into a dictionary
     |  
     |  2. get_rhyming_word - Get the list of words rhyming
     |  with the given word. The methods makes use of Pronouncing 
     |  package  provided by python community to get the rhyming 
     |  words for a word.
     |  
     |  Static methods defined here:
     |  
     |  get_rhyming_words(word)
     |      Get the list of words rhyming with given word
     |      
     |      input/argument - An english word
     |      return value - List of words rhyming with the given word
     |      
     |      NOTE - The "pronouncing" package provides the functionality to
     |      get rhyming words from the CMU Pronouncing Dictionary for a given
     |      word.
     |  
     |  serialize(word)
     |      Serialize a word into a dictionary
     |      
     |      input/argument - An english word
     |      return value - A dictionary with key/value pair for the word
     |  
     |  ----------------------------------------------------------------------
    
    
    
   ## 4. app/service.py
    
   ## Description
    Paths:
    -----
    GET /words/random?input=<comma sepearted list of words>  - Takes list of words and returns a random word out of them
    GET /words/rhyming/{word} - Takes a word and return list of words rhyming with the given word
    GET /words/pig-latin/{word} - Takes a word and returns its pig-latin translation
    -----

   ## Functions
   ### bad_request(error)
        Handles bad requests with 400_BAD_REQUEST
    
   ### get_pig_latin_word(word='Kepler')
        This endpoint will return pig-latin translation of the given word.
        
        The API call "/words/pig-latin/{word}" is routed to this
        method where {word} is any english word.
        
        NOTE - Before calling the function from PigLatin class in models module,
        following checks are performed -
        1. If the word is not a proper English word (contains any non-alphabet
         character), abort the request.
        2. If length of the word is greater than 45, abort the
        request because longest word in Oxford dictionary is of length 45.
    
   ### get_random_word()
        This endpoint  returns a word randomly selected from the
        given list of words in the query.
        
        The API call "/words/random?input=<comma sepearted list of words>" is 
        routed to this method.
        Currently,the API requires input words to be seperated by commas.
        More flexibility for the delimiters can be added later.
        
        NOTE - Before calling the function from the RandomWord class in models 
        module, follwing checks are performed - 
        1. If length of input list is less than 2 or greater than 20, abort 
        the request.
        2. If length of any word in the list is greater than 45, abort the 
        request because longest word in Oxford dictionary is of length 45.
    
   ### get_rhyming_words(word='Kepler')
        This endpoint will return list of words rhyming with the given
        words as parameter.
        
        
        It will skip the words after the first comma if a comma separated
        list is provided.
         The API call "/words/rhyming/{word}" is routed to this
        method where {word} is any english word.
        
        NOTE - Before calling the function from Rhyme class in models module, 
        following checks are performed -
        1. If the word is not a proper English word (contains any non-alphabet
         character), abort the request.
        2. If length of the word is greater than 45, abort the
        request because longest word in Oxford dictionary is of length 45.
    
   ### get_rhyming_words_index()
        This endpoint will return a response asking the user to provide
        input word.
    
   ### index()
        Get the root URL response
    
   ### initialize_logging(log_level=20)
        Initialize the default logging to STDOUT
    
   ### internal_server_error(error)
        Handles unexpected server error with 500_SERVER_ERROR
    
   ### not_found(error)
        Handles resources not found with 404_NOT_FOUND
    
   ### valid_english_word(word)
        Validate if the word is a English word.
        
        The check is on the characters of the word.It must contain alphabets just 
        from a-z or A-Z and nothing else.
    
   ### valid_length_of_word(word)
        Validate if the word has valid length
        

       
