---
rfc: 784
title: "Isi Tops20 Implementation"
date: July 1981
---
1.  MTP receiver for TCP.

2.  MTP receiver for NCP.

3.  Dispatcher.

4.  MTP sender for TCP.

5.  MTP sender for NCP.

6.  Mail composition programs (MM, HERMES, MSG, SNDMSG, ...).

7.  User mailbox files.

8.  Pending Mail files.

9.  Other Mail sources.

10. Other Mail sinks.

11. Host Mail Capability table.

12. Host special processing tables.

We are building 1 through 5, hope that others will adapt 6 to this
system (a version of MM has been adapted at ISI), using the existing 7,
defining and using 8, providing interfaces for 9 and 10 as requested,
and creating and using 11 and 12.

Page [2]                                                Sluizer & Postel

Mail Transfer Protocol

+-----+   +-----+   +------+   +------+
| MTP |   | MTP |   | USER |   |OTHER |
| TCP |   | NCP |   | MAIL |   |MAIL  |
| RCV |   | RCV |   | PGM  |   |SOURCE|
+-----+   +-----+   +------+   +------+
|         |          |         |
|         |          |         |
|         |          |         |
v         v          v         v
+----+    +----+     +----+     +----+
|    |    |    |     |    |     |    |
Pending   +----+ |  +----+ |   +----+ |   +----+ |
Files     |    |-+  |    |-+   |    |-+   |    |-+
|    |    |    |     |    |     |    |
+----+    +----+     +----+     +----+
\      |         |       /
\     |         |      /
\    |         |     /
v   v         v    v

+------------------+       TABLES
|                  |       +----+
|    DISPATCHER    |<----->|    |---+
|                  |       |    |   |
+------------------+       +----+   |
/      /     \      \          +----+
/      /       \      \
/      /         \      \
v      v           v      v
+-----+   +-----+   +-------+   +-----+
| MTP |   | MTP |   | LOCAL |   |OTHER|
| TCP |   | NCP |   |MAILBOX|   |MAIL |
| SND |   | SND |   | FILES |   |SINK |
+-----+   +-----+   +-------+   +-----+

Note that current implementation the dispatcher and the senders for
MTP-on-TCP and MTP-on-TCP are combined in one program.

Sluizer & Postel                                                Page [3]
