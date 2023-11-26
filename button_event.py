import pigpio
from time import sleep

click_count = 0

def button_event(gpio, level, tick):
    global click_count
    if level == pigpio.HIGH:
        click_count += 1
    print(f"Кнопка нажата. Число нажатий {click_count}")
    
pi = pigpio.pi()
pi.set_mode(17, pigpio.INPUT)

cb = pi.callback(17, pigpio.RISING_EDGE, button_event)
try:
    while True:
        sleep(1.0)
        
except (KeyboardInterrupt, SystemExit) as e:
    print("Чистый выход")

except Exception as e:
    print("Плохой выход")

finally:
    cb.cancel()
    pi.stop()

