---
rfc: 189
title: "Interim NETRJS Specifications"
date: July 1971
category: D
---

# 1. Introduction

The records in the data transfer channels (for virtual card reader,
printer, and punch) are generally grouped into _transactions_ pre-
ceded by headers.  The transaction header includes a sequence number
and the length of the transaction.  Network byte size must be 8 bits
in these data streams.

A transaction is the unit of buffering within the Model 91 software.
Internal buffers are 880 bytes.  Therefore, CCN cannot transmit or
receive a single transaction larger than 880 bytes.  Transactions can
be as short as one record; however, those sites which are concerned
with efficiency should send transactions as close as possible to the
880 byte limit.

There is no necessary connection between physical message boundaries
and transactions ("logical messages"); the NCP can break the "logical
message" arbitrarily into physical messages.  At CCN we will choose
to have each logical message start a new physical message, so the NCP
can send the last part of each message without waiting for an expli-
cit request, but a remote site is not required to follow this conven-
tion.

Each logical record within a transaction begins with an "op code"
byte which contains the channel identification, so its value is
unique to each channel but constant within a channel.  This choice
provides a convenient way to verify bit synchronization at the
receiver, and also allows an extension in the future to true "multi-
leaving" (i.e., multiplexing all channels within one connection in
each direction).

The only provisions for transmission error detection in the current
NETRJS protocol are (1) this "op code" byte to verify bit synchroni-
zation and (2) the transaction sequence number.  At the urging of
Crowther, we favor putting an optional 16 bit check sum in the unused
bytes of the second-level header.  It is currently assumed that if an
error is detected then the channel is to be aborted and the entire
transmission repeated.  To provide automatic retransmission we would
have to put in reverse channels for ACK/NAK messages.

# 2. Character Sets

For an ASCII VRBT, NETRJS will map ASCII in the card reader stream
into EBCDIC, and re-map the printer stream to ASCII, by the following
rules:

1.  One-to-one mapping between the three ASCII characters | ~ \
which are not in EBCDIC, and the three EBCDIC characters

```
            [vertical bar, not-sign and cent-sign] (respectively) which
            are not in ASCII.

        2.  The other six ASCII graphics not in EBCDIC will be
            translated on input to an EBCDIC question mark (?).

        3.  The ASCII control DC3 (the only one not in EBCDIC) will be
            mapped into and from the EBCDIC control TM.

        4.  The EBCDIC characters not in ASCII will be mapped in the
            printer stream into the ASCII question mark.

```

# 3. Meta-Notation

The following description of the NETRJS data transfer protocol uses a
formal notation derived from that proposed in RFC #31 by Bobrow and
Sutherland.  (The NETRJS format is also shown diagramatically in
Figure 2.)

The derived notation is both concise and easily readable, and we
recommend its use for Network documentation.  The notation consists
of a series of productions for bit string variables whose names are
capitalized.  Each variable name which represents a fixed length
field is followed by the length in bits (e.g., SEQNUMB(16)).  Numbers
enclosed in quotes are decimal, unless qualified by a leading X
meaning hex.  Since each hex digit is 4 bits, the length is not shown
explicitly in hex numbers.  For example, '1'(8) and X'FF' both
represent a string of 8 one bits.  The meta-syntactic operators are:

|       :alternative string

```
           [ ]     :optional string
           ( )     :grouping
           +       :catenation of bit strings

```

The numerical value of a bit string (interpreted as an integer) is
symbolized by a lower case identifier preceding the string expression
and separated by a colon.  For example, in "i:FIELD(8)", i symbolizes
the numeric value of the 8 bit string FIELD.

Finally, we use Bobrow and Sutherland's symbolism for iteration of a
sub-string:  (STRING-EXPRESSION = n); denotes n occurrences of STRING
EXPRESSION, implicitly catenated together.  Here any n >= 0 is
assumed unless n is explicitly restricted.

# 4. Protocol Definition

