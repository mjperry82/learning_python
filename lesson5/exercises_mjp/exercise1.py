from rich import print as rprint
from pathlib import Path

import re

base_dir = Path.cwd()
current_dir = 'lesson5/exercises_mjp/'
file_name = 'show_version.txt'
file_path = base_dir / current_dir / file_name

with open(file_path, 'r') as file:
    data = file.read()

model = r'(?P<model>[\w-]+)'
serial = r'(?P<serial>[\w]+$)'
pattern = rf'^cisco\s+{model}.*ID\s+{serial}'
#pattern = r'^cisco\s+(?P<model>[\w-]+)'

match = re.search(pattern, data, flags=re.MULTILINE|re.DOTALL)

if match:
    print(f'Model: {match.group('model')}')
    print(f'Serial: {match.group('serial')}')