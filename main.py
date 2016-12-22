from chess_timer import player
import subprocess
import RPi.GPIO as GPIO
import time

"""
It is not used interrupt
"""

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)

def check_push():
    if GPIO.input(2):
        print('pushed, {}'.format(GPIO.input(2)))
        while not GPIO.input(2):
            print('-'*30)
            return True
    return False

print("start now.")

p1 = player()
p2 = player()
p = [p1, p2]
i = 0

p[i].set_dt1()
while 1:
    if check_push():
        print("player:{}".format(i+1))
        if p[i].calc(): # True is gameover
            subprocess.call(['cat', 'p{}loss.txt'.format(i+1)])
        print(["PLAYER{} {}:{}".format(e+1, "{0:02d}".format(int(P.t.minute)), "{0:02d}".format(int(P.t.second))) for e, P in enumerate(p)])
        i = i ^ 1
        p[i].set_dt1()
