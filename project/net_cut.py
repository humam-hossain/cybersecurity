#iptables -I FORWARD -j NFQUEUE --queue-num 0
#iptables --flush
#!/usr/bin/env python
import netfilterqueue

def process_packet(packet):
    print (packet)
    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()



