import getpixelcolor as getcolor
import pynput
from pynput.mouse import Controller as mouseCont
from pynput.keyboard import Controller as keyCont
from pynput.keyboard import Key

mouse = mouseCont()

mousePos = mouse.position

def scanForObsticle():
   scannedCol = getcolor.pixel(mousePos[0] + 200, mousePos[1])
   
   if scannedCol[0] >= 150:
   
