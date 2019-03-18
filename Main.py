import pyautogui as pg
import time
from PIL import ImageGrab, ImageOps
from numpy import array
from directkeys import PressAndRelease, bt1, bt2
from directclick import left_click

# Pointers
collect = [129, 360]
confirm = [586, 351]  # OK do sprite
ok_button = [176, 235]  # volta do sprite (clicar várias vezes por causa dos eventos)
menu_sprite = [44, 67]
menu_details = [101, 67]
sprite_item_humor = [289, 721]
sprite_item_resistance = [326, 721]
sprite_1 = [924, 726]

# Boxes
box_resistance = [66, 173, 68, 175]  # !== 302
box_humor = [192, 88, 194, 90]  # != 53
box_sprite_returned = [176, 235, 178, 237]  # !== 259

pg.moveTo(280, 400)
pg.click()


def start_to_collect():
    pg.moveTo(collect)
    time.sleep(0.5)
    left_click()
    time.sleep(0.5)
    pg.moveTo(confirm)
    time.sleep(0.5)
    left_click()


def up_humor(btn):
    PressAndRelease(btn)
    print('item activated')
    pg.moveTo(sprite_1)
    left_click()
    print('left clicked')


def get_area(b):
    box = (b[0], b[1], b[2], b[3])
    img = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(img.getcolors())
    return int(a.sum())


def check_box(box, value, btn):
    h = get_area(box)
    while h != value:
        up_humor(btn)
        time.sleep(10)
        h = get_area(box)
    print('humor alto o suficiente')


def check_comeback():
    h = get_area(box_sprite_returned)
    print(h)
    while h != 259:
        time.sleep(2)
        print('nothing there')
        h = get_area(box_sprite_returned)

    pg.moveTo(ok_button)
    time.sleep(1)
    left_click()
    time.sleep(5)
    left_click()
    print('comeback done')


def boot():
    while 1:
        check_box(box_humor, 53, bt1)
        pg.moveTo(menu_details)
        time.sleep(0.5)
        left_click()
        time.sleep(0.5)
        check_box(box_resistance, 302, bt2)
        pg.moveTo(menu_sprite)
        time.sleep(0.5)
        left_click()
        time.sleep(0.5)
        start_to_collect()
        time.sleep(1)
        check_comeback()


if __name__ == "__main__":
    boot()



