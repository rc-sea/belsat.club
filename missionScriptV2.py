import picamera
import datetime as dt
from time import sleep
from picamera import PiCamera
start = 0
#start = time until camera starts
vloop = 30
ploop = 30
#loop = number of loops that will run(this is multiplied
        #by the time of the video to get the total running time)
vtime = 150
blinkon = 1
blinkoff = 4
blinkloop = 3
#time = length of the video you want running(if you want a blinking led this is
        #split into blinktime, blinkbreak and blinkloop)
        #vtime = blinkloop(blinkon + blinkoff)
vwait = 5
pwait = 5
#wait = time in between videos recording

#------------------------------------------------------

print("here")

camera = PiCamera()
camera.resolution = (1024, 768)
sleep(start)

for x in range(vloop):#how many times loop will run
    camera.annotate_text = dt.datetime.now().strftime('%H:%M:%S')
    #with open("video record.txt", "a") as myfile:
        #myfile.write("video "+str(x)+" started at" + "   Time:" + str(dt.datetime.now().strftime('%H:%M:%S')) + "\n")
    #--------This would be the data of video starting----------

    camera.start_recording("video" + str(x) + ".h264")

    for x in range(blinkloop):
        #blink green light on
        sleep(blinkon)
        #blink green off
        sleep(blinkoff)
    #length of video
                         
    camera.stop_recording()

    print("here2")
    
    #with open("video record.txt", "a") as myfile:
        #myfile.write("video "+str(x)+" ended at" + "     Time:" + str(dt.datetime.now().strftime('%H:%M:%S')) + "\n")
    sleep(vwait)

    for x in range(ploop):
        camera.capture('foo.jpg')
        sleep(pwait)
    print("here3")
