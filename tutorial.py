import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('octocat.png',cv2.IMREAD_COLOR)    # open octocat as RGB mode

#### SHOW IMAGE WITH OPENCV ####
'''
cv2.imshow('image',img)                             # show img

k = cv2.waitKey(0)                                  # wait until keystroke
if k == ord('s'):
    cv2.imwrite('octocat_clone.png',img)            # save img
cv2.destroyAllWindows()                             # close imshow window
'''


#### SHOW IMAGE WITH MATPLOT ####
'''
b,g,r = cv2.split(img)                              # split image file in b,g,r. NOT RGB!!
img2 = cv2.merge([r,g,b])

plt.imshow(img2)
plt.show()
'''

#### BASIC OPERATIONS ####
print('height, width, channel:', img.shape)         # height,width,channel
print('B,G,R at y=570, x=590:', img[570,590])       # bgr pixel values
print('type', type(img[570,590]))
print('only B at above:', img[570,590,0])           # blue only
# print(img.item(570,590,0))
img[570,590] =[255,255,255]                         # edit pixel values