---
title: "Network Meeting Notes"
date: December 1970
---
66.  Meyer will revise proposal in RFC 46.)

Meyer: Let's go back, discuss these issues, write proposals.  Later
we have an open meeting to decide on a formal proposal.

Crocker: Small group is better, perhaps I'll pick a subset.

Vezza: It's true that things aren't settled here.  Major proposals
should be on paper preparatory to a meeting.  We can't legislate
what a small group does.  It has no more authority than an
individual.

(Karp of MITRE volunteers to produce a bibliography of network
documents, perhaps by January.)

(Who has implemented logger protocol? UCSB and UCLA mod 91 have or
are planning.  SDC may have it by 21/1, found it awkward, willing
to change.)

(Discussion of file transmission.  Crocker proposes that a future
protocol change might attach a byte size such as 8, 32, 36 bits to
a connection.)

(Regarding control links, everything is transmitted in 8-bit bytes
except ECO, ERP, ERR commands, No objection was voiced to changing
the protocol so that they also must be multiples of 8-bit bytes.)

(Discussion of how to specify the end of a file.  Prior transmission
of bit count, or send EOR character at end? Suggestion that we
want global solution to the general problem of sending an
arbitrary length message, rather than just file transmission.)

(Discussion of "transaction units" or record sizes.  What is an
optimum transaction unit size? IMP message boundaries are
invisible (by protocol fiat) and are not connected with this
discussion.  Multics block size was brought up.  Nearest thing is
page size, 1024 words.)

(How to specify end of file.  Engelbart says send data packets, then
EOF packet.  Crocker suggests that CLSing connection can act as
EOF.  Vezza suggests that IMP message boundaries be used to
determine end.  If less than full IMP message, this is last part
of file.  Meyer suggests use of two connections, data channel and
control channel, over which all control messages, such as file
name, bit length, etc. are passed.)

(Discussion concerning different situations in which whole file, part
of the file, or the whole file in arbitrary chunks was wanted.)

Meyer: Why not defer this, and talk about typewriter communications,
which is most critical.

Vezza: Engelbart wants a clean general solution.

Crocker: If we get an ad hoc solution now, it may interfere with
implementing a general solution later.

(Crocker proposes format for transmitting a file of arbitrary length
records of fixed sized bytes of 8-26 bits.  A record is less than
10^5 bytes.  Each record is headed by a count byte.)

1   2               n       1    2          m
|----------------------------------------------------|
|  n |   |   |           |   | m |   |   |       |   |
|----------------------------------------------------|
<------- record -----------> <-------- record ------->

O'Sullivan: Does this model fit a terminal which has character and
graphic modes?

(Discussion about differences between keyboard and file transmission.
Uncertainty as to whether a global solution would fit both.)

(Who wants to ship files through the network? Multics and 6-10, RAND
to UCLA, MITRE using BBN.)

Crocker: Let's go away thinking about this and propose solutions
later.

(Harslem proposes format for transmitting data with operation codes.
Each record consists of: <opcode> <length> <data>.  Gives the
opportunity to send many type of status info.)

(Discussion regarding sending data and control information intermixed
or on separate connections.  Issues of pollution of data vs.
synchronization and race problems.  Claimed that synchrony
problems are easily overcome.)

(Suggestion that we really don't know much about this area.  We
should go off and write.)

Intermission

Crocker: What has to be done before we can log onto other systems?

Meyer: 3 issues: 1) ho to establish the connection, 2) what is the
character set, 3) what is the mode of transmission (relating to
full and 1/2 duplex problem).

(Discussion of orienting standard protocol towards service systems
which generally are line-oriented and 1/2 duplex.  Any systems
offering services to have a 1/2 duplex interface.)

(Discussion of whether possible or desirable for the logger protocol
to allow transmission of partial lines in a IMP message.  Less
efficient to take partial lines, reasonable to send full line.
Pointed out that NCP protocol disallows any meaning to IMP message
boundaries, so systems must be prepared to accept lines straddling
IMP message boundaries.  However, best to send complete line.)

(Discussion of whether line-oriented protocol protocol should bend so
as to accept single character transmission from full duplex
systems.  Seems that we are coming up with a protocol to allow any
system to use a line- oriented system.  To use a char-oriented
system form other systems is more difficult and requires a
separate protocol.)

Heart: I am in favor of an immediate solution.

Postel: Once something goes in, it will be hard to change it.

Crocker: I think these meetings will turn out to be more important
than we ever wanted them to be.  I am more concerned with the long
term effects than the starting date.

Van Zoeren: If we don't decide it, somebody else will decide it the
bad way.

[ This RFC was put into machine readable form for entry ]
[ into the online RFC archives by Gottfried Janik 2/98 ]
