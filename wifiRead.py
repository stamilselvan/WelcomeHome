import subprocess
import re
import time

while True:
	output = subprocess.run(['ifconfig', 'wlp2s0'], stdout=subprocess.PIPE)
	outStr = output.stdout.decode('utf-8')
	m = re.search('inet addr:(192\.\d*\.\d*\.\d*)',outStr)
	ipAddress = m.group(1)

	ipAndSlash = ipAddress + "/24"
	print(ipAndSlash)

	nMapOut = subprocess.run(['sudo', 'nmap', '-sn', ipAndSlash], stdout=subprocess.PIPE)
	nMapOutStr = nMapOut.stdout.decode('utf-8')
	matchAll = re.findall('Host is up ', nMapOutStr)
	count = len(matchAll)
	print(count)
	
	if count == 3:
		break

	if count == 2:
		break
		time.sleep(2) 
	if count == 1:
		time.sleep(2) 
		print("sleep")

subprocess.run(['play', 'music.mp3'], stdout=subprocess.PIPE)