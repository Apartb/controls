from gpiozero import LED
from time import sleep

outpin=LED(17)

while True:
  outpin.on()
  sleep(1)
  outpin.off()
  sleep(1)
