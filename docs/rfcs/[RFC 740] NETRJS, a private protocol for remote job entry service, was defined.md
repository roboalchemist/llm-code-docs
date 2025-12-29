---
rfc: 740
title: "NETRJS, a private protocol for remote job entry service, was defined"
date: November 1977
obsoletes: [189, 599]
---
1.  Introduction

The records in the data transfer channels (for virtual card
reader, printer, and punch) are generally grouped into
transactions preceded by headers.  The transaction header includes
a sequence number and the length of the transaction.  Network byte
size must be 8 bits in these data streams.

A transaction is the unit of buffering within the server software,
and is limited to 880 8-bit bytes. Transactions can be as short as
one record; however, those sites which are concerned with
efficiency should send transactions as close as possible to the
880 byte limit.

There is no necessary connection between physical message
boundaries and transactions ("logical messages"); the NCP can
break a transaction arbitrarily into physical messages. The CCN
server starts each transaction at the beginning of a new physical
message, but this is not a requirement of the protocol.

Each logical record within a transaction begins with an "op code"
byte which contains the channel identification, so its value is
unique to each channel but constant within a channel.  This choice
provides the receiver with a convenient way to verify
bit-synchronization, and it also allows an extension in the future
to true "multi-leaving" (i.e., multiplexing all channels within
one connection in each direction).

The only provisions for transmission error detection in the
current NETRJS protocol are (1) the "op code" byte to verify bit
synchronization and (2) the transaction sequence number. Under the
NETRJS protocol, a data transfer error must abort the entire
transmission; there is no provision for restart.

NETRJS Protocol

2.  Meta-Notation

The following description of the NETRJS data transfer protocol
uses a formal notation derived from that proposed in RFC 31 by
Bobrow and Sutherland. The notation consists of a series of
productions for bit string variables. Each variable name which
represents a fixed length field is followed by the length in bits
(e.g., SEQNUMB(16)).  Numbers enclosed in quotes are decimal,
unless qualified by a leading X meaning hex.  Since each hex digit
is 4 bits, the length is not shown explicitly in hex numbers.  For
example, '255'(8) and X'FF' both represent a string of 8 one bits.

The meta-syntactic operators are:

|     :alternative string

```
         [ ]   :optional string

         ( )   :grouping

         +     :catenation of bit strings

```

The numerical value of a bit string (interpreted as an integer) is
symbolized by a lower case identifier preceding the string
expression and separated by a colon.  For example, in
"i:FIELD(8)", i symbolizes the numeric value of the 8 bit string
FIELD.

Finally, we use Bobrow and Sutherland's symbolism for iteration of
a sub-string:  (STRING-EXPRESSION = n); denotes n occurrences of
STRING-EXPRESSION, implicitly catenated together.  Here any n
greater or equal to 0 is assumed unless n is explicitly
restricted.

3.  Protocol Definition

STREAM ::= (TRANSACTION = n) + [END-OF-DATA]

That is, STREAM, the entire sequence of data on a particular
open channel, is a sequence of n TRANSACTIONS followed by an
END-OF-DATA marker (omitted if the sender aborts the channel).

TRANSACTION ::= THEAD(72) + (RECORD = r) + ('0'(1) = f)

That is, a transaction consists of a 72 bit header, r records,
and f filler bits; it may not exceed 880*8 bits.

NETRJS Protocol

THEAD ::= X'FF'+f:FILLER(8)+SEQNUMB(16)+LENGTH(32)+X'00'

Transactions are to be consecutively numbered in the SEQNUMB
field, starting with 0 in the first transaction after the
channel is (re-) opened.  The 32 bit LENGTH field gives the
total length in bits of the r RECORD's which follow.  For
convenience, the using site may add f additional filler bits at
the end of the transaction to reach a convenient word boundary
on his machine; the value f is transmitted in the FILLER field
of THEAD.

RECORD ::= COMPRESSED | TRUNCATED

RJS will accept intermixed RECORD's which are COMPRESSED or
TRUNCATED in an input stream.  RJS will send one or the other
format in the printer and punch streams to a given VRBT; the
choice is determined for each terminal id.

COMPRESSED ::= '2'(2) + DEVID(6) + (STRING = p) + '0'(8)

STRING     ::= ('6'(3) + i:DUPCOUNT(5))  |

This form represents a string of i consecutive blanks

