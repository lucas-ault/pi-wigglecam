from picamera2 import PiCamera2
from time import sleep
from gpiozero import Button

shutter_button = Button(20)
camera = PiCamera2()

camera.start_preview()
shutter_button.wait_for_press()
camera.capture('/home/pi/image.jpg')
camera.stop_preview()