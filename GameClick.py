import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep

#mouse click in pc
mouse = Controller()

class gameClicker:

    # defines starting values
    def __init__(self, speed= .5, click_speed= .3):
        self.speed = speed
        self.click_speed =click_speed

    def nav_avocado(self):
        try:
            position = pt.locateOnScreen('avocado.png', confidence = 0.6)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-50, 50, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Searching for another ingredient ')

    def nav_lime(self):
        try:
            position = pt.locateOnScreen('lime.png', confidence = 0.6)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-50, 50, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Searching for another ingredient ')

    def nav_chilli(self):
        try:
            position = pt.locateOnScreen('chilli.png', confidence = 0.6)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-50, 50, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Searching for another ingredient ')

    def nav_tomato(self):
        try:
            position = pt.locateOnScreen('tomato.png', confidence = 0.6)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-50, 50, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Searching for another ingredient ')

    def nav_onion(self):
        try:
            position = pt.locateOnScreen('onion.png', confidence = 0.6)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-50, 50, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Searching for another ingredient ')

    def nav_mole(self):
        try:
            position = pt.locateOnScreen('mole.png', confidence = 0.6)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(70, 90, duration=self.speed)
            #pt.doubleClick(interval=self.click_speed)
            mouse.click(Button.left, 1)
        except Exception as e:
            print('Searching for mole')

click_bot = gameClicker(speed= 0.1, click_speed= 0.2)

while True:
    #click_bot.nav_avocado()
    #click_bot.nav_lime()
    #click_bot.nav_chilli()
    #click_bot.nav_tomato()
    #click_bot.nav_onion()
    #click_bot.nav_nut()
    click_bot.nav_mole()

    sleep(0.2)