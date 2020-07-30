# @pythonamazing(Telegram)
from PIL import Image

image = Image.open(r"image.jpg")

image.thumbnail((128, 128))

image.save("thumb.jpg")