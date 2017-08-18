#!/usr/bin/python
import hashlib
import sys
m = hashlib.md5()
eHarmonyOtptFile = open("eHarmonyOutput.txt", 'w') #Open output file to store matched passwords
passwordFile = open("eHarmony.txt", "r+") #Open the given list of hashed passwords
passwordList = passwordFile.readlines()
for i in range(0,len(passwordList)):
    passwordList[i] = passwordList[i].replace("\n","")
    for line in open("md5.txt", "r+"):  #Open the list of passwords in the wordlist
        #line = line.strip()
        m = hashlib.md5()
        line = line.replace("\n","")
        m.update(line) #encrypt the plain text passwords in the wordlist
        predictedPassword = m.hexdigest() 
        if predictedPassword==passwordList[i]: #Check if the newly hashed plain text password matched that in the given hashed password list 
            eHarmonyOtptFile.write(passwordList[i] + " " + line) #if the above condition is true. The original is written in the output file
            eHarmonyOtptFile.write('\n')
            break
            
passwordFile.close()
eHarmonyOtptFile.close()