STREAM <-- (TRANSACTION = n) + [END-OF-DATA]

That is, STREAM, the entire sequence of data on a particular open
channel, is a sequence of n TRANSACTIONS followed by an END-OF-DATA
marker (omitted if the sender aborts the channel).

TRANSACTION <-- THEAD(72) + (RECORD = r) + ('0'(1) = f)

That is, a transaction consists of a 72 bit header, r records, and f
filler bits.

THEAD <-- X'FF' + f:FILLER(8) + SEQNUMB(16) + LENGTH(32) + X'00'

Transactions are to be consecutively numbered in the SEQNUMB field,
starting with 0 in the first transaction after the channel is (re-)
opened.  The 32 bit LENGTH field gives the total length in bits of
the r RECORD's which follow.  For convenience, the using site may add
f additional filler bits at the end of the transaction to reach a
convenient word boundary on his machine; the value f is also
transmitted in the FILLER field of THEAD.

RECORD <-- COMPRESSED | TRUNCATED

RJS will accept intermixed RECORD's which are COMPRESSED or TRUNCATED
in an input stream.  RJS will send one or the other format in the
printer and punch streams to a given VRBT; the choice is determined
when CCN establishes a terminal id.

COMPRESSED  <--   '2'(2) + DEVID(6) + (STRING = p) + '0'(8)

STRING      <--   ('6'(3) + i:DUPCOUNT(5))
This form represents a string of i
consecutive blanks

('7'(3) + i:DUPCOUNT(5) + TEXTBYTE(8))
This form represents string of i consecutive
duplicated of TEXTBYTE.

('2'(2) + j:LENGTH(6) + (TEXTBYTE(8) = j))
This form represents a string of j
characters.

The first two alternatives above in the STRING production begin with
count bytes chosen to be distinguishable from the (currently defined)
Telnet control characters.  In a Telnet stream, the third count byte
would not be needed.  This is irrelevant to the current NETRJS, but
it would allow the use of compression within a Telnet data stream.

TRUNCATED <-- '3'(2) + DEVID(6) + n:COUNT(8) + (TEXTBYTE(8) = n)

DEVID(6)  <-- DEVNO(3) + t:DEVTYPE(3)

DEVID identifies a particular virtual device, i.e.,
it identifies a channel.  DEVTYPE specifies the type
of device, as follows:

t = 1:  Output to remote operator console
2:  Input from remote operator console
3:  Input from card reader
4:  Output to printer
5:  Output to card punch
6,7:  Unused

DEVNO(3) identifies the particular device of type t
at this remote site; at present only DEVNO = 0 is
possible.

END-OF-DATA <-- X'FE'
Signals end of job (output) or job stack (input).

APPENDIX B

Telnet for VRBT Operator Console

The remote operator console connections use the ASCII Telnet
protocol as in RFC #158.  Specifically:

1)  The following one-to-one character mappings are used for the
three EBCDIC graphics not in ASCII:

ASCII
in Telnet                NETRJS

|                  [vertical bar]
~                  [not-sign]
\                  [cent-sign]

2)  Initially all Telnet control characters will be ignored.  In the
future we will implement the Telnet Break facility to allow a
remote user to terminate extensive console output from a
command.

3)  An operator console input line which exceeds 133 characters
(exclusive of CR LF) will be truncated by NETRJS.

4)  NETRJS will accept BS to delete a character, and CAN to delete
the current line.  The sequence CR LF terminates each input and
output line.  HT will be translated to a single space in RJS.
All other ASCII control characters will be ignored.  NETRJS will
translate the six ASCII graphics with no equivalent in EBCDIC
into the character question mark ("?") on input.

APPENDIX C

Carriage Control

The carriage control characters sent in a printer channel by NETRJS
conform to IBM's extended USASI code, defined by the following table:

CODE                ACTION BEFORE WRITING RECORD

