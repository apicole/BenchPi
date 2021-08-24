BenchPi.py

Benchmark your pi and compare it's CPU power with your other devices.. 
This script uses imagemagic to create and rotate pitcures, add a frame and so on, loading the CPU.

For instance,  here is a basic comparison between a pi0 or a pi3b+, being the time for overall calculation

Pi		Pic Size	Sequential Multithread*
3b+		4x380Ko 	25 sec		15 sec
pi0		4x380ko	   107 sec     103 sec
3b+		4x622Ko   	52 sec		27 sec
pi0     4x622Ko    150 sec      N/A

* Multithread* relates to a command ran with & - not expecting return instantly.

