# Source: https://iperf.fr/contact.php

Title: iPerf - Contact - Bug Reports

URL Source: https://iperf.fr/contact.php

Markdown Content:
[![Image 1: iPerf.fr](https://iperf.fr/images/logo_iperf.png)](https://iperf.fr/)
iPerf - The ultimate speed test tool for TCP, UDP and SCTP Test the limits of your network + Internet neutrality test
---------------------------------------------------------------------------------------------------------------------

Mailing list
------------

To post a message to all the list members, you need to [subscribe to Iperf-users](https://lists.sourceforge.net/lists/listinfo/iperf-users/).

To see the collection of prior postings to the list, visit the [Iperf-users Archives](https://sourceforge.net/p/iperf/mailman/iperf-users/).

* * *

Bug Report for iPerf3
---------------------

Before submitting a bug report, try checking out the latest version of the code, and confirm that it’s not already fixed. Then submit to the iPerf3 issue tracker on GitHub: [https://github.com/esnet/iperf/issues](https://github.com/esnet/iperf/issues)

### Known Issues

The following problems are notable known issues, which are probably of interest to a large fraction of users or have high impact for some users, and for which issues have already been filed in the issue tracker. These issues are either open (indicating no solution currently exists) or closed with the notation that no further attempts to solve the problem are currently being made:

*   UDP performance: Some problems have been noticed with iperf3 on the ESnet 100G testbed at high UDP rates (above 10Gbps). The symptom is that on any particular run of iperf3 the receiver reports a loss rate of about 20%, regardless of the ``-b`` option used on the client side. This problem appears not to be iperf3-specific, and may be due to the placement of the iperf3 process on a CPU and its relation to the inbound NIC. In some cases this problem can be mitigated by an appropriate use of the CPU affinity (``-A``) option. (Issue #55)
*   Interval reports on high-loss networks: The way iperf3 is currently implemented, the sender write command will block until the entire block has been written. This means that it might take several seconds to send a full block if the network has high loss, and the interval reports will have widely varying interval times. A solution is being discussed, but in the meantime a work around is to try using a small block size, for example ``-l 4K``. (Issue #125, a fix will be released in iperf 3.1)
*   The ``-Z`` flag sometimes causes the iperf3 client to hang on OSX. (Issue #129)
*   When specifying the TCP buffer size using the ``-w`` flag on Linux, the Linux kernel automatically doubles the value passed in to compensate for overheads. (This can be observed by using iperf3's ``--debug`` flag.) However, CWND does not actually ramp up to the doubled value, but only to about 75% of the doubled value. Some part of this behavior is documented in the tcp(7) manual page. (Issue #145)

* * *

Bug Report for iPerf2
---------------------

The best way to get help with iPerf2 is by using its forum [https://sourceforge.net/p/iperf2/discussion/](https://sourceforge.net/p/iperf2/discussion/)

* * *

Update site iperf.fr
--------------------

To update this site, please report them to [vivien16@gueant.org](mailto:vivien16@gueant.org) and we will try to fix them quickly.

* * *

Code Authors
------------

The main authors of iPerf3 are (in alphabetical order): Jon Dugan, Seth Elliott, Bruce A. Mah, Jeff Poskanzer, Kaustubh Prabhu. Additional code contributions have come from (also in alphabetical order): Mark Ashley, Aaron Brown, Aeneas Jaißle, Susant Sahani, Bruce Simpson, Brian Tierney.

iPerf3 contains some original code from iPerf2. The authors of iPerf2 are (in alphabetical order): Jon Dugan, John Estabrook, Jim Ferbuson, Andrew Gallatin, Mark Gates, Kevin Gibbs, Stephen Hemminger, Nathan Jones, Feng Qin, Gerrit Renker, Ajay Tirumala, Alex Warshavsky.

Acknowledgements for iPerf1: Thanks to Mark Gates (NLANR), Alex Warshavsky (NLANR) and Justin Pietsch (University of Washington) who were responsible for the 1.1.x releases of Iperf. For iPerf 1.7, we would like to thank Bill Cerveny (Internet2), Micheal Lambert (PSC), Dale Finkelson (UNL) and Matthew Zekauskas (Internet2) for help in getting access to IPv6 networks / machines. Special thanks to Matthew Zekauskas (Internet2) for helping out in the FreeBSD implementation. Also, thanks to Kraemer Oliver (Sony) for providing an independent implementation of IPv6 version of Iperf, which provided a useful comparison for testing our features.

Thanks to [ESnet](https://www.es.net/) for re-rolling iperf from the ground up. iPerf3 is a killer piece of software.

Thanks to [![Image 2: Ikoula](https://iperf.fr/images/logo_ikoula.png)](https://www.ikoula.com/) for hosting iPerf.fr.
