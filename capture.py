from datetime import datetime
import time

import cv2
import numpy as np
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont


#OUTPUT_DIR = '/home/pi/ascetic/asagao/'
OUTPUT_DIR = '/var/www/html/'
OUTPUT_FILE = 'img.png'


def capture():
    c = cv2.VideoCapture(0)
    r, img = c.read()
    if img is None:
        time.sleep(1)
        return capture()
    else:
        return img

def draw_text(img, text):
    draw = PIL.ImageDraw.Draw(img)
    draw.font = PIL.ImageFont.truetype(
        "/usr/share/fonts/truetype/freefont/FreeMono.ttf", 20)

    img_size = np.array(img.size)
    txt_size = np.array(draw.font.getsize(text))
    pos_v = (img_size[1] - txt_size[1]) / 2
    pos_h = (img_size[0] - txt_size[0]) / 1
    pos = np.array([int(pos_v), int(pos_h)])

    draw.text(pos, text, (255, 255, 255))


if __name__ == '__main__':
    img = capture()
    cv2.imwrite('buf.png', img)
    img = PIL.Image.open('buf.png')
    draw_text(img, datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
    #cv2.imwrite(OUTPUT_DIR + OUTPUT_FILE, img)
    img.save(OUTPUT_DIR + OUTPUT_FILE)
    img.save(OUTPUT_DIR + 'tmp/img{}.png'.format(
        datetime.now().strftime('%Y%m%d%H%M%S')))
    print('capture.py is executed at {}'.format(
        datetime.now().strftime('%Y/%m/%d - %H:%M:%S')))
