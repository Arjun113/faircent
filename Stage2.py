import os
import json
from mmocr.utils.ocr import MMOCR
import mysql.connector

# Instance variables and paths go here
mmocr_config_dir =
mmocr = MMOCR(config_dir= mmocr_config_dir)

# mySQL initialization
mydb = mysql.connector.connect(host = 'localhost', username = "arjun", password = "arjun", database = "faircent1")
mycursor = mydb.cursor()

# Code begins here
def sortInformation(folderpath):
    folderpathSplit = list(os.path.split(folderpath))
    nameAndLoanID = folderpathSplit[len(folderpathSplit) - 1]

    for document in os.listdir(folderpath):
        if "PAN" in document:
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
           arju                 ord(word[9]) in range (97, 123)):
                                panNumber = word
        if "AADHAAR" in document:
            with open(document, 'r') as f:
                parsedJSON = json.load(f)
                parsedJSONText = parsedJSON["text"]
                # There can be three possibilities: Aadhaar being recognized as one block, set of two blocks and three blocks
                for i in range (0, len(parsedJSONText) - 3):
                    word1 = parsedJSONText[i]
                    word2 = parsedJSONText[i + 1]
                    word3 = parsedJSONText[i + 2]
                    if (len(word1) == 4 and word1 in range (0, 9999) and
                            len(word2) == 4 and word2 in range (0, 9999) and
                            len(word3) == 4 and word3 in range (0, 9999)):
                        aadhaarNumber = word1 + word2 + word3
        # Add more conditions here



