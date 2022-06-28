# Faircent Internship
## Arjun Sanghi

This bundle of files consists of the following files: 
1. `stage0Prelim.py` pulls files from a given folder and converts them all to a single format. In this case, for ease of conversion, speed and quality, I have converted all files to PNG. In-case of PDF files where one file can contain one or more pages, each page will be converted to a single PNG file with `Page_n` as part of the filename where *n* is the page number of the image in the original PDF file. The code saves everything to the same folder and deletes all the original PDF/JPG files from the folder. 
2. `Stage1CheckForNamed.py` exists to check for already obviously named files and renames them in a set format. For example, if a file contains the word **PAN** or any similar variation in it, we can reasonably assume that it contains an image or scan of a PAN card. This check is done in order to eliminate obviously named files, as OCR is resource-hungry and takes time. The code renames such files in the same folder.
3. `Stage1Unnamed.py` is one way to run OCR. However, due to Tesseract's inability to correctly process most files, using this code is not recommended without major changes to the model.
4. `Stage1UnnamedAlt.py` is my recommended way to run OCR. This uses MMOCR to pull details and categorize the files. In the current state, it can only accurately pull aadhaar and pan numbers. 
5. `Stage1IdentifyFilesUsingNumbers` further checks the numbers obtained from MMOCR to determine whether the numbers are valid and double-checks whether the files are accurately named. 
6. `driverCode.py` obtains the current date, imports other data from a Google Drive sheet that is connected to Google Forms, and inserts it all into a pre-set mySQL database.
   
The code is fully modular and all the dependencies are mentioned in `requirements.txt` so that it is easy to work on this code. 
<br>
MMOCR prefers GPU to CPU, however, the Windows support for CUDA on MMOCR is not good. To that extent, I have been testing on CPU only. For faster inference, kindly download the CUDA version of the applicabl libraries and run this on a supported NVIDIA GPU. 
<br>
<br>
### Goals:
1. Increase accuracy to 90+%, possibly via implementation of an in-house model trained using 10lakh+ customers' data. 
2. Increase inference speed using CUDA Toolkit and platform-specific recompilation instead of the current platform-agnostic versions.
<br>

mySQL database has the following columns and is named *faircent1*
![](2022-06-28-12-20-55.png)


All paths are set for my system. I have included comments wherever path needs to be changed for the system. 
<br>
My System: Windows 11, Ryzen 9 5900HS, RTX 3070, 24GB RAM, 1TB SSD. 
<br>
### Dataset credit: M. Sohail

