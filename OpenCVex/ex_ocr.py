import pytesseract
from PIL import Image
import os

def run():
    # pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tessaract"

    img = os.path.join(os.path.split(os.path.abspath(__file__))[0], "ocr.jpg")
    print img
    if not os.path.isfile(img):
        print "Image not present"
        return False
    else:
        im = Image.open(img)
        #print im
        st = pytesseract.image_to_string(im)
        print st

if __name__ == "__main__":
    run()