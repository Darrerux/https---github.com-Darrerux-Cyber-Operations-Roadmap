blocked_ports = [21, 3, 445]
def check_port(port_number):

    if port_number in blocked_ports :
        return "Danger: Port Blocked"
    else:
        return "Port Allowed"
status_1 = check_port(21)
print(f"Port is:{status_1}")