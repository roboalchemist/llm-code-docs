---
rfc: 1031
title: "MILNET Name Domain Transition"
date: November 1987
---
1989.  After this date, hosts not converted need to obtain the host
table equivalent by private arrangement (see "Migration Path" above).

Start     End
Milestone                                      Date     Date
===========================================   ======   ======
Root server operational testing               Dec 86   Jul 87
Policy announced in DDN Management Bulletin   Oct 87
Host conversion                               Oct 87   Oct 89
Host table discontinued                       Oct 89

MILNET Name Domain Timetable

Table 1

DOCUMENTATION

The Name Domain system is described in several documents that are
maintained and available from the NIC in both online and in hardcopy
form.  The documents are in "Request For Comments" format (RFC)
commonly used in the Internet to document and discuss various
networking issues.  The documents noted in Table 2 fully describe the
concepts, conventions, enhancements, requirements, and operation of
the Name Domain system.  The following paragraphs give a brief
synopsis of each document.

RFC    PH   DOCUMENT TITLE
===    ==   =======================================================

799   *    Internet Name Domains
819        Domain Naming Convention for Internet User Applications
920        Domain Requirements
921        Domain Name System Implementation Schedule - Revised
952   *    Internet Host Table Specification
953   *    Hostnames Server
974        Mail Routing and the Domain System
1032        Domain Administrators Guide
1033        Domain Administration Operations Guide
1034        Domain Names - Concepts and Facilities
1035        Domain Names - Implementation Specification

*  Included in the DDN Protocol Handbook

Name Domain Documents

Table 2

RFC-799

This RFC is an early description of the concepts of a name domain
system. It is exploratory in nature and offers scenarios for name
resolution and mail forwarding.

RFC-819

This RFC is a think peice about hierarchical naming conventions
for internetworking applications.  The conventions proposed are
aligned along administrative rather than topological boundaries
and is designed for interoperation among heterogeneous naming
environments.  Further topics of discussion include mail relaying,
name service approaches, and naming authorities.

RFC-920

This RFC contains a policy statement on the requirements of
establishing a new domain in the ARPA Internet and introduces the
limited set of top level domains.

RFC-921

This RFC contains a policy statement on the implementation
schedule of the ARPA Internet domain system (as of October 1984).
The discussion describes schedule and future operational
scenarios, as well as the transition between the two.

RFC-952

This RFC specifies the format of the host/address table maintained
by the NIC.

RFC-953

This RFC contains the official specification of the Hostname
Server Protocol.  This TCP-based protocol accesses machine-
readable name/address information in the format described by RFC-
952 and is used by hosts to obtain all or a portion of the
centralized host table.

RFC-974

This RFC presents a description of how mail systems are expected
to route messages based on domain system information.  In
particular, it discusses how mailers should interpret mail
exchanger resource records for message routing to both host and
domain names.

RFC-1032

This RFC describes the guidelines for a domain administrator to
follow to establish a new domain.

RFC-1033

This RFC provides procedures for domain administrators in
operating a domain server and maintaining their portion of the
hierarchical database.

RFC-1034

This RFC introduces domain style names, their use for ARPA
Internet mail and host address support, and the protocols and
servers used to implement domains.  The concepts and facilities of
the domain system are described.  The RFC also discusses the
hierarchical database model, resource record usage, query
formation, query resolution, and domain control.

RFC-1035

This RFC specifies the format of domain system transactions,
discusses the implementation of domain servers, and explores the
use of domain names in the context of mail and other network
software.

Several implementations of the domain system exist.  The first two
paragraphs (JEEVES and BIND) discuss the prominent (and most mature)
two implementations and their authors/maintainers.  These
implementations are available online.  The last paragraphs list
implementations under development.  Points of contact can supply more
information.

The intent of listing these implementations is to give vendors the
opportunity to inspect working code.  These implementations embody
experience with the domain system and offer interpretations of the
protocols found acceptable in operational environments.

Tops-20 Server and Resolver (JEEVES)

Some domain root servers on the ARPANET are hosted on TOPS-20 systems
and run the code called JEEVES.  The JEEVES resolver is specific to
version 5 of TOPS-20.  The code is maintained by Paul Mockapetris
(ISI), is available using anonymous FTP from host a.isi.edu, and
resides in the files

```
                   <domain.version5>version5.mss
                   <domain.version5>version5.doc
                   <domain.version5>version5.txt

```

His mail addresses are:

ARPANET:  pvm@venera.isi.edu

US MAIL:  USC Information Sciences Institute

# 4676. Admiralty Way

Marina del Rey, California 90292-6695

4BSD Unix Resolver and Server (BIND)

Most hosts running lower level domain servers on the ARPANET are
hosted on 4BSD systems and run the code called BIND.  This code is
maintained for periodic releases by Mike Karels (UCB).  His mail
addresses are:

ARPANET:  karels@okeeffe.berkeley.edu

US MAIL:  Computer Systems Research Group
Computer Science Division
Department of EE & CS
University of California
Berkeley, CA  94720

