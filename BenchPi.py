#!/usr/bin/python3
import sys
import subprocess
import os
import time
from datetime import datetime

# OPTIONS : number and size of pictures to be resized
number = 4
size   = "m"   # s / m / l
verbose= 0
multi  = " &"  # Either " &" or ""
convertcmd = ""

if len(sys.argv) > 1 :
        verbose = int(sys.argv[1])
        number  = int(sys.argv[2])
        size    = sys.argv[3]



def cleanup():
        for image in range(1,number+2):
                if (os.path.exists("img"+str(image)+".png")): os.unlink( "img"+str(image)+".png")
                if (os.path.exists(str(image)+".txt")): os.unlink( str(image)+".txt")
        if (os.path.exists("finale.jpg")): os.unlink( "finale.jpg")

cleanup()
start = time.time()
if len(sys.argv)>1:print( open('/sys/firmware/devicetree/base/model', 'r').read() + "  > " + str(number) + " x " + size)

if verbose:print(datetime.now().strftime("%H:%M:%S") + "   > Start benchmark")
for image in range(1,number+1):
        convertarg = size + "img.jpg -mattecolor white -frame 30 -background transparent -rotate "+ str(image*45) +" -resize 73% img"+str(image)+".png"
        subprocess.run (['convert ' +convertarg+ ' && echo 1 > '+ str(image)+ '.txt' + multi], shell=True)  #1 // parallel
        convertcmd += " -composite img" + str(image) + ".png -geometry +930+100"
        if verbose:print(datetime.now().strftime("%H:%M:%S") + "   >> Start Thread"+ str(image)+ ": convert "+size + "img.jpg -mattec ... img"+str(image)+".png" )
for image in range(1,number+1):
        while not (os.path.exists(str(image)+".txt")):
                time.sleep(1)
if verbose:print(datetime.now().strftime("%H:%M:%S") + "   << End Threads")
convertcmd = "logo.png -mattecolor white -frame 30 img1.png -geometry +150+80" + convertcmd + " -composite finale.jpg"
subprocess.run (['convert ' +convertcmd+ ' && echo 5 > 5.txt'], shell=True)  #2
while not (os.path.exists("5.txt")):
        time.sleep(1)
if verbose:print(datetime.now().strftime("%H:%M:%S") + "   < End benchmark ")
print( open('/sys/firmware/devicetree/base/model', 'r').read() + "  > " + str(number) + " x " + size + " = "+ str(round(time.time()- start, 3)) + " sec")
cleanup()
quit()
