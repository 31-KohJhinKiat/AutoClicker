import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep
from  whatsapp_response import response

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
            position = pt.locateOnScreen('green_dot.png', confidence = 0.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-100, 0, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_green_dot): ', e)

    #navigate to our message input box
    def nav_input_box(self):
        try:
            position = pt.locateOnScreen('paperclip.png', confidence = 0.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(100, 10, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_input_box): ', e)

    #navigate to message we want to respond to
    def nav_message(self):
        try:
            position = pt.locateOnScreen('paperclip.png', confidence = 0.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(20, -50, duration=self.speed)
            
        except Exception as e:
            print('Exception (nav_message): ', e)

    #copies message that we want to process
    def get_message(self):
        mouse.click(Button.left, 3)
        sleep(self.speed)
        mouse.click(Button.right, 1)
        sleep(self.speed)
        pt.moveRel(10, 10, duration=self.speed)
        mouse.click(Button.left, 1)
        sleep(1)
        
        self.message = pc.paste()
        print('User says: ', self.message)

    #send message to user
    def send_message(self):
        try:
            if self.message != self.last_message:
                bot_response = response(self.message)
                print('You say: ', bot_response)
                pt.typewrite(bot_response, interval= 0.2)
                #pt.typewrite('\n') # send message

                #Assign them the same message
                self.last_message = self.message
            else:
                print('no new messages')

        except Exception as e:
            print('Exception (send_message): ', e)

wa_bot = WhatsApp(speed = 0.5, click_speed= 0.4)   
sleep(2)


while True:
    wa_bot.nav_green_dot()
    wa_bot.nav_message()
    wa_bot.get_message()
    wa_bot.nav_input_box()
    wa_bot.send_message()

    sleep(10)
