---
rfc: 452
title: "TELNET Command at Host LL"
date: February 1973
---
. , : ;
! | ? (cent sign)
SPACE
BACKSPACE
TAB

When a character is mapped into its control code, the control
character is mapped into the code for IDLE.  If the control
character is entered as the last character before the newline key
is entered, the sequence of characters entered is transmitted
without the newline code.  That is, the newline code is not
transmitted when it is preceded by the control character.

When the 2741 keyboard is unlocked for input, characters received
cannot be typed until the keyboard is locked again.  After a line
is entered, received characters can then be typed.  When operating
in full duplex or ASCII half duplex, a null line entered will
allow received characters to be typed but will not cause the new
line code to be transmitted.  To cause a null line, i.e., just the
new line code to be transmitted, the control character should be
entered as the only character in the input line.  In EBCDIC
HALFDUP a null line entered will cause a null line to be
transmitted.

Output:

ASCII output received from the NVT is converted into EBCDIC with
the sequences CR-LF converted into IDLE-NL.  The EBCDIC characters
are then sent to the terminal.  Note that not all 128 ASCII codes
when converted to EBCDIC will print on a 2741.  Of the 95 ASCII
graphics and the 8 ASCII controls which are defined for the NVT
printer, the following are not visible or audible:

BACK SLASH
LEFT BRACE
RIGHT BRACE
LEFT BRACKET
RIGHT BRACKET
ASCII CONTROL BELL (BEL)
ASCII CONTROL VERTICAL TAB (HT)
ASCII CONTROL FORM FEED (FF)
ASCII CONTROL CARRIAGE RETURN (CR)

Figure 6 shows how the EBCDIC codes from X' 40' through X' FF'
will appear on a 2741 terminal.  Figure 7 shows how the EBCDIC
codes will appear when printed with a PN train on the offline
printer and Figure 8 shows how these codes appear when printed
with a TN train.

Controls:

If the first character in an input line is the control character
and the next character is a space, the rest of the line is
interpreted as a TELNET control command.  A control command
consists of a control word and parameters separated by spaces.
Controls are defined which permit TELNET controls to be
transmitted to the serving site, allow input to come from a file
or output to go to a file, allow CMS functions or transient
commands to be issued, redefine the control character or TELNET
mode, close connections or leave the TELNET command with
connections still open, as well as controls to support a reader,
punch, and printer with RJS operation.  The controls are described
below.

CONTROL x

Where x is the new control character

CLOSE

To close all connections and quit

QUIT

To leave TELNET

EBCDIC

To go into transparent mode, i.e., no translation

To translate input and output to network ASCII

Break

To send the TELNET break code

SYNC

To send the TELNET data mark code and an interrupt

AATN

To send a TELNET break and a SYNC

HIDE-YOUR-INPUT

To send the TELNET hide you input code

NOECHO

To send the TELNET noecho code

ECHO

To send the TELNET echo code

CMS command arg1...argN

To issue CMS core resident function or transient command.

INPUT fn ft
*  TERMIN
*  *

To get input from a file If fn is defaulted, input is reset to
come from the terminal.  If fn is * file input resumes after the
last line read.  After an EOF, the next line read will be the
first line of the file.

An external interrupt while input is coming from a file will cause
the line number of the next line to be read from the file to be
typed and input to be reset to come from the terminal.

OUTPUT fn OFF TERM    INPUT    INOUT
*  ON  NOTERM  NOINPUT  OUTPUT

To write output to the file "fn TERMOUT".  If fn is defaulted,
output is reset to go to the terminal.  If fn is *, file OUTPUT is
resumed with the same options as were last used.

For Output to the Terminal:

If the last character is a CR, a line with just the control
character is typed on the next line (with a NL)

If the last character is not a NL or a CR, the line is typed
without a NL (i.e., with TYPE).

For Output to a File:

If just a NL is in the line, just the control character is sent to
the file.

If the last CHAR is not NL or CR, the control character is added
after the last character, except if 130 characters must be sent to
the file.

If the last CHAR is a CR, it is included in the file.

OFF causes all output to be discarded.

ON is the default, and causes output to the terminal.

TERM causes output to also go to the terminal.

NOTERM is the default, and causes output to go the file but not to
the terminal.

OUTPUT is the default and causes just terminal output to be put to
the file "FN termout".

INPUT causes both terminal input but not output to be put to the
output file.

NOINPUT is defaulted and causes input to not go to the file.

PURGE

To purge all output currently received by the NCP.
*****NOT YET IMPLEMENTED*****

READER fn ft
* READER

