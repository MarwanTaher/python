from PIL import Image, ImageFilter

image = Image.open('./Pokedex/pikachu.jpg')
filterd_image = image.filter(ImageFilter.BLUR)
bw_image = image.convert('L')
bw_image.save('bw.png','png')
filterd_image.save('blur.png','png')
filterd_image.show()