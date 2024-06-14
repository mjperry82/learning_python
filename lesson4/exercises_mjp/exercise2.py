from rich import print as rprint
from pathlib import Path

base_dir = Path.cwd()
file_name = 'lesson4/exercises_mjp/show_ip_int_brief.txt'
file_path = base_dir / file_name

data = []

with open(file_path, 'r') as file:
    data = file.readlines()

interfaces = {}
for line in data:
    line = line.split()
    if line[4] == 'administratively':
        line[4] = f'{line[4]} {line[5]}'
        line.pop(5)

    if line[0] == 'Interface':
        continue

    intf = line[0]
    ip_addr = line[1]
    line_status = line[4]
    line_protocol = line[5]
    interfaces.update({intf: {
        'ip_addr': ip_addr,
        'line_status': line_status,
        'line_protocol': line_protocol
    }})

print()
rprint(interfaces)
print()