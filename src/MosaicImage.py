

from PIL import Image

"""



TODO
"""


class MosaicImage:
    def __init__(self, original_img, tile_size):
        self.tile_size= tile_size
        self.image = Image.new(original_img.mode, original_img.size)
        self.x_tile_count = int(original_img.size[0] / tile_size)
        self.y_tile_count = int(original_img.size[1] / tile_size)
        self.total_tiles = self.x_tile_count * self.y_tile_count

    def add_tile(self, tile_data, coords):
        img = Image.new('RGB', (self.tile_size, self.tile_size))
        img.putdata(tile_data)
        self.image.paste(img, coords)

    def save(self, path):
        self.image.save(path)

    def __str__(self):
        return 'MosaicImage'