'''--*   MIHX   *--

作者:MINOR
日期:2021年11月30日14时23分'''
import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread('D:/python/lianxi/kaohe/tupian/s1.jpg')#提取图片1
image2 = cv2.imread('D:/python/lianxi/kaohe/tupian/s2.jpg')#提取图片2
sift = cv2.SIFT_create()#SIFT特征点初始化
keypoints = sift.detect(image,None)#实现特征点和特征点描述分别输出
keypoints2 = sift.detect(image2,None)
img_sift = np.copy(image)#np.copy()属于深拷贝,拷贝前的地址和拷贝后的地址不一样.
img_sift2 = np.copy(image2)
#cv2.drawKeypoints是画圈 image为原图 keypoints为特征点 img_sift复制
cv2.drawKeypoints(image,keypoints,img_sift,flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)#用圆圈画出特征点
cv2.drawKeypoints(image2,keypoints2,img_sift2,flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)#用圆圈画出特征点
cv2.imshow('SIFT features',img_sift)
cv2.imshow('SIFT features2',img_sift2)
cv2.imwrite('../tupian/s11.png',img_sift)
cv2.imwrite('../tupian/s22.png',img_sift2)
plt.show()
cv2.waitKey()
