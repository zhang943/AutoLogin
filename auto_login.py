import os
import sys
import threading

import requests


def login():
    login_url = "http://p.nju.edu.cn/portal_io/login"
    data = {"username": username, "password": password}
    response = requests.post(login_url, data)
    print(response.json().get("reply_msg"))


def check_network_status():
    timeout = os.system("ping baidu.com -c 4")
    if timeout:
        login()
    else:
        print("The network connection is normal.\n")

    timer = threading.Timer(interval, check_network_status)
    timer.start()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python login.py interval username password")
        exit(-1)
    interval = int(sys.argv[1])
    username = sys.argv[2]
    password = sys.argv[3]

    check_network_status()
