import pygame

def scale_image(img, factor):
# function to adjust size of images
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)
    # transforms size of image according to the scale
