import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('octocat.png',cv2.IMREAD_COLOR)

b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])

plt.imshow(img2)
plt.show()

print(img.shape)

cat_color = img[156,645]
h,w = img.shape[:2]
color_to_change = [100,100,100]

for x in range (w):
    for y in range (h):
        if np.all(img[y,x] == cat_color):
            img[y,x] = color_to_change

cv2.imshow('image',img)

k = cv2.waitKey(0)

# octocat was much complicated than what I was thinking. Sorry!