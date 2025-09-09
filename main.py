import pyautogui as pgui
import time


#ask for permission
pgui.press("space")

wait = input("go? y/n: ")
time.sleep(5)
pgui.press("space")

#open dev console
pgui.keyDown("ctrl")
pgui.keyDown("shift")
pgui.press("i")
pgui.keyUp("ctrl")
pgui.keyUp("shift")

#god mode
pgui.write("var original = Runner.prototype.gameOver")
pgui.press("enter")
pgui.write("Runner.prototype.gameOver = function() {}")
pgui.press("enter")

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

pgui.write("runnerInstance.setSpeed(10)")
pgui.press("enter")

pgui.write("Runner.prototype.gameOver = original")
pgui.press("enter")

pgui.keyDown("ctrl")
pgui.keyDown("shift")
pgui.press("i")
pgui.keyUp("ctrl")
pgui.keyUp("shift")

pgui.press("space")
