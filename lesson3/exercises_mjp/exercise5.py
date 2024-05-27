exercise_folder = 'lesson3/exercises_mjp/'
file_name =  'junos_show_arp.txt'
file = exercise_folder + file_name

data = []
with open(file, 'r') as f:
    data = f.readlines()

ips = []
macs = []
for line in data[1:-1]:
    line = line.split()
    macs.append(line[0].replace(':','-'))
    ips.append(line[1])

print(macs)
print(ips)
