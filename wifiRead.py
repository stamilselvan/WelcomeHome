import subprocess
import re
import time

beepDone = False;

while True:
	output = subprocess.run(['ifconfig', 'wlp2s0'], stdout=subprocess.PIPE)
	outStr = output.stdout.decode('utf-8')
	m = re.search('inet addr:(192\.\d*\.\d*\.\d*)',outStr)
	ipAddress = m.group(1)

	ipAndSlash = ipAddress + "/24"

	nMapOut = subprocess.run(['sudo', 'nmap', '-sn', ipAndSlash], stdout=subprocess.PIPE)
	nMapOutStr = nMapOut.stdout.decode('utf-8')
	matchAll = re.findall('Host is up ', nMapOutStr)
	count = len(matchAll)

	if count == 3:
		break

	if count == 2:
		if beepDone == False:
			subprocess.run(['play', 'beep.mp3'], stdout=subprocess.PIPE)
			beepDone = True
		time.sleep(1)
		
	if count == 1:
		time.sleep(120) 

subprocess.run(['play', 'song.mp3'], stdout=subprocess.PIPE)