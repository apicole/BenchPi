#!/usr/bin/python3
import subprocess
import os
import time
from datetime import datetime

# OPTIONS : number and size of pictures to be resized 
number = 4
size = "l"   # s / m / l

def cleanup():
        for image in range(1,number+2):
                if (os.path.exists("img"+str(image)+".png")): os.unlink( "img"+str(image)+".png")
                if (os.path.exists(str(image)+".txt")): os.unlink( str(image)+".txt")
        if (os.path.exists("finale.jpg")): os.unlink( "finale.jpg")

cleanup()
start = time.time()
print(datetime.now().strftime("%H:%M:%S") + "   > Start benchmark")
for image in range(1,number+1):
        convertarg = size + "img.jpg -mattecolor white -frame 30 -background transparent -rotate "+ str(image*45) +" -resize 73% img"+str(image)+".png"
        #subprocess.run (['convert ' +convertarg+ ' && echo 1 > '+ str(image)+ '.txt'], shell=True)  #1 /+/ sequential
        subprocess.run (['convert ' +convertarg+ ' && echo 1 > '+ str(image)+ '.txt &'], shell=True)  #1 // parallel
        print(datetime.now().strftime("%H:%M:%S") + "   >> Start Thread"+ str(image)+ ": convert "+size + "img.jpg -mattec ... img"+str(image)+".png" )
for image in range(1,number+1):
        while not (os.path.exists(str(image)+".txt")):
                time.sleep(1)
print(datetime.now().strftime("%H:%M:%S") + "   << End Threads")
convertcmd = "logo.png -mattecolor white -frame 30 img1.png -geometry +150+80 -composite img2.png -geometry +930+100 -composite img3.png -geometry +550+560 -composite img4.png -geometry +1190+580 -composite finale.jpg"
subprocess.run (['convert ' +convertcmd+ ' && echo 5 > 5.txt'], shell=True)  #2
while not (os.path.exists("5.txt")):
        time.sleep(1)
print(datetime.now().strftime("%H:%M:%S") + "   < End benchmark ")
print( "  > "+ str(round(time.time()- start, 3)) + " Secondes")
cleanup()
quit()