To send a job to the RJS system at UCLA's CCN.

If fn and ft are defaulted, input will come from the card reader.

PRINTER fn ft
*  PRINTER

To receive printer output from the RJS system at UCLA's CCN.

To receive punch output from the RJS system at UCLA's CCN.

If fn and ft are defaulted, output goes to the printer.

PUNCH fn ft
*  PUNCH

If fn and ft are defaulted, output goes to the punch.

HOST      SITE      MACHINE   SYSTEM      HOST NUMBER
DEC   OCT   HEX

NMC       UCLA      SIGNA-7   SEX         1     1    01
ARC       SRI       PDP-10    NIC         2     2    02
UCSB      UCSB      360/75    OS/MVT      3     3    03
UTAH      UTAH      PDP-10    TENEX       4     4    04
MULTICS   MIT       H-645     MULTICS     6     6    06
SDC       SDC       370/155   ADEPT       8    10    08
HARV      HARVARD   PDP-10    4S72        9    11    09
LL        LL        360/67    CP/CMS     10    12    0A
CASE      CASE      PDP-10    10/50      13    15    0D
CMU       CMU       PDP-10    TOPS-10    14    16    0E
ILLIAC    AMES      360/67    TTS/360    16    18    10
AMES      AMES      B-6500    ?          15    17    0F
CCN       UCLA      360/91    OS/MVT     65   101    41
SRI       SRI-AI    PDP-10    TENEX      66   102    42
BBNA      BBN       PDP-10    TENEX      69   105    45
DMCG      MIT       PDP-10    ITS        70   106    46
RAND      RAND-RCC  PDP-10    TENEX      71   107    47
TX2       LL        TX-2      APEX       74   112    4A
BBNB      BBN       PDP-10    TENEX     133   205    85
MIATI     MIT       PDP-10    ITS       134   206    86

Serving Hosts on the APRA Network
Figure 1

