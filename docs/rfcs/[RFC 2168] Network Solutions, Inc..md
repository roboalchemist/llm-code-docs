---
rfc: 2168
title: "Network Solutions, Inc."
date: June 1997
category: Experimental
---
2.8.4)
repl         = dns_str /  backref / repl dns_str  / repl backref
dns_str      = 1*DNS_CHAR
backref      = "\" 1POS_DIGIT

flags        = "i"
DNS_CHAR     = "-" / "0" / ... / "9" / "a" / ... / "z" / "A" / ... / "Z"
POS_DIGIT    = "1" / "2" / ... / "9"  ; 0 is not an allowed backref
value domain name (see RFC-1123 [14]).

The result of applying the substitution expression to the original
URI MUST result in a string that obeys the syntax for DNS host names
[14]. Since it is possible for the regexp field to be improperly
specified, such that a non-conforming host name can be constructed,
client software SHOULD verify that the result is a legal host name
before making queries on it.

Backref expressions in the repl portion of the substitution
expression are replaced by the (possibly empty) string of characters
enclosed by '(' and ')' in the ERE portion of the substitution
expression. N is a single digit from 1 through 9, inclusive. It
specifies the N'th backref expression, the one that begins with the
N'th '(' and continues to the matching ')'.  For example, the ERE
(A(B(C)DE)(F)G)
has backref expressions:
\1  = ABCDEFG
\2  = BCDE
\3  = C
\4  = F
\5..\9  = error - no matching subexpression

The "i" flag indicates that the ERE matching SHALL be performed in a
case-insensitive fashion. Furthermore, any backref replacements MAY
be normalized to lower case when the "i" flag is given.

The first character in the substitution expression shall be used as
the character that delimits the components of the substitution
expression.  There must be exactly three non-escaped occurrences of
the delimiter character in a substitution expression. Since escaped
occurrences of the delimiter character will be interpreted as
occurrences of that character, digits MUST NOT be used as delimiters.
Backrefs would be confused with literal digits were this allowed.
Similarly, if flags are specified in the substitution expression, the
delimiter character must not also be a flag character.

Advice to domain administrators:
================================

Beware of regular expressions. Not only are they a pain to get
correct on their own, but there is the previously mentioned
interaction with DNS. Any backslashes in a regexp must be entered
twice in a zone file in order to appear once in a query response.
More seriously, the need for double backslashes has probably not been
tested by all implementors of DNS servers. We anticipate that urn.net
will be the heaviest user of regexps. Only when delegating portions
of namespaces should the typical domain administrator need to use
regexps.

On a related note, beware of interactions with the shell when
manipulating regexps from the command line. Since '\' is a common
escape character in shells, there is a good chance that when you
think you are saying "\\" you are actually saying "\".  Similar
caveats apply to characters such as

The "a" flag allows the next lookup to be for A records rather than
SRV records. Since there is no place for a port specification in the
NAPTR record, when the "A" flag is used the specified protocol must
be running on its default port.

The URN Sytnax draft defines a canonical form for each URN, which
requires %encoding characters outside a limited repertoire. The
regular expressions MUST be written to operate on that canonical
form. Since international character sets will end up with extensive
use of %encoded characters, regular expressions operating on them
will be essentially impossible to read or write by hand.

Usage
=====

For the edification of implementers, pseudocode for a client routine
using NAPTRs is given below. This code is provided merely as a
convience, it does not have any weight as a standard way to process
NAPTR records. Also, as is the case with pseudocode, it has never
been executed and may contain logical errors. You have been warned.

//
// findResolver(URN)
// Given a URN, find a host that can resolve it.
//
findResolver(string URN) {
// prepend prefix to urn.net
sprintf(key, "%s.urn.net", extractNS(URN));
do {

rewrite_flag = false;
terminal = false;
if (key has been seen) {
quit with a loop detected error
}
add key to list of "seens"
records = lookup(type=NAPTR, key); // get all NAPTR RRs for 'key'

discard any records with an unknown value in the "flags" field.
sort NAPTR records by "order" field and "preference" field
(with "order" being more significant than "preference").
n_naptrs = number of NAPTR records in response.
curr_order = records[0].order;
max_order = records[n_naptrs-1].order;

// Process current batch of NAPTRs according to "order" field.
for (j=0; j < n_naptrs && records[j].order <= max_order; j++) {
if (unknown_flag) // skip this record and go to next one
continue;
newkey = rewrite(URN, naptr[j].replacement, naptr[j].regexp);
if (!newkey) // Skip to next record if the rewrite didn't
match continue;
// We did do a rewrite, shrink max_order to current value
// so that delegation works properly
max_order = naptr[j].order;
// Will we know what to do with the protocol and services
// specified in the NAPTR? If not, try next record.
if(!isKnownProto(naptr[j].services)) {
continue;
}
if(!isKnownService(naptr[j].services)) {
continue;
}

// At this point we have a successful rewrite and we will
// know how to speak the protocol and request a known
// resolution service. Before we do the next lookup, check
// some optimization possibilities.

if (strcasecmp(flags, "S")
|| strcasecmp(flags, "P"))
|| strcasecmp(flags, "A")) {
terminal = true;
services = naptr[j].services;
addnl = any SRV and/or A records returned as additional
info for naptr[j].
}
key = newkey;

rewriteflag = true;
break;
}
} while (rewriteflag && !terminal);

// Did we not find our way to a resolver?
if (!rewrite_flag) {
report an error
return NULL;
}

// Leave rest to another protocol?
if (strcasecmp(flags, "P")) {
return key as host to talk to;
}

