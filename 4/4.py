'''--*   MIHX   *--

作者:MINOR
日期:2021年11月28日11时39分'''
import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('D:/python/lianxi/kaohe/tupian/A.png')#导入图片
image_template = cv2.imread('D:/python/lianxi/kaohe/tupian/A4.jpg')#导入模板图片
width = image_template.shape[0]#模板图片的宽
height = image_template.shape[1]#模板图片的高
print(width)
print(height)
#cv2.matchTemplate(模板匹配函数 cv2.TM_SQDIFF平方差匹配算法
res = cv2.matchTemplate(image,image_template,cv2.TM_SQDIFF)
min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)#定义最大最小值 最大最小位置
top_left = min_loc#定义左上角为最小位置 起点
#右下角=左上角加模板图片的宽 左上角加上图片的高
bottom_right = (top_left[0]+width,top_left[1]+height)
cv2.rectangle(image,top_left,bottom_right,(0,255,0),2)#在匹配结果上画一个线大小为2的绿色矩形
plt.imshow(image)#输出图片
plt.axis('off')#去除坐标轴
plt.show()
cv2.imwrite('../tupian/A2.png',image)