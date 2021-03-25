import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)   # set board mode to Broadcom
GPIO.setwarnings(False)  # don't show warnings

colors = {'red': 24, 'orange': 4, 'green': 3, 'aux1': 2, 'aux2': 17}

for c, v in colors.items():
    GPIO.setup(v, GPIO.OUT)
    GPIO.output(v, False)

def setColor(color, state):
    io = colors[color]

    if GPIO.input(io) is not int(state):
        print('Setting color', color.upper(), str(state))
        GPIO.output(io, state)

def bootSequence():
    for c, v in colors.items():
        setColor(c, True)
        time.sleep(0.2)
        setColor(c, False)

def lightPowerUp():
    # 5 second yellow flash
    for _ in range(5):
        setColor('orange', True)
        time.sleep(0.5)
        setColor('orange', False)
        time.sleep(0.5)

    # seconds steady yellow
    setColor('orange', True)
    time.sleep(5)

    # minimum 5 seconds red
    setColor('orange', False)
    setColor('red', True)
    time.sleep(5)

def turnGreen():
    # red/yellow
    setColor('orange', True)
    time.sleep(1)
    # green
    setColor('red', False)
    setColor('orange', False)
    setColor('green', True)

def turnRed():
    # yellow
    setColor('green', False)
    setColor('orange', True)
    time.sleep(3)
    # red
    setColor('orange', False)
    setColor('red', True)

#time.sleep(1)
#bootSequence()
#time.sleep(1)

lightPowerUp()

while True:
    turnGreen()
    time.sleep(5)
    turnRed()
    time.sleep(15)