// If not, keep plugging
if (!addnl) { // No SRVs came in as additional info, look them up
srvs = lookup(type=SRV, key);
}

sort SRV records by preference, weight, ...
foreach (SRV record) { // in order of preference
try contacting srv[j].target using the protocol and one of the
resolution service requests from the "services" field of the
last NAPTR record.
if (successful)
return (target, protocol, service);
// Actually we would probably return a result, but this
// code was supposed to just tell us a good host to talk to.
}
die with an "unable to find a host" error;
}

Notes:
======

-  A client MUST process multiple NAPTR records in the order
specified by the "order" field, it MUST NOT simply use the first
record that provides a known protocol and service combination.

-  If a record at a particular order matches the URI, but the
client doesn't know the specified protocol and service, the
client SHOULD continue to examine records that have the same
order. The client MUST NOT consider records with a higher value
of order. This is necessary to make delegation of portions of
the namespace work.  The order field is what lets site
administrators say "all requests for URIs matching pattern x go
to server 1, all others go to server 2".
(A match is defined as:
1)  The NAPTR provides a replacement domain name
or
2) The regular expression matches the URN
)

-  When multiple RRs have the same "order", the client should use
the value of the preference field to select the next NAPTR to
consider. However, because of preferred protocols or services,
estimates of network distance and bandwidth, etc. clients may
use different criteria to sort the records.
-  If the lookup after a rewrite fails, clients are strongly
encouraged to report a failure, rather than backing up to pursue
other rewrite paths.
-  When a namespace is to be delegated among a set of resolvers,
regexps must be used. Each regexp appears in a separate NAPTR
RR.  Administrators should do as little delegation as possible,
because of limitations on the size of DNS responses.
-  Note that SRV RRs impose additional requirements on clients.

Acknowledgments:
=================

The editors would like to thank Keith Moore for all his consultations
during the development of this draft. We would also like to thank
Paul Vixie for his assistance in debugging our implementation, and
his answers on our questions. Finally, we would like to acknowledge
our enormous intellectual debt to the participants in the Knoxville
series of meetings, as well as to the participants in the URI and URN
working groups.

References:
===========

[1]  Sollins, Karen and Larry Masinter, "Functional Requirements
for Uniform Resource Names", RFC-1737, Dec. 1994.

[2]  The URN Implementors, Uniform Resource Names: A Progress Report,
http://www.dlib.org/dlib/february96/02arms.html, D-Lib Magazine,
February 1996.

[3]  Moats, Ryan, "URN Syntax", RFC-2141, May 1997.

[4]  Gulbrandsen, A. and P. Vixie, "A DNS RR for specifying
the location of services (DNS SRV)", RFC-2052, October 1996.

[5]  Daniel, Jr., Ron, "A Trivial Convention for using HTTP in URN
Resolution", RFC-2169, June 1997.

[6]  URN-WG, "URN Resolution Services", Work in Progress.

[7]  Moore, Keith,  Shirley Browne, Jason Cox, and Jonathan Gettler,
Resource Cataloging and Distribution System, Technical Report
CS-97-346, University of Tennessee, Knoxville, December 1996

[8]  Paul Vixie, personal communication.

[9]  Crocker, Dave H. "Standard for the Format of ARPA Internet Text
Messages", RFC-822, August 1982.

[10] Orth, Charles and Bill Arms; Handle Resolution Protocol
Specification, http://www.handle.net/docs/client_spec.html

[11] Williamson, S., M. Kosters, D. Blacka, J. Singh, K. Zeilstra,
"Referral Whois Protocol (RWhois)", RFC-2167, June 1997.

[12] Information Retrieval (Z39.50): Application Service Definition
and Protocol Specification, ANSI/NISO Z39.50-1995, July 1995.

[13] IEEE Standard for Information Technology - Portable Operating
System Interface (POSIX) - Part 2: Shell and Utilities (Vol. 1);
IEEE Std 1003.2-1992; The Institute of Electrical and
Electronics Engineers; New York; 1993. ISBN:1-55937-255-9

[14] Braden, R., "Requirements for Internet Hosts - Application and
and Support", RFC-1123, Oct. 1989.

[15] Sollins, Karen, "Requirements and a Framework for URN Resolution
Systems", November 1996, Work in Progress.

# Security Considerations

=======================

The use of "urn.net" as the registry for URN namespaces is subject to
denial of service attacks, as well as other DNS spoofing attacks. The
interactions with DNSSEC are currently being studied. It is expected
that NAPTR records will be signed with SIG records once the DNSSEC
work is deployed.

The rewrite rules make identifiers from other namespaces subject to
the same attacks as normal domain names. Since they have not been
easily resolvable before, this may or may not be considered a
problem.

Regular expressions should be checked for sanity, not blindly passed
to something like PERL.

This document has discussed a way of locating a resolver, but has not
discussed any detail of how the communication with the resolver takes
place. There are significant security considerations attached to the
communication with a resolver. Those considerations are outside the
scope of this document, and must be addressed by the specifications
for particular resolver communication protocols.

Author Contact Information:
===========================

Ron Daniel
Los Alamos National Laboratory
MS B287
Los Alamos, NM, USA, 87545
voice:  +1 505 665 0597
fax:    +1 505 665 4939
email:  rdaniel@lanl.gov

Michael Mealling
Network Solutions
505 Huntmar Park Drive
Herndon, VA  22070
voice: (703) 742-0400
fax: (703) 742-9552
email: michaelm@internic.net
URL: http://www.netsol.com/
