intf = "GigabitEthernet1       10.0.2.15       YES DHCP   up                    up"

intf_fields = intf.split()

intf_name = intf_fields[0]
intf_ip_addr = intf_fields[1]
intf_status = intf_fields[2]
intf_protocol = intf_fields[3]

print(f"Interface name: {intf_name}")
print(f"IP address: {intf_ip_addr}")
print(f"Interface status: {intf_status}")
print(f"Interface protocol: {intf_protocol}")

state_line_status = ( intf_fields[4] == 'up' )
state_protocol_status = ( intf_fields[5] == 'up')

print(f"line status up: {state_line_status}")
print(f"protocol status up: {state_protocol_status}")