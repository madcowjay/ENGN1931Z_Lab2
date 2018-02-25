import picamera
import time

camera = picamera.PiCamera()
camera.rotation = 180
camera.resolution = (1920, 1080)
camera.framerate = 15
camera.start_preview()
time.sleep(2)
camera.start_recording('video.h264')
time.sleep(10)
camera.stop_recording()
camera.capture('image.jpg')
camera.stop_preview()

