# from tkinter import *
# from tkinter import ttk
# from tkinter import filedialog
# gui = Tk()
# gui.geometry("100x100")
#
#
# def getfolderpath():
#     filedialog.askdirectory()
#
#
# btnFind = ttk.Button(gui, text="Open Folder",command=getfolderpath)
# btnFind.grid(row=0,column=2)
#
# gui.mainloop()


# import numpy as np
# import imageio.v2 as imageio
# import scipy.ndimage
# import cv2
# import datetime
#
# img = 'IMG-02.jpg'
#
#
# def rgb2gray(rgb):
#     return np.dot(rgb[..., :3], [0.3989, 0.5870, 0.1140])
# # it is 2dimentional array formula to two convert image to gray scale
#
#
# def convert_img(front, back):
#     final_scatch = front*255/(255-back)
# # if image is greater then 255 then convert it to 255
#     final_scatch[final_scatch > 255] = 255
#     final_scatch[back == 255] = 255
#     print('convert success..')
#     return final_scatch.astype("uint8")
# # unit8 is for 8-bit signed integer
#
#
# read_image = imageio.imread(img)
# gray = rgb2gray(read_image)
#
# i = 255-gray
#
# # to convert it into blur image
# blur = scipy.ndimage.gaussian_filter(i, sigma=50)
# # sigma is the intencity of blurness of image
#
# r = convert_img(blur, gray)
# # this fun will convert our image
# current_time = datetime.datetime.now().strftime('%H-%M')
# cv2.imwrite(f'img{current_time}.png', r)

# -------------------------xxxxx----------------------

import cv2
import matplotlib.pyplot as plt
import datetime

img = cv2.imread('IMG-02.jpg', 0)
plt.imshow(img, cmap='gray')

inv = 255 - img
blur = cv2.GaussianBlur(inv, ksize=(21, 21), sigmaX=100, sigmaY=100)
dodge = lambda image, mask: cv2.divide(image, 255 - mask, scale=256)
blended = dodge(img, blur)
plt.imshow(blended, cmap='gray')
current_time = datetime.datetime.now().strftime('%H-%M')
cv2.imwrite(f'img{current_time}.png', blended)

# -------------------------xxxxx----------------------