```
                       [[See Figure 2 in PDF file.]]
          Extended Binary-Coded Decimal Interchange Code (EBCDIC)
                                 FIGURE 2

   and

                       [[See Figure 3 in PDF file.]]
          USA Standard Code for Information Interchange (USASCII)
                                 FIGURE 3

   ASCII    ASCII    ASCII    SYMBOLS    EBCDIC    EBCDIC
   DEC      OCT      HEX                 HEX       DEC

     0        0      (00)      NUL       (00)      00
     1        1      (01)      SOH       (01)      01
     2        2      (02)      STX       (02)      02
     3        3      (03)      ETX       (03)      03
     4        4      (04)      EOT       (37)      55
     5        5      (05)      ENQ       (2D)      45
     6        6      (06)      ACK       (2E)      46
     7        7      (07)      BEL       (2F)      47
     8       10      (08)      BS        (16)      22
     9       11      (09)      HT        (05)      05
    10       12      (0A)      LF        (25)      37
    11       13      (0B)      VT        (0B)      11
    12       14      (0C)      FF        (0C)      12
    13       15      (0D)      CR        (0D)      13
    14       16      (0E)      SO        (0E)      14
    15       17      (0F)      SI        (0F)      15
    16       20      (10)      DLE       (10)      16
    17       21      (11)      DC1       (11)      17
    18       22      (12)      DC2       (12)      18
    19       23      (13)      DC3       (13)      19
    20       24      (14)      DC4       (3C)      60
    21       25      (15)      NAK       (3D)      61
    22       26      (16)      SYN       (32)      50
    23       27      (17)      ETB       (26)      38
    24       30      (18)      CAN       (18)      24
    25       31      (19)      EM        (19)      25
    26       32      (1A)      SUB       (3F)      63
    27       33      (1B)      CTL       (27)      39
    28       34      (1C)      FS        (1C)      28
    29       35      (1D)      GS        (1D)      29
    30       36      (1E)      RS        (1E)      30
    31       37      (1F)      US        (1F)      31
    32       40      (20)      SP        (40)      64
    33       41      (21)      !         (5A)      90

    34       42      (22)      "         (7F)     127
    35       43      (23)      #         (7B)     123
    36       44      (24)      $         (5B)      91
    37       45      (25)      %         (6C)     108
    38       46      (26)      &         (50)      80
    39       47      (27)      '        (7D)     124
    40       50      (28)      (         (4D)      77
    41       51      (29)      )         (5D)      93
    42       52      (2A)      *         (5C)      92
    43       53      (2B)      +         (4E)      78
    44       54      (2C)      ,         (6D)     109
    45       55      (2D)      -         (60)      96
    46       56      (2E)      .         (4B)      75
    47       57      (2F)      /         (61)      97
    48       60      (30)      0         (F0)     240
    49       61      (31)      1         (F1)     241
    50       62      (32)      2         (F2)     242
    51       63      (33)      3         (F3)     243
    52       64      (34)      4         (F4)     244
    53       65      (35)      5         (F5)     245
    54       66      (36)      6         (F6)     246
    55       67      (37)      7         (F7)     247
    56       70      (38)      8         (F8)     248
    57       71      (39)      9         (F9)     249
    58       72      (3A)      :         (7A)     122
    59       73      (3B)      ;         (5E)      94
    60       74      (3C)      <         (4C)      76
    61       75      (3D)      =         (7E)     126
    62       76      (3E)      >         (6E)     110
    63       77      (3F)      ?         (6F)     111
    64      100      (40)      @         (7C)     124
    65      101      (41)      A         (C1)     193
    66      102      (42)      B         (C2)     194
    67      103      (43)      C         (C3)     195
    68      104      (44)      D         (C4)     196
    69      105      (45)      E         (C5)     197
    70      106      (46)      F         (C6)     198
    71      107      (47)      G         (C7)     199
    72      110      (48)      H         (C8)     200
    73      111      (49)      I         (C9)     201
    74      112      (4A)      J         (D1)     209
    75      113      (4B)      K         (D2)     210
    76      114      (4C)      L         (D3)     211
    77      115      (4D)      M         (D4)     212
    78      116      (4E)      N         (D5)     213
    79      117      (4F)      O         (D6)     214
    80      120      (50)      P         (D7)     215
    81      121      (51)      Q         (D8)     216

    82      122      (52)      R         (D9)     217
    83      123      (53)      S         (E2)     226
    84      124      (54)      T         (E3)     227
    85      125      (55)      U         (E4)     228
    86      126      (56)      V         (E5)     229
    87      127      (57)      W         (E6)     230
    88      130      (58)      8         (E7)     231
    89      131      (59)      Y         (E8)     232
    90      132      (5A)      Z         (E9)     233
    91      133      (5B)      [         (AD)     173
    92      134      (5C) (cent sign)    (4A)      74  (BACK-SLASH)
    93      135      (5D)      ]         (BD)     189
    94      136      (5E)                (71)     113  (CARAT)
    95      137      (5F)      _         (6D)     109
    96      140      (60)                (79)     121  (GRAVE)
    97      141      (61)      a         (81)     129
    98      142      (62)      b         (82)     130
    99      143      (63)      c         (83)     131
   100      144      (64)      d         (84)     132
   101      145      (65)      e         (85)     133
   102      146      (66)      f         (86)     134
   103      147      (67)      g         (87)     135
   104      150      (68)      h         (88)     136
   105      151      (69)      i         (89)     137
   106      152      (6A)      j         (91)     145
   107      153      (6B)      k         (92)     146
   108      154      (6C)      l         (93)     147
   109      155      (6D)      m         (94)     148
   110      156      (6E)      n         (95)     149
   111      157      (6F)      o         (96)     150
   112      160      (70)      p         (97)     151
   113      161      (71)      q         (98)     152
   114      162      (72)      r         (99)     153
   115      163      (73)      s         (A2)     162
   116      164      (74)      t         (A3)     163
   117      165      (75)      u         (A4)     164
   118      166      (76)      v         (A5)     165
   119      167      (77)      w         (A6)     166
   120      170      (78)      x         (A7)     167
   121      171      (79)      y         (A8)     168
   122      172      (7A)      z         (A9)     169
   123      173      (7B)      {         (8B)     139
   124      174      (7C)      |         (4F)      79  (BAR/OR)
   125      175      (7D)      }         (9B)     155
   126      176      (7E) (broken bar)   (5F)      95  (TILDE/NOT)
   127      177      (7F)      DEL       (07)       7

   ASCII   ASCII   ASCII    TELNET         EBCDIC     EBCDIC
   DEC     OCT     HEX     CONTROLS        HEX        DEC

   128     100     (80)   DATA-MARK        (80)       128
   129     101     (81)   BREAK            (38)        56
   130     102     (82)   NOP              (17)        23  IDLE
   131     103     (83)   NOECHO           (14)        20  RESTORE
   132     104     (84)   ECHO             (23)        35
   133     105     (85)   HIDE-YOUR INPUT  (24)        36  BYPASS

                        ASCII/EBCDIC Code Mappings
                                 FIGURE 4

   EBCDIC                  EBCDIC ASCII

   CENT    (4A) = ESC             (27)   (1B)

   CTL <   (4C) = LEFT BRACKET    (AD)   (5B)
   CTL >   (6E) = RIGHT BRACKET   (BD)   (5D)
   CTL (   (4D) = LEFT BRACE      (8B)   (7B)
   CTL )   (5D) = RIGHT BRACE     (9B)   (7D)
   CTL /   (61) = BACK SLASH      (4A)   (5C)
   CTL "   (7F) = CARAT           (71)   (5E)
   CTL '  (7D) = GRAVE            (79)   (60)

   CTL 6   (F6) = FS              (1C)   (1C)
   CTL 7   (F7) = GS              (1D)   (1D)
   CTL 8   (F8) = RS              (1E)   (1E)
   CTL 9   (F9) = US              (1F)   (1F)
   CTL _   (6D) = US              (1F)   (1F)

   CTL (broken bar) (5F) = DEL             (07)   (7F)

   CTL @   (7C) = NUL             (00)   (00)
   CTL A   (C1) = SOH             (01)   (01)
   CTL B   (C2) = STX             (02)   (02)
   CTL C   (C3) = ETX             (03)   (03)
   CTL D   (C4) = EOT             (37)   (04)
   CTL E   (C5) = ENQ             (2D)   (05)
   CTL F   (C6) = ACK             (2E)   (06)
   CTL G   (C7) = BEL             (2F)   (07)
   CTL H   (C8) = BS              (16)   (08)
   CTL I   (C9) = HT              (05)   (09)
   CTL J   (D1) = LF              (25)   (0A)
   CTL K   (D2) = VT              (0B)   (0B)
   CTL L   (D3) = FF              (0C)   (0C)
   CTL M   (D4) = CR              (0D)   (0D)

   CTL N   (D5) = SO              (0E)   (0E)
   CTL O   (D6) = SI              (0F)   (0F)

   CTL P   (D7) = DLE             (10)   (10)
   CTL Q   (D8) = DC1             (11)   (11)
   CTL R   (D9) = DC2             (12)   (12)
   CTL S   (E2) = DC3             (13)   (13)
   CTL T   (E3) = DC4             (3C)   (14)
   CTL U   (E4) = NAK             (3D)   (15)
   CTL V   (E5) = SYN             (32)   (16)
   CTL W   (E6) = ETB             (26)   (17)
   CTL X   (E7) = CAN             (18)   (18)
   CTL Y   (E8) = EM              (19)   (19)
   CTL Z   (E9) = SUB             (3F)   (1A)

        EBCDIC                   EBCDIC ASCII

   CTL 1 (F1) = BREAK          (38)  (81) - CIRCLE C
   CTL 2 (F2) = NOP            (17)  (82) - IDLE
   CTL 3 (F3) = NO ECHO        (14)  (83) - RESTORE
   CTL 4 (F4) = ECHO           (23)  (84)
   CTL 5 (F5) = HIDE YOU INPUT (24)  (85) - BYPASS

   DATA MARK (80) CANNOT BE ENTERED FROM THE KEYBOARD

   THE FOLLOWING 2741 KEYBOARD CHARACTERS DO NOT
   HAVE A MEANING AS A CONTROL:

         $ # * % &
         + - = _
         . , :
         ! | ? (cent sign)
         SPACE
         BACKSPACE
         TAB

                    Keyboard Control Character Mappings
                           FIGURE 5 (CONTINUED)

   [[See Figure in PDF file.]]
   Hex Code X'xy' for Characters on a 2741 Terminal

   [[See Figure in PDF file.]]
   Decimal Code D 'xxy" for Characters on a 2741 terminal

   HT  X'05' = D'005' Horizontal Tab
   LC  X'06' = D'006' Lower Case
   RES X'14' = D'020' Print Restore
   NL  X'15' = D'021' New Line
   BS  X'16' = D'022' Back Space
   IL  X'17' = D'023' Idle
   BYP X'24' = D'036' Print Bypass
   LF  X'25' = D'037' Line Feed
   UC  X'36' = D'054' Upper Case

   Hex Code X'xy' and Decimal Code D'xxy' for 2741 Control Codes

   [[See Figure in PDF file.]]
   Hex Code X'xy' for Characters on the PN train

   [[See Figure in PDF file.]]
   Decimal Code D'xxy' for characters on the PN train

   [[See Figure in PDF file.]]
   Hex Code X'xy' for Characters on th TN train

   [[See Figure in PDF file.]]
   Decimal Code D'xxy' for Characters on the TN train

          [This RFC was put into machine readable form for entry]
     [into the online RFC archives by Helene Morin, Via Genie,12/1999]

```