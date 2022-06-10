# This code converts all docs to a singular format in order to make it easier to process further
# This also helps improve the manual evaluators' experience in case they have to see these images
import os
from PIL import Image
import fitz

def convertAllFilesToPng(filepath):
    #Filepath is the only argument to this function
    ndocs  = 0
    for image in os.listdir(filepath):
        if image.endswith(".png"):
            ndocs = ndocs + 1
        elif image.endswith(".jpg") or image.endswith('.JPG'):
            imageProcess = Image.open(os.path.join(filepath, image))
            rgb_imageProcess = imageProcess.convert("RGB")
            newPath = (os.path.join(filepath, image))
            newPathEdit = newPath[0:len(newPath)-4] + ".png"
            rgb_imageProcess.save(newPathEdit, "PNG")
            imageProcess.close()
        elif image.endswith(".tiff"):
            imageProcess = Image.open(os.path.join(filepath, image))
            rgb_imageProcess = imageProcess.convert("RGB")
            newPath = (os.path.join(filepath, image))
            newPathEdit = newPath[0:len(newPath)-5] + ".png"
            rgb_imageProcess.save(newPathEdit, "PNG")
            imageProcess.close()
        elif image.endswith(".bmp"):
            imageProcess = Image.open(os.path.join(filepath, image))
            rgb_imageProcess = imageProcess.convert("RGB")
            newPath = (os.path.join(filepath, image))
            newPathEdit = newPath[0:len(newPath)-4] + ".png"
            rgb_imageProcess.save(newPathEdit, "PNG")
            imageProcess.close()
        elif image.endswith(".jpeg"):
            imageProcess = Image.open(os.path.join(filepath, image))
            rgb_imageProcess = imageProcess.convert("RGB")
            newPath = (os.path.join(filepath, image))
            newPathEdit = newPath[0:len(newPath)-5] + ".png"
            rgb_imageProcess.save(newPathEdit, "PNG")
            imageProcess.close()
        elif image.endswith(".webp"):
            imageProcess = Image.open(os.path.join(filepath, image))
            rgb_imageProcess = imageProcess.convert("RGB")
            newPath = (os.path.join(filepath, image))
            newPathEdit = newPath[0:len(newPath)-5] + ".png"
            rgb_imageProcess.save(newPathEdit, "PNG")
            imageProcess.close()
        elif image.endswith(".pdf"):
            execControl = True
            docverify = fitz.Document(os.path.join(filepath, image))
            if docverify.is_encrypted:
                execControl = False
            docverify.close()
            if execControl == True:
                document = fitz.open(os.path.join(filepath, image))
                i = 1
                for page in document:
                    pix = page.get_pixmap()
                    newPath = (os.path.join(filepath, image))
                    newPathEdit = newPath[0:len(newPath)-4] + "Page_" + str(i) + ".png"
                    pix.save(newPathEdit, "PNG")
                    i = i + 1
                document.close()

        else:
            # This will be a particularly rare case but has to be included in order to
            # prevent errors due to Pillow being unable to handle the other formats
            # Only super obscure formats will not work on this
            # This is designed to ignore mongoDB and txt files

            # Implement send to your workers' application and ignore this customer folder
            pass
    for image in os.listdir(filepath):
        if image.endswith(".png") == False:
            os.remove(os.path.join(filepath, image))







