#This script runs the basic testing on the API functionality
#The API calls will be executed with valid and invalid parameters
# Based on the validity of the API call, the HTTP response will be generated

bold=`tput bold`
normal=`tput sgr0`
red=`tput setaf 1`

#Port number on which application is running
PORT=5000

#Count of total test cases
total_test_cases=0

#Count of passed test case
passed_test_cases=0


############################################################
#Test the home index of the API
############################################################
echo "${bold}T E S T I N G   T H E   A P I   H O M E   I N D E X ${normal}"
echo "${bold} Expected output:${normal} "
expected="{\"info\":\"Home page for the API\",\"name\":\"Words REST API Service\",\"version\":\"1.0\"}"
echo "{\"info\":\"Home page for the API\",\"name\":\"Words REST API Service\",\"version\":\"1.0\"}"
echo "${bold} Actual output:${normal} "
actual=$(curl -s -H "Accept:application/json" "http://localhost:${PORT}/")
echo "${actual}"
total_test_cases=$((total_test_cases+1))

if [ "${expected}" == "${actual}" ]; then
	echo "TEST 1"
	passed_test_cases=$((passed_test_cases+1))
fi

echo ""
echo ""

############################################################
#Test the random word generation functionality of the API
############################################################
#Case 1: When no input is given to the API
#Case 2: When no of words in the list are less than 2
#Case 3: When no of words in the list are more than 20
#Case 4: When correct input is given
#Case 5: When length of any word is greater than 45

echo "${bold}T E S T I N G   T H E   R A N D O M   W O R D   G E N E R A T I O N   F U N C T I O N A L I T Y ${normal}"
echo "${red}  Case 1: When no input is given to the api${normal}"

echo "${bold}Expected output :"
echo "${normal}{\"error\":\"Bad Request\",\"message\":\"400 Bad Request: Input not provided\",\"status\":400}"
expected="{\"error\":\"Bad Request\",\"message\":\"400 Bad Request: Input not provided\",\"status\":400}"

echo "${bold}Actual output:${normal}"
actual=$(curl -s -H "Accept:application/json" "http://localhost:${PORT}/words/random")
echo "${actual}"
total_test_cases=$((total_test_cases+1))

if [ "${expected}" == "${actual}" ]; then
	echo "TEST 2"
	passed_test_cases=$((passed_test_cases+1))
fi

echo ""

echo "${red}  Case 2: When number of words in the list are less than 2 ${normal}"
echo "${bold}Expected output :"
echo "${normal}{\"error\":\"Bad Request\",\"message\":\"400 Bad Request: Length of the list is either less than 2 or greater than 20\",\"status\":400}"
expected="{\"error\":\"Bad Request\",\"message\":\"400 Bad Request: Length of the list is either less than 2 or greater than 20\",\"status\":400}"

echo "${bold}Actual output:${normal}"
actual=$(curl -s -H "Accept:application/json" "http://localhost:${PORT}/words/random?input=one")

echo "${actual}"
total_test_cases=$((total_test_cases+1))

if [ "${expected}" == "${actual}" ]; then
	echo "TEST 3"
	passed_test_cases=$((passed_test_cases+1))
fi

echo ""

echo "${red}  Case 3: When number of words in the list are more than 20 ${normal}"
echo "${bold}Expected output :"
echo "${normal}{\"error\":\"Bad Request\",\"message\":\"400 Bad Request: Length of the list is either less than 2 or greater than 20\",\"status\":400}"
expected="{\"error\":\"Bad Request\",\"message\":\"400 Bad Request: Length of the list is either less than 2 or greater than 20\",\"status\":400}"

echo "${bold}Actual output:${normal}"
actual=$(curl -s -H "Accept:application/json" "http://localhost:${PORT}/words/random?input=one,two,three,one,two,three,one,two,three,one,two,three,one,two,three,one,two,three,one,two,three")
echo "${actual}"
total_test_cases=$((total_test_cases+1))

