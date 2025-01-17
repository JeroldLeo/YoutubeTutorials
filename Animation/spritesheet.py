import json

import pygame


class Spritesheet:
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert()
        self.meta_data = self.filename.replace('png', 'json')
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()
        self.sprite_name_list = self.data['frames'].keys()

    def get_sprite(self, x, y, w, h):
        # sprite = pygame.Surface((w, h))
        # sprite.set_colorkey((0, 0, 0))
        # sprite.blit(self.sprite_sheet, (0, 0), pygame.Rect(x, y, w, h))
        sprite = self.sprite_sheet.subsurface(pygame.Rect(x, y, w, h))
        return sprite

    def parse_sprite(self, state=None):
        names = [name for name in self.sprite_name_list if state in name]
        image_sequence = []
        print(names)
        for name in names:
            sprite = self.data['frames'][name]['frame']
            x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
            image_sequence.append(self.get_sprite(x, y, w, h))
        return image_sequence
