import time
import keyboard as key
import random as rand
#import playsound as play

x=580

def main():
    rand.choice()


#Sets radio frequency up or down to maximum of 540 - 1700KHz
while True:
   if key.read_key() == "w":
        if x == 1700:
            x=1700
        else:
            x=x+10
        print(x, "KHz AM")

   if key.read_key() == "s":
        if x == 540:
            x=540
        else:
            x=x-10
        print(x, "KHz AM")

   if x == 780:
        print("Hello there!")