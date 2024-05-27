exercise_folder = 'lesson3/exercises_mjp/'
file_name =  'show_ip_int_brief.txt'
file = exercise_folder + file_name

data = []
with open(file, 'r') as f:
    data = f.readlines()


interfaces = []
ips = []
for line in data:
    line = line.split()
    if line[1][:3] == '10.':
        interfaces.append(line[0])
        ips.append(line[1])

print(interfaces)
print(ips)