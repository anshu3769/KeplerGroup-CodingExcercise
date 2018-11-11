# KeplerGroup-CodingExcercise
This repository contains the code for developing a RESTFUL words application using Python Flask. 

## Functionality provided by the API

 * User provides 2 or more words to the server, and the server randomly returns 1 word
 * User provides 1 English word, and server returns a list of English words that rhyme with that word

## Endpoints of the API

 *  GET /words or / - Renders the index page
 *  GET /words/random?input=<comma sepearted list of words> - Takes list of words and returns a random word out of them
 *  GET /words/rhyming/<string:word> - Takes a word and return list of words rhyming with the given word
  
## Prerequisite for running the application

  The easiest way to run this service is to use vagrant and virtual box. It will be a one time setup.
  Vagrant is a developers tool for creating lightweight, reproducible and portable virtual environments via 
  command-line. The flexibilty it provides is that you dont have to worry about the tools and packages that 
  your application requires everyime you need to run your application on a different machine/envirnment. Vagrant 
  will do that for you. If you dont have it already -  
  
    * To download virtualbox, please use this link - https://www.virtualbox.org/
       Click on the downloaded dmg file  and it will walk you through the installation step.
    * To download vagrant, please use this link - https://www.vagrantup.com/
       Click on the downloaded dmg file  and it will walk you through the installation step.
       
       To verify, run the command "vagrant --version". It should display the version of the vagrant
       installed. 
 
 
  NOTE - Virtual box must be installed before installing vagrant because vagrant requires virtaulization platform and 
  virtual box is best suite for it.
 
 
 ## Clone the project
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
          
          where 5000 is the port on which the application will run on guest machine(VM) and 5070
          is the port on which application will run on host machine(local machine). The application can be 
          accessed through the IP provided in the ip field.
      3. Version of python set for this virtual machine is 3. The following lines in the file sets this up.
          apt-get install -y git python3 python3-pip python3-dev build-essential
          pip3 install -r requirements.txt
   
    
 ## Set up the virtual machine
   Open the Vagrantfile and search for "host" in the the file. Enter a port number(which is not in use )
   for the host. By default, it is 5001. This port number will also work if this port is free on your machine.
   Same applies to guest port number. 
    
    Now run the command
    vagrant up
    
   When running for the first time,  "vagrant up" command will take sometime to run as it is creating the fully functional 
   environment for your application. The VM is up and running when the command complete execution.
   
 
   
  ## Login to the VM and run the application
     vagrant ssh
     cd /vagrant
     python3 run.py
 
 You should now be able to see the service running in your browser by going to http://localhost:{PORT} where PORT 
 is the port number provided in the host field in vagrant file(set to 5090 currently). You will see a 
 message about the service which looks something like this:
     
  
  
  
 
 
       
 
 
 
