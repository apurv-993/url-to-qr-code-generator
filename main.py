import qrcode
from PIL import Image, ImageDraw  
url = input("enter the url to convert in qr:")
filename = input("enter the name by which u want to save the qr code:")

if not(filename.endswith(".png")):
    filename = filename + ".png"
else:
    filename = filename   
img = qrcode.make(url)
img.save(filename)