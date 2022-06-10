import os
import pytesseract
import cv2
from PIL import Image
import numpy as np


def deSkewThresh(image):
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

path = "C:\\Users\\Arjun Sanghi\\Desktop\\Foreign Admission\\Faircent\\Work 1\\Data for OCR back\\Aadhaar card"
for image in os.listdir(path):
    img = cv2.imread(os.path.join(path, image))
    imgGrayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgGrayScaleDenoise = cv2.medianBlur(imgGrayscale, 5)
    imgGrayScaleDenoiseRotated = deSkewThresh(imgGrayScaleDenoise)
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, imgGrayScaleDenoiseRotated)
    textObtained = pytesseract.image_to_string(Image.open(filename))
    with open(os.path.join(path,image[0:len(image)-4]) + ".txt", "w+") as writefile:
        writefile.write(textObtained)



