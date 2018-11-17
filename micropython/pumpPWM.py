import machine
from time import sleep

pin19 = machine.Pin(19, machine.Pin.OUT)
pwm19 = machine.PWM(pin19)

pwm19.freq(40)
pwm19.duty(512)

sleep(10)

pwm19.freq(100)
pwm19.duty(128)

sleep(10)

pwm19.freq(200)
pwm19.duty(256)

sleep(10)

pwm19.freq(300)
pwm19.duty(512)
