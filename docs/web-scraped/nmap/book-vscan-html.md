# Source: https://nmap.org/book/vscan.html

Title: Chapter 7. Service and Application Version Detection

URL Source: https://nmap.org/book/vscan.html

Markdown Content:
Chapter 7. Service and Application Version Detection | Nmap Network Scanning
===============

[![Image 1](https://nmap.org/shared/images/nst-icons.svg#menu)](https://nmap.org/book/vscan.html#menu)[![Image 2](https://nmap.org/shared/images/nst-icons.svg#close)](https://nmap.org/book/vscan.html#)[![Image 3: Home page logo](https://nmap.org/images/sitelogo.png)](https://nmap.org/)[Nmap.org](https://nmap.org/)[Npcap.com](https://npcap.com/)[Seclists.org](https://seclists.org/)[Sectools.org](https://sectools.org/)[Insecure.org](https://insecure.org/)![Image 4](https://nmap.org/shared/images/nst-icons.svg#search)

[Download](https://nmap.org/download.html)[Reference Guide](https://nmap.org/book/man.html)[Book](https://nmap.org/book/)[Docs](https://nmap.org/docs.html)[Zenmap GUI](https://nmap.org/zenmap/)[In the Movies](https://nmap.org/movies/)
*   [Nmap Network Scanning](https://nmap.org/book/toc.html)
*   Chapter 7.Service and Application Version Detection

[Prev](https://nmap.org/book/mayo-scan.html)

[Next](https://nmap.org/book/vscan-examples.html)

Chapter 7.Service and Application Version Detection
===================================================

Table of Contents

*   [Introduction](https://nmap.org/book/vscan.html#vscan-intro)
*   [Usage and Examples](https://nmap.org/book/vscan-examples.html)
*   [Technique Described](https://nmap.org/book/vscan-technique.html)
    *   [Cheats and Fallbacks](https://nmap.org/book/vscan-technique.html#vscan-cheats-and-fallbacks)
    *   [Probe Selection and Rarity](https://nmap.org/book/vscan-technique.html#vscan-selection-and-rarity)

*   [Technique Demonstrated](https://nmap.org/book/vscan-technique-demo.html)
*   [Post-processors](https://nmap.org/book/vscan-post-processors.html)
    *   [Nmap Scripting Engine Integration](https://nmap.org/book/vscan-post-processors.html#version-detection-nse)
    *   [RPC Grinding](https://nmap.org/book/vscan-post-processors.html#version-detection-rpc)
    *   [SSL Post-processor Notes](https://nmap.org/book/vscan-post-processors.html#vscan-ssl-postprocess)

*   [`nmap-service-probes` File Format](https://nmap.org/book/vscan-fileformat.html)
    *   [`Exclude` Directive](https://nmap.org/book/vscan-fileformat.html#vscan-db-exclude)
    *   [`Probe` Directive](https://nmap.org/book/vscan-fileformat.html#vscan-db-probe)
    *   [`match` Directive](https://nmap.org/book/vscan-fileformat.html#vscan-db-match)
    *   [`softmatch` Directive](https://nmap.org/book/vscan-fileformat.html#vscan-db-softmatch)
    *   [`ports` and `sslports` Directives](https://nmap.org/book/vscan-fileformat.html#vscan-db-ports)
    *   [`totalwaitms` Directive](https://nmap.org/book/vscan-fileformat.html#vscan-db-totalwaitms)
    *   [`tcpwrappedms` Directive](https://nmap.org/book/vscan-fileformat.html#vscan-db-tcpwrappedms)
    *   [`rarity` Directive](https://nmap.org/book/vscan-fileformat.html#vscan-db-rarity)
    *   [`fallback` Directive](https://nmap.org/book/vscan-fileformat.html#vscan-db-fallback)
    *   [Putting It All Together](https://nmap.org/book/vscan-fileformat.html#vscan-fileformat-example)

*   [Community Contributions](https://nmap.org/book/vscan-community.html)
    *   [Submit Service Fingerprints](https://nmap.org/book/vscan-community.html#vscan-submit-prints)
    *   [Submit Database Corrections](https://nmap.org/book/vscan-community.html#vscan-submit-corrections)
    *   [Submit New Probes](https://nmap.org/book/vscan-community.html#vscan-submit-probe)

*   [SOLUTION: Find All Servers Running an Insecure or Nonstandard Application Version](https://nmap.org/book/vscan-find-service-fast.html)
    *   [Problem](https://nmap.org/book/vscan-find-service-fast.html#vscan-find-service-problem)
    *   [Solution](https://nmap.org/book/vscan-find-service-fast.html#vscan-find-service-solution)
    *   [Discussion](https://nmap.org/book/vscan-find-service-fast.html#vscan-find-service-discussion)

*   [SOLUTION: Hack Version Detection to Suit Custom Needs, such as Open Proxy Detection](https://nmap.org/book/vscan-hack-it.html)
    *   [Problem](https://nmap.org/book/vscan-hack-it.html#vscan-hack-it-problem)
    *   [Solution](https://nmap.org/book/vscan-hack-it.html#vscan-hack-it-solution)
    *   [Discussion](https://nmap.org/book/vscan-hack-it.html#vscan-hack-it-discussion)

[](https://nmap.org/book/vscan.html)[](https://nmap.org/book/vscan.html)

Introduction
------------

While Nmap does many things, its most fundamental feature is port scanning. Point Nmap at a remote machine, and it might tell you that ports `25/tcp`, `80/tcp`, and `53/udp` are open. Using its `nmap-services`[](https://nmap.org/book/vscan.html) database of more than 2,200 well-known services, Nmap would report that those ports probably correspond to a mail server (SMTP), web server (HTTP), and name server (DNS) respectively. This lookup is usually accurate—the vast majority of daemons listening on TCP port 25 are, in fact, mail servers. However, you should not bet your security on this! People can and do run services on strange ports. Perhaps their main web server was already on port 80, so they picked a different port for a staging or test server. Maybe they think hiding a vulnerable service on some obscure port prevents “evil hackers” from finding it. Even more common lately is that people choose ports based not on the service they want to run, but on what gets through the firewall. When ISPs blocked port 80 after major Microsoft IIS worms CodeRed and Nimda, hordes of users responded by moving their personal web servers to another port. When companies block Telnet access due to its horrific security risks, I have seen users simply run telnetd on the Secure Shell (SSH) port instead.

Even if Nmap is right, and the hypothetical server above is running SMTP, HTTP, and DNS servers, that is not a lot of information. When doing vulnerability assessments (or even simple network inventories) of your companies or clients, you really want to know which mail and DNS servers and versions are running. Having an accurate version number helps dramatically in determining which exploits a server is vulnerable to. Do keep in mind that security fixes are often back-ported to earlier versions of software, so you cannot rely solely on the version number to prove a service is vulnerable. False negatives are rarer, but can happen when silly administrators spoof the version number of a vulnerable service to make it appear patched.

Another good reason for determining the service types and version numbers is that many services share the same port number. For example, port `258/tcp` is used by both the Checkpoint Firewall-1 GUI management interface and the yak Windows chat client. This makes a guess based on the `nmap-services` table even less accurate. Anyone who has done much scanning knows that you also often find services listening on unregistered ports—these are a complete mystery without version detection. A final problem is that filtered UDP ports often look the same to a simple port scanner as open ports (see [the section called “UDP Scan (`-sU`)”](https://nmap.org/book/scan-methods-udp-scan.html "UDP Scan (-sU)")). But if they respond to the service-specific probes sent by Nmap version detection, you know for sure that they are open (and often exactly what is running).[](https://nmap.org/book/vscan.html)

Service scans sometimes reveal information about a target beyond the service type and version number. Miscellaneous information discovered about a service is collected in the “info” field. This is displayed in the `VERSION` column inside parentheses following the product name and version number. This field can include SSH protocol numbers, Apache modules, and much more.

Some services also report their configured hostnames, which differ from machines' reverse DNS[](https://nmap.org/book/vscan.html) hostnames surprisingly often. The hostname field is reported on a `Service Info` line following the port table. It sounds like a minor information leak, but can have consequences. One year at the CanSecWest security conference, I was huddled up in my room with my laptop. Suddenly the tcpdump window in the corner of my screen went wild and I realized my machine was under attack. I scanned back and found an unusual high port sitting open. Upon connecting, the port spewed a bunch of binary characters, but one ASCII field in the output gave a configured domain name. The domain was for a small enough security company that I knew exactly who was responsible. I had the front desk ring his hotel room, and boy was he surprised when I asked him to stop probing my box.

Two more fields that version detection can discover are operating system and device type. These are also reported on the `Service Info`[](https://nmap.org/book/vscan.html) line. We use two techniques here. One is application exclusivity. If we identify a service as Microsoft Exchange, we know the operating system is Windows since Exchange doesn't run on anything else. The other technique is to persuade more portable applications to divulge the platform information. Many servers (especially web servers) require very little coaxing. This type of OS detection is intended to complement Nmap's OS detection system (`-O`) and can sometimes report differing results. For example, consider a Microsoft Exchange server hidden behind a port-forwarding Unix firewall.

The Nmap version scanning subsystem obtains all of this data by connecting to open ports and interrogating them for further information using probes that the specific services understand. This allows Nmap to give a detailed assessment of what is really running, rather than just what port numbers are open. [Example 7.1](https://nmap.org/book/vscan.html#ex-version-detection-scan1 "Example 7.1. Simple usage of version detection") shows the actual output.

Example 7.1.Simple usage of version detection

[](https://nmap.org/book/vscan.html)# **`nmap -sV -T4 -F insecure.org`**

Starting Nmap ( https://nmap.org )
Nmap scan report for insecure.org (74.207.254.18)
Host is up (0.016s latency).
rDNS record for 74.207.254.18: web.insecure.org
Not shown: 95 filtered ports
PORT    STATE  SERVICE  VERSION
22/tcp  open   ssh      OpenSSH 4.3 (protocol 2.0)
25/tcp  open   smtp     Postfix smtpd
80/tcp  open   http     Apache httpd 2.2.3 ((CentOS))
113/tcp closed auth
443/tcp open   ssl/http Apache httpd 2.2.3 ((CentOS))
Service Info: Host:  web.insecure.org

Nmap done: 1 IP address (1 host up) scanned in 14.82 seconds

Nmap version detection offers the following advanced features (fully described later):

[](https://nmap.org/book/vscan.html)

*   High speed, parallel operation via non-blocking sockets and a probe/match definition grammar designed for efficient yet powerful implementation.

*   Determines the application name and version number where available—not just the service protocol.

*   Supports both the TCP and UDP protocols, as well as both textual ASCII and packed binary services.

*   Multi-platform support, including Linux, Windows, Mac OS X, FreeBSD/NetBSD/OpenBSD, Solaris, and all the other platforms on which Nmap is known to work.

*   If SSL is detected, Nmap connects using OpenSSL (if available) and tries to determine what service is listening behind that encryption layer. This allows it to discover services like HTTPS, POP3S, IMAPS, etc. as well as providing version details.

*   If a SunRPC[](https://nmap.org/book/vscan.html) service is discovered, Nmap launches its brute-force RPC grinder[](https://nmap.org/book/vscan.html) to find the program number, name, and version number.

*   IPv6 is supported, including TCP, UDP, and SSL over TCP.

*   Common Platform Enumeration (CPE)[](https://nmap.org/book/vscan.html) output for interoperation with other software (some information is only included in XML output). See [the section called “Common Platform Enumeration (CPE)”](https://nmap.org/book/output-formats-cpe.html "Common Platform Enumeration (CPE)") for more about CPE.

*   Community contributions: if Nmap gets data back from a service that it does not recognize, a _service fingerprint_[](https://nmap.org/book/vscan.html) is printed along with a submission URL.[](https://nmap.org/book/vscan.html)[](https://nmap.org/book/vscan.html) This system is patterned after the extremely successful Nmap OS Detection fingerprint submission process. New probes and corrections can also be submitted.

*   Comprehensive database: Nmap recognizes more than one thousand service signatures, covering more than 180 unique service protocols from ACAP, AFP, and AIM to XML-RPC, Zebedee, and Zebra.

[](https://nmap.org/book/vscan.html)

* * *

[Prev](https://nmap.org/book/mayo-scan.html)Scanning 676,352 IP Addresses in 46 Hours

[Up](https://nmap.org/book/toc.html)Nmap Network Scanning

[Home](https://nmap.org/book/toc.html)

[Next](https://nmap.org/book/vscan-examples.html)Usage and Examples

![Image 5](https://nmap.org/shared/images/nst-icons.svg#search)

[Nmap Security Scanner](https://nmap.org/)
------------------------------------------

*   [Ref Guide](https://nmap.org/book/man.html)
*   [Install Guide](https://nmap.org/book/install.html)
*   [Docs](https://nmap.org/docs.html)
*   [Download](https://nmap.org/download.html)
*   [Nmap OEM](https://nmap.org/oem/)

[Npcap packet capture](https://npcap.com/)
------------------------------------------

*   [User's Guide](https://npcap.com/guide/)
*   [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)
*   [Download](https://npcap.com/#download)
*   [Npcap OEM](https://npcap.com/oem/)

[Security Lists](https://seclists.org/)
---------------------------------------

*   [Nmap Announce](https://seclists.org/nmap-announce/)
*   [Nmap Dev](https://seclists.org/nmap-dev/)
*   [Full Disclosure](https://seclists.org/fulldisclosure/)
*   [Open Source Security](https://seclists.org/oss-sec/)
*   [BreachExchange](https://seclists.org/dataloss/)

[Security Tools](https://sectools.org/)
---------------------------------------

*   [Vuln scanners](https://sectools.org/tag/vuln-scanners/)
*   [Password audit](https://sectools.org/tag/pass-audit/)
*   [Web scanners](https://sectools.org/tag/web-scanners/)
*   [Wireless](https://sectools.org/tag/wireless/)
*   [Exploitation](https://sectools.org/tag/sploits/)

[About](https://insecure.org/)
------------------------------

*   [About/Contact](https://insecure.org/fyodor/)
*   [Privacy](https://insecure.org/privacy.html)
*   [Advertising](https://insecure.org/advertising.html)
*   [Nmap Public Source License](https://nmap.org/npsl/)

[![Image 6](https://nmap.org/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")[![Image 7](https://nmap.org/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")[![Image 8](https://nmap.org/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")[![Image 9](https://nmap.org/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")
