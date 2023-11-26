import pigpio
from time import sleep

pi = pigpio.pi()
pi.set_mode(17, pigpio.OUTPUT)

while True:
    pi.write(17, True)
    sleep(3.2)
    pi.write(17, False)
    sleep(3.2)
