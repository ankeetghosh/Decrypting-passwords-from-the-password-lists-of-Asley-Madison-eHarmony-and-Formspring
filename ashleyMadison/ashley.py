#!/usr/bin/python

AshleyOtptFile = open("AshleyOutput.txt", 'w') #Open output file to store matched passwords
for line in open("AshleyMadison.txt", "r+"): #Open the given list of hashed passwords
    passwordList = line.replace("\n","")
    AshleyOtptFile.write(passwordList+" "+passwordList.split(',')[3]) #Extract and write the passwords as requested
    AshleyOtptFile.write('\n')
AshleyOtptFile.close()
