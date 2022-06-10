from mmocr.utils.ocr import MMOCR

ocr = MMOCR(config_dir="C:\\Users\\ArjunSanghi\\Desktop\\Foreign Admission\\Faircent\\Work 1\\mmocr\\configs")
results = ocr.readtext("C:\\Users\\ArjunSanghi\\Desktop\\Foreign Admission\\Faircent\\Work 1\\TestForMMOCR", export = "C:\\\\Users\\ArjunSanghi\\Desktop\\Foreign Admission\\Faircent\\Work 1\\TestForMMOCR")