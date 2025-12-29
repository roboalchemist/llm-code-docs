---
rfc: 90
title: "Ccn as a Network Service Center"
date: January 1971
---
1. Processors:

CCN provides the following user software:

a) The usual FORTRAN compilers (FORT G. FORT H. WATFOR);

b) PL/1 (version 5) and PL/C (Cornell's student PL/1);

c) Assembler G;

d) IBM Algol F;

e) IBM Linkage Editor F, and a fast in-core linkage editor written
at CCN;

f) Miscellaneous processors, including:

COBOL, SPI, XP7, META-5, SNOBOL, LISP 1.5, AUTOFLOW  SIMSCRIPT
1.5, MIX (Knuth's student machine), CSMP, GPSS, ECAP, APT, PMS,
MATLAN, SYMAP, SPSS, and the BMD series}

g) the IBM file utilities, SORT, and RPG.

2. Interactive Systems

a) URSA        Conversational remote job entry system based
on alphanumeric display consoles (IBM 2260
and CCI CC301 consoles). URSA provides a
number of other services, including a "desk
calculator", an interactive/interpretive
assembler, and on-line utilities for manipu-
lation of the OS file system. It also con
tains the CCN operator interface to MVT.
URSA is not suitable for typewriter interaction
because it is designed for "instantaneous" dis
play of at least 480 characters at a time.

b) APL         IBM Program Product version of this well-known
interactive system. Currently supports IBM 2741's
(Selectric typewriter terminals) only.

c) OLMS        UCLA implementation of the Culler-Fried system;
nearly identical in language to the UCSX On-line
System.

d) TSO          IBM's new general purpose time-sharing subsystem
under MVT, to be available at CCS sometime during

# 1971. TSO supports 2741's and Teletypes (and at

CCN it will support CCI consoles). TSO is
reminiscent of CTSS in its capabilities and
command language.

E. REMOTE JOB SERVICE

The RJS ("remote Job service") subsystem, was written by CCN to
support remote batch terminals communicating over dial and leased
lines. A remote batch terminal consists of a set of unit record
devices (one or more card readers, printers, and punches) driven
either by a hardwired controller or by a small CPU (e.g., IBM Model 20
or 1130). A remote RJS user enters OS/360 jobs, complete with JCL,
into the remote reader; the jobs are spooled into the operating system
and run in their turn, and the printed and/or punched output is

returned to the remote terminal from which the jobs originated (unless
the user or operator re-routes the output). The remote terminal may
also include a console typewriter to be used by the remote operator to
receive and send messages and to exert control over his terminal.

F. FAST BATCH SUBSYSTEM

CCN has written a fast batch subsystem called QUICKRUN to provide
"instant" turnaround for small, simple batch jobs which are common in
a university computing center. QUICKRUN accepts a very simple job
control language ("QCL") without much of the generality of OS/360 JCL.

QUICKRUN is really a batch job control subsystem which itself runs
essentially as a job within MVT. Because of its lack of generality,
the QUICKRUN subsystem creates much less system overhead than normal
OS batch; this is reflected in lower cost per job in QUICKRUN.

QUICKRUN is available at remote batch terminals through RJS as
well as through a self-service card reader at CCN.

G. SPECIAL CONSIDERATIONS

1. Core Memory for Batch Jobs

CCN can easily run batch jobs requiring up to 3 million bytes,
although jobs over 600K bytes will normally not run during prime
time.

2. Disk Space

CCN provides extensive on-line disk space for permanent files. The
resident disk pack configuration includes:

220 M bytes (8 packs) of user source programs, for use through
URSA.

170 M bytes (6 packs) of user object and load modules ("binary
decks") and other files.

100 M bytes of limited-time storage (n days, where n is published
number satisfying 7<= n < 0)

This space is charged for, at about 5s per kilobyte per month.

In the future, we plan to significantly extend this on-line space
by implementing a tertiary storage system using magnetic tapes.
In addition, a batch job may always request that the user's own
disk pack be mounted, thus allowing very large private collections

of files.

3. Rates

Batch charges are based upon t(CPU time), I(number of I/O requests
), and R(core memory region size). The current rate schedule may be
obtained from:

Mr. Kenneth Tom
User Relations Supervisor
UCLA
Campus Computing Network
Math Sciences Addition
Los Angeles, California 90024

Generally speaking, the CCN Model 91 cost is very attractive for
compute-bound, heavy floating-point calculations, particularly
where large regions are required. For most other jobs, the CCN
machine is competitive with other cost-recovery computing centers
which operate without special subsidy.

G. SERVICE TO NETWORK

CCN currently plans to provide RJS, URSA, and (eventually)
TSO service to the Network. Each of these will have its own third-
level protocol. In addition, there will be a "transparent" third
level protocol to allow a user-written program running in batch or
TSO at CCN to converse directly with the Network.

The third-level protocols, in the order in which we plan to
implement them, are as follows:

1. NETRJS

NETRJS is the name of the third level protocol by which a
user process in a remote host will simulate a remote batch
terminal connected to CCN's RJS system. Thus, NETRJS will
allow a user to submit complete batch jobs to the 360/91
and receive their print and punch output streams back over
the Network. NETRJS has been specified in RFC #88 and
implementation is targeted for March, 1971.

2. NETCRT

This protocol will allow a Network user to simulate an
(idealized) CCI alphanumeric display console and use CCN's
URSA system (and eventually TS0). An initial version of
NETCRT will be circulated shortly as an RFC.

3. NETTRANS

This is the "transparent" protocol allowing a user process
at CCN to talk over the Network. It has not yet been
specified.

4. NETTYPE

This protocol will allow a real or simulated 2741 to use
TS0 (and perhaps APL) via the Network.

H. REFERENCES

1. "IBM System/360 Model 91 Functional Characteristics". IBM Form A22-6907.

2. "An Implementation of MVT". CCN Technical Report TR-1 (August, 169).

3. For more information, see CCN Users' Manual.

4. "APL/360 Primer". IBM Form GH20-0689.

5. "Planning for TS0". IBM Form GC28-6698.

6. "Remote Job Service". CCN Technical Report TR-2 (undated).

[ This RFC was put into machine readable form for entry ]
[ into the online RFC archives by Robert Lamothe 3/97 ]
