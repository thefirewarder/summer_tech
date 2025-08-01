import sys
import time
import keyboard
def render():
    for Y in range(-20, 20):
        print("")
        for X in range(-40, 40):
            imagin = ((Y/20) + centerY)/zoom
            num = ((X/40) + centerX)/zoom
            com = complex(num, imagin)
            Z = 0
            detail = 30
            while abs(Z) <= 2 and detail > 0:
                Z = (Z * Z) + com
                detail-=1
            if detail == 0:
                print("❚",end="")
            else:
                print(" ",end="")
centerX = -0.5
centerY = 0.0
zoom = 1.2
renderCount = 0
render()
while True:
    if keyboard.is_pressed('up arrow'):
        print("\033c", end="")
        centerY-=0.1
        render()
    if keyboard.is_pressed('down arrow'):
        print("\033c", end="")
        centerY+=0.1
        render()
    if keyboard.is_pressed('left arrow'):
        print("\033c", end="")
        centerX-=0.1
        render()
    if keyboard.is_pressed('right arrow'):
        print("\033c", end="")
        centerX+=0.1
        render()
    if keyboard.is_pressed('.'):
        print("\033c", end="")
        zoom+=0.1
        render()
    if keyboard.is_pressed(','):
        print("\033c", end="")
        zoom-=0.1
        render()
    