if [ "${expected}" == "${actual}" ]; then
	echo "TEST 4"
	passed_test_cases=$((passed_test_cases+1))
fi

echo ""

echo "${red}  Case 4: When correct input is given ${normal}"
echo "${bold}Expected output :${normal}"
echo "{\"random_word\":\"one\"} ${bold}OR${normal} {\"random_word\":\"two\"} ${bold}OR${normal} {\"random_word\":\"three\"}"
expected_1="{\"random_word\":\"one\"}"
expected_2="{\"random_word\":\"two\"}"
expecter_3="{\"random_word\":\"three\"}"

echo "${bold}Actual output:${normal}"
actual=$(curl -s  -H "Accept:application/json" "http://localhost:${PORT}/words/random?input=one,two,three")
echo "${actual}"
total_test_cases=$((total_test_cases+1))

if [ "${expected_1}" == "${actual}" ] || [ "${expected_2}" == "${actual}" ] || [ "${expected_3}" == "${actual}" ]; then
	echo "TEST 5"
	passed_test_cases=$((passed_test_cases+1))
fi

echo ""

echo "${red}  Case 5: When length of any word in the list is greater than 45 ${normal}"
echo "${bold}Expected output :${normal}"
echo "{\"error\":\"Bad Request\",\"message\":\"400 Bad Request: Length of one or more words is greater than 45\",\"status\":400}"
expected="{\"error\":\"Bad Request\",\"message\":\"400 Bad Request: Length of one or more words is greater than 45\",\"status\":400}"

