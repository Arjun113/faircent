'''
The classification is split into named and unnamed in order to save server cycles.
Incase it is noticed that named does not have any tangible effect or causes errors in recognition,
we will change the entire process to go through unnamed.
The way to do it is to remove the if condition check for whether the file is named or not
'''

import os
import json
from spellchecker import SpellChecker
from translate import Translator
from mmocr.utils.ocr import MMOCR
from PIL import Image

mmocr_config_dir = "C:\\Users\\ArjunSanghi\\Desktop\\Foreign Admission\\Faircent\\Work 1\\mmocr\\configs" # Change this for your system
mmocr = MMOCR(config_dir= mmocr_config_dir)
spellcheck = SpellChecker()
translate = Translator(to_lang='en')

def recognizeFiles(filepath, namedict):
    panDocumentCounter = 0
    aadharDocumentCounter = 0
    chequeDocumentCounter = 0
    rentAgreementDocumentCounter = 0
    bankStatementDocumentCounter = 0
    if os.path.exists(filepath) == False:
        return
    results = mmocr.readtext(filepath, export = filepath)

    for document in os.listdir(filepath):
        numberOfEmptyStrings = 0
        os.mkdir(os.path.join(filepath, "temp"))
        imageCorrectlyOCRed = False
        # MMOCR dictates that empty strings will usually be found when the content is not rotated correctly
        # I will use this property to check for rotation and correct it
        if "out_" in document:
            while imageCorrectlyOCRed == False:
                imageCorrectlyOCRed = True
                with open(os.path.join(filepath, document), "r") as f:
                    parsedJSONDict = json.load(f)
                    usableText = list(parsedJSONDict.get("text"))
                    for word in usableText:
                        if word == "":
                            numberOfEmptyStrings += 1
                    if numberOfEmptyStrings >= 5: # Change this as per results seen
                        # Image not rotated correctly
                        imageCorrectlyOCRed = False
                        with Image.open(os.path.join(filepath, document[4:len(document) - 4] + ".png")) as img:
                            img.rotate(90).save(os.path.join(filepath, "temp\\" + document[4:len(document) - 4] + ".png"))
                        result = mmocr.readtext(os.path.join(filepath, "temp\\" + document[4:len(document) - 4] + ".png"), export = filepath)
                    else:
                        imageCorrectlyOCRed = True
                    f.close()



    for document in os.listdir(filepath):
        if "out_" in document:
            with open(os.path.join(filepath, document), "r") as f:
                parsedJSONDict = json.load(f)
                usableText = list(parsedJSONDict.get("text"))
                misspelled = spellcheck.unknown(usableText)
                for i in range (0, len(usableText)):
                    if usableText[i] in misspelled:
                        usableText[i] = spellcheck.correction(usableText[i])
                # PAN card verification
                if "permanent" in usableText and "account" in usableText and "number" in usableText:
                    # Renaming
                    source = os.path.join(filepath, document[4:len(document) - 4] + ".png")
                    dest = os.path.join(filepath, "_PAN" + str(panDocumentCounter) + ".png")
                    os.rename(source, dest)
                    panDocumentCounter += 1
                # Aadhaar card verification
                if "aadhaar" in usableText:
                    # Renaming
                    source = os.path.join(filepath, document[4:len(document) - 4] + ".png")
                    dest = os.path.join(filepath, "_AADHAAR" + str(aadharDocumentCounter) + ".png")
                    os.rename(source, dest)
                    aadharDocumentCounter += 1
                # Bank Statement
                if "statement" in usableText:
                    # Renaming
                    source = os.path.join(filepath, document[4:len(document) - 4] + ".png")
                    dest = os.path.join(filepath, "_BANKSTATEMENT" + str(bankStatementDocumentCounter) + ".png")
                    os.rename(source, dest)
                    bankStatementDocumentCounter += 1
                # Cheque
                if "bank" in usableText or "payable" in usableText or "bearer" in usableText:
                    # Renaming
                    source = os.path.join(filepath, document[4:len(document) - 4] + ".png")
                    dest = os.path.join(filepath, "_CHEQUE" + str(chequeDocumentCounter) + ".png")
                    os.rename(source, dest)
                    chequeDocumentCounter += 1














