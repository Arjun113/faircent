# This code integrates all the main pieces of code together
import json
import random
import stage0Prelim
import Stage1UnnamedAlt
import Stage1CheckForNamed
import Stage2
import mysql.connector as mysql
import os
import shutil
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# mySQL initialization
myconnection = mysql.connect(host = "localhost", username = "arjun", pwd = "arjun", database = "faircent1") # Change host to your server
mycursor = myconnection.cursor()

# Instance Variables (these have to be set to 0 for every user session)
panCardDocuments = 0
aadhaarCardDocuments = 0
chequeDocuments = 0
linksDict = dict()

# Input filepath
filepath = str(input("Enter the folder path"))

# Convert All Files To PNG
stage0Prelim.convertAllFilesToPng(filepath)

# check for pre-named files
namedDict = Stage1CheckForNamed.checkForNamed(filepath)

# unnamed classification
Stage1UnnamedAlt.recognizeFiles(filepath, namedDict)

# pan and aadhaar extraction
panAadhaarDetailsTuple = Stage2.sortInformation(filepath)

# split the filepath
splitFilePath = list(os.path.split(filepath))

# check for the existence of separate PAN, Aadhaar, Cheque folders
filepathForChecking = str()
for i in range (0, len(splitFilePath) - 2): # Assuming we have to move two directories back
    word = splitFilePath[i]
    filepathForChecking = os.path.join(filepathForChecking, word)

foldersNeeded = ("PANCard", "AadhaarCard", "CancelledCheque")
for thing in foldersNeeded:
    pathToFolder = os.path.join(filepathForChecking, thing)
    if not os.path.exists(pathToFolder):
        exit(69) # Prevent code from erroring out in future and throwing non-excepted errors

# Copy files to these folders
    pathToBorrowerDocs = os.path.join(filepathForChecking, "Borrower Docs")
    if not os.path.exists(pathToBorrowerDocs):
        exit()
    for document in os.listdir(pathToBorrowerDocs):
        # PAN
        if "PAN" in document:
            source = os.path.join(pathToBorrowerDocs, document)
            nameAndLoanID = splitFilePath[len(splitFilePath) - 1]
            destination = os.path.join(filepathForChecking, "PANCard", nameAndLoanID + "Page_" + str(panCardDocuments + 1))
            shutil.move(source, destination)
            panCardDocuments += 1
            if panCardDocuments == 1:
                linkToPanCard = destination
        elif "AADHAAR" in document:
            source = os.path.join(pathToBorrowerDocs, document)
            nameAndLoanID = splitFilePath[len(splitFilePath) - 1]
            destination = os.path.join(filepathForChecking, "AadhaarCard", nameAndLoanID)
            shutil.move(source, destination)
            aadhaarCardDocuments += 1
            if aadhaarCardDocuments == 1:
                linkToAadhaarCard = destination
        elif "CHEQUE" in document:
            source = os.path.join(pathToBorrowerDocs, document)
            nameAndLoanID = splitFilePath[len(splitFilePath) - 1]
            destination = os.path.join(filepathForChecking, "CancelledCheque", nameAndLoanID)
            shutil.move(source, destination)
            chequeDocuments += 1
            if chequeDocuments == 1:
                linkToCancelledCheque = destination

# Check of existence of these variables and create another tuple
if "linkToCancelledCheque" in globals().keys():
    linksDict["Cancelled Cheque"] = globals().get("linkToCancelledCheque")
if "linkToPanCard" in globals().keys():
    linksDict["PAN card"] = globals().get("linkToPanCard")
if "linkToAadhaarCard" in globals().keys():
    linksDict["Aadhaar Card"] = globals().get("linkToAadhaarCard")


''' 
Here is where we pull data from Google Forms
and convert it to a Pandas Dataframe
'''
# Define the scope
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# Add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secrets.json', scope)

# Authorize the clientsheet
client = gspread.authorize(creds)

# Open spreadsheet
sheet = client.open("Faircent Demo Form (Responses)")
sheet_instance = sheet.get_worksheet(0)

