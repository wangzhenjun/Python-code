import re
from pytesser import *

def image_to_txt(img):
    return tesseract(img)
def tesseract(img):
    text = image_to_string(img)
    text = re.sub('[\W]','',text)
    return text

