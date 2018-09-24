import netifaces
import platform
import requests
import socket

network = {}
computer_data = {}

network["ip"] = requests.get("https://api.ipify.org").text
network["local_ip"] = socket.gethostbyname(socket.gethostname())
network["hostname"] = socket.gethostname()
network["mac_addr"] = netifaces.ifaddresses("eth0")[netifaces.AF_LINK][0]["addr"]

computer_data["processor"] = platform.processor()
computer_data["type"] = platform.machine()
computer_data["system"] = platform.system()
computer_data["version"] = platform.platform()
computer_data["release"] = platform.uname().release

network["computer"] = computer_data

print(network)
