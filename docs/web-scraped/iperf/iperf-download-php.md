# Source: https://iperf.fr/iperf-download.php

Title: Download iPerf3 and original iPerf pre-compiled binaries

URL Source: https://iperf.fr/iperf-download.php

Markdown Content:
iPerf - Download iPerf3 and original iPerf pre-compiled binaries
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

[![Image 2: Windows](https://iperf.fr/images/logo_windows.png)**Windows**](https://iperf.fr/iperf-download.php#windows)
Binaries are available at :

*   [https://files.budman.pw](https://files.budman.pw/)
*   [https://github.com/ar51an/iperf3-win-builds](https://github.com/ar51an/iperf3-win-builds)

[![Image 3: macOS](https://iperf.fr/images/logo_apple.png)**macOS**](https://iperf.fr/iperf-download.php#macos) : 
*   HomeBrew : brew install iperf3
*   MacPorts : sudo port install iperf3

[![Image 4: Android](https://iperf.fr/images/logo_android.png)**Android**](https://iperf.fr/iperf-download.php#android) : 
Building iperf3 for Android : [https://github.com/davidBar-On/android-iperf3/](https://github.com/davidBar-On/android-iperf3/)

[![Image 5: Ubuntu](https://iperf.fr/images/logo_ubuntu.png)**Ubuntu** / Debian / Mint](https://iperf.fr/iperf-download.php#ubuntu)
launch a terminal and type sudo apt-get install iperf3

[![Image 6: Fedora](https://iperf.fr/images/logo_fedora.png)**Fedora** / Red Hat / CentOS / Rocky](https://iperf.fr/iperf-download.php#fedora)
launch a terminal and type yum install iperf3

[![Image 7: FreeBSD](https://iperf.fr/images/logo_freebsd.png)**FreeBSD**](https://iperf.fr/iperf-download.php#freebsd)
launch a terminal and type sudo pkg install benchmarks/iperf3

![Image 8: french](https://iperf.fr/images/logo_fr.png)[French forum for iPerf](https://lafibre.info/iperf/)

* * *

iPerf3 server log script :
--------------------------

![Image 9: iperf3tocsv](https://iperf.fr/images/logo_kgersen.png)[iperf3tocsv.py](https://iperf.fr/download/scripts/iperf3tocsv.py) (2.5 KiB) by [Kirth Gersen](https://github.com/kgersen/iperf3protect)

Log for iPerf3 : display "date,ip,localport,remoteport,duration,protocol,num_streams,cookie,sent,sent_mbps,rcvd,rcvd_mbps,totalsent,totalreceived" 

* * *

How to perform a more recent installation of Iperf than the one included in Ubuntu / Debian / Mint ?
----------------------------------------------------------------------------------------------------

1.   Removing the old version: sudo apt remove iperf3 libiperf0
2.   Install the dependency: sudo apt install libsctp1
3.   Take a recent Ubuntu distribution from [https://launchpad.net/ubuntu/+source/iperf3](https://launchpad.net/ubuntu/+source/iperf3)
4.   Download iperf3_3.xx-1_amd64.deb and libiperf0_3.xx-1_amd64.deb packages (use amd64 version for a standard version of Ubuntu)
5.   Install downloaded packages: sudo dpkg -i libiperf0_3.xx-1_amd64.deb iperf3_3.xx-1_amd64.deb
6.   Remove downloaded packages that are now unnecessary: rm libiperf0_3.xx-1_amd64.deb iperf3_3.xx-1_amd64.deb
