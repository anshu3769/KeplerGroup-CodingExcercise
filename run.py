"""
Kepler Group Coding Excercise

Start the Service
"""

import os
from app import app,service

# Pull options from environment
DEBUG = (os.getenv('DEBUG', 'False') == 'True')
PORT = os.getenv('PORT', '5000')

######################################################################
#   M A I N
######################################################################
if __name__ == "__main__":
    print("****************************************")
    print(" KEPLER GROUP CODING EXCERCISE   SERVICE   RUNNING")
    print("****************************************")
    app.run(host='0.0.0.0', port=int(PORT), debug=DEBUG)
