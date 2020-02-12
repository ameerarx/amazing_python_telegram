from PIL import Image
img = Image.open("pic.png")

box = (100,100,300,300)
new_img = img.crop(box)
new_img.save("new_pic_1s.png")
