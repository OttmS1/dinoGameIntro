import pyautogui as pgui
import time


#ask for permission
pgui.press("space")

wait = input("go? y/n: ")
time.sleep(3)
pgui.press("space")

#open dev console
pgui.keyDown("ctrl")
pgui.keyDown("shift")
pgui.press("i")
pgui.keyUp("ctrl")
pgui.keyUp("shift")

time.sleep(0.25)

#crank speed
pgui.write("runnerInstance.setSpeed(100000)")
pgui.press("enter")

pgui.keyDown("ctrl")
pgui.keyDown("shift")
pgui.press("i")
pgui.keyUp("ctrl")
pgui.keyUp("shift")

pgui.press("space")

time.sleep(5.5)
pgui.keyDown("ctrl")
pgui.keyDown("shift")
pgui.press("i")
pgui.keyUp("ctrl")
pgui.keyUp("shift")

time.sleep(0.1)
pgui.write("runnerInstance.setSpeed(10)")
pgui.press("enter")


pgui.keyDown("ctrl")
pgui.keyDown("shift")
pgui.press("i")
pgui.keyUp("ctrl")
pgui.keyUp("shift")

pgui.press("space")
