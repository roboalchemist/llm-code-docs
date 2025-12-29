---
rfc: 662
title: "One of the reasons for such a poor performance is the output buffering strategy"
---
35.0). The service system configuration was 2 cpu's and 384 K primary memory.
The development machine configuration was 1 cpu and 256 K of primary memory.
The development system load was limited to the file transfer processes and the
initializer process. The MIT Multics is connected to the IMP number 44 (port 0)
by a rather short cable (approximately 100 feet long.) The CISL Multics is
connected to the IMP number 6 (port 0) by an approximately l5OO feet long cable.
8oth IMPs are in close physical proximity (approximately 2000 feet,) and are
connected to each other by a 5O kilobits per second line. The results given
above show considerable improvement in the performance with the new IMP DIM.

Since there is considerable interest in the Multics development community in
using the file transfer facility for transmitting Multics System Tapes between
the two systems, we are providing here an estimate of time that would be taken
to transmit the current MST. MST 23.4-0A contains 334,231 words. When
multiplied by 36 (the word length in bits) this yields the total number of bits
to be approximately 12.5 million. Assuming a file transfer rate of 27,500 bits
per second, it will take approximately 7 minutes and 30 seconds to transmit the
system 23.4-0A.

In the experiment outlined above, there was only one file being transferred at
any given tine between the two systems. We conducted another experiment to get
an estimate of performance in the situation of multiple file transfers occurring
simultaneously. This experiment consisted of first two, and then three,
simultaneous file-transfers from the development system to the service system.
These file transfers were started by different processes logged in from separate
consoles. Because these file-transfers were started manually, we could not
obtain perfect simultaneity and results obtained for the total bandwidth are
essentially approximate. For two simultaneous file transfers the total bit rate
was approximately 40,000 bits per second and bit rate for each file transfer was
approximately 20,000 bits per second. For three simultaneous file transfers,
total bit rate remained at approximately 40,000 bits per second and bit rate for
individual transfers was approximately 13,500 bits per second.

-3-
