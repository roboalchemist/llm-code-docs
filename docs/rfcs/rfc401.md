---
title: "Conversion of NGP-0 Coordinates to Device"
category: D.6
---
1.   move coordinate to a register and extend sign
2.   integer multiply by Q (if necessary)
3.   arithmetic shift left by (I-n)
4.   integer add S

This procedure would generally be much faster than:

1.   move coordinate to register and extend sign
2.   float fractional coordinate
3.   floating point multiply
4.   floating point add
5.   conversion to fixed point

[ This RFC was put into machine readable form for entry ]

```
       [ into the online RFC archives by BBN Corp. under the   ]
       [ direction of Alex McKenzie.                      1/97 ]

```