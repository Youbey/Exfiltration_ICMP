from scapy.all import IP, ICMP, send, sniff
import base64
import re

def decode_icmp_response(packet):
    # Vérifie si le paquet est de type ICMP et provient d'une adresse se terminant par .200
    if ICMP in packet and check_ip(packet[IP].src):
        file_contents = packet[ICMP].load
        # Supprime le faux message à la fin du fichier
        file_contents = file_contents.split(b'P4s')[0]
        # Décode le contenu du fichier à partir de Base64
        try:
            decoded_contents = base64.b64decode(file_contents).decode('utf-8')
            print("Réponse ICMP reçue :")
            print(decoded_contents)
            # Sauvegarde le fichier
            with open("received_file.txt", "w") as received_file:  # Ouvre le fichier en mode texte
                received_file.write(decoded_contents)
                print("Fichier sauvegardé sous 'received_file.txt'")
        except Exception as e:
            print(f"Erreur de décodage : {e}")

def check_ip(ip):
    # Retourne True si l'adresse IP se termine par .200, sinon False
    return ip.endswith('.200')

if __name__ == "__main__":
    target_ip = "192.168.38.200"  # Remplacez par l'adresse IP cible
    # Écoute des réponses ICMP pour 30 secondes
    sniff(filter="icmp", prn=decode_icmp_response, timeout=30)
