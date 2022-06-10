# Change lines 21 and 22 for the path. I have used os.path.join according to my system configuration. Please change it for your own configuration.
# Libraries are to kept static (always uncompressed, compiled and in memory)
# Add your base files path in line 16

import cv2
import numpy as np
import pytesseract
import os
from PIL import Image
from spellchecker import SpellChecker
from translate import Translator
import subprocess
from mmocr.utils.ocr import MMOCR

translate = Translator(to_lang="en")
spellcheck = SpellChecker()
mmocr = MMOCR()

ocrBaseFilesPath =
pythonPathLocalChangerLine = r"set PYTHONPATH = C:\Users\Arjun Sanghi\Desktop\Foreign Admission\Faircent\Work 1\ultimateMICR-SDK-master\binaries\windows\x86_64; C:\Users\Arjun Sanghi\Desktop\Foreign Admission\Faircent\Work 1\ultimateMICR-SDK-master\python"

def recognizeFiles(filepath, namedict):
    if os.path.exists(filepath) == False:
        return
    splitPath = list(filepath.split("\\"))
    usedPath = splitPath[len(splitPath)-1]
    for document in os.listdir(filepath):
        folderPathAsUsed = os.path.join(usedPath, document)
        if namedict.get(folderPathAsUsed) == 0:
            textReturnedByInferenceRunOnImage = runOCR(filepath, document)
            textReturnedAfterSpellcheck = spellcheckGatheredData(textReturnedByInferenceRunOnImage)
            textReturnedAfterTranslation = translateGatheredData(textReturnedAfterSpellcheck)
        with open(os.path.join(filepath, document[0:len(document)-4] + ".txt"), "w+") as f:
            f.write(textReturnedAfterTranslation)







def runOCR(filePath, document):
    img = cv2.imread(os.path.join(filePath, document))
    imgGrayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgGrayScaleDenoiseRotated = deskewThresh(imgGrayscale)
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, imgGrayScaleDenoiseRotated)
    textObtained = pytesseract.image_to_string(Image.open(filename))
    return textObtained





def deskewThresh(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    rotated2 = cv2.threshold(rotated, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    return rotated2


def spellcheckGatheredData(textObtained):
    textObtainedSplit = textObtained.split(" ")
    textObtainedSplitSpellcorrected = list()
    textObtainedSplitSpellcorrectedstr = str()
    editedString = str()
    misspelled = spellcheck.unknown(textObtainedSplit)
    k = 0
    for word in textObtainedSplit:
        if word in misspelled:
            textObtainedSplitSpellcorrected[k] = spellcheck.correction(word)
        k = k + 1
    for i in range(0, len(textObtainedSplitSpellcorrected)):
        textObtainedSplitSpellcorrectedstr += textObtainedSplitSpellcorrected[i]
    textObtainedSplitSpellcorrected = list(textObtainedSplitSpellcorrectedstr)
    for i in range(0, len(textObtainedSplitSpellcorrected)):
        if textObtainedSplitSpellcorrected[i] not in [" ", ".", ",", ":", "\\", "]", "[", "(", ")", "*", "#", "@", "!", "%",
                                               "^", "&", "`", "~", "<", ">", "?", "/", "|", "-", "_", "=", "+", "{",
                                               "}", ";", "/'", '"']:
            editedString = editedString + textObtainedSplitSpellcorrected[i]
    return editedString

def translateGatheredData(textObtainedSplitSpellcorrected):
    textObtainedSpellcorrectedTranslated = list()
    k = 0
    for word in textObtainedSplitSpellcorrected:
        intermediateWord = translate.translate(word)
        textObtainedSpellcorrectedTranslated[k] = intermediateWord
    stringFormOfTranslatedData = str(textObtainedSpellcorrectedTranslated)
    return stringFormOfTranslatedData


def chequeRecognition(filepath, document):
    subprocess.run("")
    subprocess.run("setlocal")
    subprocess.run(pythonPathLocalChangerLine)
    subprocess.run(["python", "recognizer.py", "--image", "# give path", os.path.join(filepath,document), "C:\\Users\\Arjun Sanghi\\Desktop\Foreign Admission\\Faircent\\Work 1\\ultimateMICR-SDK-master\\assets", "--format", "e13b"])
    subprocess.run("endlocal")
