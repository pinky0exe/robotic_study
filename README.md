# robotic_study
Python projects and studying exercises in robotics field. Raspberry PI must have.

hello_blink.py - A program written using the RPi.GPIO module. When executed, it supplies and also removes voltage to pin number 11 at intervals of 3.2 seconds. To end the program, press CTRL + C.

hello_blink_pigpio.py - Similar program as hello_blink.py, but using the pigpio module. The selection of a contact is made not by its physical numbering, but by the numbering of the processor. (We put 17 from GPIO_17 instead of 11, 27 from GPIO_27 instead of 13, etc.)

All the programs listed below are also written using the pigpio module.

hello_button.py - When the program is executed, the signal arriving at the GPIO_17 pin is read. When a signal appears, voltage is applied to the GPIO_27 pin in the same way as in hello_blink_pigpio.py.
​
button_event.py - When the program is executed, the signal arriving at the GPIO_17 pin is read. When the signal state changes, the click_count counter is increased by 1 and displayed on the command line.
