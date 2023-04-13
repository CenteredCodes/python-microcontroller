from picozero import RGBLED, Speaker, Switch
from time import sleep

rgb = RGBLED(red=1, green=2, blue=3)
pull = Switch(18)
pulll = Switch(16)
speaker = Speaker(5)

def pop():
    print("Pop")
    rgb.color = (255, 0, 255)
    speaker.play(262,0.1)
    rgb.color = (0,0,0)
    sleep(0.1)
    rgb.color = (255, 0, 255)
    speaker.play(262, 0.6)
    rgb.off()
    
def pop1():
    print("POP!!!!")
    speaker.play(2620,0.1)
    rgb.color = (0,0,0)
    sleep(0.1)
    rgb.color = (100, 100, 100)
    speaker.play(2620, 0.6)
    rgb.off()


pull.when_closed = pop
pulll.when_closed = pop1