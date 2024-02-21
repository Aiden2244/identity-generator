
# IDENTITY GENERATOR


### About
**New Alias** is an alias generator designed to protect online identity. It generates 
plausible-sounding names, usernames, and passphrases, as well as real open addresses in the 
United States that are not tied to any particular individual or business (made available
through the OpenAddress project - you can read more on them here: https://openaddresses.io/). 

### Installation and Usage
This program is available as the python package "new-alias". If python is installed on your system,
then you should be able to run "pip install new-alias" (with a dash) without any issues. After the 
package is installed, the program can be run on the command line by simply typing the package name 
"new_alias" (with an underscore).

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


