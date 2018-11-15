"""Kepler Group Coding Excercise

Application starts running from this module.
It also initializes logging for the application.

As a user, you will be running "python3 run.py"
to start the application.
"""

import os
from app import app,service

#Pull options from environment, if provided, otherwise default will be chosen
#DEBUG = (os.getenv('DEBUG', 'False') == 'True')
PORT = os.getenv('PORT', '5000')

######################################################################
#   M A I N
######################################################################
if __name__ == "__main__":
    print("****************************************")
    print("KEPLER GROUP CODING EXCERCISE")
    print("SERVICE IS  RUNNING")
    print("****************************************")
  
    #Initialize logging
    service.initialize_logging()

    #Run the application 
    app.run(host='0.0.0.0', port=int(PORT))
