import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
import cv2 

df = pd.read_csv("3m vid.csv") # read the dataset
df = df.iloc[:, :-1] # exclude the last column 

def img(data):
    celcius = []
    for index, row in data.iterrows():
         row = (row/10)-273.5 # change data to celcius
         celcius.append(row)
    frame = np.array(celcius)
    # input the frame number 
    return (np.flip(frame[0].reshape(32, 32))) # flip the frame 
frame = img(df) 

def visualize(data_processed):
     new_inferno = cm.get_cmap('inferno', 10) # visualize in inferno colormap 
     plt.pcolormesh(data_processed, cmap = new_inferno)
     plt.axis('off')
     plt.xticks([]), plt.yticks([])
     plt.savefig('visualize/3m/frame3_0.png', bbox_inches = 'tight', pad_inches = 0.0)
     # plt.show()
     return 0

visualize(frame)

def thresh_seg(data_processed):
     upper_thresh = data_processed < 30 # set upper value
     under_thresh = data_processed > 23 # set under value
     thresh = np.logical_and(upper_thresh, under_thresh)*1
     binary = cm.get_cmap('inferno', 2)
     plt.pcolormesh(thresh, cmap = binary)
     plt.axis('off')
     plt.xticks([]), plt.yticks([])
     plt.savefig('threshold/thres4_0', bbox_inches='tight', pad_inches=0.0)
     # plt.show()
     return 0

thresh_seg(frame)
thres_img = cv2.imread('threshold/3m/thres3_0.png')

def opening(threshold_img):
     kernel_erosion = np.ones((1,2), np.uint8) # set erosion mask
     kernel_dilation = np.ones((3,2), np.uint8) # set dilation mask
     erosion = cv2.erode(threshold_img, kernel_erosion, iterations=16) # iterate to reduce noises
     dilation = cv2.dilate(erosion, kernel_dilation, iterations=20) # dilate from reduced noise frame
     titles = ['input', 'erosion', 'dilation']
     images = [threshold_img, erosion, dilation]
     for i in range(3):
          plt.subplot(1,3,i+1)
          plt.imshow(images[i])
          plt.title(titles[i])
          plt.xticks([]), plt.yticks([])
     plt.show()
     plt.imshow(dilation)
     plt.axis('off')
     plt.xticks([]), plt.yticks([])
     plt.savefig('bbox/3m/bbox3_0.png', bbox_inches='tight', pad_inches=0.0)
     return 0

opening(thres_img)