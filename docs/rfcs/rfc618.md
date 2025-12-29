---
rfc: 618
title: "A Few Observations on NCP Statistics"
---
.login 62,#
JOB 2 Harvard 5.06A-18 TTY25
Your name please (last name first): Taft
You are logged in as 62,404000
0728 31-Jan-74 Thur
SCHEDULED PM ON THURSDAYS, 0830-1200 EOT

.imp error

NCP version 1573.1604 operating statistics

07:29:02 31-JAN-74

NCP (link 0) message errors:
Socket not found: 2184

-2-

Improper state: 323
Illegal message type: 2
Last discarded allocation from PARC-MAXC (XEROX) link 12
Timed-out exec ICPs: 3

NCP messages:
Type Received Sent
NOP 81850 0
RTS 3688 2507
STR 2388 3562
CLS 6055 6059
ALL 183050 101442
GVB 772 0
RET 0 772
INS 109 0
ECO 7472 15426
ERP 15065 7472
ERR 2 0
RST 2782 226
RRP 162 2782

Received NCP error messages:
Type Count
Most recent error: type 4 from UCLA-CCN
Data (octal) 4 74 0 10 0 0 74 254 0 200
(decimal)    4 60 0  8 0 0 60 172 0 128

IMP data message faults:
Hardware fault: 2
Link not found: 8
Discarded RFNMs: 10
Simulated (timed out) RFNMs: 10

Received IMP messages:
Regular 590812
Err w/o id 3
NOP 4
RFNM 490095
Dest dead 366
Inc trans 52
IMP reset 2

Histogram of received data message sizes
Bits Count
<1 3
<16 146834
<32 39751

-3-

<64 7044
<128 196983
<256 46099
<512 147609
<1024 534
<2048 1820
<4096 1152
<8192 2979

# 72. free buffers

7% average buffer utilization

.kjob/k
Job 2, User [62,404000] Logged off TTY25 0729 31-Jan-74
Runtime 0 Min, 03.29 Sec

-4-