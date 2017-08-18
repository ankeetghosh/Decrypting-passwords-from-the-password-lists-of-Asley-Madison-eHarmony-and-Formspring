#!/usr/bin/python
import uuid
import hashlib
import sys

open("formspringOutput.txt", 'w').close() ## Emptying the Output file
flag = 0
with open("formspringOutput.txt", 'a') as formSpringOtptFile: #Open output file to store matched passwords
    for lineForm in open("formspring.txt", "r+"): #Open the given list of hashed passwords
        hashPassword = lineForm.replace("\n","")
        for line in open("sha256.txt", "r+"): #Open the list of passwords in the wordlist
            password = line.replace("\n","")
            for i in range(0,100):
                salt = "{0:0=2d}".format(i)
                try:
                    WordListPwdHash  = hashlib.sha256(salt.encode() + password.encode()).hexdigest() #encrypt the plain text passwords in the wordlist after adding the salt
                except ValueError:
                    break
                if(WordListPwdHash == hashPassword): #Check if the newly hashed plain text password matched that in the given hashed password list 
                    formSpringOtptFile.write(hashPassword + " " + line) #if the above condition is true. The original password is written in the output file
                    flag = 1
                    break
            if(flag == 1):
                flag = 0
                break

