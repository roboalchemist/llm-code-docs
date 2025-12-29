---
title: "FTP Comments and Response to RFC 430"
date: February 1973
---
1. The command-reply sequence needs to be tightened in both
specification and implementations to allow convenient use of FTP by
programs or "automatons".

2. A 300 reply greeting upon first connecting to the FTP server
should be required and not optional. This avoids the programs having
to wait an arbitrary time for such a greeting before issuing
commands. Commands may only be sent after the 300 reply is received
from the server.

3. RFC 454 needs a discussion of transfer between two FTP servers
arranged by the user via the LSTN or GSOC commands.

4. Perhaps we should allow specification of data transfer parameters
in a single command line (for reasons of efficiency).  A suggested
format is to have <SP> separate the parameters bunched together in a
single line (requiring only a single reply).  Consider the following
sequences:
STRU F TYPE I BYTE 36 MODE S <CR><LF>
reply - 200 OK

5. Further discussion of MAIL and MAIL.file commands seems
necessary. Perhaps we will get some useful input from the MAIL
meeting at SRI on February 23, The following issues seem
particularly relevant to me:
a) Allowing mail to multiple users. It should be required that
FTP servers allow this.

b) Using NIC idents. FTP servers should accept some standard
form of user name. This could be NIC idents or last name with
optional use of initials.
c) Uniform conventions for who the mail is from, day, time,
etc., and how the mail is delivered to user. The mail usually gets
tagged twice or sometimes not tagged at all.  Perhaps we need a
different mechanism for indicating who the mail is from than
provided by the USER command.
d) handling bulk or junk mail (particularly the NIC documents
that may be sent on-line by the NIC). Perhaps mail.file should put a
file in user's directory and notify him of the same. The user does
not see all the junk on his console but can print the file on a
printer and read that class of mail at his leisure.

[ This RFC was put into machine readable form for entry ]
[ into the online RFC archives by Alex McKenzie with    ]

```
       [ support from GTE, formerly BBN Corp.             9/99 ]

```