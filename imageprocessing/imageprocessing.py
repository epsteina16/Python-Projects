#image proccessing

from PIL import Image
from PIL import ImageFilter

im = Image.open('example.jpg')
im.show
#rotate and resize
one = im.resize((128, 128))
two = im.rotate(45)

#filters

three = im.filter(ImageFilter.MinFilter)

#three.show()