blank               Space one line before printing
0                 Space two lines before printing
-                 Space three lines before printing
+                 Suppress space before printing
1                 Skip to channel 1
2                 Skip to channel 2
3                 Skip to channel 3
4                 Skip to channel 4
5                 Skip to channel 5
6                 Skip to channel 6
7                 Skip to channel 7
8                 Skip to channel 8
9                 Skip to channel 9
A                 Skip to channel 10
B                 Skip to channel 11
C                 Skip to channel 12

APPENDIX D

Network/RJS Command Summary

Terminal Control and Information Command

SIGNON          First command of a session; identifies VRBT by giving
its terminal id.

SIGNOFF         Last command of a session; RJS waits for any data
transfer in progress to complete and then closes all
connections.

STATUS          Outputs on the remote operator console a complete
list, or a summary, of all jobs in the system for
this VRBT, with an indication of their processing
status in the Model 91.

ALERT           Outputs on the operator console the special "Alert"
message, if any, from CCN computer operator.  The
Alert message is also automatically sent when the
user does a SIGNON, or whenever the message changes.

MSG             Sends a message to CCN computer operator or to any
other RJS terminal (real or virtual).  A message from
the computer operator or another RJS terminal will
automatically appear on the remote operator console.

Job Control and Routing Commands

Under CCN's job management system, the default destination for output
is the input source.  Thus, a job submitted under a given VRBT will
be returned to that VRBT (i.e., the same terminal id), unless the
user's JCL overrides the default destination.

RJS places print and punch output described for a particular remote
terminal into either an Active Queue or a Deferred Queue.  When the
user opens his print or punch output channel, RJS immediately starts
sending job output from the Active Queue, and continues this queue is
empty.  Job output in the Deferred Queue, on the other hand, must be
called for by job name, (via a RESET command from the remote opera-
tor) before RJS will send it.  The Active/Deferred choice for output
from a job is determined by the deferral status of the VRBT when the
job is entered; the deferral status, which is set to the Active
option when the user signs on, may be changed by the SET command.

SET             Allows the remote user to change certain properties
of his VRBT for the duration of the current session;

(a)  May change the default output destination to be
another (real or virtual) RJS terminal or the central
facility.

(b)  May change the deferral status of the VRBT.

DEFER           Moves the print and punch output for a specified job
or set of jobs from the Active Queue to the Deferred
queue.  If the job's output is in the process of
being transmitted over a channel, RJS aborts the
channel and saves the current output location before
moving the job to the Deferred Queue.  A subsequent
RESET command will return it to the Active Queue with
an implied Backspace (BSP).

RESET           Moves specified job(s) from Deferred to Active Queue
so they may be sent to user.  A specific list of job
names or all jobs can be moved with one RESET
command.

ROUTE           Re-routes output of specified jobs (or all jobs)
waiting in the Active and Deferred Queues for this
VRBT.  The new destination may be any other RJS
terminal or the central facility.

ABORT           Cancels a job which was successfully submitted and
awaiting execution or is current executing in the
Model 91.  If he cancelled job was in execution, all
output it produced ill be returned.

Output Stream Control Commands

BSP (BACKSPACE) "Backspaces" output stream within current sysout data
set.  Actual amount backspaced depends upon sysout
blocking but is typically equivalent to a page on the
line printer.

CAN (CANCEL)    (a) On an output channel, CAN causes the rest of the
output in the sysout data set currently being
transmitted to be omitted.  Alternatively, may
omit the rest of the sysout data sets for the job
currently being transmitted; however, the remain-
ing system and accounting messages will be sent.

(b) On an input channel, CAN causes RJS to ignore the
job currently being read.  However, the channel
is not aborted as a result, and RJS will continue
reading in jobs on the channel.

(c) CAN can delete all sysout data sets for specified
job(s) waiting in Active or Deferred Queue.

RST (RESTART)   (a) Restarts a specified output stream at the begin-
ning of the current sysout data set or, option-
ally, at the beginning of the job.

