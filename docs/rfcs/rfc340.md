---
rfc: 340
title: "The proposed change to the TELNET protocol calling for one standard"
date: May 1972
---
1.  Cal comp plotter attached to a teletype has logic permitting a
program to turn the plotter on and off.  When operating I believe
it uses an 8 bit code which could conflict with Telnet signals.

2.  Numerically controlled machines, either controlled from a user
terminal or code prepared by a HOST computer to be punched on the
paper tape punch at a teletype way require the use of an arbitrary
8 bit code.

3.  Experiments controlled from alphanumeric terminal or sensor data
collected through a cal-comp like connection may require the use
of a full 8 bit code.

In these cases a transparent data type with a provision for a return
to ASCII mode seems desirable.

Hide Your Input:

As more and more use of data base systems in the network is
considered, the need for and importance of using access keys,
passwords, etc. grows.  The fact that it is difficult to select the
length of input to be hidden is not a persuasive argument.  Potential
solutions seem to exist, e.g. the protocol could provide for accepting
length statements from the user program, data base system, operating
system, etc. and in default of this, use a default length representing
the server system expected optimum length.

[ This RFC was put into machine readable form for entry ]

```
       [ into the online RFC archives by BBN Corp. under the   ]
       [ direction of Alex McKenzie.                   12/96   ]

```