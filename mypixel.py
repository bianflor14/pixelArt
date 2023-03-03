from CSEPixelArt import *


def cloud(img, pos_x, pos_y):
    for x in range(1, 3):
        img[0+pos_y][x+pos_x] = (255, 255, 255)
    for x in range(0, 4):
        img[1+pos_y][x+pos_x] = (255, 255, 255)


def flowers(img, pos_x, pos_y):
    for x in range(1, 2):
        img[0+pos_y][x+pos_x] = (255, 182, 193)
    for x in range(0, 1):
        img[1+pos_y][x+pos_x] = (255, 182, 193)
    for x in range(2, 3):
        img[1+pos_y][x+pos_x] = (255, 182, 193)
    for x in range(1, 2):
        img[1+pos_y][x+pos_x] = (255, 255, 51)
    for x in range(1, 2):
        img[2+pos_y][x+pos_x] = (255, 182, 193)
    for x in range(1, 3):
        img[3 + pos_y][x + pos_x] = (86, 178, 52)
    for x in range(1, 2):
        img[4 + pos_y][x + pos_x] = (86, 178, 52)


def main():
    img = create_img(16, 16, (153, 217, 234))
    cloud(img, 3, 3)
    cloud(img, 3, 8)
    cloud(img, 11, 1)
    cloud(img, 11, 6)
    flowers(img, 3, 11)
    flowers(img, 11, 11)

    print("myPixel.png")
    save_img(img, "example-5.png")
    print("myPixel.png")
    save_img(img, "example-5-big.png", 20)


main()
