# -*- coding: utf-8 -*-

from __future__ import print_function  #python2.7和python3共存的方式

from PIL import Image
from PIL import *
from svm import *
from svmutil import *

img_path = 'D:\\Users\\wzhj\\MachineLearning\\recogImage\\111649-20160715101301014-860377697.png'
img_path_2 = 'D:\\Users\\wzhj\\MachineLearning\\recogImage\\2.jpg'
image = Image.open(img_path_2)
#image.rotate(0.1).show()
imgry = image.convert('L')  # 转化为灰度图


def get_bin_table(threshold=200):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table

table = get_bin_table()
out = imgry.point(table, '1')
out.save('fun_binary.jpg')
print(out)


def sum_9_region(img, x, y):
    """
    9邻域框,以当前点为中心的田字框,黑点个数
    :param x:
    :param y:
    :return:
    """
    # todo 判断图片的长宽度下限
    cur_pixel = img.getpixel((x, y))  # 当前像素点的值
    width = img.width
    height = img.height

    if cur_pixel == 1:  # 如果当前点为白色区域,则不统计邻域值
        return 0

    if y == 0:  # 第一行
        if x == 0:  # 左上顶点,4邻域
            # 中心点旁边3个点
            sum = cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y + 1))
            return 4 - sum
        elif x == width - 1:  # 右上顶点
            sum = cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y + 1))

            return 4 - sum
        else:  # 最上非顶点,6邻域
            sum = img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y + 1)) \
                  + cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y + 1))
            return 6 - sum
    elif y == height - 1:  # 最下面一行
        if x == 0:  # 左下顶点
            # 中心点旁边3个点
            sum = cur_pixel \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y - 1)) \
                  + img.getpixel((x, y - 1))
            return 4 - sum
        elif x == width - 1:  # 右下顶点
            sum = cur_pixel \
                  + img.getpixel((x, y - 1)) \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y - 1))

            return 4 - sum
        else:  # 最下非顶点,6邻域
            sum = cur_pixel \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x, y - 1)) \
                  + img.getpixel((x - 1, y - 1)) \
                  + img.getpixel((x + 1, y - 1))
            return 6 - sum
    else:  # y不在边界
        if x == 0:  # 左边非顶点
            sum = img.getpixel((x, y - 1)) \
                  + cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x + 1, y - 1)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y + 1))

            return 6 - sum
        elif x == width - 1:  # 右边非顶点
            # print('%s,%s' % (x, y))
            sum = img.getpixel((x, y - 1)) \
                  + cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x - 1, y - 1)) \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y + 1))

            return 6 - sum
        else:  # 具备9领域条件的
            sum = img.getpixel((x - 1, y - 1)) \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y + 1)) \
                  + img.getpixel((x, y - 1)) \
                  + cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x + 1, y - 1)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y + 1))
            return 9 - sum


#去噪声

print (sum_9_region(out,0,1))

#图片字符切割
def get_crop_imgs(img):
    """
    按照图片的特点,进行切割,这个要根据具体的验证码来进行工作. # 见原理图
    :param img:
    :return:
    """
    child_img_list = []
    for i in range(6):
        x = 0 + i * (6 + 4)  # 见原理图
        y = 0
        child_img = img.crop((x, y+24, x + 18, y + 40))
        child_img_list.append(child_img)

    return child_img_list

child_img_list =get_crop_imgs(out)
for i in range(len(child_img_list)):
    child_img_list[i].save('%s .jpg' % i)
print(child_img_list[0].save('0.jpg'))
def get_feature(img):
    """
    获取指定图片的特征值,
    1. 按照每排的像素点,高度为10,则有10个维度,然后为6列,总共16个维度
    :param img_path:
    :return:一个维度为10（高度）的列表
    """

    width, height = img.size

    pixel_cnt_list = []
    height = 10
    for y in range(height):
        pix_cnt_x = 0
        for x in range(width):
            if img.getpixel((x, y)) == 0:  # 黑色点
                pix_cnt_x += 1

        pixel_cnt_list.append(pix_cnt_x)

    for x in range(width):
        pix_cnt_y = 0
        for y in range(height):
            if img.getpixel((x, y)) == 0:  # 黑色点
                pix_cnt_y += 1

        pixel_cnt_list.append(pix_cnt_y)

    return pixel_cnt_list

print(get_feature(child_img_list[0]))
svm_root = ""
def train_svm_model():
    """
    训练并生成model文件
    :return:
    """
    y, x = svm_read_problem(svm_root + '/train_pix_feature_xy.txt')
    model = svm_train(y, x)
    svm_save_model(model_path, model)


def svm_model_test():
    """
    使用测试集测试模型
    :return:
    """
    yt, xt = svm_read_problem(svm_root + '/last_test_pix_xy_new.txt')
    model = svm_load_model(model_path)
    p_label, p_acc, p_val = svm_predict(yt, xt, model)#p_label即为识别的结果

    cnt = 0
    for item in p_label:
        print('%d' % item, end=',')
        cnt += 1
        if cnt % 8 == 0:
            print('')


model_path = ''