from machine import PWM, Pin
from time import sleep

servo = PWM(Pin(28))
servo.freq(50)

angle_0 = int(2.5 / 20 * 65536)
angle_45 = int(2.0 / 20 * 65536)
angle_90 = int(1.5 / 20 * 65536)
angle_135 = int(1.0 / 20 * 65536)
angle_180 = int(0.5 / 20 * 65536)
angle_45=int(2.0/20*65536)

#import random
#r=random.randint(1,5)
servo.duty_u16(0)
i=0
while i<1:
    if servo.duty_u16(angle_0):
        break
    else:
        servo.duty_u16(angle_0) #そこから動くじゃなく、毎回０の位置に移動
        sleep(2)
        servo.duty_u16(angle_45)
        sleep(2)
        servo.duty_u16(angle_90)
        sleep(2)
        servo.duty_u16(angle_135)
        sleep(2)
        servo.duty_u16(angle_180)
        sleep(2)
        i+=1