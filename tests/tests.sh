#This script runs the basic testing on the API functionality
#The API calls will be executed with valid and invalid parameters
# Based on the validity of the API call, the HTTP response will be generated

bold=$(tput bold)
normal=$(tput sgr0)
red='\033[0;31m'
nc='\033[0m'


#Test the home index of the API
echo "${bold}T E S T I N G   T H E   A P I   H O M E   I N D E X ${normal}"
echo "${bold} Expected output:${normal} "
echo "{\"info\":\"Home page for the API\",\"name\":\"Words REST API Service\",\"version\":\"1.0\"}"
echo "${bold} Actual output:${normal} "
curl -H "Accept:application/json" "http://localhost:5000/"

echo "\n"
echo "\n"


#Test the random word generation functionality of the API
#Case 1: When no input is given to the API
#Case 2: When no of words in the list are less than 2
#Case 3: When no of words in the list are more than 20
#Case 3: When correct input is given

echo "${bold}T E S T I N G   T H E   R A N D O M   W O R D   G E N E R A T I O N   F U N C T I O N A L I T Y"
echo "${red}  Case 1: When no input is given to the api${nc}"
echo "${bold}Expected output :"
echo "${normal}{\"error\":\"Bad Request\",\"message\":\"400 Bad Request: Input not provided\",\"status\":400}"

echo "${bold}Actual output:${normal}"
curl -H "Accept:application/json" "http://localhost:5000/words/random"

echo "\n"

echo "${red}  Case 2: When no of words in the list are less than 2 ${nc}"
echo "${bold}Expected output :"
echo "${normal}{\"error\":\"Bad Request\",\"message\":\"400 Bad Request: Length of the list is either less than 2 or greater than 20\",\"status\":400}"

echo "${bold}Actual output:${normal}"
curl -H "Accept:application/json" "http://localhost:5000/words/random?input=one"

echo "\n"

echo "${red}  Case 3: When no of words in the list are more than 20 ${nc}"
echo "${bold}Expected output :"
echo "${normal}{\"error\":\"Bad Request\",\"message\":\"400 Bad Request: Length of the list is either less than 2 or greater than 20\",\"status\":400}"

echo "${bold}Actual output:${normal}"
curl -H "Accept:application/json" "http://localhost:5000/words/random?input=one,two,three,one,two,three,one,two,three,one,two,three,one,two,three,one,two,three,one,two,three"

echo "\n"

echo "${red}  Case 4: When correct input is given ${nc}"
echo "${bold}Expected output :${normal}"
echo "{\"random_word\":\"one\"} ${bold}OR${normal} {\"random_word\":\"two\"} ${bold}OR${normal} {\"random_word\":\"three\"}"
echo "${bold}Actual output:${normal}"
curl -H "Accept:application/json" "http://localhost:5000/words/random?input=one,two,three"


echo "\n"
echo "\n"

#Test the getting rhyming words functionality of the API
#Case 1: When the word is not a valid english word
#Case 2: When correct input is provided

echo "${bold}T E S T I N G   T H E   R H Y M I N G   W O R D S   F U N C T I O N A L I T Y"
echo "${red}  Case 1: When the word is not a valid english word ${nc}"
echo "${bold}Expected output :"
echo "${normal}{\"error\":\"Bad Request\",\"message\":\"400 Bad Request: The word is not a valid english word\",\"status\":400}"

echo "${bold}Actual output:${normal}"
curl -H "Accept:application/json" "http://localhost:5000/words/rhyming/1cat"

echo "\n"

echo "${red}  Case 2: When correct input is given ("earth" is given as input)${nc}"
echo "${bold}Expected output :"
echo "${normal}[\"berth\",\"birth\",\"dearth\",\"firth\",\"fuerth\",\"furth\",\"gerth\",\"girth\",\"hirth\",\"kerth\",\"kurth\",\"mirth\",\"perth\",\"rebirth\",\"unearth\",\"wentworth\",\"werth\",\"wirth\",\"worth\",\"wurth\"]"
echo "${bold}Actual output:${normal}"
curl -H "Accept:application/json" "http://localhost:5000/words/rhyming/earth"

echo "\n"
echo "\n"

#Test the pig-latin word translation  functionality of the API
#Case 1: When the word is not a valid english word
#Case 2: When correct input is given

echo "${bold}T E S T I N G   T H E   P I G   L A T I N   T R A N S L A T I O N     F U N C T I O N A L I T Y"
echo "${red}  Case 1: When the word is not a valid english word ${nc}"
echo "${bold}Expected output :"
echo "${normal}{\"error\":\"Bad Request\",\"message":\"400 Bad Request: The word is not a valid english word\",\"status\":400}" "

echo "${bold}Actual output:${normal}"
curl -H "Accept:application/json" "http://localhost:5000/words/pig-latin/2who@"

echo "\n"

echo "${red}  Case 2: When correct input is given ("who" is given as input)${nc}"
echo "${bold}Expected output :"
echo "${normal}{\"pig_latin_word\":\"howay\"} "

echo "${bold}Actual output:${normal}"
curl -H "Accept:application/json" "http://localhost:5000/words/pig-latin/who"
