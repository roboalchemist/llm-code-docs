---
rfc: 1032
title: "DOMAIN ADMINISTRATORS GUIDE"
date: November 1987
---
1. Send electronic mail to HOSTMASTER@SRI-NIC.ARPA

2. Call the toll-free NIC hotline at (800) 235-3155

3. Use FTP to get background RFCs and other files maintained
online at the NIC.  Some pertinent RFCs are listed below in
the REFERENCES section of this memo.

# REFERENCES

The references listed here provide important background information
on the domain-naming system.  Path names of the online files
available via anonymous FTP from the SRI-NIC.ARPA host are noted in
brackets.

1. Defense Communications Agency DDN Defense Communications
System, DDN Management Bulletin No. 22, Domain Names
Transition, March 1984.

```
         [ DDN-NEWS:DDN-MGT-BULLETIN-22.TXT ]

      2. Defense Communications Agency DDN Defense Communications
```

System, DDN Management Bulletin No. 32, Phase I of the Domain
Name Implementation, January 1987.

```
         [ DDN-NEWS:DDN-MGT-BULLETIN-32.TXT ]

      3. Harrenstien, K., M. Stahl, and E. Feinler, "Hostname
```

Server", RFC-953, DDN Network Information Center, SRI
International, October 1985.  [ RFC:RFC953.TXT ]

4. Harrenstien, K., M. Stahl, and E. Feinler, "Official DoD
Internet Host Table Specification", RFC-952, DDN Network
Information Center, SRI International, October 1985.

```
         [ RFC:RFC952.TXT ]

      5. ISO, "Codes for the Representation of Names of Countries",
         ISO-3166, International Standards Organization, May 1981.
         [ Not online ]

      6. Lazear, W.D., "MILNET Name Domain Transition", RFC-1031,
```

Mitre Corporation, October 1987.  [ RDC:RFC1031.TXT ]

7. Lottor, M.K., "Domain Administrators Operations Guide",
RFC-1033, DDN Network Information Center, SRI International,
July 1987.  [ RFC:RFC1033.TXT ]

8. Mockapetris, P., "Domain Names - Concepts and Facilities",
RFC-1034, USC Information Sciences Institute, October 1987.

```
         [ RFC:RFC1034.TXT ]

      9. Mockapetris, P., "Domain Names - Implementation and
```

Specification", RFC-1035, USC Information Sciences Institute,
October 1987.  [ RFC:RFC1035.TXT ]

10. Mockapetris, P., "The Domain Name System", Proceedings of the
IFIP 6.5 Working Conference on Computer Message Services,
Nottingham, England, May 1984.  Also as ISI/RS-84-133, June

1984.  [ Not online ]

11. Mockapetris, P., J. Postel, and P. Kirton, "Name Server
Design for Distributed Systems", Proceedings of the Seventh
International Conference on Computer Communication, October
30 to November 3 1984, Sidney, Australia.  Also as
ISI/RS-84-132, June 1984.  [ Not online ]

12. Partridge, C., "Mail Routing and the Domain System", RFC-974,
CSNET-CIC, BBN Laboratories, January 1986.

```
         [ RFC:RFC974.TXT ]

     13. Postel, J., "The Domain Names Plan and Schedule", RFC-881,
         USC Information Sciences Institute, November 1983.
         [ RFC:RFC881.TXT ]

     14. Reynolds, J., and Postel, J., "Assigned Numbers", RFC-1010
         USC Information Sciences Institute, May 1986.
         [ RFC:RFC1010.TXT ]

     15. Romano, S., and Stahl, M., "Internet Numbers", RFC-1020,
         SRI, November 1987.
         [ RFC:RFC1020.TXT ]

```

The following questionnaire may be FTPed from SRI-NIC.ARPA as
NETINFO:DOMAIN-TEMPLATE.TXT.

---------------------------------------------------------------------

To establish a domain, the following information must be sent to the
NIC Domain Registrar (HOSTMASTER@SRI-NIC.ARPA):

NOTE: The key people must have electronic mailboxes and NIC
"handles," unique NIC database identifiers.  If you have access to
"WHOIS", please check to see if you are registered and if so, make
sure the information is current.  Include only your handle and any
changes (if any) that need to be made in your entry.  If you do not
have access to "WHOIS", please provide all the information indicated
and a NIC handle will be assigned.

(1)  The name of the top-level domain to join.

For example:  COM

(2) The NIC handle of the administrative head of the organization.
Alternately, the person's name, title, mailing address, phone number,
organization, and network mailbox.  This is the contact point for
administrative and policy questions about the domain.  In the case of
a research project, this should be the principal investigator.

For example:

Administrator

Organization  The NetWorthy Corporation
Name          Penelope Q. Sassafrass
Title         President
Mail Address  The NetWorthy Corporation

# 4676. Andrews Way, Suite 100

Santa Clara, CA 94302-1212
Phone Number  (415) 123-4567
Net Mailbox   Sassafrass@ECHO.TNC.COM
NIC Handle    PQS

