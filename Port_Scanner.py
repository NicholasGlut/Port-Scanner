import socket

print("\nThis is a program that scans ports within a specified range.")

while True:
    host = input("\nEnter IP address (Type exit to exit): ")
    if host.upper() == "EXIT":          # Exits program
        exit()
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creates a socket 
        s.settimeout(1)     
        ping = s.connect_ex((host,80)) # Attempts conncetion to port 80
        print(f"ping returned {ping}")
        if ping == 0:
            print(f"{host} is up.")
            break
        else:
            # Sometimes the ping does not return 0 but is up, takes this into account
            print(f"{host} is down.")
            i = input("would you like to scan anyway (Y/N)? ")
            if i == "Y":
                break
            else:
                continue
    except socket.error:
        print(f"{host} is down.")


start_port = int(input("Enter starting port: "))
end_port = int(input("Enter final port: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(0.1)

total_ports = 0
open_ports = []

try:
    # for loop scanning each port
    for port in range(start_port, end_port + 1):  
        if s.connect_ex((host,port)) == 0:
            print(f"Port {port} is open on {host}.")
            total_ports += 1
            open_ports.append(port)
        else:
            print(f"Port {port} is closed on {host}")
except socket.error as e:
    print(f"Error conecting to {host}:{port}:{e}")
finally:
    s.close()

print(f"\nAll ports within range {start_port} and {end_port} have been scanned. ")
print(f"There are total of {total_ports} open on {host}")
print(f"These are all open ports:\n{open_ports}")
