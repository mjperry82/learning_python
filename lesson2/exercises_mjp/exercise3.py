ip1 = '10.0.0.1'
ip2 = '172.16.0.1'
ip3 = '192.168.255.1'
ip4 = '100.64.0.1'
ip5 = '224.0.0.5'
ip6 = '8.8.8.8'
ip7 = '1.1.1.1'
ip8 = '38.0.0.1'
ip9 = '12.0.0.1'
ip10 = '169.254.1.1'

ip_list = [
    ip1,
    ip2,
    ip3,
    ip4,
    ip5
]

print(ip_list)

ip_list.append(ip6)
ip_list.extend([ip7, ip8])
ip_list = ip_list + [ip9, ip10]

print(ip_list)
ip_list.pop()
ip_list.pop(0)

print(ip_list)

ip_list[0] = '2.2.2.2'

print(ip_list[0])