import scapy.all as scapy
request = scapy.ARP()
request.pdst = '192.168.205.255/22' #Your IP Address
broadcast = scapy.Ether()
broadcast.dst = 'ff:ff:ff:ff:ff:ff' #Sends a broadcast message
packet = request/broadcast
client = scapy.srp(packet, timeout=3, verbose=0)
print("IP "+" "*18+"Mac")
for sent, received in client:
    print(f'{received.psrc}"+" '*18+f"{received.hwsrc}") #prints the source IP and mac address

