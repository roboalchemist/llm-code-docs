---
rfc: 1797
title: "Class A Subnet Experiment"
date: April 1995
category: Experimental
---
7.189.2.39.IN-ADDR.ARPA. PTR Interesting.Alter.Net.

which means that the 189.2.39 branch of the IN-ADDR tree would be
delegated to Alternet for the purposes of this experiment.

To support this, the 39.IN-ADDR.ARPA branch is delegated to the IANA
to be managed at ISI.  The nameserver for this branch is
IN-ADDR.EP.NET (39.17.199.10).  Participants in this experiment
should contact the administrator of this nameserver to have their
portion of the address space further delegated.  The administrator
for this server can be reached at <aexpreg@isi.edu>.

Another aspect of the testing that should be performed is to have
providers interchange addresses to test the portability of subnetted
class A addresses.  It is not intended that this would be the model
for actual use.

For example, if AS 690 and AS 1800 want to try out routing holes
in each others' allocations within their AS, that should be
encouraged.  That is, suppose AS 690 handed some address of their
addresses to AS 1800, and vice-versa.  This type of testing will
be necessary to see if the addresses can be made portable in
larger sub-A allocations.

This is experiment will be of limited duration and these addresses
may be reassigned to other uses when the experiment is over.

This experiment will begin on 1-May-95.

The current date for the termination of this experiment is 1-Dec-95.

# Security Considerations

Security issues are not discussed in this memo.

# Author's Address

Internet Assigned Numbers Authority (IANA)
Information Sciences Institute
University of Southern California
4676 Admiralty Way, Suite 1001
Marina del Rey, CA 90292-6695

Phone: 1-310-822-1511
EMail: iana@isi.edu
