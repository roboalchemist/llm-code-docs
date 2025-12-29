---
rfc: 338
title: "EBCDIC/ASCII MAPPING FOR NETWORK RJE"
date: May 1972
---
1. The 360 program may be intended to manipulate ASCII text from
the Network.  In that case, the Network user needs to have all
ASCII characters, including the mavericks, uniquely mapped
into EBCDIC in some (standard) manner.

2. The present mapping is convenient only if a user at an AT&T
Model 33/35 Teletype (or simulator thereof) needs a different
mapping for ease of use.

For the first case, we have changed the mapping of the 6 maverick
ASCII characters from "?", using instead Winett's rules III (c) and
III (d):

ASCII             EBCDIC
-----             ------

```
        [                X'AD'
        ]                X'BD'
        {                X'8B'
        }                X'9B'
        ^                X'71'
        `                X'79'

```

For the user with a Model 33/35 Teletype, we have expanded the set of
virtual remote batch terminal types, adding "TTY" to "ASCII" and
"EBCDIC".  A user establishes his virtual remote batch terminal as
type TTY by either doing his initial ICP to socket 15 (vs. 11 for
EBCDIC, 13 for ASCII), or by doing an ICP to Socket 1 and entering
the command "TTYRJS" (vs. "RJS" for EBCDIC, "ARJS" for ASCII).  The
mapping used by NETRJS for a TTY remote is:

Model 33          Corresponding
Graphic               ASCII               EBCDIC
--------          -------------           ------
\                   \                   <bent bar>

<up arrow>            ^                     |

```
    <left arrow>          _                     _

      [                   [                  <cent sign>

      ]                   ]                   X'BD'

```

This is ugly, but it is probably the best we can do.

D. CONCLUSIONS

It is obvious that one pair of translation tables won't do the job;
NETRJS needs (at least) two mappings for each direction.  How long
will it be before an important set of users appears with a different
terminal character set, requiring yet a different mapping? [6] An rje
server site needs to be prepared to provide a variety of translation
tables, and perhaps to allow a user to specify his own table(s); this
mini-subset of "Date Reconfiguration Service" might be necessary to
prevent translation-table-proliferation.  The tendency in Network
discussions has been to put the burden upon the user sites to adapt
to different conventions.  In the real world of users and servers,
the server will often have to do the adapting.

NOTES AND REFERENCES

[1] R.T. Braden, Interim NETRJS Specifications, RFC #189 (NIC
\#7133), July 15, 1971.

[2] Please note that "RJS" is the proper name of a particular rje
package written at CCN the generic name for remote batch
service is "rje".

[3] Notice that the mapping question discussed in this RFC is
significant only for the virtual card reader and printer
connections in NETRJS.  The punch connection is always
transparent, i.e., never translated.  The remote operator
connections use the extended EBCDIC/ASCII mapping including
the maverick characters, but this is not important since
operator commands require only a limited character set.

[4] Joel Winett, "_The_ EBCDIC Codes and their Mapping to ASCII",
RFC #183 (NIC #7127), July 21, 1971.

[5] Winett lists only 88 basic EBCDIC graphics, excluding the
space which he regards as a control character.  This is a
matter of taste, but we find it less confusing to include the
space as a graphic.

[6] CCN recently received a new Teletype-replacement terminal.
This machine has a bastardized graphic character set -- mostly
ASCII, with a sprinkling of both (!) EBCDIC and TTY.

+-------------------------------------+
|                          Full ASCII |
| a b ... z  | ` ^ { }  ~             |
|                                     |
+-----+-------------------------------------+--------------+
|33/35|                                     |   AT&T TWX   |
|     |          `   [   ]                  | (Mod 33/35   |
|     |                                     |      tty)    |
+------+-----+------+-----------------------+      |              |
|Basic |     |      |                       |      |              |
|EBCDIC|     |      |     <SP>              |      |              |
|      |     |   "  |     A B ... Z         |      | <left arrow> |
|      |     |   !  |     0 1 ... 9         |      |              |
|      |     |      |     + - * / ( )       |      |  <up arrow>  |
|      |     |      |     . , ' =           |      |              |
|      |     |      |     $ &               |      |              |
|      |     |      |   < > : ? % # @       |      |              |
|      |     |      |                       |      |              |
|      +-----+------+-----------------------+------+--------------+
|            |      |                       |      |
|            |      |        _              |      |
|            |      |                       |      |
|            +------+-----------------------+------+
|                   |                       |
|                   | PL/1   <bent bar> |   |
|                   |  Set                  |
|                   +-----------------------+
|                           <cent sign>     |
|  Basic EBCDIC                             |
+-------------------------------------------+

Figure 1.  Character Sets Commonly Abused

[This RFC is also available in .PS and .PDF format.]

[This RFC was put into machine readable form for entry]

```
    [into the online RFC archives by Helene Morin, Viagenie, 12/99]

```