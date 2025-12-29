---
rfc: 973
title: "Domain System Changes and Observations"
date: January 1986
---
X.ISI.EDU.    10000 A   <address of X.ISI.EDU.>
Y.GOV.        10000 A   <address of Y.GOV.>

and the following to the child zone:

ISI.EDU.      10000 NS  X.ISI.EDU.
10000 NS  Y.GOV.

# 50000. SOA <SOA information>

X.ISI.EDU.    10000 A   <address of X.ISI.EDU.>
Y.GOV.        10000 A   <address of Y.GOV.>

Note the following:

In both cases, the A RR for Y.GOV is included, even though
Y.GOV isn't in the EDU or ISI.EDU domains.  This RR isn't
authoritative, but is included to guarantee that the address of
Y.GOV is passed with delegations to it.  Strictly speaking this
RR need not be in either zone, but its presence is recommended.
The X.ISI.EDU A RR is absolutely essential.  The only time that
a server should use the glue RRs is when it is returning the NS
RRs and doesn't otherwise have the address of the server.  For
example, if the parent server also was authoritative for GOV,
the glue RR would typically not be consulted.  However, it is
still a good idea for it to be present, so that the zone is
self-sufficient.

The child zone and the parent zone have identical NS RRs for
the ISI.EDU domain.  This guarantees that no matter which
server is asked about the ISI.EDU domain, the same set of name
servers is returned.

The child zone and the parent zone have A RRs for the name
servers in the NS RRs that delegate the ISI.EDU domain.  This
guarantees that in addition to knowing the name servers for the
ISI.EDU domain, the addresses of the servers are known as well.

The TTLs for the NS RRs that delegate the ISI.EDU domain and
the A RRs that represent the addresses of the name servers are
all the same.  This guarantees that all of these RRs will
timeout simultaneously.  In this example, the value 10000 has
no special significance, but the coincidence of the TTLs is
significant.

These guidelines haven't changed any of the flexibility of the
system; the name of a name server and the domains it serves are
still independent.

It might also be the case that the organization called ISI wanted
to take over management of the IN-ADDR domain for an internal
network, say 128.99.0.0.  In this case, we would have additions to
the parent zone, say IN-ADDR.ARPA.

We might add the following to the parent zone:

99.128.IN-ADDR.ARPA. 2000 NS  Q.ISI.EDU.
2000 NS  XX.MIT.EDU.
Q.ISI.EDU.           2000 A   <address of Q.ISI.EDU.>
XX.MIT.EDU.          2000 A   <address of XX.MIT.EDU.>

and the following to the child zone:

99.128.IN-ADDR.ARPA. 2000 NS  Q.ISI.EDU.
2000 NS  XX.MIT.EDU.

# 5000. SOA <SOA information>

Q.ISI.EDU.           2000 A   <address of Q.ISI.EDU.>
XX.MIT.EDU.          2000 A   <address of XX.MIT.EDU.>

SOA serials

The serial field of the SOA RR for a domain is supposed to be a
continuously increasing (mod 2**32) value which denotes the

version of the database.  The idea is that you can tell that a
zone has changed by comparing serial numbers.  When you change a
zone, you should increment the serial field of the SOA.

All RRs with the same name, class, and type should have the same TTL.

The logic here is that all of them will timeout simultaneously if
cached and hence the cache can be reliably used.

Case consistency

The domain system is supposed to preserve case, but be case
insensitive.  However, it does nobody any good to put both RRs for
domain name xxx and XXX in the data base - It merely makes caching
ambiguous and decreases the efficiency of compression.  This
consistency should also exist in the duplicate RRs that mark
delegation in the delegator and delegatee.  For example, if you
ask the NIC to delegate UZOO.EDU to you, your database shouldn't
say uzoo.edu.

Inappropriate use of aliases

Canonical names are preferred to aliases in all RRs.  One reason
is that the canonical names are closer to the information
associated with a name.  A second is that canonical names are
unique, and aliases are not, and hence comparisons will work.

In particular, the use of aliases in PTR RRs of the IN-ADDR domain
or in NS RRs that mark delegation is discouraged.

EXPERIENCES

This section discusses some unusual situations and common bugs which
are encountered in the present system, and should be helpful in
problem determination and tuning.  Put differently, you should try to
make your code defend against these attacks, and you should expect to
be the object of complaint if you make these attacks.

UDP addresses

When you send a query to a host with multiple addresses, you might
expect the response to be from the address to which you sent the
query.  This isn't the case with almost all UNIX implementations.

UDP checksums

Many versions of UNIX generate incorrect UDP checksums, and most
ignore the checksum of incoming UDP datagrams.  The typical
symptom is that your UNIX domain code works fine with other
UNIXes, but won't communicate with TOPS-20 or other systems.
(JEEVES, the TOPS-20 server used for 3 of the 4 root servers,
ignores datagrams with bad UDP checksums.)

Making up data

There are lots of name servers which return RRs for the root
servers with 99999999 or similar large values in the TTL.  For
example, some return RRs that suggest that ISIF is a root server.
(It was months ago, but is no longer.)

One of the main ideas of the domain system is that everybody can
get a chunk of the name space to manage as they choose.  However,
you aren't supposed to lie about other parts of the name space.
Its OK to remember about other parts of the name space for caching
or other purposes, but you are supposed to follow the TTL rules.

Now it may be that you put such records in your server or whatever
to ensure a server of last resort.  That's fine.  But if you
export these in answers to queries, you should be shot.  These
entries get put in caches and never die.

Suggested domain meta-rule:

If you must lie, lie only to yourself.

PROBLEM AREAS

This section discusses some shortcomings in the present system which
may be addressed in future versions.

Compression and types

The present specification attempts to allow name servers and
resolvers to cache RRs for classes they don't "understand" as well
as to allow compression of domain names to minimize the size of
UDP datagrams.  These two goals conflict in the present scheme
since the only way to expand a compressed name is to know that a
name is expected in that position.

One technique for addressing this problem would be to preface
binary data (i.e. anything but a domain name) with a length octet.

The high order two bits of the length octet could contain either
01 or 10, which are illegal for domain names.  To compensate for
the additional bytes of data, we could omit the RDATA length field
and terminate each RR with a binary length field of zero.

Caching non-existent names

In the present system, a resolver has no standard method for
caching the result that a name does not exist, which seems to make
up a larger than expected percentage of queries.  Some resolvers
create "does not exist" RRs with TTLs to guarantee against
repetitive queries for a non-existent name.

A standard technique might be to return the SOA RR for the zone
(note that only authoritative servers can say name does not exist)
in the reply, and define the semantics to be that the requester is
free to assume that the name does not exist for a period equal to
the MINIMUM field of the SOA.

Cache conflicts

When a resolver is processing a reply, it may well decide to cache
all RRs found in sections of the reply.  The problem is that the
resolver's cache may already contain a subset of these RRs,
probably with different TTLs.

If the RRs are from authoritative data in the answer section, then
the cache RRs should be replaced.  In other cases, the correct
strategy isn't completely clear.  Note that if the authoritative
data's TTL has changed, then the resolver doesn't have enough
information to make the correct decision in all cases.

This issue is tricky, and deserves thought.

# REFERENCES

[1]  Mockapetris, P., "Domain Names - Concepts and Facilities",
RFC-882, USC Information Sciences Institute, November 1983.

[2]  Mockapetris, P., "Domain Names - Implementation and
Specification", RFC-883, USC Information Sciences Institute,
November 1983.

[3]  Partridge, C., "Mail Routing and the Domain System", RFC-974,
CSNET-CIC, BBN Laboratories, January 1986.
