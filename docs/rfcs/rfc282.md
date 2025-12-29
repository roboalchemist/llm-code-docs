---
rfc: 282
title: "The second Network Graphics Group Meeting was convened at the"
date: December 1971
---
1.  There shall be a "virtual screen" and a Standard Graphics
Stream.

2.  The origin is in the center.

3.  Coordinates are signed, 2's complement fractions (-.5 to
+.499).

4.  The Standrd Graphics Stream will consist of 8-bit bytes
initially, coordinates are two bytes. ( A "set coordinate size"
operator will be introduced if and when needed.)

5.  Network ASCII will be used for text output, with default to
upper case where necessary.  Control characters are, for the time
being, site specific.

6.  Where appropriate, operators shall have "absolute,"
"relative," and "local" (to a subpicture) modes.

7.  The protocol will be organized on a "levels of complexity"
basis, with level 0 comprising operators for simple picture
drawing, level 1 comprising operators for one level of subpicture
definition ("macros", or loosely, "subroutines") and level 2
comprising "viewport" and "window" type operators.

Note that the discussion dealt specifically with graphics OUTPUT.
The Protocol Committee was also empowered to prepare recommendations
for an input-side protocol, but first priority is to be attached to
the formulation of an acceptable output-side protocol.

OPERATORS

As the Protocol Committee's draft is not immediately available, the
following list of low-level operators (the syntax and semantics of
which were discussed at length during the meeting) may be of interest
here:

1. Erase and reset to origin.  This operator causes the screen to
be erased and the beam to be positioned at the 0,0 (virtual screen
center) point.  A new picture is started.

2. Move.  No line is drawn the beam is positioned to the specified
x, y position.  There are specific operators for "move relative",
"move absolute" and "move local" modes.

3. Draw.  A line (of the current "linetype" -- see 5, below) is
drawn from the present beam position to the specified x, y
position.  Modes are as with move.  Treatment of the "off-screen"
condition is at the displaying host's option.

4. Point.  Display a point at the specified position.  Modes are
as with move.

5. Line type.  Draw lines of the specified type until further
notice.  Currently defined types are solid (0), dashed (1), dotted
(2).  If a requested type is not implemented, default to the
next-lower-valued type.  After an "erase", type is solid until
changed.

6. Line intensity.  Requests line intensity to be as follows: 0 =
off, 128 = normal, 255 = brightest, intermediate values = map
appropriately.  After an "erase", intensity is normal until
changed.

7. Text.  Cause display of a specified number of specified (Net
ASCII) characters.  There are specific operators for "return beam"
after last character (to position before text display) and "leave
beam" (wherever it ends up).  Size is to be whatever the
displaying host considers "normal".  Treatment of "right-hand
margin" and ASCII controls is host-specified at present.  (A
character size operator may be specified later.)

8. Escape.  If the console is  of specified type, pass a specified
number of bytes directly to it.

Operators for viewports and subpictures were also discussed.
Bouknight and Kelly prepared an BNF treatment of all points
discussed, which will appear in the Protocol Committee's draft.

OTHER BUSINESS

The remaining technical discussion dealt with graphic input, on a
rather general level.

Michener extended the attendees' thanks to Andy Moorer for having
hosted the meeting.

Cotton volunteered to host the next meeting at Mitre, Washington, in
mid-April, at which time we hope to have had enough experience with
the connection protocol and first-pass output protocol to agree on a
"final" statement of them, and to have done enough thinking about the
input side to specify a first-pass protocol for it (unless the
Protocol Committee manages to do so first)

APPENDIX - LIST OF ATTENDEES

Marshall Abrams, Ntl. Bureau of Stds.

Jack Bouknight, U. of Ill.

Jackson T. Cole, Rome Air Development Ctr.

Ira Cotton, MITRE

Daniel Debrosse, UTAH

Eric Harslem, RAND

Karl Kelly, U. of Ill.

David Liddle, Owens Illinois

John Melvin, SRI

Ed Meyer, MAC

James Michener, MAC

James Moorer, SAIL

Hamid Naficy, UCLA

Mike Padlipsky, MAC

Ken Pogran, MAC

Jon Postel, UCLA

Jerry Powell, MITRE

Jean Saylor, SDC

Ron Stoughton, UCSB

Elaine Thomas, BBN

Howard Wactlar, Carnegie-Mellon

Bill White, SUHP

[This RFC was put into machine readable form for entry]

```
     [into the online RFC archives by Kelly Tardif, Viag�nie 10/99]

```