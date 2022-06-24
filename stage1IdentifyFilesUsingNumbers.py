# This piece of code identifies files based on their OCR results


# Instance variables go here
import os

ocrResultsPath = # Insert path to OCR results here (absolute)
ocrBasePath = # Insert path to the OCR base files (database of OCR.txt files pre-generated)

# Functions begin here

def checkForDocument(resultPath): # Argument has to be filled with path to the customer folder
    # Condition for preliminary PAN card = First three chars A-Z, fourth recognizer, fifth Surname first letter, 6-9 chars 0-9, 10th char checksum
    for document in os.listdir(resultPath):
        if ".txt" in os.path.join(resultPath, document): #Only text files will pass this check
            with open(os.path.join(resultPath, document), "r+") as file:
                stringObtained = file.read()
                for i in range (0, len(stringObtained)):
                    if (ord(stringObtained[i]) in range(65, 91) and
                            ord(stringObtained[i+1]) in range(65, 91) and
                            ord(stringObtained[i+2]) in range(65, 91) and
                            ord(stringObtained[i+3]) in (67, 80, 72, 70, 65, 84, 66, 76, 74, 71) and
                            ord(stringObtained[i+4]) == ((list(os.path.join(resultPath, document).split("\\")))[2])[0] and  #First letter of second item (separated by dash)
                            stringObtained[i+5] in range(0, 10) and
                            stringObtained[i+6] in range(0, 10) and
                            stringObtained[i+7] in range(0, 10) and
                            stringObtained[i+8] in range(0, 10) and
                            ord(stringObtained[i+9]) in range(65, 91)):
                        source = os.path.join(resultPath, document)
                        destination = os.path.join(resultPath, "_PAN.png")
                        os.rename(source, destination)
                    elif (stringObtained[i] in range(0,10) and
                            stringObtained[i+1] in range(0, 10) and
                            stringObtained[i+2] in range(0, 10) and
                            stringObtained[i+3] in range(0, 10) and
                            stringObtained[i+4] in range(0, 10) and
                            stringObtained[i+5] in range(0, 10) and
                            stringObtained[i+6] in range(0, 10) and
                            stringObtained[i+7] in range(0, 10) and
                            stringObtained[i+8] in range(0, 10) and
                            stringObtained[i+9] in range(0, 10) and
                            stringObtained[i+10] in range(0, 10) and
                            stringObtained[i+11] in range(0, 10)):
                        source = os.path.join(resultPath, document)
                        destination = os.path.join(resultPath, "_AADHAR.png")
                        os.rename(source, destination)
                    elif ("bank" in stringObtained):






