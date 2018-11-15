# KeplerGroup-CodingExcercise
This repository contains the code for developing a RESTFUL API using Python Flask. 


## Requirements of the excercise to be fulfilled by the API
  
 Functional Requirements- 
 * User provides 2 or more words to the server, and the server randomly returns 1 word
 * User provides 1 English word, and server returns a list of English words that rhyme with that word
 * User provides 1 English word, and server returns its pig latin translation
 
 Non functional requirements-
 * The application should be able to run on Ubuntu 18.04.
 * Code should be written in python 3+ version.
 * Setup instructions to run the code should be provided.
 * Automated testing of the API should be provided
 
 
 ## Directory Structure
 
 ```bash
├── app
│   ├──__init__.py
│   ├── service.py
│   ├── models.py
│     
├── tests
|   ├── README.md
│   ├── tests.sh
│  
├── doc
|   ├── README.md
│
├── README.md
├── Vagrantfile
├── requirments.txt
├── run.py
├── README.md
|
├── .github
│    ├── BUG_TEMPLATE.md
│    ├── ISSUE_TEMPLATE.md
│
└── .gitignore
```

## Endpoints of the API

 *  GET /words or / - Renders the index page
 *  GET /words/random?input={comma sepearted list of words} - Takes list of words and returns a random word out of them
 *  GET /words/rhyming/{string:word} - Takes a word and returns list of words rhyming with the given word
 *  GET /words/pig-latin/{string:word} - Takes a word and returns its pig latin translation
 

  
## Environment setup to run the application

  The easiest way to run this service is to use vagrant and virtual box. It will be a one time setup.
  Vagrant is a developers tool for creating lightweight, reproducible and portable virtual environments via 
  command-line. The flexibilty it provides is that you dont have to worry about the tools and packages that 
  your application requires everyime you need to run your application on a different machine/envirnment. Vagrant 
  will do that for you. If you dont have it already -  
  
 * To download virtualbox, please use this link - 
   https://www.virtualbox.org/
   
     Click on the downloaded dmg file  and it will walk you through the installation step.
     
 * To download vagrant, please use this link -
   https://www.vagrantup.com/
   
      Click on the downloaded dmg file  and it will walk you through the installation step.
       
  To verify, run the command "vagrant --version". It should display the version of the vagrant
  installed. 
 
 
    NOTE - Virtual box must be installed before installing vagrant because vagrant requires virtaulization platform and 
    virtual box is best suite for it.
 
 
 
 ## Running the application
   1. Clone the repository
    Clone the project on your machine and create your Vagrant VM. Run the following
    commands to clone the repository and creating virtual machine for the project.
     
    git clone https://github.com/anshu3769/KeplerGroup-CodingExcercise.git
    cd KeplerGroup-CodingExcercise
    
    
 ## Some things to know about the Vagrantfile
     vi Vagrantfile
    
      1.  The following line downloads ubuntu-18.04 image for the VM
          config.vm.box = "ubuntu/bionic64"
          
      2. The follwing lines set up network ip and port forwarding
          config.vm.network "forwarded_port", guest: 5000, host: 5070, host_ip: "127.0.0.1"
          config.vm.network "private_network", ip: "192.168.33.10"
          
          where 5000 is the port on which the application will run on guest machine(VM) and 5090
          is the port on which application will run on host machine(local machine). You can change these
          ports based on the availabilty of free ports on your machine. The application can be 
          accessed through the IP provided in the ip field.
      3. Version of python for this virtual machine is 3. The following lines in the file sets this up.
          apt-get install -y git python3 python3-pip python3-dev build-essential
          pip3 install -r requirements.txt
   
    
 ## Set up the virtual machine
    After the ports has been set in the Vagrantfile, run the command
    vagrant up
    
   When running for the first time,  "vagrant up" command will take sometime to run as it is creating the fully functional 
   environment for your application. The VM is up and running when the command complete execution.
   
   
  ## Login to the VM and run the application
     vagrant ssh
     cd /vagrant
     python3 run.py
 
 You should now be able to see the service running in your browser by going to http://localhost:5090 or      http://127.0.0.1:5090 where 5090 is the port number provided in the host field in vagrant file(can be changed 
 if required). You will see a message about the service which looks something like this:
 
    {"info":"Home page for the API",
     "name":"Words REST API Service",
     "version":"1.0"}
     
  
 ## Running the API actions:
     
     Run the following on the browser:
     
   http://localhost:5090/words/random?input=one,two,three
     
     Expected output: 
     
     {"random-word":"one"}
             or
     {"random-word":"two"}
             or
     {"random-word":"three"}
     
     
   http://localhost:5090/words/rhyming/cat
     
     Expected output:
     
     ["arnatt","at","at-bat","balyeat","bat","batt","batt,"dat","delatte","deslatte","elat",","hat","hatt","hnat", ....]
     
  
   http://localhost:5090/words/pig-latin/who
   
     {pig-latin-word: "howay"}
     
     
     
 ## Running the tests on
 
    To run the tests, please go to the tests/ directory and follow the steps provided in the README.md file present in 
    tests directory.
     
     
     
    
 
 
       
 
 
 
