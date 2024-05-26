exercise_folder = 'lesson2/exercises_mjp/'
banner = '-' * 80
file_name = 'show_arp.txt'
file_location = exercise_folder + file_name

show_arp = []
with open(file_location, 'r') as file:
    show_arp = file.readlines()

print(banner)
print(f"'show_arp' type is {type(show_arp)} and its length is: {len(show_arp)}")
print()
print("show arp preview:")

print(f"    {show_arp[0]}")
print(f"    {show_arp[1]}")
print(f"    {show_arp[-1]}")
print(banner)

print()

fields = show_arp[0].split()
print(banner)
print(f"There are {len(fields)} entries in 'fields'")
print(f"The first entry in fields is '{fields[0]}' and the last entry is '{fields[-1]}'")
fields.remove('(min)')
fields[3] = fields[3] + '_' + fields[4]
fields.remove('Addr')
print(fields)
print(banner)