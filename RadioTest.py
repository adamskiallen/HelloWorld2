import keyboard as key # type: ignore
import time

radio = True
freq = 1000

print("Radio Initiated")
while radio == True:
    if key.read_key() == "w":
        if freq == 1700:
            freq = 540
        else:
            freq = freq + 10    
        print(freq,"KHz")
        print(radio)
    elif key.read_key() == "s":
        if freq == 540:
            freq = 1700
        else:
            freq = freq - 10
        print(freq, "KHz")
        print(radio)
    elif key.read_key() == "o":
        print("Radio Off")
        radio = False
        time.sleep(5)
        print("I'm still sleeping")
        time.sleep(10000)
        