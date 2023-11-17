from scapy.all import IP, ICMP, send, sniff
import time
from scapy.packet import Raw
from scapy.layers.inet import ICMP
import base64

def send_file_in_icmp_request(file_path: str, ip_address: str):
    # Read the file contents
    with open(file_path, "rb") as f:
        file_contents = f.read()

    # Modify the file contents (e.g., encode or compress it)
    # For demonstration, let's assume we encode it in base64
    encoded_contents = base64.b64encode(file_contents)

    # Create an ICMP echo request packet with the modified file contents
    icmp_packet = IP(dst=ip_address) / ICMP() / Raw(load=encoded_contents)

    # Send the ICMP request packet
    send(icmp_packet)

def decode_icmp_response(packet):
    if ICMP in packet and packet[ICMP].type == 8:
        file_contents = packet[ICMP].load
        decoded_contents = base64.b64decode(file_contents)
        print("Received ICMP response:")
        print(decoded_contents.decode())
        # Save the file
        with open("received_file.txt", "wb") as received_file:
            received_file.write(decoded_contents)
            print("File saved as received_file.txt")

if __name__ == "__main__":
    file_path = "C:\\Users\\ayoub\\OneDrive\\Documents\\UBS\\A1\\Réseau\\test.txt"
    target_ip = "192.168.172.242"
    send_file_in_icmp_request(file_path, target_ip)

    # Listen for ICMP responses for 30 seconds
    # sniff(filter=f"icmp and host {target_ip}", prn=decode_icmp_response, timeout=30)