('7'(3) + i:DUPCOUNT(5) + TEXTBYTE(8)) |

This form represents string of i consecutive duplicates of
TEXTBYTE.

('2'(2) + j:LENGTH(6) + (TEXTBYTE(8) = j))

This form represents a string of j characters.

TRUNCATED  ::= '3'(2) + DEVID(6) + n:COUNT(8) + (TEXTBYTE(8)=n)

DEVID(6)   ::= DEVNO(3) + t:DEVTYPE(3)

DEVID identifies a particular virtual device, i.e., it
identifies a channel.  DEVTYPE specifies the type of device, as
follows:

t = 1:  Output to remote operator console
2:  Input from remote operator console
3:  Input from card reader
4:  Output to printer
5:  Output to card punch
6,7:  Unused

NETRJS Protocol

DEVNO identifies the particular device of type t at this remote
site; at present only DEVNO = 0 is possible.

END-OF-DATA ::=X'FE'

Signals end of job (output) or job stack (input).

NETRJS Protocol

APPENDIX B

Telnet for VRBT Operator Console

The remote operator console connections use the ASCII Telnet
protocol. Specifically:

1.  The following one-to-one character mappings are used for the
three EBCDIC graphics not in ASCII:

ASCII in Telnet     |  NETRJS
----------------------------------------------------
broken vertical bar |  solid vertical bar
tilde               |  not sign
back slash          |  cent sign

2.  Telnet controls are ignored.

3.  An operator console input line which exceeds 133 characters
(exclusive of CR LF) is truncated by NETRJS.

4.  NETRJS accepts BS (Control-H) to delete a character and CAN
(Control-X) to delete the current line.  The sequence CR LF
terminates each input and output line.  HT (Control-I) is
translated to a single space. An ETX (Control-C) terminates
(aborts) the session.  All other ASCII control characters are
ignored.

5.  NETRJS translates the six ASCII graphics with no equivalent in
EBCDIC into the character question mark ("?") on input.

NETRJS Protocol

APPENDIX C

Carriage Control

The carriage control characters sent in a printer channel by NETRJS
conform to IBM's extended USASI code, defined by the following table:

CODE       ACTION BEFORE WRITING RECORD
----       ----------------------------
Blank      Space one line before printing
0          Space two lines before printing
-          Space three lines before printing
+          Suppress space before printing
1          Skip to channel 1
2          Skip to channel 2
3          Skip to channel 3
4          Skip to channel 4
5          Skip to channel 5
6          Skip to channel 6
7          Skip to channel 7
8          Skip to channel 8
9          Skip to channel 9
A          Skip to channel 10
B          Skip to channel 11
C          Skip to channel 12

NETRJS Protocol

APPENDIX D

Network/RJS Command Summary

This section presents an overview of the RJS Operator Commands, for
the complete form and parameter specifications please see references
2 and 3.

Terminal Control and Information Commands

SIGNON       First command of a session; identifies VRBT by giving
its terminal id.

SIGNOFF      Last command of a session; RJS waits for any data
transfer in progress to complete and then closes all
connections.

STATUS       Outputs on the remote operator console a complete
list, or a summary, of all jobs in the system for
this VRBT, with an indication of their processing
status in the batch host.

ALERT        Outputs on the remote operator console an "Alert"
message, if any, from the computer operator.  The
Alert message is also automatically sent when the
user does a SIGNON, or whenever the message changes.

MSG          Sends a message to the computer operator or to any
other RJS terminal (real or virtual).  A message from
the computer operator or another RJS terminal will
automatically appear on the remote operator console.

Job Control and Routing Commands

Under CCN's job management system, the default destination for
output is the input source.  Thus, a job submitted under a given
VRBT will be returned to that VRBT (i.e., the same terminal id),
unless the user's JCL overrides the default destination.

RJS places print and punch output destined for a particular remote
terminal into either an Active Queue or a Deferred Queue.  When
the user opens his print or punch output channel, RJS immediately
starts sending job output from the Active Queue, and continues
until this queue is empty.  Job output in the Deferred Queue, on
the other hand, must be called for by job name, (via a RESET
command from the remote operator)  before RJS will send it.  The
Active/Deferred choice for output from a job is determined by the

NETRJS Protocol

deferral status of the VRBT when the job is entered; the deferral
status, which is set to the Active option when the user signs on,
may be changed by the SET command.

