# Source: https://iperf.fr/iperf-servers.php

Title: iPerf - Public iPerf3 servers

URL Source: https://iperf.fr/iperf-servers.php

Markdown Content:
iPerf - Public iPerf3 servers
===============

[![Image 1: iPerf.fr](https://iperf.fr/images/logo_iperf.png)](https://iperf.fr/)
iPerf - The ultimate speed test tool for TCP, UDP and SCTP Test the limits of your network + Internet neutrality test
=====================================================================================================================

*   [Home](https://iperf.fr/)
*   [Download iPerf binaries](https://iperf.fr/iperf-download.php)
*   [Public iPerf3 servers](https://iperf.fr/iperf-servers.php)
*   [iPerf user docs](https://iperf.fr/iperf-doc.php)
*   [French iPerf forum](https://lafibre.info/iperf/)
*   [Contact](https://iperf.fr/contact.php)

### Table of contents :

1.   [Public iPerf3 servers](https://iperf.fr/iperf-servers.php#public-servers)
2.   [Script to host a iPerf3 server](https://iperf.fr/iperf-servers.php#host-iperf3)
3.   [Emulating wide area network delays with Linux](https://iperf.fr/iperf-servers.php#netem)

* * *

Public iPerf3 servers
---------------------

iPerf3 servers will only allow one iPerf connection at a time. Multiple tests at the same time is not supported. If a test is in progress, the following message is displayed: "iperf3: error - the server is busy running a test. try again later"

| [Europe](https://iperf.fr/iperf-servers.php#europe) |
| --- |
| iPerf3 server | Localization | Data center | Hosting | Speed | TCP congestion control | Port | IP version | Contact | Test date |
| **ping.online.net ping6.online.net ping-90ms.online.net ping6-90ms.online.net** | France Île-de-France | [Scaleway Vitry DC3](https://www.google.fr/maps/place/61+Rue+Julian+Grimau,+94400+Vitry-sur-Seine/@48.77479,2.3794436,301m/data=!3m1!1e3!4m2!3m1!1s0x47e673f578c8e219:0x53f9662e2d821ffb) | [![Image 2: online.net](https://iperf.fr/images/logo_scaleway.png)](https://www.scaleway.com/) | 100 Gbit/s | BBR | 5200 TCP/UDP to 5209 TCP/UDP | IPv4 or IPv6 | [mikmak](https://lafibre.info/iperf/online-iperf/msg180514/#msg180514) | OK 03/2025 |
| **iperf3.moji.fr** | France Île-de-France | DC Moji | [![Image 3: Moji](https://iperf.fr/images/logo_moji.webp)](https://moji.fr/) | 100 Gbit/s | BBR | 5200 TCP/UDP to 5240 TCP/UDP | IPv4 and IPv6 | [@nemavdotio](https://twitter.com/nemavdotio) | OK 03/2025 |
| **speedtest.milkywan.fr** | France Île-de-France | CBO Croissy-Beaubourg | [![Image 4: MilkyWan](https://iperf.fr/images/logo_milkywan.webp)](https://milkywan.fr/) | 40 Gbit/s | BBR | 9200 TCP/UDP to 9240 TCP/UDP | IPv4 and IPv6 | [@huguesdelamure](https://x.com/huguesdelamure) | OK 03/2025 |
| **iperf.par2.as49434.net** | France Île-de-France | DC Harmony Hosting | [![Image 5: Harmony Hosting](https://iperf.fr/images/logo_harmony_hosting.png)](https://harmony.hosting/) | 40 Gbit/s | ? | 9200 TCP/UDP to 9240 TCP/UDP | IPv4 and IPv6 | [@g_marsot](https://twitter.com/g_marsot) | OOS 03/2025 |
| **paris.bbr.iperf.bytel.fr paris.cubic.iperf.bytel.fr mrs.bbr.iperf.bytel.fr mrs.cubic.iperf.bytel.fr lyo.bbr.iperf.bytel.fr lyo.cubic.iperf.bytel.fr tls.bbr.iperf.bytel.fr tls.cubic.iperf.bytel.fr str.bbr.iperf.bytel.fr str.cubic.iperf.bytel.fr poi.bbr.iperf.bytel.fr poi.cubic.iperf.bytel.fr ren.bbr.iperf.bytel.fr ren.cubic.iperf.bytel.fr** | France Paris BBR France Paris Cubic France Marseille BBR France Marseille Cubic France Lyon BBR France Lyon Cubic France Toulouse BBR France Toulouse Cubic France Strasbourg BBR France Strasbourg Cubic France Poitiers BBR France Poitiers Cubic France Rennes BBR France Rennes Cubic | Data centers Bouygues Telecom | [![Image 6: Bouygues Telecom](https://iperf.fr/images/logo_bouygues_telecom.png)](https://www.bouyguestelecom.fr/) | 10 Gbit/s 10 Gbit/s 10 Gbit/s 10 Gbit/s 10 Gbit/s 10 Gbit/s 10 Gbit/s 10 Gbit/s 10 Gbit/s 10 Gbit/s 10 Gbit/s 10 Gbit/s 10 Gbit/s 10 Gbit/s | BBR Cubic BBR Cubic BBR Cubic BBR Cubic BBR Cubic BBR Cubic BBR Cubic | 9200 TCP to 9240 TCP | IPv4 and IPv6 | [@lafibre.info](https://bsky.app/profile/lafibre.info) | OK 03/2025 |
| **speedtest.serverius.net** (Port 5002: add **-p 5002**) | Netherlands | Serverius data center | [![Image 7: Serverius datacenters](https://iperf.fr/images/logo_serverius.png)](https://serverius.net/) | 10 Gbit/s | Cubic | 5002 TCP/UDP | IPv4 and IPv6 | [@serveriusbv](https://twitter.com/serveriusbv) | OK 03/2025 |
| **nl.iperf.014.fr** | Netherlands | NextGenWebs data center | [![Image 8: 014.fr](https://iperf.fr/images/logo_014.png)](https://014.fr/) | 1 Gbit/s | Cubic | 10415 TCP/UDP to 10420 TCP/UDP | IPv4 only | [@014_fr](https://twitter.com/014_fr) | OK 03/2025 |
| **ch.iperf.014.fr** | Switzerland Zurich | HostHatch data center | [![Image 9: 014.fr](https://iperf.fr/images/logo_014.png)](https://014.fr/) | 3 Gbit/s | Cubic | 15315 TCP/UDP to 15320 TCP/UDP | IPv4 only | [@014_fr](https://twitter.com/014_fr) | OK 03/2025 |
| **iperf.eenet.ee** | Estonia | [EENet Tartu](https://www.google.fr/maps/place/Tartu,+Estonie/) | [![Image 10: EENet](https://iperf.fr/images/logo_eenet.png)](https://www.eenet.ee/) |  | ? | 5201 TCP/UDP | IPv4 only | [@EENet_HITSA](https://twitter.com/EENet_HITSA) | OOS 03/2025 |
| **iperf.astra.in.ua** | Ukraine Lviv | [Astra Lviv](https://www.google.fr/maps/place/ASTRA:+your+star+Internet/@49.8137147,24.0379979,181m/data=!3m1!1e3!4m5!3m4!1s0x473ae792a53f6883:0xa708ef57c029c32f!8m2!3d49.813673!4d24.0384111?hl=fr) | [![Image 11: Астра](https://iperf.fr/images/logo_astra.png)](https://astra.in.ua/) | 10 Gbit/s | ? | 5201 TCP/UDP to 5206 TCP/UDP | IPv4 and IPv6 | noc@astra.in.ua | OOS 03/2025 |
| **iperf.volia.net** | Ukraine | [Volia Kiev](https://www.google.fr/maps/place/Kikvidze+St,+1%2F2,+Kyiv,+Ukraine/@50.4182095,30.5498797,373m/data=!3m1!1e3!4m2!3m1!1s0x40d4cf6ea4eb9f77:0x6e651c039c8a501a!6m1!1e1?hl=fr) | [![Image 12: ВОЛЯ](https://iperf.fr/images/logo_volia.png)](http://volia.com/) |  | BBR | 5201 TCP/UDP | IPv4 only | [@voliaofficial](https://twitter.com/voliaofficial) | OK 03/2025 |
|  |
| [Africa](https://iperf.fr/iperf-servers.php#africa) |
| iPerf3 server | Localization | Data center | Hosting | Speed | TCP congestion control | Port | IP version | Contact | Test date |
| **iperf.angolacables.co.ao** | Angola Luanda | AngoNAP Luanda | [![Image 13: Angola Cables](https://iperf.fr/images/logo_angola_cables.avif)](https://angolacables.co.ao/) | 10 Gbit/s | Cubic | 9200 TCP/UDP to 9240 TCP/UDP | IPv4 and IPv6 | [contact](mailto:sd.ip@angolacables.co.ao) | OK 03/2025 |
|  |
| [Asia](https://iperf.fr/iperf-servers.php#asia) |
| iPerf3 server | Localization | Data center | Hosting | Speed | TCP congestion control | Port | IP version | Contact | Test date |
| **speedtest.uztelecom.uz** | Uzbekistan Tashkent | [Infosystems](https://www.google.fr/maps/place/Infosystems/@41.3251919,69.3170839,297m/data=!3m1!1e3!4m13!1m7!3m6!1s0x38ae8b0cc379e9c3:0xa5a9323b4aa5cb98!2z0KLQsNGI0LrQtdC90YIsINCj0LfQsdC10LrQuNGB0YLQsNC9!3b1!8m2!3d41.2994958!4d69.2400734!3m4!1s0x38aef51e34ce0557:0xf2b8c867a43a0792!8m2!3d41.3253678!4d69.3173564) | [![Image 14: Uztelecom](https://iperf.fr/images/logo_uztelecom.png)](https://uztelecom.uz/) | 10 Gbit/s | HTCP | 5200 TCP/UDP to 5209 TCP/UDP | IPv4 and IPv6 | [@KhurshidSuyunov](https://twitter.com/KhurshidSuyunov) | OK 03/2025 |
| **iperf.biznetnetworks.com** | Indonesia | [Biznet - Midplaza Cimanggis](https://www.google.fr/maps/place/Biznet+Technovillage/@-6.4353143,106.8969055,251m/data=!3m1!1e3!4m8!1m2!2m1!1sBiznet+Networks+Jl.+Biznet+Technovillage+No.+1+16965+Cimanggis+West+Java,+Indonesia!3m4!1s0x0000000000000000:0xe794f80c0724e861!8m2!3d-6.435587!4d106.8971158) | [![Image 15: Biznet Networks](https://iperf.fr/images/logo_biznetnetworks.png)](http://www.biznetnetworks.com/) | 1 Gbit/s | ? | 5201 TCP to 5203 TCP | IPv4 and IPv6 | [Biznet Networks](http://www.biznetnetworks.com/) | OOS 03/2025 |
|  |
| [Oceania](https://iperf.fr/iperf-servers.php#oceania) |
| iPerf3 server | Localization | Data center | Hosting | Speed | TCP congestion control | Port | IP version | Contact | Test date |
| **speedtest-iperf-akl.vetta.online** | New Zealand Auckland | Vetta Online Auckland | [![Image 16: Vetta Online](https://iperf.fr/images/logo_vetta.png)](https://www.vetta.online/) | 10 Gbit/s | ? | 5200 TCP to 5209 TCP | IPv4 only | [contact](https://www.vetta.online/contact/) | OOS 03/2025 |
|  |
| [Americas](https://iperf.fr/iperf-servers.php#americas) |
| iPerf3 server | Localization | Data center | Hosting | Speed | TCP congestion control | Port | IP version | Contact | Test date |
| **iperf.he.net** | USA California | [Hurricane Fremont 1](https://www.google.fr/maps/place/Hurricane+Electric/@37.489826,-121.9309676,128m/data=!3m1!1e3!4m2!3m1!1s0x808fc644b35fd311:0xee25ef985cd52aef) | [![Image 17: he.net](https://iperf.fr/images/logo_hurricane_electric.png)](https://he.net/) |  | ? | 5201 TCP/UDP | IPv4 and IPv6 | [HE forums](https://forums.he.net/) | busy 03/2025 |

To add / remove a public iPerf3 server, please report them to :

*   Bluesky : [@lafibre.info](https://bsky.app/profile/lafibre.info)
*   Mastodon : [@lafibreinfo](https://mamot.fr/@lafibreinfo)
*   X : [@lafibreinfo](https://x.com/lafibreinfo)
*   LinkedIn : [Vivien GUEANT](https://www.linkedin.com/in/viviengueant/)
*   Forum : [LaFibre.info](https://lafibre.info/iperf/)

* * *

Script to host a iPerf3 server with Linux (Ubuntu / Debian)
-----------------------------------------------------------

iPerf3 not allow multiple tests to a server => it is necessary to start several iPerf processes for not having the message **iperf3: error - the server is busy running a test. try again later**

Systemd script to start 41 iPerf3 server (port 9200 to port 9240). 

**sudo adduser iperf --disabled-login --gecos iperf**

**sudo nano /etc/systemd/system/iperf3-server@.service**

> [Unit] Description=iperf3 server on port %i After=syslog.target network.target [Service] ExecStart=/usr/bin/iperf3 -s -1 -p %i Restart=always RuntimeMaxSec=3600 User=iperf [Install] WantedBy=multi-user.target DefaultInstance=5201

The "Restart = always" allows to restart iperf3 after one hour (RuntimeMaxSec = 3600) to limit the cases of no response or when the iperf3 server has ended abruptly.

**sudo systemctl daemon-reload**

To activate iperf3 when the server starts up: 

**for p in $(seq 9200 9240); do sudo systemctl enable iperf3-server@$p ; done**

> $ for p in $(seq 9200 9240); do sudo systemctl enable iperf3-server@$p ; done Created symlink /etc/systemd/system/multi-user.target.wants/iperf3-server@9200.service → /etc/systemd/system/iperf3-server@.service. Created symlink /etc/systemd/system/multi-user.target.wants/iperf3-server@9201.service → /etc/systemd/system/iperf3-server@.service. Created symlink /etc/systemd/system/multi-user.target.wants/iperf3-server@9202.service → /etc/systemd/system/iperf3-server@.service. Created symlink /etc/systemd/system/multi-user.target.wants/iperf3-server@9203.service → /etc/systemd/system/iperf3-server@.service. Created symlink /etc/systemd/system/multi-user.target.wants/iperf3-server@9204.service → /etc/systemd/system/iperf3-server@.service. Created symlink /etc/systemd/system/multi-user.target.wants/iperf3-server@9205.service → /etc/systemd/system/iperf3-server@.service. Created symlink /etc/systemd/system/multi-user.target.wants/iperf3-server@9206.service → /etc/systemd/system/iperf3-server@.service. Created symlink /etc/systemd/system/multi-user.target.wants/iperf3-server@9207.service → /etc/systemd/system/iperf3-server@.service. Created symlink /etc/systemd/system/multi-user.target.wants/iperf3-server@9208.service → /etc/systemd/system/iperf3-server@.service. Created symlink /etc/systemd/system/multi-user.target.wants/iperf3-server@9209.service → /etc/systemd/system/iperf3-server@.service. Created symlink /etc/systemd/system/multi-user.target.wants/iperf3-server@9210.service → /etc/systemd/system/iperf3-server@.service. Created symlink /etc/systemd/system/multi-user.target.wants/iperf3-server@9211.service → /etc/systemd/system/iperf3-server@.service. ...

**sudo reboot**

* * *

To view the status and logs of iPerf3 :

**sudo systemctl status iperf3-server@***

**sudo journalctl -u iperf3-server@***

* * *

To disable iperf3 when starting the server :

**for p in $(seq 9200 9240); do sudo systemctl disable iperf3-server@$p ; done**

* * *

Emulating wide area network delays with Linux
---------------------------------------------

[NetEm](https://www.linuxfoundation.org/collaborate/workgroups/networking/netem) (already enabled in the Linux kernel) provides Network Emulation functionality for testing protocols by emulating the properties of wide area networks. 

To simulate an additional latency of 80 ms, just type **sudo tc qdisc add dev eth0 root netem delay 80ms**

It just adds a fixed amount of delay to all packets going out of the local Ethernet. 

To stop the additional latency, just type **sudo tc qdisc change dev eth0 root netem delay 0ms**

Lines to add to the file **/etc/rc.local** before **exit 0**, to add 40ms of latency :

> # Add +40ms latency tc qdisc add dev eth0 root netem delay 40ms

Note: If your network interface is not **eth0**, replace **eth0** with the name of your network interface
