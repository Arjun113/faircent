# This code checks for the existence of an obviously named file
import os
from spellchecker import SpellChecker
spell = SpellChecker()
def checkForNamed(filepath):
    edited_names = dict()
    namedOrNot = dict()
    if os.path.exists(filepath) == False:
        return
    for document in os.listdir(filepath):
        editedString = ""
        usableName = document[0:len(document)-4]
        usableNameLower = usableName.lower()
        wordListName = list(usableNameLower.split(" "))
        misspelled = spell.unknown(wordListName)
        usableNameLowerCorrected = str()
        for j in range (0, len(wordListName)):
            if wordListName[j] in misspelled:
                wordListName[j] = spell.correction(wordListName[j])
        for word in wordListName:
            usableNameLowerCorrected += word
        usableNameLowerCorrectedletterwise = list(usableNameLowerCorrected)
        for i in range(0, len(usableNameLowerCorrectedletterwise)):
            if usableNameLowerCorrectedletterwise[i] not in [" ", ".", ",", ":","\\","]", "[", "(", ")", "*", "#", "@", "!", "%", "^", "&", "`", "~", "<", ">", "?", "/", "|","-", "_", "=", "+", "{","}", ";", "/'", '"']:
                editedString = editedString + usableNameLowerCorrectedletterwise[i]
        edited_names[document] = editedString

    fileNameList = list(edited_names.keys())
    panFileCount = 0
    aadhaarFileCount = 0
    bankstatementFileCount = 0
    passbookFileCount = 0
    chequeFileCount = 0
    rentFileCount = 0
    payslipFileCount = 0
    billFileCount = 0
    itrFileCount = 0
    for i in range(0, len(fileNameList)):
        name = edited_names.get(fileNameList[i])
        if "pan" in name:
            panFileCount += 1
            source = os.path.join(filepath, fileNameList[i])
            splitPath = list(filepath.split("\\"))
            dest = os.path.join(filepath, splitPath[len(splitPath)-1] + "_PAN" + str(panFileCount) + ".png")
            os.rename(source, dest)
            namedOrNot[dest] = True
        elif "aadhaar" in name or "adhaar" in name or "aadhar" in name or "adhar" in name:
            aadhaarFileCount += 1
            source = os.path.join(filepath, fileNameList[i])
            splitPath = list(filepath.split("\\"))
            dest = os.path.join(filepath, splitPath[len(splitPath) - 1] + "_ADHR" + str(aadhaarFileCount) + ".png")
            os.rename(source, dest)
            namedOrNot[dest] = True
        elif "statement" in name:
            bankstatementFileCount += 1
            source = os.path.join(filepath, fileNameList[i])
            splitPath = list(filepath.split("\\"))
            dest = os.path.join(filepath, splitPath[len(splitPath) - 1] + "_BANK" + str(bankstatementFileCount) + ".png")
            os.rename(source, dest)
            namedOrNot[dest] = True
        elif "passbook" in name or "pasbook" in name:
            passbookFileCount += 1
            source = os.path.join(filepath, fileNameList[i])
            splitPath = list(filepath.split("\\"))
            dest = os.path.join(filepath, splitPath[len(splitPath) - 1] + "_PASSBOOK" + str(passbookFileCount) + ".png")
            os.rename(source, dest)
            namedOrNot[dest] = True
        elif "cheque" in name or "check" in name or "cheq" in name:
            chequeFileCount += 1
            source = os.path.join(filepath, fileNameList[i])
            splitPath = list(filepath.split("\\"))
            dest = os.path.join(filepath, splitPath[len(splitPath) - 1] + "_CHEQUE" + str(chequeFileCount) + ".png")
            os.rename(source, dest)
            namedOrNot[dest] = True
        elif "rent" in name:
            rentFileCount += 1
            source = os.path.join(filepath, fileNameList[i])
            splitPath = list(filepath.split("\\"))
            dest = os.path.join(filepath, splitPath[len(splitPath) - 1] + "_RENTAGREEMENT" + str(rentFileCount) + ".png")
            os.rename(source, dest)
            namedOrNot[dest] = True
        elif "payslip" in name or "salary" in name or "salry" in name:
            payslipFileCount += 1
            source = os.path.join(filepath, fileNameList[i])
            splitPath = list(filepath.split("\\"))
            dest = os.path.join(filepath, splitPath[len(splitPath) - 1] + "_PAYSLIP" + str(payslipFileCount) + ".png")
            os.rename(source, dest)
            namedOrNot[dest] = True
        elif 'bill' in name:
            billFileCount += 1
            source = os.path.join(filepath, fileNameList[i])
            splitPath = list(filepath.split("\\"))
            dest = os.path.join(filepath, splitPath[len(splitPath) - 1] + "_BILL" + str(billFileCount) + ".png")
            os.rename(source, dest)
            namedOrNot[dest] = True
        elif 'income' in name or 'tax' in name or 'return' in name or 'itr' in name:
            itrFileCount += 1
            source = os.path.join(filepath, fileNameList[i])
            splitPath = list(filepath.split("\\"))
            dest = os.path.join(filepath, splitPath[len(splitPath) - 1] + "_ITR" + str(itrFileCount) + ".png")
            os.rename(source, dest)
            namedOrNot[dest] = True
        else:
            # If nothing can be figured out, send to unnamed classifier
            # We will add functions here for this.
            namedOrNot[os.path.join(filepath, fileNameList[i])] = False
        return namedOrNot