SET           Allows the remote user to change certain properties
of his VRBT for the duration of the current session;

(a)  May change the default output destination to be
another (real or virtual) RJS terminal or the
central facility.

(b)  May change the deferral status of the VRBT.

DEFER         Moves the print and punch output for a specified job
or set of jobs from the Active Queue to the Deferred
Queue. If the job's output is in the process of
being transmitted over a channel, RJS aborts the
channel and saves the current output location before
moving the job to the Deferred Queue.  A subsequent
RESET command will return it to the Active Queue
with an implied Backspace (BSP).

RESET         Moves specified job(s) from Deferred to Active Queue
so they may be sent to user.  A specific list of job
names or all jobs can be moved with one RESET
command.

ROUTE         Re-routes output of specified jobs (or all jobs)
waiting in the Active and Deferred Queues for the
VRBT.  The new destination may be any other RJS
terminal or the central facility.

ABORT         Cancels a job which was successfully submitted and
awaiting execution or is currently executing.

Output Stream Control Commands

BSP (BACKSPACE)  "Backspaces" output stream within current sysout
data set.  Actual amount backspaced depends upon
sysout blocking but is roughly equivalent to a page
on the line printer.

CAN (CANCEL)  (a)  On an output channel, CAN causes the rest of
the output in the sysout data set currently being
transmitted to be omitted. Alternatively, may omit
the rest of the sysout data sets for the job
currently being transmitted; however, the remaining

NETRJS Protocol

system and accounting messages will be sent.

(b)  On an input channel, CAN causes RJS to ignore
the job currently being read.  However, the channel
is not aborted as a result, and RJS will continue
reading in jobs on the channel.

(c)  CAN can delete all sysout data sets for
specified job(s) waiting in Active or Deferred
Queue.

RST (RESTART) (a)  Restarts a specified output stream at the
beginning of the current sysout data set or,
optionally, at the beginning of the job.

(b)  Marks as restarted specified job(s) whose
transmission was earlier interrupted by system
failure or user action (e.g., DEFER command or
aborting the channel).  When RJS transmits these
jobs again it will start at the beginning of the
partially transmitted sysout data set or,
optionally, at the beginning of the job. This
function may be applied to jobs in either the Active
or the Deferred Queue; however, if the job was in
the Deferred Queue then RST also moves it to the
Active Queue.  If the job was never transmitted, RST
has no effect other than this queue movement.

REPEAT        Sends additional copies of the output of specified
jobs.

EAM           Echoes the card reader stream back in the printer
and/or punch stream.

NETRJS Protocol

APPENDIX E

NETRJS TERMINAL OPTIONS

When a new NETRJS virtual terminal is defined, certain options are
available; these options are listed below.

1. Truncated/Compressed Data Format

A VRBT may use either the truncated data format (default) or
the compressed format for printer and punch output.  See
Reference 9 for discussion of the virtues of compression.

2. Automatic Coldstart Job Resubmission

If "R" (Restart) is specified in the accounting field on the
JOB card and if this option is chosen, RJS will automatically
resubmit the job from the beginning if the server operating
system should be "coldstarted" before all output from the job
is returned.  Otherwise, the job will be lost and must be
resubmitted from the remote terminal in case of a coldstart.

3. Automatic Output RESTART

With this option, transmission of printer output which is
interrupted by a broken connection always starts over at the
beginning.  Without this option, the output is backspaced
approximately one page when restarted, unless the user forces
the output to start over from the beginning with a RESTART
command when the printer channel is re-opened and before
printing begins.

4. Password Protection

This option allows a password to be supplied when a terminal is
signed on, preventing unauthorized use of the terminal ID.

5. Suppression of Punch Separator and Large Letters.

This option suppresses both separator cards which RJS normally
puts in front of each punched output deck, and separator pages
on printed output containing the job name in large block
letters.  These separators are an operational aid when the
ouptut is directed to a real printer or punch, but generally
undesirable for an ARPA user who is saving the output in a file
for on-line examination.

NETRJS Protocol

APPENDIX F

Character Translation by CCN Server

A VRBT declares its character set for job input and output by the
initial connection socket it chooses. A VRBT can have the ASCII-68,
the ASCII-63, or the EBCDIC character set.  The ASCII-63 character
mapping was added to NETRJS at the request of users whose terminals
are equipped with keyboards like those found on the model 33
Teletype.

