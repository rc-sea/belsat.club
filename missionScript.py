import picamera
import vcgencmd
import datetime as dt
from time import sleep
from picamera import PiCamera

camera = PiCamera()
sleep(0)
#time until start recording

for x in range(30):#how many times loop will run
    camera.annotate_text = dt.datetime.now().strftime('%H:%M:%S')
    with open("video record.txt", "a") as myfile:
            myfile.write("video "+str(x)+" started at" + "   Time:" + str(dt.datetime.now().strftime('%H:%M:%S')) + "\n")

    camera.start_recording("video" + str(x) + ".h264")

    sleep(2)
    #length of video
                         
    camera.stop_recording()
    
    with open("video record.txt", "a") as myfile:
        myfile.write("video "+str(x)+" ended at" + "     Time:" + str(dt.datetime.now().strftime('%H:%M:%S')) + "\n")
    sleep(5)
    #length of wait time
