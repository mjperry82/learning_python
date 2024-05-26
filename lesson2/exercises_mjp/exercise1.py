from ipaddress import ip_address,ip_interface,ip_network

ip_base = "192.168.254."

prefix_length = input("Enter a prefix length between 25 and 30: ")
prefix_length = int(prefix_length)

host_length = 32 - prefix_length
num_ips = 2**host_length
num_hosts = num_ips - 2

network1 = 0
network2 = network1 + num_ips

host1 = network1 + 1
host2 = network2 - 2

print(f'There are {num_hosts} in each subnet.')
print(f'The network number of the first subnet is {network1} and the second subnet is {network2}.')
print(f'The first host of subnet one is {host1} and the last host is {host2}.')