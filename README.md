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

### Veil - backdoor framework

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
