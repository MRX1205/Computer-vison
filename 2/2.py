'''--*   MIHX   *--

作者:MINOR
日期:2021年11月27日15时45分'''
import matplotlib.pyplot as plt
import cv2

image = cv2.imread('../tupian/lenanoise.png')#读取图片
#用cv2.getStructuringElement函数  cv2.MORPH_RECT新建一个5*5的矩形卷积核
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)#变灰度图
#cv2.morphologyEx处理函数 cv2.MORPH_OPEN为处理方式  kernel处理范围
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)#开运算处理图像 先腐蚀后膨胀，作用是去除图片中的小白点
closeing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)#闭运算 处理图像 去除小黑点
plt.imshow(closeing)#输出图像
plt.axis('off')
plt.show()
cv2.imwrite('../tupian/lenaoise2.png',closeing)

