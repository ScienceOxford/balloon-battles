from microbit import *
import radio

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

radio.config(channel=7, group=0, queue=1) # CHANGE THIS
radio.on()

'''
INPUTS
joystick:bit
'''
buttons = {2: 'A',
           516: 'B',
           684: 'C',
           768: 'D',
           853: 'E',
           819: 'F'}

def button_press():
    press = pin2.read_analog()
    if press < 900:
        for number in range(press-5, press+5):
            if number in buttons:
                return buttons[number]

def joystick_push():
    x = int(pin0.read_analog() - 512)
    y = int(pin1.read_analog() - 512)
    left = int( (y + x) * 1)
    right = int( (y - x) * 1)
    return left, right

'''
MAIN CODE
'''

while True:
    joystick = joystick_push()
    message = str(joystick[0]) + " " + str(joystick[1])
    radio.send(message)
    sleep(10)
