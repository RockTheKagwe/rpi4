from Tkinter import *
import tkFont
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup()
GPIO.output()

win = Tk()

myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')

def ledON():
    print("LED Button pressed")
    if GPIO.input(40):
        GPIO.output(40, GPIO.LOW)
        ledButton['text'] = 'LED ON'
    else :
        GPIO.output(40, GPIO.HIGH)
        ledButton['text'] = 'LED OFF'

def exitProgram():
    print('Exit Button Pressed')
    GPIO.cleanup()
    win.quit()
    
win.title('First GUI')
win.geometry('480 x 320')

exitButton = Button(win, text = 'Exit', font = myFont, command = exitProgram, height = 2, width = 6)
exitButton.pack(side = BOTTOM)

ledButton = Button(win, text = 'LED ON', font = myFont, command = ledON, height = 2, width = 8)
ledButton.pack()