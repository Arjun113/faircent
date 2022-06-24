import os
import json

# Instance variables and paths go here
panNumber = None
aadhaarNumber = None

# Code begins here
def sortInformation(folderpath):
    global panNumber
    global aadhaarNumber
    folderpathSplit = list(os.path.split(folderpath))
    nameAndLoanID = folderpathSplit[len(folderpathSplit) - 1]

    for document in os.listdir(folderpath):
        if "out_" in document:
            if "PAN" in document or "AADHAAR" in document:
                with open(document, "r") as f:
                    parsedJSON = json.load(f)
                    parsedJSONText = parsedJSON["text"]
                    for word in parsedJSONText:
                        # PAN Number checks here
                        if (len(word) == 10 and
                                ord(word[0]) in range (97, 123) and
                                ord(word[1]) in range (97, 123) and
                                ord(word[2]) in range (97, 123) and
                                ord(word[3]) in [67, 80, 72, 70, 65, 84, 66, 76, 74, 71] and
                                ord(word[4]) in range(97, 123) and
                                word[5] in range (0, 10) and
                                word[6] in range (0, 10) and
                                word[7] in range (0, 10) and
                                word[8] in range (0, 10) and
                                ord(word[9]) in range (97, 123)):
                                    panNumber = word
            if "AADHAAR" in document:
                with open(document, 'r') as f:
                    parsedJSON = json.load(f)
                    parsedJSONText = parsedJSON["text"]
                    # There can be three possibilities: Aadhaar being recognized as one block, set of two blocks and three blocks
                    for i in range (0, len(parsedJSONText) - 3):
                        if parsedJSONText[i] in range (0, 9999999999):
                            aadhaarNumber = parsedJSONText[i]
            if "BANKSTATEMENT" in document:
                with open(document, "r") as f:
                    parsedJSON = json.load(f)
                    parsedJSONText = parsedJSON["text"]
                    # Add any conditions here
            if "CHEQUE" in document:
                with open(document, "r") as f:
                    parsedJSON = json.load(f)
                    parsedJSONText = parsedJSON["text"]
                    # Add any conditions here
        return (panNumber, aadhaarNumber)




