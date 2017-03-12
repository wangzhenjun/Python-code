from cStringIO import StringIO
from PIL import Image

def image_data_to_tiff(img_path):
    img = Image.open(img_path)
    img = img.convert('RGBA')

    img = binarize_image(img)
    img = img.convert('L')
    return img

def binarize_image(img):
    pixdata = img.load()
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x,y][0]<100 or pixdata[x,y][1]<100 or pixdata[x,y][2]<100:
                pixdata[x,y] = (0,0,0,255)
            else:
                pixdata[x,y] = (255,255,255,255)
    return img
