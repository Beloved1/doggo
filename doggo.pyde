
def setup():
    size(400, 400)
    dog = loadImage("dog.jpg")
    image (dog, 0, 0)
    loadPixels()
    print(red(pixels[0]), green(pixels[0]), blue(pixels[0]))
    print(red(pixels[57]), green(pixels[57]), blue(pixels[57]))
    c =  color(255, 255 , 0)       
    pixels[57] = c
    updatePixels()
    print(red(pixels[57]), green(pixels[57]), blue(pixels[57]))
