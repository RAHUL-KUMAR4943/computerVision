# -*- coding: utf-8 -*-
"""Cv_i2V.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dOY8x0YIZDCwc-jOy_Al_1Ve7YSCa-Um
"""

import numpy as np
x = [1,2,3,4,5]
type(x)

arr = np.array(x)
arr

type(x)

type(arr)

np.arange(1,13)

np.arange(1,14,3)

np.zeros((2,5))

arr1 = np.random.randint(10,1000,50)

arr1

np.random.seed(5)
arr1 = np.random.randint(10,1000,70)

arr1

arr1.reshape(10,7)

np.ones((4,4))

arr2 = np.random.randint(0,1000,50).reshape(10,5)

arr2

arr2.max()

arr2.min()

arr2.mean()

arr2.argmin()

arr2.argmax()

arr2.shape

row = 3
col = 3
arr2[row,col]

arr2[3,3]

arr2[:,4]

arr2[7,:]

arr2

arr2[0:4,0:3]

arr2[1:3,2:4]

arr2[0:2,0:4] = 1

arr2

arr3 = arr2.copy()

arr3

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open("/content/IMG_20220408_081438.jpg")

img2 = Image.open("/content/passport_size_pic.jpg")
img2

img2

img2.shape

type(img2)

img2.mode

img2_array = np.array(img2)
img2_array.shape

plt.imshow(img2_array)

im1 = img2_array.copy()

im2 = img2_array.copy()

im3 = img2_array.copy()

plt.imshow(im1)

plt.imshow(im2)

plt.imshow(im3)

im1[:,:,0]

im2[:,:,1]

im3[:,:,2]

im1[:,:,0] = 0
plt.imshow(im1)

im2[:,:,1] = 0
plt.imshow(im2)

im3[:,:,2] = 0
plt.imshow(im3)

img4=im1.copy()
plt.imshow(img4)

img4[:,:,2] = 0
plt.imshow(img4)

img4

img4[:,:,1] = 0

img4

plt.imshow(img4)

im2[:,:,2]

img5 = Image.open("/content/Opponent_colors jpg.jpg")

img5

plt.imshow(img5)

img5 = np.array(img5)

img5

img6 = img5.copy()

img7 = img5.copy()

img8 = img5.copy()

plt.imshow(img6)

plt.imshow(img7)

"""plt.imshow(img8)"""

img7[:,:,0] = 0

plt.imshow(img7)

img7[:,:,1] = 0
plt.imshow(img7)



img7[:,:,2] = 0
plt.imshow(img7)

img7[:,:]

img8

plt.imshow(img8)

img8 = np.array(img8)

img8

plt.imshow(img8)

img9 = img8.copy()

type(img9)

plt.imshow(img9)

img9[:,:]

img9[:,:,0] = 255
plt.imshow(img9)

img9[:,:,1] = 255
plt.imshow(img9)

img9[:,:,2] = 255
plt.imshow(img9)

img9.shape

img2

img5

imgg = Image.open("/content/Opponent_colors jpg.jpg")

imgg

imgg1 = np.array(imgg)

imgg1

plt.imshow(imgg1)

type(img2)

arr1 = np.array(img2)

arr1.shape

img2.getbbox()

img.size

img2.size

arr1.size

img2.format

img2.rotate(90)

img2

type(img2)

img2.getbbox()

img2.size

img2.format

img2.rotate(90)

img2.rotate(330)



img2

img_c= img2.copy()

img2.paste(img_c,(20,20))

img2

img_c



img2.rotate(210)

img2

img_c

img2.paste(img_c,(500,700))

img2

img2.paste(img_c,(1200,900))

img2

img2.resize((800,1000))

crop = img2.crop((0,0,700,500))

crop

flip = img2.transpose(Image.FLIP_TOP_BOTTOM)

flip

flip = img2.transpose(Image.FLIP_LEFT_RIGHT)

flip

filter = Image.open("/content/filter_useCV.jpg")

filter1 = filter.resize((600,700))

filter1

from PIL import Image, ImageFilter

filter2 = filter1.filter(ImageFilter.BLUR)

filter2

filter2 = filter1.filter(ImageFilter.CONTOUR)
filter2.show()

filter2

filter3 = filter1.filter(ImageFilter.EMBOSS)

filter3

filter4 = filter1.filter(ImageFilter.EDGE_ENHANCE)

filter4

filter5 = filter1.filter(ImageFilter.SMOOTH)

filter5

filter6 = Image.Image.split(filter1)

filter6[0]

filter6[1]

filter6[2]

filter1_arr = np.array(filter1)

plt.imshow(filter1_arr[:,:,0] , cmap='gray')

plt.imshow(filter1_arr[:,:,1] , cmap='gray')

plt.imshow(filter1_arr[:,:,2] , cmap='gray')

