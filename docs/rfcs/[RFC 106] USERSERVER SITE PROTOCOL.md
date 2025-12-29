---
title: "Userserver Site Protocol"
date: March 1971
---
1.)    Does system operate on keyboard terminal input on one
character at a time (e.g. searching for a special
character other than end of line), or does it accumulate
a line at a time and operate on the line when a
special character is entered, e.g. Carriage Return (CR)?

```
         [ ]  Line at time

         [ ]  Character at time

         [ ]  Both (Explain) __________________________________

       _____________________________________________________________

       _____________________________________________________________

       _____________________________________________________________

```

2.)    What maximum buffer size does your system provide for
input of a physical line from a keyboard terminal, and
for output to a terminal, printer, or screen?

Input______Char

Output_____Char

Remarks: ____________________________________________________

_____________________________________________________________

_____________________________________________________________

_____________________________________________________________

=================
* If there is insufficient space on the questionnaire, continue
answers on back of page.

** Fill out separate questionnaire for each HOST to be directly
interfaced to an IMP.

Network HOST Questionnaire (Continued)

3.)    Describe the effect in your system of use of the following
keying conventions.  Indicate how implemented, i.e. is there
a hardware interrupt?  Does the terminal respond?  How?
What is sent into system as data, what is echoed, etc.
If the key(s) are not available, so indicate (as may be
the case for Newline for some systems, line feed for 2741's,
etc.). If available but has no meaning, so indicate.

Key Strokes        Implementation           System Action

CR       __________________________   __________________

LF       __________________________   __________________

NL       __________________________   __________________

CR,LF      __________________________   __________________

Terminal Type =  __________________________

If appropriate, enter data for other terminal types on the
back of this page.

4.)    What special character or characters are used in your
system to awaken some process during the entry of data
from a terminal (e.g. control C for some systems, break on
others, etc.)?

Character(s)                 Operation

___________    ___________________________________________

___________    ___________________________________________

___________    ___________________________________________

___________    ___________________________________________

Network HOST Questionnaire (Continued)

5.)    List the types of keyboard terminals and codes supported
by your system.

__________________________________________________________

__________________________________________________________

__________________________________________________________

6.)    What internal code(s) is used in your system to represent
character sets?  If not ASCII nor EBCDIC, attach a copy of
the code.

__________________________________________________________

__________________________________________________________

__________________________________________________________

7.)    For each terminal type do you support it in:

Half Duplex (Pure) _______________________________________

Half Duplex (with Break or Attention) ____________________

Half Duplex (Break & Reverse Break) ______________________

Full Duplex (without echo) _______________________________

Full Duplex (with echo) __________________________________

8.)   For optional echo systems, at initial connect time
is the terminal assumed to require an echo?

```
            [ ] Yes

            [ ] No

```

Network HOST Questionnaire (Continued)

9.)   Does your system perform error detection (e.g. parity
check) on terminal input and, if so, is this a hardware
or software check?

_____________________________________________________________

_____________________________________________________________

_____________________________________________________________

10.)   Does your system support punched paper tape input?  If so,
what sort of end of line sequence is used?

_____________________________________________________________

_____________________________________________________________

_____________________________________________________________

[ This RFC was put into machine readable form for entry ]

```
            [ into the online RFC archives by S.M.H. 5/97 ]

```