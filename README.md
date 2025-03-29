# SERVER-RAID
SERVER-RAID its an software writted on python to execute resonaince attacks on web aplication servers.

It is very useful not only for gathering information about different technologies but also for gaining access to hidden resources such as secret websites not intended for 
the public, exclusive and private services, APIs, or similar.

The tool comes equipped with automated configurations of Tor and Proxychains so that you can carry out attacks without worrying about your anonymity, although it is always good practice to verify that everything is functioning correctly in case something unexpected occurs. The reconnaissance attacks included in the tool are as follows: 

- Default Webpage download + data entry/file discovery.
- Server type discovery.
- Domain scraping.
- DNS brute force attack.
- Download full webpage from a domain.
- Server supported HTTP methods.
- Server port scan/service discovery.

This tool also evades certain security measures due to the design of the attacks and dynamic anonymity tools, such as: 

- DNSSEC (a commonly used measure to prevent AXFR attacks, which can be bypassed using DNS brute force).
- IP blocking due to excessive queries or geographic origin of the IP.
- WAF evasion for some fingerprinting attacks present in the tool, such as: (server type discovery, HTTP methods discovery).

Please note that there are other security measures, such as 403/401 codes and WAF, for Tor nodes that are not being taken into account...

####Requeriments####

- wget 
- python3 
- git 
- nmap 
- tor
- torsocks
- proxychains
- python3-requests 
- python3-colorama
- python3-dnspython

####knowledge required to understand and manipulate the tool####

Python3 coding structures (loops,variables,functions,libs,arrays and the others...).

HTML/CSS coding.

HTTP Methods.

Server Code answers.

DNS hierarchical structure and theory.

Some security measures on web applications (DNSSEC,WAF,IP blockers and blacklists IPs).

Reconnaissance attacks and their types.

The use of commands and libraries.

Ports,Certificates,Protocols(HTTP/HTTPS/IP/SMTP/IMAP/WEBSOCKET/ICMP/DNS).

APIs of Navigation if you want to spoof youre own data (OS,User-Agent,GPS,Timezone and others...)

The use of online robots and robots.txt file.

####Explanation of attacks that appears on the tool####

1. Default Webpage Download + Data Entry/File Discovery

Explanation: This attack involves downloading the default webpage served by a web server. The attacker looks for file paths and data entry points within the HTML tags of the page. This can include forms, input fields, and links to other resources.

Purpose: The goal is to identify potential vulnerabilities, such as exposed file paths or forms that could be exploited for further attacks (e.g., SQL injection, XSS).

2. Server Type Discovery

Explanation: This technique involves determining the type of web server that is running on a target domain. Like attacker you can achieve this by sending an HTTP GET request and analyzing the response headers, which often contain information about the server software and its version.

Purpose: Knowing the server type helps attackers identify specific vulnerabilities associated with that server software, allowing them to tailor their attacks accordingly.

3. Domain Scraping

Explanation: Domain scraping refers to the process of collecting information from a target domain. This includes retrieving the robots.txt file, which indicates which parts of the site should not be crawled, as well as extracting all href paths (links) and DNS domains listed in the SSL/TLS certificate.

Purpose: The information gathered can be used to map the structure of the website, identify sensitive areas, and discover additional subdomains or services that may be vulnerable.

4. DNS Brute Force Attack

Explanation: A DNS brute force attack involves systematically guessing subdomains of a target domain using a predefined list of common subdomain names. The attacker sends DNS queries to see which subdomains exist.

Purpose: The goal is to uncover hidden or less obvious subdomains that may not be publicly listed but could contain sensitive information or vulnerabilities.

5. Download Full Webpage from a Domain

Explanation: This attack involves downloading the entire content of a webpage, including HTML, CSS, JavaScript, images, and other resources. Tools can be used to fetch all associated files from the server.

Purpose: By analyzing the full webpage, attackers can gather information about the site's structure, technologies used, and potential client-side vulnerabilities (e.g., insecure JavaScript).

6. Server Supported HTTP Methods

Explanation: This technique involves determining which HTTP methods (such as GET, POST, PUT, DELETE) are supported by the web server. Attackers can send requests using different methods and analyze the server's responses to see which methods are allowed.

Purpose: Identifying supported HTTP methods can reveal potential attack vectors. For example, if a server supports the PUT method, it may allow attackers to upload files to the server or explote other kind of HTTP verb tampering methods, which could lead to code execution.

7. Server Port Scan/Service Discovery

Explanation: A port scan is a technique used to identify open ports on a server and the services running on those ports. Attackers use tools like Nmap to probe a range of ports to determine which ones are open and what services are associated with them.

Purpose: The goal is to gather information about the server's configuration and identify potential entry points for further attacks. Open ports may indicate running services that could be vulnerable to exploitation.
