'''--*   MIHX   *--

作者:MINOR
日期:2021年11月27日15时00分'''
import matplotlib.pyplot as plt
import cv2

image = cv2.imread('../tupian/lena.png')#从文件夹中提取图片

#定义一个函数lena image表示函数的形参 (minVal=100,maxVal=200)表示最小阈值和最大阈值
def lena(image,minVal=100,maxVal=200):
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)#将原始图片的BGR格式转换为RGB格式
    image = cv2.Canny(image,minVal,maxVal)#调用cv2.Canny对图像进行处理
    plt.imshow(image)#显示处理后的image图像
    plt.axis('off')#去除显示图像的坐标轴
    plt.show()#输出图像
lena(image)#调用函数 将图片作为实参传回给形参
cv2.imwrite('../tupian/lena2.png',image)#保存处理后的图像 并命名为lena2.png