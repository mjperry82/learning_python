from rich import print as rprint
from pathlib import Path

base_dir = Path.cwd()
file_name = 'lesson4/exercises_mjp/arubacx_show_vlan.txt'
file_path = base_dir / file_name

with open(file_path, 'r') as file:
    data = file.readlines()

vlans = {}

for line in data[3:]:
    line = line.split()
    vlan_id = int(line[0])
    interfaces = line[5]

    intf_list = []

    interfaces = interfaces.split(',')

    for interface in interfaces:
        if '-' in interface:
            start_intf, end_intf = interface.split('-')
            base_intf = start_intf[:-1]
            start = int(start_intf[-1:])
            end = int(end_intf[-1:])
            for num in range(start,end+1):
                intf_list.append(f"{base_intf}{num}")
        else:
            intf_list.append(interface)
        
    vlans.update({vlan_id: set(intf_list)})

output1 = vlans[1].intersection(vlans[2])
output1= output1.intersection(vlans[3])

output2 = {''}
for key in vlans.keys():
   output2 = output2.union(vlans[key])
output2.remove('')

output3 = vlans[12].union(vlans[13])

rprint(output1)
rprint(output2)
rprint(output3)