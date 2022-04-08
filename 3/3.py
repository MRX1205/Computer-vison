'''--*   MIHX   *--

作者:MINOR
日期:2021年11月27日21时16分'''
import cv2
import matplotlib.pyplot as plt
import numpy as np

def image(img):
    father_picture = r"../tupian/"
    return"{}{}".format(father_picture,img)#定义一个函数来读取图片的路径
image = cv2.imread(image('coins.jpg'))#读取原始图片
images = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#将原始图片BGR格式转为GRAY格式 灰度图
#relt coins 分别为用cv2.threshold函数处理处理出来的图像的名字和图像内容
#cv2.THRESH_BINARY为二值化方式 cv2.THRESH_OTSU为自动取阈值 这时最低阈值为0 255表示最大阈值
relt,coins = cv2.threshold(images,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#contours为轮廓 hierarchy为轮廓层次的内容
#cv2.findcontours函数表示查找图像的轮廓 cv2.RETR_EXTERNAL表示只检测图像的外部轮廓
#cv2.CHAIN_APPROX_SIMPLE表示存储图像的所有轮廓 coins表示对coins图像进行处理

contours, hierarchy= cv2.findContours(coins, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours函数表示在image图像中画出上面提取的外部轮廓
#-1表示为所有提取的轮廓 (0,255,0)表示绿色 2表示线条的粗细
cv2.drawContours(image,contours,-1,(0,255,0),2)
plt.imshow(image)#显示图像
plt.axis('off')
plt.show()#输出图像
cv2.imwrite('../tupian/coins2.png',image)#保存图像