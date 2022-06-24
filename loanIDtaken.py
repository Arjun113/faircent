# This code creates a JSON file with all the loan IDs already taken to be able to assign a new one to fresh customers without error

# All imports come here
import os
import json

# Input directory
folderpath = str(input("Input the folder which needs searching - "))

listOfloanID = list()

# The work begins here
for subfolder in os.listdir(folderpath):
    loanID = ""
    for letter in subfolder:
        if letter.isdigit():
            loanID = loanID + str(letter)
    listOfloanID = listOfloanID + loanID

with open("listOfLoanIDTaken.json", "w+") as file:
    json.dump(listOfloanID, file, indent=2)

# CODE OVER. JSON DUMP DONE.