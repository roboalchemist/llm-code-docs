---
rfc: 42
title: "Message Data Types"
date: March 1970
---
0.     YOURLOCAL
1.     MYLOCAL
2.     U.S. Ascii
3.     EBCDIC
4.     Mod 33 TTY Ascii

5.     Load table driven translator table #n.  If, in the
future, the X and Y transformation boxes are table
driven, this gives the table.  The table number n is
stored in the second byte of the message.
6.     Use table driven translator table #n.
7.     Network standard graphics message.

Examples of Local Types:

1.     Local Character sets, e.g., Lincoln writer, DEC Ascii,
etc.
2.     Graphics local messages, e.g., TX-2 Apex display
executive calls, GSAM.

[ This RFC was put into machine readable form for entry ]
[ into the online RFC archives by Robbie Bennet 11/98   ]