Since CCN operates an EBCDIC machine, its NETRJS server translates
ASCII input to EBCDIC and translates printer output back to ASCII.
The details of this translation are described in the following.

For ASCII-68, the following rules are used:

1.  There is one-to-one mapping between the three ASCII characters
broken vertical bar, tilde, and back slash, which are not in
EBCDIC, and the three EBCDIC characters vertical bar, not
sign, and cent sign (respectively), which are not in ASCII.

2.  The other six ASCII graphics not in EBCDIC are translated on
input to unused EBCDIC codes, shown in the table below.

3.  The ASCII control DC4 is mapped to and from the EBCDIC control
TM.

4.  The other EBCDIC characters not in ASCII are mapped in the
printer stream into the ASCII question mark.

For ASCII-63, the same rules are used except that the ASCII-63 codes
X'60' and X'7B' - X'7E' are mapped as in the following table.

EBCDIC              | ASCII-68 VRBT       | ASCII-63 VRBT
---------------------------------------------------------------
vertical bar  X'4F' | vertical bar  X'7C' | open bracket  X'5B'
not sign      X'5F' | tilde         X'7E' | close bracket X'5D'
cent sign     X'4A' | back slash    X'5C' | back slash    X'5C'
underscore    X'6D' | underscore    X'5F' | left arrow    X'5F'
.             X'71' | up arrow      X'5E' | up arrow      X'5E'
open bracket  X'AD' | open bracket  X'5B' | .             X'7C'
close bracket X'BD' | close bracket X'5D' | .             X'7E'
.             X'8B' | open brace    X'7B' | .             X'7B'
.             X'9B' | close brace   X'7D' | .             X'7D'
.             X'79' | accent        X'60' | .             X'60'

NETRJS Protocol

APPENDIX G

# REFERENCES

1. "Interim NETRJS Specifications", R. T. Braden.  RFC #189:  NIC
\#7133, July 15, 1971.

This was the basic system programmer's definition document.  The
proposed changes mentioned on the first page of RFC #189 were
never implemented, since the DTP then in vogue became obsolete.

2. "NETRJS Remote Operator Commands", R. T. Braden.  NIC #7182,
August 9, 1971

This document together with References 3 and 8 define the remote
operator (i.e. user) command language for NETRJS, and form the
basic user documentation for NETRJS at CCN.

3. "Implementation of a Remote Job Service", V. Martin and T. W.
Springer.  NIC #7183, July, 1971.

4. "Remote Job Entry to CCN via UCLA Sigma 7; A scenario", UCLA/CCN.
NIC #7748, November 15, 1971.

This document described the first NETRJS user implementation
available on a server host.  This program is no longer of general
interest.

5. "Using Network Remote Job Entry", E. F. Harslem.  RFC #307:  NIC
\#9258, February 24, 1972.

This document is out of date, but describes generally the Tenex
NETRJS user process "RJS".

6. "EBCDIC/ASCII Mapping for Network RJS", R. T. Braden.  RFC #338:
NIC #9931, May 17, 1972.

The ASCII-63 mapping described here is no longer correct, but
CCN's standard ASCII-68/EBCDIC mapping is described correctly.
This information is accurately described in Appendix F of the
current document.

NETRJS Protocol

7. "NETRJT--Remote Job Service Protocol for TIP's", R. T. Braden. RFC
\#283: NIC 38165, December 20, 1971.

This was an attempt to define an rje protocol to handle TIPs.
Although NETRJT was never implemented, many of its features are
incorporated in the current Network standard RJE protocol.

8. "CCN NETRJS Server Messages to Remote User", R. T. Braden.  NIC
\#20268, November 26, 1973.

9. "FTP Data Compression", R. T. Braden.  RFC #468:  NIC #14742,
March 8, 1973.

10. "Update on NETRJS", R. T. Braden.  RFC #599: NIC #20854, December
13, 1973.

This updated reference 1, the current document combines the two.

11. "Network Remote Job Entry -- NETRJS", G. Hicks.  RFC #325: NIC
9632, April 6, 1972.

12. "CCNRJS: Remote Job Entry between Tenex and UCLA-CCN", D.
Crocker.  NUTS Note 22, [ISI]<DOCUMENTATION>CCNRJS.DOC, March 5,
1975.

13. "Remote Job Service at UCSB", M. Krilanovich.  RFC #477: NIC
\#14992, May 23, 1973.
