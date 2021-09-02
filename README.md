BenchPi.py<br><br>
Benchmark your pi and compare it's CPU power with your other devices.. <br><br>
This script uses imagemagic to create and rotate pitcures, add a frame and so on, loading the CPU.<br><br>
You can adjust the picture quality, quantity enable verbose details, and check the the result of sequential/multithread shell commands by either setting script options or  specifying arguments during command line .<br>
<br>
Prerequisite : install ImageMagick :<br>
>  <b>sudo apt install imagemagick -y</b><br>

Download BenchPi.py: <br>
>  <b>git clone https://github.com/apicole/BenchPi; cd BenchPi;</b><br>

Usage : <br>
 >  <b>nano BenchPi.py</b><br>
    * Adjust quantity and quality of images to manipulate on lines 4-5-6-7
 
 >  <b>python3 BenchPi.py</b><br>
    * Run the Benchmark with 'default' parameters previously set

 >  <b>python3 BenchPi.py 1 5 m</b><br>
    * Run the Benchmark with command line arguments :

    - 1 = verbose (0/1)
    - 5 = quantity of images to process
    - m = quality of images to process
    
<br>
Here is a basic comparison between a pi0 or a pi3b+, being the time for overall calculation<br><br><br>
  Pi&nbsp;&nbsp;Pic quality&nbsp;&nbsp;Sequential&nbsp;Multithread*<br> 

  <br>
  3b+&nbsp;&nbsp;4&nbsp;x&nbsp;s &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;21 sec&nbsp;&nbsp;&nbsp;&nbsp;14 sec<br>
  3b+&nbsp;&nbsp;4&nbsp;x&nbsp;m &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;37 sec&nbsp;&nbsp;&nbsp;&nbsp;22 sec<br>
  3b+&nbsp;&nbsp;4&nbsp;x&nbsp;l &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;84 sec&nbsp;&nbsp;&nbsp;&nbsp;54 sec<br>
  pi4&nbsp;&nbsp;&nbsp;4&nbsp;x&nbsp;l &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;xx sec&nbsp;&nbsp;&nbsp;&nbsp;14 sec<br>
<br>
 With other dimensions.. <br>
  3b+&nbsp;&nbsp;4x380Ko&nbsp;&nbsp;&nbsp;&nbsp;25 sec&nbsp;&nbsp;&nbsp;&nbsp;15 sec<br>
  pi0&nbsp;&nbsp;4x380ko&nbsp;&nbsp;&nbsp;107 sec&nbsp;&nbsp;&nbsp;103 sec<br>
  3b+&nbsp;&nbsp;4x622Ko&nbsp;&nbsp;&nbsp;&nbsp;52 sec&nbsp;&nbsp;&nbsp;&nbsp;27 sec<br>
  pi0&nbsp;&nbsp;4x622Ko&nbsp;&nbsp;&nbsp;150 sec&nbsp;&nbsp;&nbsp;N/A<br>
  
* Multithread* relates to a command ran with & - not expecting return instantly.

