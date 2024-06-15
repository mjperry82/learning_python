from rich import print as rprint
from pathlib import Path

import re

base_dir = Path.cwd()
current_dir = 'lesson5/exercises_mjp/'
file_name = 'aruba_cx_show_ipv6_intf.txt'
file_path = base_dir / current_dir / file_name

with open(file_path, 'r') as file:
    data = file.read()

print()

intf_name_raw = r'(?P<intf_name>[\d/]+)'
intf_state_raw = r'(?P<intf_state>[\w]+)'
admin_state_raw = r'^Admin state is\s+(?P<admin_state>[\w}]+)$'
ipv6_addr_raw = r'^IPv6 address:\n\s+(?P<ipv6_addr>[\w:]+/\d{1,3})'

intf_name = None
intf_state = None
admin_state = None
ipv6_addr = None

pattern = rf'^Interface\s+{intf_name_raw}\s+is\s+{intf_state_raw}$'

match = re.search(pattern, data, flags=re.M)

if match:
    intf_name = match.group('intf_name')
    intf_state = match.group('intf_state')

match = re.search(admin_state_raw, data, flags=re.M)

if match:
    admin_state = match.group('admin_state')

match = re.search(ipv6_addr_raw, data, flags=re.M)

if match:
    ipv6_addr = match.group('ipv6_addr')

print(f'Interface name: {intf_name}')
print(f'Interface State: {intf_state}')
print(f'Admin State: {admin_state}')
print(f'IPv6 Address: {ipv6_addr}')    

