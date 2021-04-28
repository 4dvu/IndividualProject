import cv2
from matplotlib import pyplot as plt

img = cv2.imread('process/img1_0.png', 0)
plt.hist(img.ravel(), bins = 'auto')
plt.xlabel('grayscale value')
plt.ylabel('pixel count')
plt.show()

