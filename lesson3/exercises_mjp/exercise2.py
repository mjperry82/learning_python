exercise_folder = 'lesson3/exercises_mjp/'
file_name = 'show_ip_int_brief.txt'
file = exercise_folder + file_name

data = []
with open(file, 'r') as f:
    data = f.readlines()

target_line = [ x for x in data if '10.220' in x ]

target_line = target_line[0].split()

intf_name = target_line[0]
ip_addr = target_line[1]

print(f"Interface name: {intf_name}")
print(f"Ip address is: {ip_addr}")