---
title: "Recent Extensions to the SUPDUP Protocol"
date: March 1978
---
734.   An updated 734 will be issued when the protocol stabilizes again.

Three new variables  have  been added to  the initial  negotiation.   In
order,  they are SMARTS,  ISPEED,  and OSPEED.   Consequently, the count
should now be -10,,0, or, in octal, 777770000000.

The SMARTS  variable  specifies what "smarts" (in general, what graphics
capabilities)  the terminal  has.  Like the TTYOPT variable, a bit being
true implies  that the terminal has this option.  RFC 746 describes this
variable  and the  SUPDUP   graphics   option  in complete  detail.   If
the  graphics extension is not to be used, SMARTS should be set to 0.

The ISPEED  and OSPEED  variables are respectively the input and  output
baud rates  of the  terminal,  if  known.   For  example,  a  150./1200.
baud terminal  would  have an ISPEED of 150.   and an OSPEED of 1200.  A
speed  of zero means the line speed is indeterminate.

The %TPPRN   TTYOPT   bit  (value  0,,200) has  been  added.   This  bit
specifies  that the system should  swap parenthesis with square brackets
on input.   This is  often  desirable  for  LISP users  who  are using a
terminal  which has  parenthesis   as   a   shift  character   but   not
square   brackets. This bit is normally off and servers are not required
to implement it.

-1-