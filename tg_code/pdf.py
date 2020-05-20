# @pythonamazing(Telegram)
from PIL import Image

image1 = Image.open(r'C:\Users\logo.png')

im1 = image1.convert('RGB')

im1.save(r'C:\Users\name.pdf')