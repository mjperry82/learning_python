from rich import print as rprint
from pathlib import Path

import re

base_dir = Path.cwd()
current_dir = 'lesson5/exercises_mjp/'
file_name = 'show_ip_bgp_neighbors.txt'
file_path = base_dir / current_dir / file_name

with open(file_path, 'r') as file:
    data = file.read()

print("\n\n")

bgp_neigbor_ip_raw = r'(?P<bgp_neighbor_ip>[0-9\.]+)'
remote_as_raw = r'(?P<remote_as>[0-9]+)'
bgp_version_raw = r'(?P<bgp_version>[\d])'
remote_router_id_raw = r'(?P<remote_router_id>[\d\.]+)'
bgp_state_raw = r'(?P<bgp_state>[a-zA-Z]+)'

pattern = rf'^BGP neighbor is\s+{bgp_neigbor_ip_raw}.+remote AS\s+{remote_as_raw}' + \
        rf'.+BGP version\s+{bgp_version_raw}.+remote router ID\s+{remote_router_id_raw}' + \
        rf'.+BGP state =\s+{bgp_state_raw}.+\d+w\d+d$'

match = re.search(pattern, data, flags=re.M|re.DOTALL)

bgp_neighbor = {}
if match:
    
    bgp_neighbor = {
        'bgp_neighbor_ip': match.group('bgp_neighbor_ip'),
        'remote_as': match.group('remote_as'),
        'bgp_version': match.group('bgp_version'),
        'remote_router_id': match.group('remote_router_id'),
        'bgp_state': match.group('bgp_state')
    }

rprint(bgp_neighbor)


    