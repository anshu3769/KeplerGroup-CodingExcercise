
## Steps to run the tests on the API
  The script tests.sh will run the basic tests on the API. Follow the steps to run the tests.
   
   
  ## 1. Once your application is up and running, go to the directory tests/ (on VM). 
   On another terminal/shell, from the repo's home directory
  i.e. KeplerGroup-CodingExcercise/, execute the following commands to go the VM- 
 
     vagrant ssh
     cd /vagrant
     cd tests/
       
  ## 2. Give execute permissions to the script.
     chmod 755 tests.sh
   
  ## 3. Run the tests
      bash ./tests.sh
      
      
 ## NOTE
     This test script is using 5000 as its guest port number. If you have set up different port number fo the guest 
     machine in vagrant file, please use that in place of 5000. For that, just change PORT variable in the tests.sh 
     script and save the file.
  
