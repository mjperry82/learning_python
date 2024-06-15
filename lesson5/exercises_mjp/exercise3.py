from rich import print as rprint
from pathlib import Path

import re

base_dir = Path.cwd()
current_dir = 'lesson5/exercises_mjp/'
file_name = 'arista_show_ip_arp.txt'
file_path = base_dir / current_dir / file_name

with open(file_path, 'r') as file:
    data = file.read()

ip_addr_raw = r'(?P<ip_addr>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
mac_addr_raw = r'(?P<mac_addr>\w{4}\.\w{4}\.\w{4})'
pattern = rf'^{ip_addr_raw}.+?{mac_addr_raw}'

match = re.findall(pattern, data, flags=re.M)

arp_list = []
if match:
    arp_list = dict(match)

rprint(arp_list)