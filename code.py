# Imports
import time
import usb_hid
import board

from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode


# Initialize Keybaord
keyboard = Keyboard(usb_hid.devices)

# Define HID Key Output Actions
hid_actions = [
    {
        #open Pycharm (shortcut)
        "name": "Scene 1",
        "held": False,
        "keycode": (Keycode.CONTROL, Keycode.Q, Keycode.ALT),
        "button": None,
        "led": None,
    },
    {
        #arduino (shortcut)
        "name": "Scene 2",
        "held": False,
        "keycode": (Keycode.CONTROL, Keycode.W, Keycode.ALT),
        "button": None,
        "led": None,
    },
    {
        #freecad (shortcut)
        "name": "Scene 3",
        "held": False,
        "keycode": (Keycode.CONTROL, Keycode.E, Keycode.ALT),
        "button": None,
        "led": None,
    },
    {
        #easyEda (shortcut)
        "name": "Scene 4",
        "held": False,
        "keycode": (Keycode.CONTROL, Keycode.R, Keycode.ALT),
        "button": None,
        "led": None,
    },
    {	#valorant (shortcut)
        "name": "Scene 5",
        "held": False,
        "keycode": (Keycode.CONTROL, Keycode.T, Keycode.ALT),
        "button": None,
        "led": None,
    },
    {	#screen capture (shortcut)
        "name": "Scene 6",
        "held": False,
        "keycode": (Keycode.WINDOWS, Keycode.SHIFT, Keycode.S),
        "button": None,
        "led": None,
    },
    {	#turn off screen (shortcut)
        "name": "Scene 7",
        "held": False,
        "keycode": (Keycode.CONTROL, Keycode.ALT, Keycode.DELETE),
        "button": None,
        "led": None,
    },
    {   #save and close a file (shortcut)
        "name": "Scene 8",
        "held": False,
        "keycode": (Keycode.CONTROL, Keycode.S),
        "button": None,
        "led": None,
    },
    {   #no attribuate
        "name": "Scene 9",
        "held": False,
        "keycode": (),
        "button": None,
        "led": None,
    },
    {	#no attribuate
        "name": "Scene 10",
        "held": False,
        "keycode": (),
        "button": None,
        "led": None,
    },
    {	#no attribuate
        "name": "Scene 11",
        "held": False,
        "keycode": (),
        "button": None,
        "led": None,
    },
    {	#no attribuate
        "name": "Scene 12",
        "held": False,
        "keycode": (),
        "button": None,
        "led": None,
    },
]


# Define button pins
btn_pins = [
    board.GP0,
    board.GP3,
    board.GP8,
    board.GP10,
    board.GP1,
    board.GP4,
    board.GP6,
    board.GP11,
    board.GP2,
    board.GP5,
    board.GP7,
    board.GP9,
]

# Setup all Buttons as Inputs with PullUps
for i in range(12):
    button = DigitalInOut(btn_pins[i])
    button.direction = Direction.INPUT
    button.pull = Pull.UP
    hid_actions[i]["button"] = button


# Loop around and check for key presses
while True:

    for i in range(12):

        # check if button is pressed but make sure it is not held down
        if not hid_actions[i]["button"].value and not hid_actions[i]["held"]:

            # print the name of the command for debug
            print(hid_actions[i]["name"])
            print(i)

            # send the keyboard commands
            keyboard.send(*hid_actions[i]["keycode"])
            
            # press kay to realize action
            if i == 6:
              time.sleep(0.35)
              keyboard.send(Keycode.ENTER)
                
            if i == 7:
              time.sleep(1.5)
              keyboard.send(Keycode.OPTION, Keycode.F4)
                

            # set the held to True for debounce
            hid_actions[i]["held"] = True

        # remove the held indication if it is no longer held
        elif hid_actions[i]["button"].value and hid_actions[i]["held"]:
           hid_actions[i]["held"] = False
            

            
            
                