There are two distribution mailing lists that publish information
about BIND.  General discussions can be received by contacting
bindrequest@ucbarpa.berkeley.edu and requesting to join the BIND
list.  Information relating to testing developmental versions of BIND
can be received by contacting bind-test-request@ucbarpa.berkeley.edu
and requesting to join the BIND-TEST list.

A commercial version of BIND is distributed with Sun Microsystems'
operating system version 3.2.  The point of contact is Bill Nowicki.
His addresses are:

ARPANET:  nowicki@sun.com

US MAIL:  Sun Microsystems

# 2550. Garcia Avenue

Mountain View, CA 94043

MS-DOS Server and Resolver

FTP Software is working on a port of BIND to their PC/TCP environment
under MS/DOS (their PC/TCP package).  They already have a resolver
that depends on recursive queries.  The point of contact is Philip A.
Prindeville.  His mail addresses are:

ARPANET:  pap4@ai.ai.mit.edu

US MAIL:  FTP Software Inc
P.O. Box 150
Kendall Sq. Branch
Boston, MA  02142

Tops-20 Resolver

A resolver is being written in C for Tops-20 and ITS by Rob Austein.
He encourages contacts from Tops-10, WAITS, and TENEX system
programmers.  His mail addresses are:

ARPANET:  sra@xx.lcs.mit.edu.

US MAIL:  MIT LCS NE43-503

# 545. Technology Square

Cambridge MA 02139

Symbolics Resolver

Symbolics Inc. has an implementation for the 36xx series Lisp
Machines.  Steven L. Sneddon is the point of contact.  His addresses
are:

ARPANET:  sned@pegasus.scrc.symbolics.com

US MAIL:  Manager, Networks and Communications
Symbolics, Inc.

# 11. Cambridge Center

Cambridge, MA 02142

Xerox Cedar Resolver

Xerox has a resolver running in the Cedar language/environment at
Xerox PARC.  John Larson is the point of contact.  His addresses are:

ARPANET:  jlarson.pa@xerox.com

US MAIL:  Xerox Palo Alto Research Center

# 3333. Coyote Hill Road

Palo Alto, CA  94304

Harris Resolver

There is a domain resolver for the Harris H series that handles
canonical name, host address, name server, and mail agent (MX)
records.  Bruce Orchard is the point of contact.  His addresses are:

ARPANET:  orchard/bruc@scarecrow.waisman.wisc.edu

US MAIL:  549 Waisman Center
University of Wisconsin-Madison

# 1500. Highland Avenue

Madison, Wisconsin  53705-2280

Fuzzball Server and Resolver

Dave Mills has both server and solver for the so-called PDP11/LSI- 11
Fuzzballs.  However, these are not complete implementations and do
not support zone transfers and so forth.  They have little use
outside the fuzzball community, since the code is in assembler and is
not for Unix.  His addresses are:

ARPANET:  mills@udel.edu

US MAIL:  Electrical Engineering Department
University of Delaware
Newark, DE 19716

Multics Resolver

There is a resolver for Multics that is nearly ready for release.
Art Beattie is the point of contact.  His addresses are:

ARPANET:  beattie%pco@bco-multics.arpa

US MAIL:  MS K55
Honeywell Bull
PO Box 8000
Phoenix, AZ, 85066-8000

VAX/VMS Resolver

There is a partial resolver implementation (only supports address
queries and IN-ADDR PTR lookups) that is part of the CMU/TEK TCP/IP
package for VAX/VMS.  It is written in BLISS-32.  Vince Fuller is the
point of contact.  His addresses are:

ARPANET:  vince.fuller@c.cs.cmu.edu

US MAIL:  Computer Science Department
Carnegie-Mellon University
Schenley Park
Pittsburgh, Pa.  15213

Macintosh Resolver and Server

Tom Unger has ported BIND to the Macintosh.  This was done using the
Macintosh Programmer's Workshop and CITI's MacIP that currently
consists of IP, UDP, and a Berkeley style socket library.  His mail
addresses are:

ARPANET:  tom@citi.umich.edu

US MAIL:  Center for Information and Technology Integration
University of Michigan

# 2901. Hubbard

Ann Arbor, MI 48105

ORDERING INFORMATION

Documents are available online from the NIC (IP address 10.0.0.51 or
26.0.0.73) by using FTP with the login ANONYMOUS and the password
GUEST.  RFCs are in files named RFC:RFCnnn.TXT and are simple ASCII
files ready for printing.  Pages within the documents are separated
by a form feed character on a line by itself.

Hardcopy of the documents and software mentioned in the discussions
above may be obtained from the NIC or the author.  Prices are
available on request and are documented in DDN Newsletter #50 (12 Dec
1986).  The address and phone numbers of the NIC are listed below.

DDN Network Information Center
SRI International, Room EJ291

# 333. Ravenswood Avenue

Menlo Park, CA 94025

(800) 235-3155
(415) 859-3695
