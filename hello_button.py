import pigpio
from time import sleep


pi = pigpio.pi()
pi.set_mode(27, pigpio.OUTPUT)
pi.set_mode(17, pigpio.INPUT)
pi.set_pull_up_down(17, pigpio.PUD_DOWN)

while True:
    if pi.read(17) == 1:
        pi.write(27, True)
        sleep(3.2)
        pi.write(27, False)
        sleep(3.2)
    