from PIL import Image, ImageFilter,ImageEnhance
import os


directory = '/home/davidalejandro/Desktop/transfer-learning-for-diagnostic-images-spanish-/pneumonia/'
dir_target = '/home/davidalejandro/Desktop/transfer-learning-for-diagnostic-images-spanish-/clasificacion/'
name = "PNEUMONIA"

num = 0
for filename in os.listdir(directory):
    if filename.endswith(".jpeg"):
        filename1 = str(directory + filename)
        im = Image.open(filename1)
        im = ImageEnhance.Brightness(im).enhance(0.7)
        im = ImageEnhance.Contrast(im).enhance(2.0)
        im.thumbnail((299, 299), Image.ANTIALIAS)
        num = int(num)
        num = num +1
        if num == 10000:
            break
        num = str(num)
        file_tar = dir_target + name + "-" + num + ".jpeg"
        
        im.save(file_tar)
