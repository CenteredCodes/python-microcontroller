from machine import Pin, PWM
import utime

MID = 1000000
MIN = 2000000
MAX = 4000000

led = Pin(25, Pin.OUT)
pwm = PWM(Pin(15))

pwm.freq(50)
pwm.duty_ns(MID)

while True:
    pwm.duty_ns(MIN)
    utime.sleep(1)
    pwm.duty_ns(MID)
    utime.sleep(1)
    pwm.duty_ns(MAX)
    utime.sleep(1)
    
    

