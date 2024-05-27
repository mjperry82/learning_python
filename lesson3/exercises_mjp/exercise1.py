base_ip = "192.168.254."
banner = "-" * 80

while True:
    prefix = input("Please enter a subnet prefix between 25 and 30: ")
    prefix = int(prefix)
    if prefix >= 25 and prefix <= 30:
        break
    
    error = f"You entered {prefix} which is not between 25 and 30"
    print(error)

host_length = 32 - prefix
number_ips = 2 ** host_length
hosts_per_subnet = number_ips - 2

print("Subnets:")
print(f" Number of subnets: {int(256/number_ips)}")
print(f" Hosts per subnet: {hosts_per_subnet}")
network_ip = 0
while network_ip <256:
    print(f" Subnet Number: {base_ip}{network_ip}")
    if network_ip == 0:
        host1 = network_ip + 1
        host2 = network_ip + hosts_per_subnet
        print(f"  The first host is {base_ip}{host1}")
        print(f"  The last host is {base_ip}{host2}")
    network_ip += number_ips


