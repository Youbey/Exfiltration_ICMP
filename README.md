# Exfiltrating a File Through an ICMP Packet

This project is about exfiltrating a file through an ICMP packet. You can choose between the first method `ICMP_scapy.py` which has the basic fonctionality to send a coded file through an ICMP packet. Or `ICMP_scapy2.py`that has more security added to it, for example it sends more than one ICMP packet, the file is coded and it has corrupt characters added to the coded file to keep it from being recognized and decoded.

The following are the steps to run the project:

1. Clone the repository.
2. Install the required libraries.
3. Run the script.

For more information on how to run the project, please refer to the [Usage](#usage) section.

**Please note that this project is for educational purposes only and should not be used for any malicious activities.**

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Getting Started

All you have to do is to download the file `ICMP_scapy.py` and `test.txt` files, download the libraries in the 
[Prerequesities](#prerequisites) and you're good to go :)

### Prerequisites

You need python 3.x on your machine and the following libraries:
 - scapy
 - time
 - random
 - base64

## Usage

Both methods are user-friendly! Simply input the IP address of your destination into the `target_IP` field for both approaches. Additionally, enter your IP address on the receiver's machine for the first method.
