#!/usr/bin/env python3
import subprocess
import argparse
import re

def change_mac(interface, mac):
	print ("[+] Changing MAC Address for "+interface+" to "+mac)
	
	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",mac])
	subprocess.call(["ifconfig",interface,"up"])

def get_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-i","--interface", dest="interface",help="Network interface you want to change")
	parser.add_argument("-m","--mac", dest="mac",help="MAC Address (00:11:aa:ab:a0:0i) you want to use for the interface")
	options = parser.parse_args()
	if not options.interface:
		parser.error("[-] Please specify a network interface, use --help for more info.")
	if not options.mac:
		parser.error("[-] Please specify a MAC Address(ii:nn:in:n0:00:0n), use --help for more info")
	return options

def get_current_mac(interface):
	ifconfig_result = subprocess.check_output(["ifconfig", interface])
	mac_address_search_result = re.search( r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
	if mac_address_search_result:
		return mac_address_search_result.group(0)
	else:
		print ("[-] Could not read MAC address.")

options = get_arguments()
current_mac = get_current_mac(options.interface)
print ("Current MAC = " + str(current_mac))

#change_mac(options.interface, options.mac)
#current_mac = get_current_mac(options.mac)
#if current_mac == options.mac:
#	print ("[+] MAC address was successfully changed to " + current_mac)
#else:
#	print ("[-] MAC address did not get changed.")

