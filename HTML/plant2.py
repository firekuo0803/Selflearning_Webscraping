# coding: utf-8
import cv2
import numpy as np
import math
img = cv2.imread("E:/desktop/17202.jpg")
img2 = cv2.imread("E:/desktop/17202.jpg")

name = '丙酮'

dot1 = [1098,563]
dot2 = [1202,640]


img2 = cv2.rectangle(img2, (dot1[0], dot1[1]), (dot2[0], dot2[1]), (255, 0, 255), 3)


Rs = []
Gs = []
Bs = []

for i in range(dot1[0],dot2[0]):
    for p in range(dot1[1],dot2[1]):
     B1, G1, R1 = img[p,i]
     Rs.append(R1)
     Gs.append(G1)
     Bs.append(B1)
     img2= cv2.circle(img2, (i, p), 1, (0, 0, 255), thickness=-1)
# print(Rs)
# print(Bs)
# print(Gs)

aR = 0
aG = 0
aB = 0
for r in Rs:
    aR = aR + r
aR = aR/len(Rs)

for g in Gs:
    aG = aG + g
aG = aG/len(Gs)

for b in Bs:
    aB = aB + b
aB = aB/len(Bs)
print([aR,aG,aB])
img2 = cv2.putText(img2, f'R:{round(aR, 2)} G:{round(aG, 2)} B:{round(aB, 2)}', (dot1[0], dot1[1]-50), cv2.FONT_HERSHEY_PLAIN, 3.0, (0, 100, 150), thickness=5)

# img3 = cv2.circle(img, (90, 60), 1, (50, 70, 100), thickness=-1)
# x,y,z = img3[60,90]
# print([x,y,z])

cv2.imshow('A', img2)
cv2.imwrite(f'E:/desktop/{name}.jpg', img2)
cv2.waitKey(0)
cv2.destroyAllWindow()

