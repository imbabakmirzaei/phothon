from PIL import Image

img = Image.open('src/Daemon.jpeg')

print(img.size)
print(type(img))
print(img.format)
img.show()