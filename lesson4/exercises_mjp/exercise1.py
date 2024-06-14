from rich import print as rprint
from pathlib import Path

base_dir = Path.cwd()
file_name = 'lesson4/exercises_mjp/show_ip_int_brief.txt'
file_path = base_dir / file_name

data = []

with open(file_path, 'r') as file:
    data = file.readlines()

intf_ip = {}
for line in data:
    line = line.split()
    
    intf = line[0]
    ip = line[1]

    if ip == 'IP-Address' or ip == 'unassigned':
        continue

    intf_ip.update({intf: ip})

print()
rprint(intf_ip)
print()