# Get the last row and the data corresponding to it
numberOfColumns = sheet_instance.row_count
customerDataFrame = pd.DataFrame(sheet_instance.row_values(numberOfColumns))

# Assign values to another dictionary
customerDetails = dict()
customerDetails["firstName"] = customerDataFrame["First Name"]
customerDetails["lastName"] = customerDataFrame["Last Name"]
customerDetails["age"] = customerDataFrame["Age"]
customerDetails["gender"] = customerDataFrame["Gender"]
customerDetails["address"] = customerDataFrame["Address"]
customerDetails["city"] = customerDataFrame["City"]
customerDetails["state"] = customerDataFrame["State"]
customerDetails["pinCode"] = customerDataFrame["PIN code"]
customerDetails["bloodGroup"] = customerDataFrame["Blood Group"]
customerDetails["annualIncome"] = customerDataFrame["Annual Income for the Financial Year 2021-22"]
customerDetails["panNumberAsSubmitted"] = customerDataFrame["PAN Number"]
customerDetails["aadhaarNumberAsSubmitted"] = customerDataFrame["Aadhaar Number"]
customerDetails["loanAmountDesired"] = customerDataFrame["Loan Amount needed in Indian Rupees"]
customerDetails["loanPurpose"] = customerDataFrame["Purpose of Loan"]
customerDetails["emailID"] = customerDataFrame["Email Address"]
customerDetails["mobileNumber"] = customerDataFrame["Mobile Number"]
customerDetails["dob"] = customerDataFrame["Date of Birth"]
customerDetails["panCardName"] = customerDataFrame["Name on PAN Card"]
customerDetails["aadhaarCardName"] = customerDataFrame["Name on Aadhaar Card"]

# Generate loan ID
with open("listOfLoanIDTaken.json", "r") as file:
    data = json.load(file)
    listOfLoanIDAlreadyTaken = list(data["text"])
loanIDCorrectlyGenerated = False
while not loanIDCorrectlyGenerated:
    potentialLoanID = random.randint(100000000, 2000000000)
    if str(potentialLoanID) not in listOfLoanIDAlreadyTaken:
        loanIDCorrectlyGenerated = True
        loanIDFinal = potentialLoanID
    else:
        loanIDCorrectlyGenerated = False
listOfLoanIDAlreadyTaken.append(str(loanIDFinal))
with open("listOfLoanIDTaken.json", "w+") as file: # Update JSON file containing the already allotted loan IDs
    json_object = json.load(file)
    json_object["data"] = listOfLoanIDAlreadyTaken


# date of registration
dateRegistration = datetime.today()

# mySQL variables definition
sql1 = "insert into demo (loanID, firstNameAsSubmitted, lastNameAsSubmitted, emailID, mobileNumber, gender, dateOfBirth, address, city, state, pincode, loanAmountDesired, loanPurpose, aadhaarNumberAsSubmitted, aadhaarNumber, panNumberAsSubmitted, panNumber, nameOnPanCard, nameonAadhaarCard, dateOfRegistration"
sql2 = " values(%S, %S, %S, %S, %S, %S, %S, %S, %S, %S, %S, %S, %S, %S, %S, %S, %S, %S, %S, %S)"
values = (loanIDFinal,)
values = values + (customerDetails["firstName"], customerDetails["lastName"])
values = values + (customerDetails["emailID"], customerDetails["mobileNumber"])
values = values + (customerDetails["gender"], customerDetails["dob"])
values = values + (customerDetails["address"], customerDetails["city"], customerDetails["state"], customerDetails["pinCode"])
values = values + (customerDetails["loanAmountDesired"], customerDetails["loanPurpose"])
values = values + (customerDetails["aadhaarNumberAsSubmitted"], panAadhaarDetailsTuple[1])
values = values + (customerDetails["panNumberAsSubmitted"], panAadhaarDetailsTuple[0])
values = values + (customerDetails["panCardName"], customerDetails["aadhaarCardName"], dateRegistration.strftime("%D//%M//%Y"))

# mySQL command run
mycursor.execute(sql1 + sql2, values)
myconnection.commit()

# I am operating under the assumption that basic checks for PAN and Aadhaar will be done from data collection end.

