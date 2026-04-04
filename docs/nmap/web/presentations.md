# Source: https://nmap.org/presentations/

Title: Fyodor's Nmap Presentations (Video, Audio, and Slides)

URL Source: https://nmap.org/presentations/

Markdown Content:
**Fyodor's Nmap Presentations**

[![Image 1](http://fpix.us/pics_me/fyodor-csw08-ryo-talk-crop-scale-250x250.jpg)](http://fpix.us/pics_me/fyodor-csw08-ryo-talk-crop-2450x2450.jpg)
I ([Fyodor](http://insecure.org/fyodor/)) gave my first formal security presentation at CanSecWest in May of 2000 and have enjoyed speaking ever since. Security conferences are a great way to learn, network, and party with like-minded hackers. I've presented at many events, including [Defcon](http://www.defcon.org/), [CanSecWest](http://www.cansecwest.com/), [Black Hat Briefings](http://www.blackhat.com/), [IT Security World](http://www.misti.com/default.asp?page=65&Return=70&ProductID=5091), [Security Masters' Dojo](http://www.cansecwest.com/dojo.html), [ShmooCon](http://www.shmoocon.org/), [IT-Defense](http://www.it-defense.de/), [FOSDEM](http://www.fosdem.org/), [SFOBug](http://www.sfobug.org/), [Stanford University](http://www.stanford.edu/), [George Washington University](http://www.gwu.edu/), and various corporate events.

Many of my presentations are listed on this page. Most of them only have slides available, which often don't provide enough context to follow the talks. Some of my newer talks (where noted) have video and audio recordings posted.

[](https://nmap.org/presentations/)
These are my favorite presentations with audio and video available.

[Black Hat USA / Defcon 2010—Mastering the Nmap Scripting Engine](https://nmap.org/presentations/BHDC10/)

[![Image 2](https://nmap.org/presentations/BHDC10/defcon18-preso-thumbnail-300x250.jpg)](https://nmap.org/presentations/BHDC10/) Most hackers can use [Nmap](https://nmap.org/) for simple port scanning and [OS detection](https://nmap.org/book/man-os-detection.html), but the [Nmap Scripting Engine (NSE)](https://nmap.org/book/nse.html) takes scanning to a whole new level. Nmap's high-speed networking engine can now spider web sites for SQL injection vulnerabilities, brute-force crack and query MSRPC services, find open proxies, and more. Nmap includes more than 130 NSE scripts for network discovery, vulnerability detection, exploitation, and authentication cracking. 
Rather than give a dry overview of NSE, Fyodor and Nmap co-maintainer David Fifield demonstrate practical solutions to common problems. They have scanned millions of hosts with NSE and discuss vulnerabilities found on enterprise networks and how Nmap can be used to quickly detect those problems on your own systems. Then they demonstrate how easy it is to write custom NSE scripts by writing one from scratch and using it to hack a webcam. All in 38 minutes, as given live at Defcon 18!

[Black Hat USA / Defcon 2008—Nmap: Scanning the Internet](https://nmap.org/presentations/BHDC08/)

[![Image 3](https://nmap.org/presentations/BHDC08/pres-snapshot2-scale-300x150.png)](https://nmap.org/presentations/BHDC08/) The [Nmap Security Scanner](https://nmap.org/) was built to efficiently scan large networks, but I took this to a new level by scanning millions of Internet hosts during the Summer of 2008 as part of my Worldscan project. I present the most interesting findings and empirical statistics from these scans, along with practical advice for improving your own scan performance. An overview of new Nmap features is also provided, including the [Nmap Scripting Engine](https://nmap.org/book/nse.html), [Zenmap UI](https://nmap.org/book/zenmap.html), new performance options, Ncat, and Ndiff. Most of these features have since been integrated into official Nmap releases.

[ShmooCon 2006—Advanced Network Reconnaissance with Nmap](https://nmap.org/presentations/Shmoo06)

[![Image 4](https://nmap.org/presentations/Shmoo06/Video-Thumbnail-Scaled-300x228.jpg)](https://nmap.org/presentations/Shmoo06/) While many security practitioners use Nmap, few understand its full power. Nmap deserves part of the blame for being too helpful. A simple command such as "nmap scanme.insecure.org" leaves Nmap to choose the scan type, timing details, target ports, output format, source ports and addresses, and more. You can even specify -iR (random input) and let Nmap choose the targets! Hiding all of these details makes Nmap easy to use, but also easy to grow complacent with. Many people never explore the hundreds of available options and scan techniques for more powerful scanning. 
In this presentation, Nmap author Fyodor details advanced Nmap usage—from clever hacks for teaching Nmap new tricks, to new and undocumented features for bypassing firewalls, optimizing scan performance, finding free porn, defeating intrusion detection systems, and more. A special Shmoo version of Nmap was released at the conference, though all the features discussed are now integrated with official Nmap releases.

[](https://nmap.org/presentations/)
The presentations in this section generally only have slides available (no video), or they are superseeded by newer talks in the [Featured Section](https://nmap.org/presentations/#featured) above.

*   [Wireshark Sharkfest 2011—Nmap Turbo Talk](https://nmap.org/presentations/Sharkfest11/) a short (25 minute) presentation on Nmap and recent work.

*   [CanSecWest 2009—Ninja Scanning](https://nmap.org/presentations/CSW09/) demonstrates new Nmap features and advanced scanning techniques.

*   [iSec Partners Forum (2008)—The New Nmap](https://nmap.org/presentations/iSec08/). A 30-minute presentation about new and upcoming features in Nmap. This was less than 2 weeks after my longer Black Hat and Defcon 2008 talks, and is mostly a subset of that material.

*   Wireshark Sharkfest (2008)—I particpated on a panel on the future of open source networking tools with Wireshark author Gerald Combs, Kismet author Mike Kershaw. Session video is [available here](http://www.lovemytool.com/blog/2008/04/round-table.html).

*   [Defcon 13 (2005)—Nmap Hacking](https://nmap.org/presentations/Defcon13/). I provide several missions related to host discovery, single service discovery on a large network, and bypassing firewalls. Then I demonstrate how to solve them effectively using Nmap and complimentary tools.

*   [CanSecWest 2005—Nmap Hacking](https://nmap.org/presentations/CanSecWest05/). This talk covers advanced host discovery, and introduces the Nmap ARP scanning for the first time

*   [IT-Defense 2004—Network Reconnaissance with Nmap](https://nmap.org/presentations/IT-Defense04/). I start by covering footprinting to find an organizations IP addresses, then demonstrate how close examination of raw packets can help determine IP spoofing by firewalls. Next I discuss techniques for enhancing performance, bypassing firewall rules, and evading intrusion detection systems.

*   [Yahoo Security Conference 2003—Network Reconnaissance with Nmap](https://nmap.org/presentations/Yahoo03/). This is my first talk to introduce [Nmap Version Detection](https://nmap.org/book/vscan.html). It also covers footprinting, performance, and IDS evasion.

*   [Defcon 11 (2003)—Advanced Network Reconnaissance](https://nmap.org/presentations/Defcon11/).

*   [San Francisco OpenBSD Users' Group (SFOBUG) 2003—Nmap](https://nmap.org/presentations/SFOBUG03/). This informal talk used scans of [www.openbsd.org](http://www.openbsd.org/) to demonstrate key features of Nmap as well as a few useful scanning tricks.

*   [CanSecWest 2003—Advanced Network Reconnaissance](https://nmap.org/presentations/CanSecWest03/)

*   [Affiliated Computer Systems (ACS) Client Symposium (2001)—Security Risks of Emerging Technologies: Wireless Networks and Intrusion Detection Systems](https://nmap.org/presentations/ACS01/). This presentation discussed the risks inherent in wireless networks and IDS systems, and how an enterprise can set those up securely to mitigate the risks.

*   [CanSecWest 2001—Stealth Scanning & IDS Evasion Techniques](https://nmap.org/presentations/CanSecWest01/). Demonstrated how Nmap can be used for stealth scanning, then demonstrated advanced IDS evasion techniques. Custom tools were provided for locating Black ICE IDS installations on networks (or the Internet), and then manipulating their reported results.

*   [Open Source Developers' European Meeting 2001—Network Reconnaissance Techniques](https://nmap.org/presentations/OSDEM01/). Introduced Nmap (which was only 3.5 years old) and explain advanced (at the time) techniques for host discovery, port scanning, and network topology detection.

*   [Defcon 7 (1999): Introduction to Scanning](https://nmap.org/presentations/Defcon7/M0dify-Fyodor-Introduction-to-Scanning-Video.m4v). The official (registered) speaker was M0dify, but Fyodor ended up joining him on stage when it became clear that the whole talk was about Nmap.
