---
rfc: 388
title: "After a lapse of 5 months since RFC #323 was issued (23 March), I am"
date: August 1972
obsoletes: [323                                            23]
---
.
.
|type   |    Count      |
+-------+---------------+

Thus, the data you send will look roughly like this.

+--------------------------------+
word 0                |            DAY/TIME            |
+--------------------------------+
word 1                |          CONTROL WORD          |
+--------------------------------+
|            DATA FOR            |
|           DESTINATION          |
|                1               |
+--------------------------------+
|            DATA FOR            |
|           DESTINATION          |
|               2                |
+--------------------------------+
.
.
.
+--------------------------------+
|          DATA FOR              |
|        DESTINATION             |
|              N                 |
+--------------------------------+
|       CONTROL MESSAGE          |

# . DISTRIBUTION           |

# . |

# . |

|                                |
word n                +--------------------------------+

On completion of transmission of the last message, and after you
receive the RFNM for this last message, close the connection.

In the original specification, we said that the data gathering
program would ICP to some well-known socket.  We believe this to be
an unnecessary complication and instead, we will merely open a
connection on your 241 (decimal), expecting you to send data as soon
as our Allocate command is received by your NCP.  Please let me know
if this cannot be done (i.e. you need the ICP).

If you connect to UCLA-NMC socket 241, we will send you our own 24
hour data.  Anyone interested in capturing these statistics is
welcome to do so.

Please note that these summarized statistics are for standard local
24 hour period (e.g. local midnight to local midnight).  They are not
for a sliding 24 hour period ending with the time at which statistics
were requested.  Also, the data is to be collected only for open
connections on links 0, 2-71.

The following are participating (others) are heartily invited):
UCLA-NMC, DMCG, LL-67.

[This RFC was put into machine readable form for entry]

```
     [into the online RFC archives by Helene Morin, Via Genie, 12/99]

```