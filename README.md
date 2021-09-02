BenchPi.py<br><br><br>
<br>
Benchmark your pi and compare it's CPU power with your other devices.. <br><br>
This script uses imagemagic to create and rotate pitcures, add a frame and so on, loading the CPU.<br><br>
You can change the Sequential&nbsp;Multithread* by (un)commenting line 22 / 23 basically adding " &" at the end to run the shell command without waiting for a result.<br>
<br>
Download : <br>
>  git clone https://github.com/apicole/BenchPi<br>

Usage : <br>
 >  nano BenchPi.py<br>
    - Adjust quantity and size of images to manipulate<br>
 >  python3 BenchPi.py<br>
    - Run the Benchmark<br>

<br><br><br>
For instance,  here is a basic comparison between a pi0 or a pi3b+, being the time for overall calculation<br><br><br>
  Pi&nbsp;&nbsp;Pic Size&nbsp;&nbsp;Sequential&nbsp;Multithread*<br> 
  3b+&nbsp;&nbsp;4x380Ko&nbsp;&nbsp;&nbsp;&nbsp;25 sec&nbsp;&nbsp;&nbsp;&nbsp;15 sec<br>
  pi0&nbsp;&nbsp;4x380ko&nbsp;&nbsp;&nbsp;107 sec&nbsp;&nbsp;&nbsp;103 sec<br>
  3b+&nbsp;&nbsp;4x622Ko&nbsp;&nbsp;&nbsp;&nbsp;52 sec&nbsp;&nbsp;&nbsp;&nbsp;27 sec<br>
  pi0&nbsp;&nbsp;4x622Ko&nbsp;&nbsp;&nbsp;150 sec&nbsp;&nbsp;&nbsp;N/A<br>
  
  3b+&nbsp;&nbsp;4xMedium&nbsp;&nbsp;&nbsp;&nbsp;21 sec&nbsp;&nbsp;&nbsp;14 sec<br>
  3b+&nbsp;&nbsp;4xMedium&nbsp;&nbsp;&nbsp;&nbsp;37 sec&nbsp;&nbsp;&nbsp;22 sec<br>
  3b+&nbsp;&nbsp;4xLarge&nbsp;&nbsp;&nbsp;&nbsp;84 sec&nbsp;&nbsp;&nbsp;54 sec<br>
  pi4&nbsp;&nbsp;4xLarge&nbsp;&nbsp;&nbsp;&nbsp;xx sec&nbsp;&nbsp;&nbsp;14 sec<br>
<br>
* Multithread* relates to a command ran with & - not expecting return instantly.