(3)  The NIC handle of the technical contact for the domain.
Alternately, the person's name, title, mailing address, phone number,
organization, and network mailbox.  This is the contact point for
problems concerning the domain or zone, as well as for updating
information about the domain or zone.

For example:

Technical and Zone Contact

Organization  The NetWorthy Corporation
Name          Ansel A. Aardvark
Title         Executive Director
Mail Address  The NetWorthy Corporation

# 4676. Andrews Way, Suite 100

Santa Clara, CA. 94302-1212
Phone Number  (415) 123-6789
Net Mailbox   Aardvark@ECHO.TNC.COM
NIC Handle    AAA2

(4)  The name of the domain (up to 12 characters).  This is the name
that will be used in tables and lists associating the domain with the
domain server addresses.  [While, from a technical standpoint, domain
names can be quite long (programmers beware), shorter names are
easier for people to cope with.]

For example:  TNC

(5)  A description of the servers that provide the domain service for
translating names to addresses for hosts in this domain, and the date
they will be operational.

A good way to answer this question is to say "Our server is
supplied by person or company X and does whatever their standard
issue server does."

For example:  Our server is a copy of the one operated by
the NIC; it will be installed and made operational on
1 November 1987.

(6) Domains must provide at least two independent servers for the
domain.  Establishing the servers in physically separate locations
and on different PSNs is strongly recommended.  A description of the
server machine and its backup, including

(a) Hardware and software (using keywords from the Assigned
Numbers RFC).

(b) Host domain name and network addresses (which host on which
network for each connected network).

(c) Any domain-style nicknames (please limit your domain-style
nickname request to one)

For example:

- Hardware and software

VAX-11/750  and  UNIX,    or
IBM-PC      and  MS-DOS,  or
DEC-1090    and  TOPS-20

- Host domain names and network addresses

BAR.FOO.COM 10.9.0.193 on ARPANET

- Domain-style nickname

BR.FOO.COM (same as BAR.FOO.COM 10.9.0.13 on ARPANET)

(7)  Planned mapping of names of any other network hosts, other than
the server machines, into the new domain's naming space.

For example:

BAR-FOO2.ARPA (10.8.0.193) -> FOO2.BAR.COM
BAR-FOO3.ARPA (10.7.0.193) -> FOO3.BAR.COM
BAR-FOO4.ARPA (10.6.0.193) -> FOO4.BAR.COM

(8)  An estimate of the number of hosts that will be in the domain.

(a) Initially
(b) Within one year
(c) Two years
(d) Five years.

For example:

(a) Initially  =   50
(b) One year   =  100
(c) Two years  =  200
(d) Five years =  500

(9)  The date you expect the fully qualified domain name to become
the official host name in HOSTS.TXT.

Please note: If changing to a fully qualified domain name (e.g.,
FOO.BAR.COM) causes a change in the official host name of an
ARPANET or MILNET host, DCA approval must be obtained beforehand.
Allow 10 working days for your requested changes to be processed.

ARPANET sites should contact ARPANETMGR@DDN1.ARPA.  MILNET sites
should contact HOSTMASTER@SRI-NIC.ARPA, 800-235-3155, for
further instructions.

(10) Please describe your organization briefly.

For example: The NetWorthy Corporation is a consulting
organization of people working with UNIX and the C language in an
electronic networking environment.  It sponsors two technical
conferences annually and distributes a bimonthly newsletter.

---------------------------------------------------------------------

This example of a completed application corresponds to the examples
found in the companion document RFC-1033, "Domain Administrators
Operations Guide."

(1)  The name of the top-level domain to join.

COM

(2)  The NIC handle of the administrative contact person.

NIC Handle    JAKE

(3)  The NIC handle of the domain's technical and zone
contact person.

NIC Handle    DLE6

(4)  The name of the domain.

SRI

(5)  A description of the servers.

Our server is the TOPS20 server JEEVES supplied by ISI; it
will be installed and made operational on 1 July 1987.

(6)  A description of the server machine and its backup:

(a) Hardware and software

DEC-1090T   and  TOPS20
DEC-2065    and  TOPS20

(b) Host domain name and network address

KL.SRI.COM  10.1.0.2 on ARPANET, 128.18.10.6 on SRINET
STRIPE.SRI.COM  10.4.0.2 on ARPANET, 128.18.10.4 on SRINET

(c) Domain-style nickname

None

(7)  Planned mapping of names of any other network hosts, other than
the server machines, into the new domain's naming space.

SRI-Blackjack.ARPA (128.18.2.1) -> Blackjack.SRI.COM
SRI-CSL.ARPA (192.12.33.2) -> CSL.SRI.COM

(8)  An estimate of the number of hosts that will be directly within
this domain.

(a) Initially  =   50
(b) One year   =  100
(c) Two years  =  200
(d) Five years =  500

(9)  A date when you expect the fully qualified domain name to become
the official host name in HOSTS.TXT.

31 September 1987

(10)  Brief description of organization.

SRI International is an independent, nonprofit, scientific
research organization.  It performs basic and applied research
for government and commercial clients, and contributes to
worldwide ecomomic, scientific, industrial, and social progress
through research and related services.
