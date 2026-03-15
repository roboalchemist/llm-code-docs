# Source: https://iperf.fr/iperf-doc.php

Title: iPerf3 and iPerf2 user documentation

URL Source: https://iperf.fr/iperf-doc.php

Markdown Content:
iPerf - iPerf3 and iPerf2 user documentation
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

1.   [Change between iPerf 2.0, iPerf 3.0 and iPerf 3.1](https://iperf.fr/iperf-doc.php#3change)
2.   [iPerf 3 user documentation](https://iperf.fr/iperf-doc.php#3doc)
3.   [Change between iPerf 2.0.6, iPerf 2.0.7 and iPerf 2.0.8](https://iperf.fr/iperf-doc.php#change)
4.   [iPerf 2 user documentation](https://iperf.fr/iperf-doc.php#doc)

* * *

Change between iPerf 2.0, iPerf 3.0 and iPerf 3.1
-------------------------------------------------

*   **iPerf2 features currently supported by iPerf3 :**
    *   TCP and UDP tests
    *   Set port (-p)
    *   Setting TCP options: No delay, MSS, etc.
    *   Setting UDP bandwidth (-b)
    *   Setting socket buffer size (-w)
    *   Reporting intervals (-i)
    *   Setting the iPerf buffer (-l)
    *   Bind to specific interfaces (-B)
    *   IPv6 tests (-6)
    *   Number of bytes to transmit (-n)
    *   Length of test (-t)
    *   Parallel streams (-P)
    *   Setting DSCP/TOS bit vectors (-S)
    *   Change number output format (-f)

*   **New Features in iPerf 3.0 :**
    *   Dynamic server (client/server parameter exchange) – Most server options from iPerf2 can now be dynamically set by the client
    *   Client/server results exchange
    *   A iPerf3 server accepts a single client simultaneously (multiple clients simultaneously for iPerf2)
    *   iPerf API (libiperf) – Provides an easy way to use, customize and extend iPerf functionality
    *   -R, Reverse test mode – Server sends, client receives
    *   -O, --omit N : omit the first n seconds (to ignore [TCP slowstart](https://en.wikipedia.org/wiki/Slow-start))
    *   -b, --bandwidth n[KM] for TCP (only UDP for IPERF 2): Set target bandwidth to n bits/sec (default 1 Mbit/sec for UDP, unlimited for TCP).
    *   -V, --verbose : more detailed output than before
    *   -J, --json : output in JSON format
    *   -Z, --zerocopy : use a 'zero copy' sendfile() method of sending data. This uses much less CPU.
    *   -T, --title str : prefix every output line with this string
    *   -F, --file name : xmit/recv the specified file
    *   -A, --affinity n/n,m : set CPU affinity (cores are numbered from 0 - Linux and FreeBSD only)
    *   -k, --blockcount #[KMG] : number of blocks (packets) to transmit (instead of -t or -n)
    *   -4, --version4 : only use IPv4
    *   -6, --version6 : only use IPv6
    *   -L, --flowlabel : set IPv6 flow label (Linux only)
    *   -C, --linux-congestion : set congestion control algorithm (Linux and FreeBSD only) (-Z in iPerf2)
    *   -d, --debug : emit debugging output. Primarily (perhaps exclusively) of use to developers.
    *   -s, --server : iPerf2 can handle multiple client requests. iPerf3 will only allow one iperf connection at a time.

*   **New Features in iPerf 3.1 :**
    *   -I, --pidfile file write a file with the process ID, most useful when running as a daemon.
    *   --cport : Specify the client-side port.
    *   --sctp use SCTP rather than TCP (Linux, FreeBSD and Solaris).
    *   --udp-counters-64bit : Support very long-running UDP tests, which could cause a counter to overflow
    *   --logfile file : send output to a log file.

*   **iPerf2 Features Not Supported by iPerf3 :**
    *   Bidirectional testing (-d / -r)
    *   Data transmitted from stdin (-I)
    *   TTL : time-to-live, for multicast (-T)
    *   Exclude C(connection) D(data) M(multicast) S(settings) V(server) reports (-x)
    *   Report as a Comma-Separated Values (-y)
    *   Compatibility mode allows for use with older version of iPerf (-C)

* * *

iPerf 3 user documentation
--------------------------

| GENERAL OPTIONS |
| --- |
| Command line option | Description |
| **-p**, --port _**n**_ | The server port for the server to listen on and the client to connect to. This should be the same in both client and server. Default is 5201. |
| **--cport**_**n**_ | Option to specify the client-side port. (new in iPerf 3.1) |
| **-f**, --format _**[kmKM]**_ | A letter specifying the format to print bandwidth numbers in. Supported formats are 'k' = Kbits/sec 'K' = KBytes/sec 'm' = Mbits/sec 'M' = MBytes/sec The adaptive formats choose between kilo- and mega- as appropriate. |
| **-i**, --interval _**n**_ | Sets the interval time in seconds between periodic bandwidth, jitter, and loss reports. If non-zero, a report is made every _**interval**_ seconds of the bandwidth since the last report. If zero, no periodic reports are printed. Default is zero. |
| **-F**, --file name | **client-side:** read from the file and write to the network, instead of using random data; **server-side:** read from the network and write to the file, instead of throwing the data away. |
| **-A**, --affinity _**n/n,m-F**_ | Set the CPU affinity, if possible (Linux and FreeBSD only). On both the client and server you can set the local affinity by using the n form of this argument (where n is a CPU number). In addition, on the client side you can override the server’s affinity for just that one test, using the n,m form of argument. Note that when using this feature, a process will only be bound to a single CPU (as opposed to a set containing potentialy multiple CPUs). |
| **-B**, --bind _**host**_ | Bind to _**host**_, one of this machine's addresses. For the client this sets the outbound interface. For a server this sets the incoming interface. This is only useful on multihomed hosts, which have multiple network interfaces. |
| **-V**, --verbose | give more detailed output |
| **-J**, --json | output in JSON format |
| **--logfile** file | send output to a log file. (new in iPerf 3.1) |
| **--d**, --debug | emit debugging output. Primarily (perhaps exclusively) of use to developers. |
| **-v**, --version | Show version information and quit. |
| **-h**, --help | Show a help synopsis and quit. |
|  |
| SERVER SPECIFIC OPTIONS |
| Command line option | Description |
| **-s**, --server | Run iPerf in server mode. (This will only allow one iperf connection at a time) |
| **-D**, --daemon | Run the server in background as a daemon. |
| **-I**, --pidfile _**file**_ | write a file with the process ID, most useful when running as a daemon. (new in iPerf 3.1) |
|  |
| CLIENT SPECIFIC OPTIONS |
| Command line option | Description |
| **-c**, --client _**host**_ | Run iPerf in client mode, connecting to an iPerf server running on _**host**_. |
| **--sctp** | Use SCTP rather than TCP (Linux, FreeBSD and Solaris). (new in iPerf 3.1) |
| **-u**, --udp | Use UDP rather than TCP. See also the [-b](https://iperf.fr/iperf-doc.php#3bandwidth) option. |
| **-b**, --bandwidth _**n[KM]**_ | Set target bandwidth to n bits/sec (default 1 Mbit/sec for UDP, unlimited for TCP). If there are multiple streams (-P flag), the bandwidth limit is applied separately to each stream. You can also add a ’/’ and a number to the bandwidth specifier. This is called "burst mode". It will send the given number of packets without pausing, even if that temporarily exceeds the specified bandwidth limit. |
| **-t**, --time _**n**_ | The time in seconds to transmit for. iPerf normally works by repeatedly sending an array of _**len**_ bytes for _**time**_ seconds. Default is 10 seconds. See also the [-l](https://iperf.fr/iperf-doc.php#3len), [-k](https://iperf.fr/iperf-doc.php#3blockcount) and [-n](https://iperf.fr/iperf-doc.php#3num) options. |
| **-n**, --num _**n[KM]**_ | The number of buffers to transmit. Normally, iPerf sends for 10 seconds. The -n option overrides this and sends an array of _**len**_ bytes _**num**_ times, no matter how long that takes. See also the [-l](https://iperf.fr/iperf-doc.php#3len), [-k](https://iperf.fr/iperf-doc.php#3blockcount) and [-t](https://iperf.fr/iperf-doc.php#3time) options. |
| **-k**, --blockcount _**n[KM]**_ | The number of blocks (packets) to transmit. (instead of -t or -n) See also the [-t](https://iperf.fr/iperf-doc.php#3time), [-l](https://iperf.fr/iperf-doc.php#3len) and [-n](https://iperf.fr/iperf-doc.php#3num) options. |
| **-l**, --length _**n[KM]**_ | The length of buffers to read or write. iPerf works by writing an array of _**len**_ bytes a number of times. Default is 128 KB for TCP, 8 KB for UDP. See also the [-n](https://iperf.fr/iperf-doc.php#3num), [-k](https://iperf.fr/iperf-doc.php#3blockcount) and [-t](https://iperf.fr/iperf-doc.php#3time) options. |
| **-P**, --parallel _**n**_ | The number of simultaneous connections to make to the server. Default is 1. |
| **-R**, --reverse | Run in reverse mode (server sends, client receives). |
| **-w**, --window _**n[KM]**_ | Sets the socket buffer sizes to the specified value. For TCP, this sets the TCP window size. (this gets sent to the server and used on that side too) |
| **-M**, --set-mss _**n**_ | Attempt to set the TCP maximum segment size (MSS). The MSS is usually the MTU - 40 bytes for the TCP/IP header. For ethernet, the MSS is 1460 bytes (1500 byte MTU). |
| **-N**, --no-delay | Set the TCP no delay option, disabling Nagle's algorithm. Normally this is only disabled for interactive applications like telnet. |
| **-4**, --version4 | only use IPv4. |
| **-6**, --version4 | only use IPv6. |
| **-S**, --tos _**n**_ | The type-of-service for outgoing packets. (Many routers ignore the TOS field.) You may specify the value in hex with a '0x' prefix, in octal with a '0' prefix, or in decimal. For example, '0x10' hex = '020' octal = '16' decimal. The TOS numbers specified in RFC 1349 are: IPTOS_LOWDELAY minimize delay 0x10 IPTOS_THROUGHPUT maximize throughput 0x08 IPTOS_RELIABILITY maximize reliability 0x04 IPTOS_LOWCOST minimize cost 0x02 |
| **-L**, --flowlabel _**n**_ | Set the IPv6 flow label (currently only supported on Linux). |
| **-Z**, --zerocopy | Use a "zero copy" method of sending data, such as sendfile(2), instead of the usual write(2). This uses much less CPU. |
| **-O**, --omit _**n**_ | Omit the first n seconds of the test, to skip past the TCP [TCP slowstart](https://en.wikipedia.org/wiki/Slow-start) period. |
| **-T, --title _**str**_** | Prefix every output line with this string. |
| **-C**, --linux-congestion _**algo**_ | Set the [congestion control algorithm](https://en.wikipedia.org/wiki/TCP_congestion-avoidance_algorithm) (Linux only for iPerf 3.0, Linux and FreeBSD for iPerf 3.1). |

See also [https://github.com/esnet/iperf](https://github.com/esnet/iperf)

* * *

Change between iPerf 2.0.6, iPerf 2.0.7 and iPerf 2.0.8
-------------------------------------------------------

*   **2.0.6 change set (rjmcmahon@rjmcmahon.com) March 2014 :**
    *   Increase the shared memory for report headers reducing mutex contention. Needed to increase performance. Minor code change that should be platform/os independent

*   **2.0.7 change set (rjmcmahon@rjmcmahon.com) August 2014 :**
    *   Linux only version which supports end/end latency (assumes clocks synched)
    *   Support for smaller report interval (5 milliseconds or greater)
    *   End/end latency with UDP (mean/min/max), display in milliseconds with resolution of microseconds
    *   Socket read timeouts (server only) so iperf reports occur regardless of no received packets
    *   Report timestamps now display millisecond resolution
    *   Local bind supports port value using colon as delimeter (-B 10.10.10.1:60001)
    *   Use linux realtime scheduler and packet level timestamps for improved latency accuracy
    *   Suggest PTP on client and server to synch clocks to microsecond
    *   Suggest a quality reference for the PTP grandmaster such as a GPS disciplined oscillator from companies like Spectracom

*   **2.0.8 change set (as of 12 january 2015) :**
    *   Fix portability, compile and test with Linux, Win10, Win7, WinXP, MacOS and Android
    *   Client now requires -u for UDP (no longer defaults to UDP with -b)
    *   Maintain legacy report formats
    *   Support for -e to get enhanced reports
    *   Support TCP rate limited streams (via the -b) using token bucket
    *   Support packets per second (UDP) via pps as units, (e.g. -b 1000pps)
    *   Display PPS in both client and server reports (UDP)
    *   Support realtime scheduler as a command line option (--realtime or -z)
    *   Improve client tx code path so actual tx offerred rate will converge to the -b value
    *   Improve accuracy of microsecond delay calls (in platform independent manner)
    *   (Use of Kalman filter to predict delay errors and adjust delays per predicted error)
    *   Display target loop time in initial client header (UDP)
    *   Fix final latency report sent from server to client (UDP)
    *   Include standard deviation in latency output
    *   Suppress unrealistic latency output (-/-/-/-)
    *   Support SO_SNDTIMEO on send so socket write won't block beyond -t (TCP)
    *   Use clock_gettime if available (preferred over gettimeofday())
    *   TCP write and error counts (TCP retries and CWND for linux)
    *   TCP read count, TCP read histogram (8 bins)
    *   Server will close the socket after -t seconds of no traffic

See also [https://sourceforge.net/projects/iperf2/](https://sourceforge.net/projects/iperf2/)

* * *

iPerf 2 user documentation
--------------------------

![Image 2: iPerf](https://iperf.fr/images/logo_iperf_command.png)![Image 3](https://iperf.fr/images/white.png)[Tuning a TCP connection](https://iperf.fr/iperf-doc.php#tuningtcp)

[Tuning a UDP connection](https://iperf.fr/iperf-doc.php#tuningudp)

[Running multicast servers and clients](https://iperf.fr/iperf-doc.php#multicast)

[IPv6 Mode](https://iperf.fr/iperf-doc.php#ipv6)

[Representative Streams](https://iperf.fr/iperf-doc.php#repmode)

[Running iPerf as a daemon](https://iperf.fr/iperf-doc.php#daemon)

[Running iPerf as a Windows Service](https://iperf.fr/iperf-doc.php#service)

[Adaptive Window Sizes](https://iperf.fr/iperf-doc.php#adaptive)

[Compiling](https://iperf.fr/iperf-doc.php#compiling)

| GENERAL OPTIONS |
| --- |
| Command line option | Environment variable option | Description |
| **-f**, --format _**[bkmaBKMA]**_ | $IPERF_FORMAT | A letter specifying the format to print bandwidth numbers in. Supported formats are 'b' = bits/sec 'B' = Bytes/sec 'k' = Kbits/sec 'K' = KBytes/sec 'm' = Mbits/sec 'M' = MBytes/sec 'g' = Gbits/sec 'G' = GBytes/sec 'a' = adaptive bits/sec 'A' = adaptive Bytes/sec The adaptive formats choose between kilo- and mega- as appropriate. Fields other than bandwidth always print bytes, but otherwise follow the requested format. Default is 'a'. _**NOTE:**_ here Kilo = 1024, Mega = 1024^2 and Giga = 1024^3 when dealing with bytes. Commonly in networking, Kilo = 1000, Mega = 1000^2, and Giga = 1000^3 so we use this when dealing with bits. If this really bothers you, use -f b and do the math. |
| **-i**, --interval _**#**_ | $IPERF_INTERVAL | Sets the interval time in seconds between periodic bandwidth, jitter, and loss reports. If non-zero, a report is made every _**interval**_ seconds of the bandwidth since the last report. If zero, no periodic reports are printed. Default is zero. |
| **-l**, --len _**#[KM]**_ | $IPERF_LEN | The length of buffers to read or write. iPerf works by writing an array of _**len**_ bytes a number of times. Default is 8 KB for TCP, 1470 bytes for UDP. Note for UDP, this is the datagram size and needs to be lowered when using IPv6 addressing to 1450 or less to avoid fragmentation. See also the [-n](https://iperf.fr/iperf-doc.php#num) and [-t](https://iperf.fr/iperf-doc.php#time) options. |
| **-m**, --print_mss | $IPERF_PRINT_MSS | Print the reported TCP MSS size (via the TCP_MAXSEG option) and the observed read sizes which often correlate with the MSS. The MSS is usually the MTU - 40 bytes for the TCP/IP header. Often a slightly smaller MSS is reported because of extra header space from IP options. The interface type corresponding to the MTU is also printed (ethernet, FDDI, etc.). This option is not implemented on many OSes, but the read sizes may still indicate the MSS. |
| **-p**, --port _**#**_ | $IPERF_PORT | The server port for the server to listen on and the client to connect to. This should be the same in both client and server. Default is 5001, the same as ttcp. |
| **-u**, --udp | $IPERF_UDP | Use UDP rather than TCP. See also the [-b](https://iperf.fr/iperf-doc.php#bandwidth) option. |
| **-w**, --window _**#[KM]**_ | $TCP_WINDOW_SIZE | Sets the socket buffer sizes to the specified value. For TCP, this sets the TCP window size. For UDP it is just the buffer which datagrams are received in, and so limits the largest receivable datagram size. |
| **-B**, --bind _**host**_ | $IPERF_BIND | Bind to _**host**_, one of this machine's addresses. For the client this sets the outbound interface. For a server this sets the incoming interface. This is only useful on multihomed hosts, which have multiple network interfaces. For iPerf in UDP server mode, this is also used to bind and join to a multicast group. Use addresses in the range 224.0.0.0 to 239.255.255.255 for multicast. See also the [-T](https://iperf.fr/iperf-doc.php#ttl) option. |
| **-C**, --compatibility | $IPERF_COMPAT | Compatibility mode allows for use with older version of iPerf. This mode is not required for interoperability but it is highly recommended. In some cases when using representative streaming you could cause a 1.7 server to crash or cause undesired connection attempts. |
| **-M**, --mss _**#[KM}**_ | $IPERF_MSS | Attempt to set the TCP maximum segment size (MSS) via the TCP_MAXSEG option. The MSS is usually the MTU - 40 bytes for the TCP/IP header. For ethernet, the MSS is 1460 bytes (1500 byte MTU). This option is not implemented on many OSes. |
| **-N**, --nodelay | $IPERF_NODELAY | Set the TCP no delay option, disabling Nagle's algorithm. Normally this is only disabled for interactive applications like telnet. |
| **-V** (from v1.6 or higher) | . | Bind to an IPv6 address Server side: $ iperf -s -V Client side: $ iperf -c <Server IPv6 Address> -V Note: On version 1.6.3 and later a specific IPv6 Address does not need to be bound with the [-B](https://iperf.fr/iperf-doc.php#bind) option, previous 1.6 versions do. Also on most OSes using this option will also respond to IPv4 clients using IPv4 mapped addresses. |
| **-h**, --help |  | Print out a summary of commands and quit. |
| **-v**, --version |  | Print version information and quit. Prints 'pthreads' if compiled with POSIX threads, 'win32 threads' if compiled with Microsoft Win32 threads, or 'single threaded' if compiled without threads. |
|  |
| SERVER SPECIFIC OPTIONS |
| Command line option | Environment variable option | Description |
| **-s**, --server | $IPERF_SERVER | Run iPerf in server mode. (iPerf2 can handle multiple client requests) |
| **-D** (from v1.2 or higher) | . | Run the server as a daemon (Unix platforms) On Win32 platforms where services are available, iPerf will start running as a service. |
| **-R** (only for Windows, from v1.2 or higher) | . | Remove the iPerf service (if it's running). |
| **-o** (only for Windows, from v1.2 or higher) | . | Redirect output to given file. |
| **-c**, --client _**host**_ | $IPERF_CLIENT | If iPerf is in server mode, then specifying a host with -c will limit the connections that iPerf will accept to the _**host**_ specified. Does not work well for UDP. |
| **-P**, --parallel _**#**_ | $IPERF_PARALLEL | The number of connections to handle by the server before closing. Default is 0 (which means to accept connections forever). |
|  |
| CLIENT SPECIFIC OPTIONS |
| Command line option | Environment variable option | Description |
| **-b**, --bandwidth _**#[KM]**_ | $IPERF_BANDWIDTH | The UDP bandwidth to send at, in bits/sec. This implies the -u option. Default is 1 Mbit/sec. |
| **-c**, --client _**host**_ | $IPERF_CLIENT | Run iPerf in client mode, connecting to an iPerf server running on _**host**_. |
| **-d**, --dualtest | $IPERF_DUALTEST | Run iPerf in dual testing mode. This will cause the server to connect back to the client on the port specified in the [-L](https://iperf.fr/iperf-doc.php#listenport) option (or defaults to the port the client connected to the server on). This is done immediately therefore running the tests simultaneously. If you want an alternating test try [-r.](https://iperf.fr/iperf-doc.php#tradeoff) |
| **-n**, --num _**#[KM]**_ | $IPERF_NUM | The number of buffers to transmit. Normally, iPerf sends for 10 seconds. The -n option overrides this and sends an array of _**len**_ bytes _**num**_ times, no matter how long that takes. See also the [-l](https://iperf.fr/iperf-doc.php#len) and [-t](https://iperf.fr/iperf-doc.php#time) options. |
| **-r**, --tradeoff | $IPERF_TRADEOFF | Run iPerf in tradeoff testing mode. This will cause the server to connect back to the client on the port specified in the [-L](https://iperf.fr/iperf-doc.php#listenport) option (or defaults to the port the client connected to the server on). This is done following the client connection termination, therefore running the tests alternating. If you want an simultaneous test try [-d.](https://iperf.fr/iperf-doc.php#dualtest) |
| **-t**, --time _**#**_ | $IPERF_TIME | The time in seconds to transmit for. iPerf normally works by repeatedly sending an array of _**len**_ bytes for _**time**_ seconds. Default is 10 seconds. See also the [-l](https://iperf.fr/iperf-doc.php#len) and [-n](https://iperf.fr/iperf-doc.php#num) options. |
| **-L**, --listenport _**#**_ | $IPERF_LISTENPORT | This specifies the port that the server will connect back to the client on. It defaults to the port used to connect to the server from the client. |
| **-P**, --parallel _**#**_ | $IPERF_PARALLEL | The number of simultaneous connections to make to the server. Default is 1. Requires thread support on both the client and server. |
| **-S**, --tos _**#**_ | $IPERF_TOS | The type-of-service for outgoing packets. (Many routers ignore the TOS field.) You may specify the value in hex with a '0x' prefix, in octal with a '0' prefix, or in decimal. For example, '0x10' hex = '020' octal = '16' decimal. The TOS numbers specified in RFC 1349 are: IPTOS_LOWDELAY minimize delay 0x10 IPTOS_THROUGHPUT maximize throughput 0x08 IPTOS_RELIABILITY maximize reliability 0x04 IPTOS_LOWCOST minimize cost 0x02 |
| **-T**, --ttl _**#**_ | $IPERF_TTL | The time-to-live for outgoing multicast packets. This is essentially the number of router hops to go through, and is also used for scoping. Default is 1, link-local. |
| **-F** (from v1.2 or higher) | . | Use a representative stream to measure bandwidth, e.g. :- $ iperf -c <server address> -F <file-name> |
| **-I** (from v1.2 or higher) | . | Same as -F, input from stdin. |

* * *

Tuning a TCP connection
-----------------------

 The primary goal of iPerf is to help in tuning TCP connections over a particular path. The most fundamental tuning issue for TCP is the TCP window size, which controls how much data can be in the network at any one point. If it is too small, the sender will be idle at times and get poor performance. The theoretical value to use for the TCP window size is the _**bandwidth delay product**_, 
> bottleneck bandwidth * round trip time

 In the below modi4/cyclops example, the bottleneck link is a 45 Mbit/sec DS3 link and the round trip time measured with ping is 42 ms. The bandwidth delay product is 
> 45 Mbit/sec * 42 ms 
> 
> = (45e6) * (42e-3) 
> 
> = 1890000 bits
> 
> = 230 KByte

 That is a starting point for figuring the best window size; setting it higher or lower may produce better results. In our example, buffer sizes over 130K did not improve the performance, despite the bandwidth delay product of 230K. 
Note that many OSes and hosts have upper limits on the TCP window size. These may be as low as 64 KB, or as high as several MB. iPerf tries to detect when these occur and give a warning that the actual and requested window sizes are not equal (as below, though that is due to rounding in IRIX). For more information on TCP window sizes, see the [LaFibre.info](https://lafibre.info/tester-son-debit/ping-systeme-exploitation/). Here is an example session, between node1 in Illinois and node2 in North Carolina. These are connected via the vBNS backbone and a 45 Mbit/sec DS3 link. Notice we improve bandwidth performance by a factor of 3 using proper TCP window sizes. Use the adaptive window sizes feature on platforms which allow setting window sizes in the granularity of bytes.

> **node2>** iperf -s
> ------------------------------------------------------------
> Server listening on TCP port 5001
> TCP window size: 60.0 KByte (default)
> ------------------------------------------------------------
> [  4] local <IP Addr node2> port 5001 connected with <IP Addr node1> port 2357
> [ ID] Interval       Transfer     Bandwidth
> [  4]  0.0-10.1 sec   6.5 MBytes   **5.2 Mbits/sec node1>** iperf -c node2
> ------------------------------------------------------------
> Client connecting to node1, TCP port 5001
> TCP window size: 59.9 KByte (default)
> ------------------------------------------------------------
> [  3] local <IP Addr node1> port 2357 connected with <IP Addr node2> port 5001
> [ ID] Interval       Transfer     Bandwidth
> [  3]  0.0-10.0 sec   6.5 MBytes   5.2 Mbits/sec
> 
> * * *
> 
> **node2>** iperf -s -w 130k
> ------------------------------------------------------------
> Server listening on TCP port 5001
> TCP window size:  130 KByte
> ------------------------------------------------------------
> [  4] local <IP Addr node 2> port 5001 connected with <IP Addr node 1> port 2530
> [ ID] Interval       Transfer     Bandwidth
> [  4]  0.0-10.1 sec  19.7 MBytes  **15.7 Mbits/sec node1>** iperf -c node2 -w 130k
> ------------------------------------------------------------
> Client connecting to node2, TCP port 5001
> TCP window size:  129 KByte (WARNING: requested  130 KByte)
> ------------------------------------------------------------
> [  3] local <IP Addr node1> port 2530 connected with <IP Addr node2> port 5001
> [ ID] Interval       Transfer     Bandwidth
> [  3]  0.0-10.0 sec  19.7 MBytes  15.8 Mbits/sec

 Another test to do is run parallel TCP streams. If the total aggregate bandwidth is more than what an individual stream gets, something is wrong. Either the TCP window size is too small, or the OS's TCP implementation has bugs, or the network itself has deficiencies. See above for TCP window sizes; otherwise diagnosing which is somewhat difficult. If iPerf is compiled with pthreads, a single client and server can test this, otherwise setup multiple clients and servers on different ports. Here's an example where a single stream gets 16.5 Mbit/sec, but two parallel streams together get 16.7 + 9.4 = 26.1 Mbit/sec, even when using large TCP window sizes: 
> **node2>** iperf -s -w 300k
> ------------------------------------------------------------
> Server listening on TCP port 5001
> TCP window size:  300 KByte
> ------------------------------------------------------------
> [  4] local <IP Addr node2> port 5001 connected with <IP Addr node1> port 6902
> [ ID] Interval       Transfer     Bandwidth
> [  4]  0.0-10.2 sec  20.9 MBytes  **16.5 Mbits/sec**[  4] local <IP Addr node2> port 5001 connected with <IP Addr node1> port 6911
> [  5] local <IP Addr node2> port 5001 connected with <IP Addr node2> port 6912
> [ ID] Interval       Transfer     Bandwidth
> [  5]  0.0-10.1 sec  21.0 MBytes  **16.7 Mbits/sec**[  4]  0.0-10.3 sec  12.0 MBytes  **9.4 Mbits/sec node1>** ./iperf -c node2 -w 300k
> ------------------------------------------------------------
> Client connecting to node2, TCP port 5001
> TCP window size:  299 KByte (WARNING: requested  300 KByte)
> ------------------------------------------------------------
> [  3] local <IP Addr node2> port 6902 connected with <IP Addr node1> port 5001
> [ ID] Interval       Transfer     Bandwidth
> [  3]  0.0-10.2 sec  20.9 MBytes  16.4 Mbits/sec
> 
> **node1>** iperf -c node2 -w 300k -P 2
> ------------------------------------------------------------
> Client connecting to node2, TCP port 5001
> TCP window size:  299 KByte (WARNING: requested  300 KByte)
> ------------------------------------------------------------
> [  4] local <IP Addr node2> port 6912 connected with <IP Addr node1> port 5001
> [  3] local <IP Addr node2> port 6911 connected with <IP Addr node1> port 5001
> [ ID] Interval       Transfer     Bandwidth
> [  4]  0.0-10.1 sec  21.0 MBytes  16.6 Mbits/sec
> [  3]  0.0-10.2 sec  12.0 MBytes   9.4 Mbits/sec

 A secondary tuning issue for TCP is the maximum transmission unit (MTU). To be most effective, both hosts should support Path MTU Discovery. Hosts without Path MTU Discovery often use 536 as the MSS, which wastes bandwidth and processing time. Use the -m option to display what MSS is being used, and see if this matches what you expect. Often it is around 1460 bytes for ethernet. 
> **node3>** iperf -s -m
> ------------------------------------------------------------
> Server listening on TCP port 5001
> TCP window size: 60.0 KByte (default)
> ------------------------------------------------------------
> [  4] local <IP Addr node3> port 5001 connected with <IP Addr node4> port 1096
> [ ID] Interval       Transfer     Bandwidth
> [  4]  0.0- 2.0 sec   1.8 MBytes   6.9 Mbits/sec
> [  4] **MSS size 1448 bytes (MTU 1500 bytes, ethernet)**[  4] Read lengths occurring in more than 5% of reads:
> [  4]   952 bytes read   219 times (16.2%)
> [  4]  1448 bytes read  1128 times (83.6%)

 Here is a host that doesn't support Path MTU Discovery. It will only send and receive small 576 byte packets. 
> **node4>** iperf -s -m
> ------------------------------------------------------------
> Server listening on TCP port 5001
> TCP window size: 32.0 KByte (default)
> ------------------------------------------------------------
> [  4] local <IP Addr node4> port 5001 connected with <IP Addr node3> port 13914
> [ ID] Interval       Transfer     Bandwidth
> [  4]  0.0- 2.3 sec   632 KBytes   2.1 Mbits/sec
> **WARNING: Path MTU Discovery may not be enabled.**[  4] **MSS size 536 bytes (MTU 576 bytes, minimum)**[  4] Read lengths occurring in more than 5% of reads:
> [  4]   536 bytes read   308 times (58.4%)
> [  4]  1072 bytes read    91 times (17.3%)
> [  4]  1608 bytes read    29 times (5.5%)

 iPerf supports other tuning options, which were added for exceptional network situations like HIPPI-to-HIPPI over ATM. 

* * *

Tuning a UDP connection
-----------------------

iPerf creates a constant bit rate UDP stream. This is a very artificial stream, similar to voice communication but not much else.

You will want to adjust the datagram size (-l) to the size your application uses.

The server detects UDP datagram loss by ID numbers in the datagrams. Usually a UDP datagram becomes several IP packets. Losing a single IP packet will lose the entire datagram. To measure packet loss instead of datagram loss, make the datagrams small enough to fit into a single packet, using the -l option. The default size of 1470 bytes works for ethernet. Out-of-order packets are also detected. (Out-of-order packets cause some ambiguity in the lost packet count; iPerf assumes they are not duplicate packets, so they are excluded from the lost packet count.) Since TCP does not report loss to the user, I find UDP tests helpful to see packet loss along a path.

 Jitter calculations are continuously computed by the server, as specified by RTP in RFC 1889. The client records a 64 bit second/microsecond timestamp in the packet. The server computes the relative transit time as (server's receive time - client's send time). The client's and server's clocks do not need to be synchronized; any difference is subtracted out in the jitter calculation. Jitter is the smoothed mean of differences between consecutive transit times. 
> **node2>** iperf -s -u -i 1
> ------------------------------------------------------------
> Server listening on UDP port 5001
> Receiving 1470 byte datagrams
> UDP buffer size: 60.0 KByte (default)
> ------------------------------------------------------------
> [  4] local <IP Addr node2> port 5001 connected with <IP Addr node1> port 9726
> [ ID] Interval       Transfer     Bandwidth       Jitter   Lost/Total Datagrams
> [  4]  0.0- 1.0 sec   1.3 MBytes  10.0 Mbits/sec  0.209 ms    1/  894 (0.11%)
> [  4]  1.0- 2.0 sec   1.3 MBytes  10.0 Mbits/sec  0.221 ms    0/  892 (0%)
> [  4]  2.0- 3.0 sec   1.3 MBytes  10.0 Mbits/sec  0.277 ms    0/  892 (0%)
> [  4]  3.0- 4.0 sec   1.3 MBytes  10.0 Mbits/sec  0.359 ms    0/  893 (0%)
> [  4]  4.0- 5.0 sec   1.3 MBytes  10.0 Mbits/sec  0.251 ms    0/  892 (0%)
> [  4]  5.0- 6.0 sec   1.3 MBytes  10.0 Mbits/sec  0.215 ms    0/  892 (0%)
> [  4]  6.0- 7.0 sec   1.3 MBytes  10.0 Mbits/sec  0.325 ms    0/  892 (0%)
> [  4]  7.0- 8.0 sec   1.3 MBytes  10.0 Mbits/sec  0.254 ms    0/  892 (0%)
> [  4]  8.0- 9.0 sec   1.3 MBytes  10.0 Mbits/sec  0.282 ms    0/  892 (0%)
> [  4]  0.0-10.0 sec  12.5 MBytes  10.0 Mbits/sec  0.243 ms    1/ 8922 (0.011%)
> 
> **node1>** iperf -c node2 -u -b 10m
> ------------------------------------------------------------
> Client connecting to node2, UDP port 5001
> Sending 1470 byte datagrams
> UDP buffer size: 60.0 KByte (default)
> ------------------------------------------------------------
> [  3] local <IP Addr node1> port 9726 connected with <IP Addr node2> port 5001
> [ ID] Interval       Transfer     Bandwidth
> [  3]  0.0-10.0 sec  12.5 MBytes  10.0 Mbits/sec
> [  3] Sent 8922 datagrams

 Notice the higher jitter due to datagram reassembly when using larger 32 KB datagrams, each split into 23 packets of 1500 bytes. The higher datagram loss seen here may be due to the burstiness of the traffic, which is 23 back-to-back packets and then a long pause, rather than evenly spaced individual packets. 
> **node2>** iperf -s -u -l 32k -w 128k -i 1
> ------------------------------------------------------------
> Server listening on UDP port 5001
> Receiving 32768 byte datagrams
> UDP buffer size:  128 KByte
> ------------------------------------------------------------
> [  3] local <IP Addr node2> port 5001 connected with <IP Addr node1> port 11303
> [ ID] Interval       Transfer     Bandwidth       Jitter   Lost/Total Datagrams
> [  3]  0.0- 1.0 sec   1.3 MBytes  10.0 Mbits/sec  0.430 ms    0/   41 (0%)
> [  3]  1.0- 2.0 sec   1.1 MBytes   8.5 Mbits/sec  5.996 ms    6/   40 (15%)
> [  3]  2.0- 3.0 sec   1.2 MBytes   9.7 Mbits/sec  0.796 ms    1/   40 (2.5%)
> [  3]  3.0- 4.0 sec   1.2 MBytes  10.0 Mbits/sec  0.403 ms    0/   40 (0%)
> [  3]  4.0- 5.0 sec   1.2 MBytes  10.0 Mbits/sec  0.448 ms    0/   40 (0%)
> [  3]  5.0- 6.0 sec   1.2 MBytes  10.0 Mbits/sec  0.464 ms    0/   40 (0%)
> [  3]  6.0- 7.0 sec   1.2 MBytes  10.0 Mbits/sec  0.442 ms    0/   40 (0%)
> [  3]  7.0- 8.0 sec   1.2 MBytes  10.0 Mbits/sec  0.342 ms    0/   40 (0%)
> [  3]  8.0- 9.0 sec   1.2 MBytes  10.0 Mbits/sec  0.431 ms    0/   40 (0%)
> [  3]  9.0-10.0 sec   1.2 MBytes  10.0 Mbits/sec  0.407 ms    0/   40 (0%)
> [  3]  0.0-10.0 sec  12.3 MBytes   9.8 Mbits/sec  0.407 ms    7/  401 (1.7%)
> 
> **node1>** iperf -c node2 -b 10m -l 32k -w 128k
> ------------------------------------------------------------
> Client connecting to node2, UDP port 5001
> Sending 32768 byte datagrams
> UDP buffer size:  128 KByte
> ------------------------------------------------------------
> [  3] local <IP Addr node2> port 11303 connected with <IP Addr node1> port 5001
> [ ID] Interval       Transfer     Bandwidth
> [  3]  0.0-10.0 sec  12.5 MBytes  10.0 Mbits/sec
> [  3] Sent 401 datagrams

* * *

Multicast
---------

To test multicast, run several servers with the bind option (-B, --bind) set to the multicast group address. Run the client, connecting to the multicast group address and setting the TTL (-T, --ttl) as needed. Unlike normal TCP and UDP tests, multicast servers may be started after the client. In that case, datagrams sent before the server started show up as losses in the first periodic report (61 datagrams on arno below).

> **node5>** iperf -c 224.0.67.67 -u --ttl 5 -t 5
> ------------------------------------------------------------
> Client connecting to 224.0.67.67, UDP port 5001
> Sending 1470 byte datagrams
> Setting multicast TTL to 5
> UDP buffer size: 32.0 KByte (default)
> ------------------------------------------------------------
> [  3] local <IP Addr node5> port 1025 connected with 224.0.67.67 port 5001
> [ ID] Interval       Transfer     Bandwidth
> [  3]  0.0- 5.0 sec   642 KBytes   1.0 Mbits/sec
> [  3] Sent 447 datagrams
> 
> **node5>** iperf -s -u -B 224.0.67.67 -i 1
> ------------------------------------------------------------
> Server listening on UDP port 5001
> Binding to local address 224.0.67.67
> Joining multicast group  224.0.67.67
> Receiving 1470 byte datagrams
> UDP buffer size: 32.0 KByte (default)
> ------------------------------------------------------------
> [  3] local 224.0.67.67 port 5001 connected with <IP Addr node5> port 1025
> [ ID] Interval       Transfer     Bandwidth       Jitter   Lost/Total Datagrams
> [  3]  0.0- 1.0 sec   131 KBytes   1.0 Mbits/sec  0.007 ms    0/   91 (0%)
> [  3]  1.0- 2.0 sec   128 KBytes   1.0 Mbits/sec  0.008 ms    0/   89 (0%)
> [  3]  2.0- 3.0 sec   128 KBytes   1.0 Mbits/sec  0.010 ms    0/   89 (0%)
> [  3]  3.0- 4.0 sec   128 KBytes   1.0 Mbits/sec  0.013 ms    0/   89 (0%)
> [  3]  4.0- 5.0 sec   128 KBytes   1.0 Mbits/sec  0.008 ms    0/   89 (0%)
> [  3]  0.0- 5.0 sec   642 KBytes   1.0 Mbits/sec  0.008 ms    0/  447 (0%)
> 
> **node6>** iperf -s -u -B 224.0.67.67 -i 1
> ------------------------------------------------------------
> Server listening on UDP port 5001
> Binding to local address 224.0.67.67
> Joining multicast group  224.0.67.67
> Receiving 1470 byte datagrams
> UDP buffer size: 60.0 KByte (default)
> ------------------------------------------------------------
> [  3] local 224.0.67.67 port 5001 connected with <IP Addr node5> port 1025
> [ ID] Interval       Transfer     Bandwidth       Jitter   Lost/Total Datagrams
> [  3]  0.0- 1.0 sec   129 KBytes   1.0 Mbits/sec  0.778 ms   61/  151 (40%)
> [  3]  1.0- 2.0 sec   128 KBytes   1.0 Mbits/sec  0.236 ms    0/   89 (0%)
> [  3]  2.0- 3.0 sec   128 KBytes   1.0 Mbits/sec  0.264 ms    0/   89 (0%)
> [  3]  3.0- 4.0 sec   128 KBytes   1.0 Mbits/sec  0.248 ms    0/   89 (0%)
> [  3]  0.0- 4.3 sec   554 KBytes   1.0 Mbits/sec  0.298 ms   61/  447 (14%)

Start multiple clients or servers as explained above, sending data to the same multicast server. (If you have multiple servers listening on the multicast address, each of the servers will be getting the data)

* * *

IPv6 Mode
---------

Get the IPv6 address of the node using the 'ifconfig' command.

 Use the -V option to indicate that you are using an IPv6 address Please note that we need to explicitly bind the server address also. 
Server side:

$ iperf -s -V

Client side:

$ iperf -c <Server IPv6 Address> -V>

Note: iPerf version 1.6.2 and eariler require a IPv6 address to be explicitly bound with the [-B](https://iperf.fr/iperf-doc.php#bind) option for the server.

* * *

Using Representative Streams to measure bandwidth
-------------------------------------------------

Use the -F or -I option. If you want to test how your network performs with compressed / uncompressed streams, just create representative streams and use the -F option to test it. This is usually due to the link layer compressing data. 
The -F option is for file input.

The -I option is for input from stdin.

E.g. 

Client: $ iperf -c <server address> -F <file-name>

Client: $ iperf -c <server address> -I

* * *

Running the server as a daemon
------------------------------

Use the -D command line option to run the server as a daemon. Redirect the output to a file.

E.g. iperf -s -D > iperflog. This will have the iPerf Server running as a daemon and the server messages will be logged in the file iperfLog.

* * *

Using iPerf as a Service under Win32
------------------------------------

There are three options for Win32: -o outputfilename output the messages into the specified file-s -D install iPerf as a service and run it-s -R uninstall the iPerf service 
Examples:

iperf -s -D -o iperflog.txt will install the iPerf service and run it. Messages will be reported into "%windir%\system32\iperflog.txt"iperf -s -R will uninstall the iPerf service if it is installed.
Note: If you stop want to restart the iPerf service after having killed it with the Microsoft Management Console or the Windows Task Manager, make sure to use the proper OPTION in the service properties dialog.

* * *

Adaptive window sizes (under development)
-----------------------------------------

Use the -W option on the client to run the client with the adaptive window size. Ensure that the server window size is fairly big for this option.

 E.g.. If the server TCP window size is 8KB, it does not help having a client TCP window size of 256KB.

 256KB Server TCP Window Size should suffice for most high bandwidth networks. 
Client changes the TCP window size using a binary exponential algorithm. This means that you may notice that TCP window size suggested may vary according to the traffic in the network, iPerf will suggest the best window size for the current network scenario.

* * *

Compiling
---------

Once you have the distribution, on UNIX, unpack it using gzip and tar. That will create a new directory 'iperf-<version#>' with the source files and documentation.

iPerf compiles cleanly on many systems including Linux, SGI IRIX, HP-UX, Solaris, AIX, and Cray UNICOS. Use '**make**' to configure for your OS and compile the source code.

> gunzip -c iperf-<version>.tar.gz | tar -xvf -
> cd iperf-<version>
> ./configure
> make

To install iPerf, use '**make install**', which will ask you where to install it. To recompile, the easiest way is to start over. Do '**make distclean**' then '**./configure; make**'. See the Makefile for more options.
