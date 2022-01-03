import numpy as np

from common import log, get_args
from draw import DrawLineOnImage


log('STARTING...')

x, y, width, alpha = get_args()

log('ARGUMENTS:', f'x = {x}', f'y = {y}', f'width = {width}', f'alpha = {alpha}')

# create input image
image_width = int(width * 1.5)
image_height = int(width * 1.5)
log('INPUT IMAGE:', f'height = {image_height}', f'width = {image_width}')
image = 255 * np.ones(shape=[image_height, image_width,  3], dtype=np.uint8)

log('DRAWING...')

drawing = DrawLineOnImage(image)
drawing.show_image()
