import time
from pynput.keyboard import Key, Controller
import webbrowser as web
import pyautogui as pg

def sendwhatmsg(phone_no, message, wait_time=20):

    web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+message)
    time.sleep(2)
    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(wait_time-2)
    pg.press('enter')

#Inputs starts here

numbers = ['+6599999999','+6588888888']  #Input a list of numbers

#The below is a message based on URL Encoding
message = 'Test Message'


for number in numbers:
    sendwhatmsg(number,message,10)

    print("Number of messages sent so far: " + str(num_msg))

    keyboard = Controller()

    # keyboard.press(Key.ctrl.value) #this would be for your key combination
    keyboard.press(Key.ctrl.value)
    keyboard.press('w')
    keyboard.release('w')
    # keyboard.release(Key.ctrl.value) #this would be for your key combination
    keyboard.release(Key.ctrl.value)
    time.sleep(1)
    keyboard.press(Key.enter.value)
    keyboard.release(Key.enter.value)
    time.sleep(13)