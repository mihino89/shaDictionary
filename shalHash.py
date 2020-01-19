#!/usr/bin/python

from urllib.request import urlopen
import hashlib
from termcolor import colored

sha1hash = input("[*] enter sha1 hash value: ")

passList = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

for password in passList.split('\n'):
    hashGuess = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
    if hashGuess == sha1hash:
        print(colored("[*] The password is: " + str(password), 'green'))
        quit()
    else:
        print(colored("[-] Password guess " + str(password) + " does not match, trying next...", 'red'))

print("Password is not in password list")


