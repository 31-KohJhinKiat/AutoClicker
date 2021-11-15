import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep

#mouse click in pc
mouse = Controller()

#instructions for whatsapp bot
class WhatsApp:

    # defines starting values
    def _init_(self, speed= 0.5, click_speed= 0.5):
        self.speed = speed
        self.click_speed =click_speed
        self.message = ''
        self.last_message = ''

    #navigate to green dots for new messages
    def nav_green_dot(self):
        try:
            position = 