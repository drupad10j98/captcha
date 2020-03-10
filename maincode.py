from captcha.image import ImageCaptcha 
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random
import os


image = ImageCaptcha(width=100, height=30, font_sizes=[30])

captcha_text = []
for i in range(4):
    c = str(random.randint(0,9))
    captcha_text.append(c)
captcha_text = ''.join(captcha_text)
print(captcha_text)

captcha_image = Image.open(image.generate(captcha_text))
captcha_image = np.array(captcha_image)

image.write(captcha_text, str(i)+'_'+captcha_text + '.png') 
plt.imshow(captcha_image)
plt.show() 