echo "${bold}Actual output:${normal}"
actual=$(curl -s  -H "Accept:application/json" "http://localhost:${PORT}/words/random?input=one,twoeeeeeeeeeeeeeeeeeeanananaeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
echo "${actual}"
total_test_cases=$((total_test_cases+1))

if [ "${expected}" == "${actual}" ]; then
	echo "TEST 6"
	passed_test_cases=$((passed_test_cases+1))
fi

echo ""
echo ""

############################################################
#Test the getting rhyming words functionality of the API
############################################################
#Case 1: When the word is not a valid english word
#Case 2: When length of the word is greater than 45
#Case 3: When correct input is provided

echo "${bold}T E S T I N G   T H E   R H Y M I N G   W O R D S   F U N C T I O N A L I T Y ${normal}"
echo "${red}  Case 1: When the word is not a valid english word ${normal}"
echo "${bold}Expected output :"
echo "${normal}{\"error\":\"Bad Request\",\"message\":\"400 Bad Request: The word is not a valid english word\",\"status\":400}"
expected="{\"error\":\"Bad Request\",\"message\":\"400 Bad Request: The word is not a valid english word\",\"status\":400}"

echo "${bold}Actual output:${normal}"
actual=$(curl -s -H "Accept:application/json" "http://localhost:${PORT}/words/rhyming/1cat")
echo "${actual}"
total_test_cases=$((total_test_cases+1))

if [ "${expected}" == "${actual}" ]; then
	echo "TEST 7"
	passed_test_cases=$((passed_test_cases+1))
fi

echo ""


echo "${red}  Case 2: When length of the word is greater than 45 ${normal}"
echo "${bold}Expected output :${normal}"
echo "{\"error\":\"Bad Request\",\"message\":\"400 Bad Request: Length of one or more words is greater than 45\",\"status\":400}"
expected="{\"error\":\"Bad Request\",\"message\":\"400 Bad Request: Length of one or more words is greater than 45\",\"status\":400}"

echo "${bold}Actual output:${normal}"
actual=$(curl -s  -H "Accept:application/json" "http://localhost:${PORT}/words/rhyming/twoeeeeeeeeeeeeeeeeeeeeeeeeeeeeabanaeeeeeeeeeeeeeeeeeeeeeeeee")
echo "${actual}"
total_test_cases=$((total_test_cases+1))

if [ "${expected}" == "${actual}" ]; then
	echo "TEST 8"
	passed_test_cases=$((passed_test_cases+1))
fi

echo ""

echo "${red}  Case 3: When correct input is given ("earth" is given as input)${normal}"
echo "${bold}Expected output :"
echo "${normal}[\"berth\",\"birth\",\"dearth\",\"firth\",\"fuerth\",\"furth\",\"gerth\",\"girth\",\"hirth\",\"kerth\",\"kurth\",\"mirth\",\"perth\",\"rebirth\",\"unearth\",\"wentworth\",\"werth\",\"wirth\",\"worth\",\"wurth\"]"
expected="[\"berth\",\"birth\",\"dearth\",\"firth\",\"fuerth\",\"furth\",\"gerth\",\"girth\",\"hirth\",\"kerth\",\"kurth\",\"mirth\",\"perth\",\"rebirth\",\"unearth\",\"wentworth\",\"werth\",\"wirth\",\"worth\",\"wurth\"]"

echo "${bold}Actual output:${normal}"
actual=$(curl -s -H "Accept:application/json" "http://localhost:${PORT}/words/rhyming/earth")
echo "${actual}"
total_test_cases=$((total_test_cases+1))

if [ "${expected}" == "${actual}" ]; then
	echo "TEST 9"
	passed_test_cases=$((passed_test_cases+1))
fi

echo ""
echo ""

###############################################################
#Test the pig-latin word translation  functionality of the API
###############################################################
#Case 1: When the word is not a valid english word
#Case 2: When length of the word is greater than 45
#Case 3: When correct input is given

echo "${bold}T E S T I N G   T H E   P I G   L A T I N   T R A N S L A T I O N     F U N C T I O N A L I T Y ${normal}"
echo "${red}  Case 1: When the word is not a valid english word ${normal}"
echo "${bold}Expected output :"
echo "${normal}{\"error\":\"Bad Request\",\"message\":\"400 Bad Request: The word is not a valid english word\",\"status\":400}"
expected="{\"error\":\"Bad Request\",\"message\":\"400 Bad Request: The word is not a valid english word\",\"status\":400}"
echo "${bold}Actual output:${normal}"
actual=$(curl -s -H "Accept:application/json" "http://localhost:${PORT}/words/pig-latin/2who@")
echo "${actual}"
total_test_cases=$((total_test_cases+1))

if [ "${expected}" == "${actual}" ]; then
	echo "TEST 10"
	passed_test_cases=$((passed_test_cases+1))
fi

echo ""


echo "${red}  Case 2: When length of the word is greater than 45 ${normal}"
echo "${bold}Expected output :${normal}"
echo "{\"error\":\"Bad Request\",\"message\":\"400 Bad Request: Length of one or more words is greater than 45\",\"status\":400}"
expected="{\"error\":\"Bad Request\",\"message\":\"400 Bad Request: Length of one or more words is greater than 45\",\"status\":400}"

echo "${bold}Actual output:${normal}"
actual=$(curl -s  -H "Accept:application/json" "http://localhost:${PORT}/words/pig-latin/twoeeeeeeeeeeeeeeeeeeeeeeeeeeeeabanaeeeeeeeeeeeeeeeeeeeeeeeee")
echo "${actual}"
total_test_cases=$((total_test_cases+1))

if [ "${expected}" == "${actual}" ]; then
	echo "TEST 11"
	passed_test_cases=$((passed_test_cases+1))
fi

echo ""

echo "${red}  Case 3: When correct input is given (who is given as input)${normal}"
echo "${bold}Expected output :"
echo "${normal}{\"pig_latin_word\":\"howay\"}"
expected="{\"pig_latin_word\":\"howay\"}"

echo "${bold}Actual output:${normal}"
actual=$(curl -s -H "Accept:application/json" "http://localhost:${PORT}/words/pig-latin/who")
echo "${actual}"
total_test_cases=$((total_test_cases+1))

if [ "${expected}" == "${actual}" ]; then
	echo "TEST 12"
	passed_test_cases=$((passed_test_cases+1))
fi

echo ""
echo ""

echo "Passed tests/Total tests = ${passed_test_cases}/${total_test_cases}"