(b) Marks as restarted specified job(s) whose
transmission was earlier interrupted by system
failure or user action (e.g., DEFER command or
aborting the channel).  When RJS transmits these
jobs again it will start at the beginning of the
partially transmitted sysout data set or, option-
ally, at the beginning of the job.  This function
may be applied to jobs in either the Active or
the Deferred Queue; however, if the job was in
the Deferred Queue then RST also moves it to the
Active Queue.  If the job was never transmitted,
RST has no effect other than this queue movement.

REPEAT          Sends additional copies of the output of specified
jobs.

EAM             Echoes the card reader stream back in the printer or
punch stream, or both.

+---------------------------------+
|               RJS               |
+---------------------------------+
^   |         ^  |  |
|   v         |  v  v
+------------------------------+
CCN -- Server      |                              |
|          NETRJS              |
+------------------------------+
^   |          ^    |     |
|   v          |    v     v
+----------+      +---------------+
|  TELNET  |      |  Data  Xfer   | (server)
|  Server  |      |  3rd Level    |
+----------+      +---------------+
^     |          ^     |     |
---------------------|-----|----------|-----|-----|-----------------
O   |  O  |          |     |     |
p   |  p  |         C|    C|    C|
e I |  e O|       I h|  O h|  P h|
ARPA            r n |  r u|       n a|  u a|  u a|
a p |  a t|       p n|  t n|  n n|
Network         t u |  t p|       u n|  p n|  c n|
o t |  o u|       t e|  u e|  h e|
r   |  r t|         l|  t l|    l|
---------------------|-----|----------|-----|-----|-----------------
|     |          |     |     |
|     V          |     V     V
+----------+      +---------------+
|  TELNET  |      |  Data  Xfer   | (user)
|  Server  |      |  3rd Level    |
+----------+      +---------------+
Remote              ^                ^     |     |
/  "Virtual       |     |     |
User              /    Remote Batch  |     V     V
/     Terminal"  +------------------+
/                 |                  |
V                  |     NETRJS       |
+---------+               |     User         |
/          |<------------->|     Process      |
/ Console   |               |                  |
+____________|               +------------------+
^     |     |
|     V     V
(file) (file) (file)

FIGURE 1. SCHEMATIC OF NETRJS OPERATION

+------+ +------+ +-----------+ +---------------------+
TRANSACTION <--> | X'FF'| |Filler| |Sequence   | | Data Length         |
|      | | Count| |   Number  | |     in bits         |
+------+ +------+ +-----------+ +---------------------+
+------+
| X'00'|  { RECORD } *
|      |
+------+

<----  n text bytes  ------>
+--+-----+   +--------+   +--------+        +--------+
TRUNCATED <--> |11|Devid|   | n (8)  |   | Text   | . . .  | Text   |
RECORD         |  | (6) |   |        |   | (8)    |        | (8)    |
+--+-----+   +--------+   +--------+        +--------+

/                                         \
| +---+----+                               | *
| |110| n  |  (n blanks)                   |
| |   |(5) |                               |
| +---+----+                               |
|                                          |
+--+-----+ / +---+----+   +--------+                  |
COMPRESSED<--> |10|Devid|<  |111| n  |   |Char-   |  (n replications |
RECORD         |  | (6) | \ |   |(5) |   |  acter |  of "Character") |
+--+-----+ | +---+----+   +--------+                  |
|                                          |
| +--+-----+   +--------+      +--------+  |
| |10|  n  |   | Text   | . . .| Text   |  |
| |  | (6) |   | (8)    |      | (8)    |  |
| +--+-----+   +--------+      +--------+  |
\                                          /
+------+
| X'00'|
|      |
+------+

FIGURE 2.  DATA TRANSFER PROTOCOL IN NETRJS

[ This RFC was put into machine readable form for entry ]
[   into the online RFC archives by Tony Hansen 11/98   ]
