EX 818 M
----
*Advanced Networking Test for Passwords for Web Applications*
 <br><br>
EX-818-M (Exploit 818 Mikrotik) is A tool that pulls all cards or passwords in the network ( Mikrotik ) without entering any pearls from the system.

**The goal is to extract passwords**

## Features
* Multithreaded scanning.
* Includes request rate throttling.
* Not stop when getting password
* Uses multiple algorithms for automatically detecting valid and invalid pages.
* User agent randomization.
* Works both as a command-line tool and Python module.
* Support for MacOS, and Linux operating systems, and Phone.
* Reporting: simple, Text.

## Image

![EX818M](https://github.com/HathemAhmed/ex818m/blob/master/index.png)

## Usage

| Description                                                | Command                                                                 |
|------------------------------------------------------------|-------------------------------------------------------------------------|
| Help                                                       | `ex818.py --help`                                                        |
| Check  ip:port and use numbers.                            | `ex818.py -i <IP> -p 80 -n <MinNumber>,<MaxNumber>`
| Check a file output .                                      | `ex818.py -i <IP> -p 80 -n <MinNumber>,<MaxNumber> -o <file> output.txt`                                          |



## Requirements
* Python3.6 or Python3.7


## Installation [Optional]
`sudo python3 setup.py install`


## Compatibility
The project is compatible with Python 3.

## Frequently Asked Questions
**Q:** How to use EX818M with all levels?

**A:** 
By guessing the password numbers and selecting the correct password


**Q:** How do I deal with the numbers you guess?

**A:**
Preferably use the first four or five digits of the password you have already used


## Legal disclaimer
This project is designed for educational and ethical testing purposes only. In order for the owner of the network to close the gap

## Thanks
I thank my friends for supporting me ^^

## Author
*Hathem Ahmed*
* Website : [https://crazyhackers.ga](https://crazyhackers.ga)
* FaceBook: [https://FB.com/mhm.hack](https://FB.com/mhm.hack)
