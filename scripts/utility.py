import pygame

BASE_IMG_PATH = 'assets/images/'

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    print(f"ASSET FOUND: {BASE_IMG_PATH + path}")
    img.set_colorkey((0, 0, 0))
    return img
