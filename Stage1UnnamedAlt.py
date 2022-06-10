'''
The classification is split into named and unnamed in order to save server cycles.
Incase it is noticed that named does not have any tangible effect or causes errors in recognition,
we will change the entire process to go through unnamed.
The way to do it is to remove the if condition check for whether the file is named or not
'''

import os
from spellchecker import SpellChecker
from translate import Translator
from mmocr.utils.ocr import MMOCR

mmocr = MMOCR(det = None, recog = "CRNN_TPS")
spellcheck = SpellChecker()
translate = Translator(to_lang='en')

ocrBaseFilesPath = # Indicate the path for the base OCR recognition if needed. Should not be necessary at all

def recognizeFiles(filepath, namedict):
    if os.path.exists(filepath) == False:
        return
    for document in os.listdir(filepath):
        splitPath = list(filepath.split("\\"))
        usedPath = os.path.join(splitPath[len(splitPath-1)], document)
        namedictKeys = namedict.keys()






