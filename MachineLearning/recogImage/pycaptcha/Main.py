
import image,captcha
import ImageEnhance

img_path = 'E:\\yixin\\920435.png'


if __name__ == '__main__':
    # img = image.image_data_to_tiff(img_path)
    # text = captcha.image_to_txt(img)
    # print text

    enhancer = ImageEnhance.Contrast(image)
    image_enhancer = enhancer.enhance(4)
    print image_to_string(image_enhancer)
