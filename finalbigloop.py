import picamera
import vcgencmd
import datetime as dt
from time import sleep
from picamera import PiCamera

camera = PiCamera()
while vcgencmd.measure_volts('core') != 0:
    camera.annotate_text = dt.datetime.now().strftime('%H:%M:%S')
    camera.start_recording('video' + dt.datetime.now().strftime('%H:%M:%S') + '.h264')
    #camera.wait_recording(10)
    for x in range(10):
        with open("voltage-2.txt", "a") as myfile:
            myfile.write(str(vcgencmd.measure_volts('core')) + "   Time:" + str(dt.datetime.now().strftime('%H:%M:%S')) + "\n")
        sleep(1)
    camera.stop_recording()
    for x in range(60):
        with open("voltage.txt", "a") as myfile:
            myfile.write(str(vcgencmd.measure_volts('core')) + "   Time:" + str(dt.datetime.now().strftime('%H:%M:%S')) + "\n")
        sleep(1)
