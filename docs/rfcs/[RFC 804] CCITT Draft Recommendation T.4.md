---
title: "CCITT Draft Recommendation T.4"
---

# 1. Scanning track

The  message  area  should  be  scanned  in  the   same
direction  in  the  transmitter  and  receiver.  Viewing the
message area in a vertical  plane,  the  scanning  direction
should  be from left to right and subsequent scans should be
adjacent and below the previous scan.

# 2. Dimensions of apparatus

CCITT Draft Recommendation T.4                      PAGE   2

The following dimensions should be used:

a.  A normal definition  standard  and  an  optional  higher
definition standard of 3.85 and 7.7 line/mm respectively
in vertical direction;
b.  1728 black and white picture elements along the  scanned
line;
c.  A scanning line length of 215 mm.  Other  scanning  line
lengths  may  be  employed  in  which  case the scanning
density  should  be  changed  to  maintain  the  correct
picture proportions;
d.  Input documents up to a minimum of ISO A4 size should be
accepted.

# 3. Transmission time per scanning line

A total scanning line is defined as  the  sum  of  DATA
bits  plus  any  required  FILL bits plus the EOL bits.  The
minimum transmission times of the total scanning line should
conform to the following:

a.  20 milliseconds recommended standard  with  an  optional
fall-back to the 40 milliseconds option;
b.  10  milliseconds  recognized  option  with  a  mandatory
fall-back to the 20 milliseconds standard;
c.  5  milliseconds  recognized  option  with  a   mandatory
fall-back  to  the  10  milliseconds  option  and the 20
milliseconds standard;
d.  40 milliseconds recognized option.

The  identification  and   choice   of   this   minimum
transmission time is to be made in the pre-message (Phase B)
portion  of  the  T.30  control  procedure.    The   maximum
transmission  time of any total scanning line should be less
than 5 seconds.

# 4. Coding scheme

The  one-dimensional   run   length   encoding   scheme
recommended for Group 3 apparatus is as follows:

a.  DATA
A line of data is  composed  of  a  series  of  variable
length  code  words.   Each  code  word represents a run
length of either all white or all black.  White runs and
black  runs alternate.  A total of 1728 picture elements
represent one horizontal scanning line of  the  document
of  standard  A4  size.   In  order  to  insure that the
receiver maintains color synchronization, all DATA lines
will  begin  with  a white run length code word.  If the
actual scanning line begins with a black  run,  a  white
run  length  of  zero  will be sent.  Black or white run
lengths, up to a maximum length  of  one  scanning  line

CCITT Draft Recommendation T.4                      PAGE   3

(1728  picture elements or pels) are defined by the code
words in Tables 1 and 2.  The  code  words  are  of  two
types:  Terminating  Code  words and Make Up Code words.
Each run length is represented by either one Terminating
Code  word  or  one  Make  Up  Code  word  followed by a
Terminating Code word.

Run lengths in the range of 0 to  63  pels  are  encoded
with their appropriate Terminating Code word.  Note that
there is a different list of code words  for  black  and
white run lengths.

Run lengths in the range of 64 to 1728 pels are  encoded
first  by  the  Make  Up  Code word representing the run
length which is equal to or shorter than that  required.
This  is  then  followed  by  the  Terminating Code word
representing the difference  between  the  required  run
length  and  the  run  length represented by the Make Up
Code.

b.  END OF LINE (EOL)

This code word follows each  line  of  DATA.   It  is  a
unique  code word that can never be found within a valid
line of  DATA;  therefore,  resynchronization  after  an
error burst is possible.

In addition, this signal will occur prior to  the  first
DATA line of a page.

Format: 000000000001

c.  FILL

A  pause  may  be  placed  in  the   message   flow   by
transmitting  FILL.  FILL may be inserted between a line
of DATA and an EOL, but never within  a  line  of  DATA.
Fill  must  be  added  to insure that each line of DATA,
FILL, and EOL exceeds the minimum transmission time of a
total   scanning  line  established  in  the  premessage
control procedure.  The maximum length for a single line
of  FILL  is  5  seconds,  after  which the receiver may
disconnect.

Format: variable length string of 0's.

d.  RETURN TO CONTROL (RTC)

The end of  a  document  transmission  is  indicated  by
sending   six  consecutive  EOL's.   Following  the  RTC
signal, the  transmitter  will  send  the  post  message
commands in the standard T.30 blocked format at the data
rate.

CCITT Draft Recommendation T.4                      PAGE   4

Format: 000000000001 ... ... ... ... 000000000001
(total of 6 times)

CCITT Draft Recommendation T.4                      PAGE   5

Table 1a. Terminating White Codes
Code            Lng     Run
---------------------------
CCITT Draft Recommendation T.4                      PAGE   6

CCITT Draft Recommendation T.4                      PAGE   7

Table 1b. Make Up White Codes
Code            Lng     Run
---------------------------
CCITT Draft Recommendation T.4                      PAGE   8

Table 2a. Terminating Black Codes
Code            Lng     Run
---------------------------
CCITT Draft Recommendation T.4                      PAGE   9

CCITT Draft Recommendation T.4                      PAGE  10

Table 2b. Make Up Black Codes
Code            Lng     Run
---------------------------
CCITT Draft Recommendation T.4                      PAGE  11

Note: It is recognized that machines exist which accommodate
larger   paper   widths   whilst  maintaining  the  standard
horizontal resolution.  This option has been provided for by
the addition of the Make Up Code Set defined as follows:

Table 3. Extended Make Up Codes (Black and White)
Code            Lng     Run
---------------------------
The identification and choice of  either  the  standard
code  table  or the extended code table is to be made in the
pre-message  (Phase  B)  portion   of   the   T.30   control
procedures.

## 4.2. Two dimensional coding scheme

The one-dimensional coding scheme defined in 4.1 may be
extended  as an option to a two-dimensional scheme.  This is
the subject of further study.

# 5. Modulation and demodulation method

It is  provisionally  agreed  that  Group  3  apparatus
operating  on  the  general switched telephone network shall
utilize the modulation scrambler,  equalization  and  timing
signals  defined  in Recommendation V.27ter, specifically in
the preamble and 2, 3, 6, 7, 9 and 10.

The  data  signalling  rates  to  be  used  are   those
recommended  in  Recommendation V.27ter, i.e.  4800 and 2400
bit/s.

Note 1: Some administrations pointed out that it  would  not
be  possible  to  guarantee the service at a data signalling
rate higher than 2400 bit/s.

Note 2: It should be noted  that  there  are  equipments  in
service  using,  inter  alia, other modulation methods.  The

CCITT Draft Recommendation T.4                      PAGE  12

arrangement of interworking between equipment conforming  to
Recommendation  T.4 and these existing equipments is subject
to further study.

Note 3: For higher speed operation, such as may be  possible
on  leased circuits, it is provisionally agreed that Group 3
apparatus may utilize the signals specifically defined in 1,
2, 3, 4, 7, 8, 9, 11, and 12 of Recommendation V.29.
