exercise_folder = 'lesson2/exercises_mjp/'

file_name = 'show_version.txt'
file_location = exercise_folder + file_name

file = open(file_location, "r")

data = file.read()

print(data.split("\n")[0])
print(type(data))

file.close()

print()
print()

with open(file_location, "r") as file:
    data = file.readlines()
    print(data[0])
    print(type(data))