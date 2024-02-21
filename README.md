
# IDENTITY GENERATOR


### About

Identity generator is an alias generator designed to protect online identity. It generates 
plausible-sounding names, usernames, and passphrases, as well as real open addresses in the 
United States that are not tied to any particular individual or business (made available
through the OpenAddress project). 

### Installation and Usage

This program is available as the python package "id-gen". If python is installed on your system,
then you should be able to run "pip install id-gen" without any issues. I had to install pycairo
and pkg-config on my Ubuntu system the first time I ran it, which I was able to do with the 
command "sudo apt install pkg-config libcairo2-dev". 

After the package and any other essential binaries are installed, the program can be run on the
command line by simply typing the package name "id-gen".

### Attributions

This program relies on some external data sources and libraries to work. They are as follows:
* **Name Generation:** uses open source name files that can be found here: 
https://gist.github.com/elifiner/cc90fdd387449158829515782936a9a4
* **Username Generation:** uses an open source word dictionary that can be found here:
https://github.com/dwyl/english-words?search=1
* **Passphrase Generation:** uses an open source text file of words that can be found here:
https://gist.github.com/deekayen/4148741
* **Address Generation:** uses the python library 'random-address', the documentation for which 
can be found here:
https://pypi.org/project/random-address/
('random-address' is available through the MIT License)

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


