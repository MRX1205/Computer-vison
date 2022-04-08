'''--*   MIHX   *--

作者:MINOR
日期:2021年11月29日23时30分'''
import cv2
import matplotlib.pyplot as plt
cap = cv2.VideoCapture('../tupian/1.mp4')#导入源视频
success,image = cap.read()#success表示视频是否读取成功 True或flase image表示为读取视频的内容
count= 1#定义一个计数 初始为1

while success:#当视频读取成功时
    # 运用cv2.CAP_PROP_POS_MSEC每隔0.2秒读取当前帧数的一张图片 count表示次数
    cap.set(cv2.CAP_PROP_POS_MSEC, 0.2 * 1000 * count)#运用cv2.CAP_PROP_POS_MSEC
    cv2.imwrite('D:/python/lianxi/kaohe/new_tupian/image0' + str(count) + ".png",image) # 存储图片的地址 以及对图片的命名
    success, image = cap.read()#image表示读取到图片的内容
    plt.imshow(image)#输出图片
    plt.axis('off')#去除坐标轴
    plt.show()
    count += 1#计数加1
    print('Total image: ', count)#输出提示次数

