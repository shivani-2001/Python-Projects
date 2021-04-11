import PIL
from PIL import Image

img1 = Image.open('groupimage2.jpg')
height1, width1 = img1.size

img1 = img1.resize((height1, width1), PIL.Image.ANTIALIAS)
img1.save('shivanisigfinal2.jpg')

if height1 >= width1:
    wpercent1 = (width1/float(img1.size[0]))
    hsize1 = int((float(img1.size[1])*float(wpercent1)))
    img1 = img1.resize((width1, hsize1), PIL.Image.ANTIALIAS)
    print(img1)
else:
    hpercent1 = (height1 / float(img1.size[1]))
    wsize1 = int((float(img1.size[0]) * float(hpercent1)))
    img1 = img1.resize((wsize1, height1), PIL.Image.ANTIALIAS)
    print(img1)
img1.save('shivanisigfinal1.jpg')

img1_open = Image.open('shivanisigfinal2.jpg')
img2_open = Image.open('shivanisigfinal1.jpg')

if img1_open.size>img2_open.size:
    img2_open.save('final.jpg')

else:
    img1_open.save('final.jpg')