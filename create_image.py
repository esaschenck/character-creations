# Required packages

import cv2
import numpy as np



#Cartoonify a face
#This code is adapted from the tutorial at https://towardsdatascience.com/turn-photos-into-cartoons-using-python-bb1a9f578a7e

print("done!")

#comes from a tutorial https://towardsdatascience.com/turn-photos-into-cartoons-using-python-bb1a9f578a7e

def cartoonify(preCartoon, line_size = 7, blur_value = 7, total_color = 9):
  
  def read_file(filename):
    img = cv2.imread(filename)
    #cv2.imshow(img)
    return img

  #uploaded = files.upload()
  #filename = next(iter(uploaded))
  img = read_file(preCartoon)

  def edge_mask(img, line_size, blur_value):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, blur_value)
    edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, blur_value)
    return edges


  edges = edge_mask(img, line_size, blur_value)
  #cv2_imshow(edges)


  def color_quantization(img, k):
  # Transform the image
    data = np.float32(img).reshape((-1, 3))

  # Determine criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)

  # Implementing K-Means
    ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    result = center[label.flatten()]
    result = result.reshape(img.shape)
    return result


  img = color_quantization(img, total_color)

  blurred = cv2.bilateralFilter(img, d=7, sigmaColor=200,sigmaSpace=200)

  cartoon = cv2.bitwise_and(blurred, blurred, mask=edges)

  #import os
  #import matplotlib.pyplot as plt

  #folderName = 'D:/Users/data'
  #os.makedirs(folderName)
  #plt.savefig(cartoon)

  #cv2.imwrite('testPhotos', cartoon)


  # same images from stackoverflow: https://stackoverflow.com/questions/14452824/how-can-i-save-an-image-with-pil

  return cartoon

  

