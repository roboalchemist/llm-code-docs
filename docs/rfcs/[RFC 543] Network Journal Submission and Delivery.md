---
rfc: 543
title: "Network Journal Submission and Delivery"
date: July 1973
---
...etc...
.<CR>
(pause)

```
            [256 Mail completed successfully]
            <^Z>
            [*] DISC <CR>
            [*] QUIT <CR>

```

NETWORK JOURNAL DELIVERY

Three modes of Journal delivery are currently available to NLS users;
each user can select any one or a combination of ways of receiving
journal mail:

(1)   ONLINE -- an entry containing the text of the mail or, for
longer items, a citation to it, made in the user's initial
file, which resides in his directory at SRI-ARC.

RFC 543         Network Journal Submission and Delivery     13 July 1973

(2)   HARDCOPY -- the text of the mail is sent to the user (i.e.,
to an address of his choosing) via the U.S. Postal Service.

(3)   NETWORK -- Journal mail will be delivered to a user via the
Net, to a host and mailbox of his choosing.  If you wish
this option, let the NIC know and give them the name of your
host and mailbox.

Short messages ('Submit Message') will be delivered in
their entirety to the remote user, preceded by the usual
sort of header giving author, date and time, citation
number, and title:

JEW 4-APR-73 11:21  15490
SMFS Runs on TENEX 1.31 at the NIC
Message: Dave-- The NIC came up on TENEX 1.31 on
1-APR...

A citation to larger Journal articles ('Submit File')
will sent:

JEW 4-APR-73 17:51  15491
Farming Batch Work out to UCSB -- A Scenario
Location: SRI-ARC <MJOURNAL> 15491.NLSXNLS

In place of the usual link (which appears in ONLINE
delivery) is a host name (SRI-ARC) and a pathname to
the file at the host.  Using it, the remote user or a
process running on his behalf can fetch a copy of the
file from SRI-ARC FTP.  The parameter ';XNLS' signals
SRI-ARC's FTP server process to convert the NLS file
to sequential form (using a default conversion
algorithm) before transmission to the user through the
Net.

By Network Journal delivery, mail will be delivered via FTP mail
command to a host (i.e., to it's FTP server process) and mailbox
address of the user's choosing.

These two parameters will be maintained in the NIC Ident file
for each user who selects NETWORK delivery, and can, like his
delivery mode, be viewed or changed from the Ident System in
NLS.  Initial values for host and mailbox address have been
solicited from the Network community (see RFC 510 -- 16400,).

RFC 543         Network Journal Submission and Delivery     13 July 1973

The implementation of Network Journal submission and delivery
described here is a first-cut.  A more flexible and slightly cleaner
user interface will be fashioned when the File Transfer Protocol
(FTP), upon which both implementations will rely, is revised to deal
more comprehensibly with the issue of mail delivery, forwarding, and
recording (see RFC 524 -- 15146,1).

[This RFC was put into machine readable form for entry]
[into the online RFC archives by Via Genie 12/99]
