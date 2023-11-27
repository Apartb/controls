import board
import digitalio

led = digitalio.DigitalInOut(board.GP18)
led.direction = digitalio.Direction.OUTPUT
pi_input = diigitalio.DigitalInOut(board.GP13)
pi_input.switch_to_input(pull=digitalio.Pull.DOWN)
while True:
  if pi_input.value == True:
    print("received")
    led.value = True
  else:
    led.value = False
