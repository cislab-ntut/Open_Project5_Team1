from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open("3.bmp")
carrierRGB = img.getpixel((0, 0))
x = int(input("Input coordinate x: "))
y = int(input("Input coordinate y: "))
cipherText = raw_input("Input cipher text you want to secrete: ")
coordinate = (x, y)
if carrierRGB[2] > 1:
    carrierRGB = carrierRGB[0], carrierRGB[1], carrierRGB[2] - 1
else:
    carrierRGB = carrierRGB[0], carrierRGB[1], carrierRGB[2] + 1


draw = ImageDraw.Draw(img)
font = ImageFont.truetype("AquaKana.ttc", 16)
draw.text(coordinate, cipherText, carrierRGB, font)
img.save("output.bmp")
print("A stego image has been created")
