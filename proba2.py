from PIL import Image
image = Image.open('flora.jpg')
rotated_img = image.rotate(45, expand=True)
rotated_img.show()