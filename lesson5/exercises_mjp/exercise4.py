from rich import print as rprint
from pathlib import Path

import re

base_dir = Path.cwd()
current_dir = 'lesson5/exercises_mjp/'
file_name = 'show_lldp.txt'
file_path = base_dir / current_dir / file_name

with open(file_path, 'r') as file:
    data = file.read()

pattern = r'^Chassis id:.+?Vlan ID:.+?$'

match = re.findall(pattern, data, flags=re.M|re.DOTALL)

remote_system_name_raw = r'(?P<remote_port>.+?$)'
remote_port_raw = r'(?P<local_port>.+?$)'
local_port_raw = r'(?P<system_name>.+?$)'

pattern = rf'^Port id:\s+{remote_system_name_raw}.+?Local Port id:\s+{remote_port_raw}' + \
    rf'.+?^System Name:\s+{local_port_raw}'

print()
for item in match:
    m = re.search(pattern, item, flags=re.M|re.DOTALL)
    
    local_port = m.group('local_port')
    system_name = m.group('system_name')
    remote_port = m.group('remote_port')

    print(f'Local Port: {local_port}')
    print(f'System Name: {system_name}')
    print(f'Remote Port: {remote_port}')
    print()