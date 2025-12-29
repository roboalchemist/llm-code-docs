---
title: "From a programming language point of view, this concept is similar to the UNCCL"
---

# Introduction

In this paper an attempt is made to specify a high level progratming language
for computer networks, and more specifically the ARPA network. The main con-
cept introduced.is the one of an abstract Network Machine, which is consistent
with the idea of a HOST asking a service from the computer network considered
as an overall camputing facility. The dialogue is always between a HOST ard
the Network Machine which language is always the same, though its configuration
may vary accordirg to the real remote HOST.

From a programming language point of view, this concept is similar to the UNCCL
proposed in 1958 [STRO58}] but never implemented, however; the application to.a
computer network implies a realtime interaction between programs. Also, the
possibility for the user to use NIL either in a standard mode or in an extermled
mode where he defines himself his own entities should give to NIL a maximm of
flexibility.

# 1. Basic concepts introduced in NIL

## 1.1. Aim of NIL

The two main cbjectives of NIL are:

a) to describe the envirorment in which a program is executed
(its complement ))} this involves the description of:

- data formats and data structures

- exchanges with input and output devices and characteristics
- expected fron then .

- interface with operating systen

b) to express the front end part of an interactive systen:

The data flow through an interactive systen generally decreases
as the data reaches the kernel of the system: it is assumed
that in many interactive systems a separable module exists or
can be defined which involves a great amount of data exchanged
with the user, and much less exchanged with the rest of the
system. This module is called Front-Frd. It is important that
the response time of the system is affected as little as possible
by additional transmission delays. Also, it is desirable to
keep the data rates as low as possible on the network.

It is assumed that the transfer of a Front End does not imply to solve the
whole problem of program transferability.

~ Network Working Group M. Elie
Request for Caments #51 4 May 70

1.2

1.2.1

1.2.2

1.2.3

NIL subcategorization

As pointed out by S. Volansky [ ] it's convenient to divide languages
in several sublanguages corresponding to their main functions. NIL is
thus. subdivided in:

- a control sublanguage

an operation sublanguage

a data declaration sublanguage
- an environment sublanguage

Control sublanguage

The control sublanguage states WHEN a computation is done: It describes
the flow of control or ordering of the computations. With some infor-
mation contained from the other sections of the language, it also states
WHERE the computations are to be executed,

As a computer network introduces loose connections between several systems,
the control language of the Network Machine should be able,in an elaborate
version, of assigning computations to available processors, taking into
account the time delays and resource allocation problems involved. It is
not our purpose to consider this level at the moment.

Operation’ sublanguage

The operation sublanguage describes the operations to be performed on the
data without indication of the sequencing between operations, it answers
to the question of HOW an operation is performed. The operations are sub-
divided into two groups.

~ a canputation group
- a data manipulation group

The later is the most important part of NIL since its main purpose is the
transformation of data structures and patterns.

Data declaration sublanguage

The data declaration sublanguage is necessary to declare the variables
and data structures on which operations are performed.

The possibility is given to build structures of atcmic elements called
beads. NIL provides a standard set of beads used in the "standard mode";
in the "extended mode" a user may define new beads and new structures of
them.

Network Working Group : . . M. Elie
Request for Comments #51 : i 4 May 70

### 1.2.4. Envirorment sublanguage

The environment sublanguage expresses the context in which a program
expects to operate; expected characteristics of the peripherals,
semantics of the exchanges with the outside world through a particular
operating system. .

Thus a complete "program descriptor" will contain four distinct sections:

envirorment section
data declaration section
control section
operation section

The identification section is anitted because it corresponds to the log
in and socket grabbing part of the initialization procedure.

\

## 1.3. The Network Machine

One fundamental concept in NIL is that of an abstract Network Machine
which has the following characteristics:

- an infinite memory: there is no problem of menory allocation
or garbage collection in this machine. But as an item must be
accessible, it must still have an address.

- variable word length: a word may be considered as the smallest
intelligible and addressable item of data. The atomic element
called bead is in fact the machine word. The structure and

length of each type of beads are expressed in the data defini~
tion sublanguage.

As presented on figure 1.3.1, one HOST KS Network
only communicates with a Network Mach- HOST Machine
ine which may operate in two modes.

figure 1.3.1

- standard mode where the beads sy Fkepase
their structures,and the alldwed transformations on them are
standard and need not to be redefined: standard beads and
structures are knowm of every HOST

- extended mode where in addition to or instead of the standard
data definitions and manipulation, a HOST may specify new beads
structures and transformations. The extended mode allows the
user to define his om machine as the Network Machine. This is
then equivalent to the modes MY LOCAL, YOUR LOCAL proposed
in REC #42 by Ancona. If the definition of a name has not been
altered the standard definition is assumed.

Network Working Group M. Elie
Request for Comments #51 4 May 70

The data definition sublanguage is as well used for the purpose of document-
ing the set of standard beads.

The instruction set of the Network Machine stands at a high level per-
mitting global transformations of data structures. °

The envirorment of the Network Machine is determined by the subset of
the envirorment of the server's HOST which is used by the program in
execution; the systen HOST-Network Machine can take two main configura-
tions shown in figure 1.3.2.

a) The Network Machine stands for the user of a
program provided by the HOST (server HOST)

user peteork b) The HOST machine is the user of a program
HOST | (server) provided by the Network Machine.
The server machine assigns its hardware environ-
ment to the user machine. This choice is made
so that programs can be remotely used without
being modified; it is up to the user of a remote
Network server program to adapt himself and his own envirorment.
Machine HOST
(user) Thus, when the Network Machine is server, it
defines the Data Definition and Environment
figure 1.3.2 sections.

a Network Working Group
Request for Comments 751

1.4

Implementation

M, Elie

# 4. May 70

The data and environment definition sublanguages should be able to
HOST description Network Machine

describe as well envirorment and
data in HOSTs as data in Net-
work Machine. At the limit
it should enable two programs
written in different languages
to communicate,

as long as the data

: representation they use are

expressible in the data de-
scription sublanguage.

In each HOST will be
implemented a "generator"
which will accept rules
describing the HOST data
structures and environ-
ment and will generate
an adequate translator
to translate then in
Network Machine format,
as shown in the figure
1.4.1.

Once the network machine
standards will be settled

~it seems valuable to think

about emulating the tran-
slator using a micropro-
gramed unit which would

be either added to the
Host or rather to the IMp"
thus avoiding the load of
a translation which may
involve lengthy operations
on the bit level - (Figure
1.4.2.)

= -(description
T non standard mode)
Network Machine
/ standard mode

>

/
/ GENERATOR l
/ |
|
/ |
: t
/ .
Data in TRANSLATOR |_D2ta is L
sora ‘Or Network Machine
format
figure 1.4.1
Network
HOST < Machine
Figure 1.4.2

Network Working Group M. Elie
Request for Comments #51 : . 4 May 70

2.

2.1

2.2

Data definition sublanguage
Fields

All communications with the Network Machine are done using
strings of bits: these strings of bits, also referred to as
messages are parsed by the receiving HOST to reconstruct inside
its memory the data structures in its own memory and code.

Bits are grouped into significant fields: a field is a group
of bits having definite contents. “It may contain:

a) an element of data (data field)

b) some bit pattern specifying environment parameters
¢) ‘a pointer

a) the identification of same other fields.

The method to describe the formats of beads is derived from
the method of description of a binary message suggested in
RFC #31:

a) each field is declared with its name and length in
number of bits.

b) commonly used fixed values of a field that correspond
‘to a special meaning, may be given names.

¢) legal ways of concatenating fields are initiated by
rules; when only certain fixed values of a field are
allowed, they may be either specified by their
valve or by the corresponding name.

Data beads.

Data fields (type (a)) are concatenated to form data beads:
a bead is an indivisible atomic unit of data.Used as
building element of any data structure to be transmitted
between HOSTs and Network Machine. A bead is the smallest
unit of data that can be referenced.

The legal ways of forming a bead by concatenation of several
fields are indicated in a construction rule. Beads have a
fixed length and an unambiguous structure. In real machine
beads are usually defined as an integer number of contiguous
registers. This constraint does not apply here, though it
may turn out to be more efficient to favor HOSTs with, for
instance, 32 bit.words, and 4 bytes per word, which are the
most common word structure on the ARPA network. *

Data beads may be considered as the operands of the language
in which fields of type (b) and (c) would be operators.

Network Working Group M. Elie
Request for Conments #51 4 May 70

2.3

2.3.1

Control fields

The way data beads are linked oreto the other and the environ-
ment in which they operate are specified by additional control
fields which cannot be referenced and are operators on or
identifiers of the following string of beads, or linkage
between individual beads.

The scopé of a control field may as well be all the beads or
substructures of a structure, if it is specified at the level
of the head of the structure. To be more precise, two kinds
of structures of beads must be defined: homogeneous and
heterogeneous structures.

A structure is defined as hanogeneous if both a unique type
of bead and a fixed parameter environment for the whole
structure is specified at the head of the structure.

A structure is defined as heterogeneous if at least one of
the following conditions is true,

- different types of beads are used for building the
structure

~ the envirorment in which lie the beads of the structure
is changing within the structure.

Five main control fields need to be defined.

a) MODIFY

b) . FLAG

c) POINTER

@) IDENTIFICATION
e) PARAMETER

MODIFY field

The MODIFY field is a one bit field preceding every bead of

a heterogeneous structure: it is a flag set when followed

by one or several control fields of type b, d, or e, which aim
at modifying either the environment of data beads or their
type. This field has the value:

# 1. iff the attached data bead type and its environment do

not change

0-if the attached element is a control field or a
sequence of control fields of type b, d, or e specify-

ing a change in type/or environment of following data
beads. :

Network Working Group M. Elie
Request for Comments #51 4 May 70

### 2.3.2. FLAG field

When set, the MODIFY field is immediately followed by an 8
bit FLAG field indicating which of the IDENTIFICATION and
several possible PARAMETER fields are present; when set to
one each individual bit means the following:

bit number
0 ' IDENTIFICATION field present

# 21. first parameter field present

# 2. second parameter field present

# 6. sixth parameter field present

-7 next: field, is another FLAG field

for same more parameters (in case
| more than 6 parameters may be
‘attached to a bead environment).

### 2.3.3. POINTER field

The number and nature of pointers to be attached to each bead
depends on the structure definition. A given list structure
may need one forward pointer. A ring structure may use an
additional pointer to the first element. The necessary
linkage between beads are defined in the structure definition
thereafter the necessary pointer fields autcmatically added to
each data bead. A bead is referenced within a structure by

an address relative to the head of the structure. Thus a

# 16. bit pointer field should be fully sufficient to contain

this address.

### 2.3.4. IDENTIFICATION field

The IDENTIFICATION field is an 8 bit field which identifies a

bead type among the list of defined bead types. Standard bead
types are numbered from zero up and non~standard bead types are
numbered from 255 dom. The non-standard types nunbering is
special to each server program or to a set of server prograns.

The IDENTIFICATION fields follow a MODIFY field of value 1 when-
ever the bead type has not been defined all over the structure

in the structure root. Identification fields are also used at

the level of the head of the structure to specify the type of
identical elements (beads or structures) used within this structure.

### 2.3.5. PARAMETER field

The PARAMETER field gives the list of the environment parameters

in which the following string of data beads lies. A PARAMETER
field is specific of a bead type; it directly follows the MODIFY
field when there is no arbiguity or the type of the next data beads.

Network Working Group M. Elie
Request for Conments #51 4 May 70

Example: ‘the paranter field of the standard bead BEAMMVT
will contain the following fields.

a2 bit field indicating the type of movement generated

# 00. do not display Trove the beam

/ 01° © display final point point.

# 10. display vector : vector

# 11. unused

- a4 bit field indicating beam intensity, by a number
fron 0 to 15, 0 meaning a null intensity, and 15 the
maximum possible intensity.

# 7. al bit field for blinking

# 0. off

loam

al bit field for light pen sensitivity

# 0. off ;

# 1. on

## 2.4. Metalanguage definition

A COBOL - report like meta language is used in the examples
because of its readibility, as well in the beads as in the
structure definitions.

Symbol Meaning
+ . concatanation
{ } choice
{ ] : optional choice
¢ pis i pusnse repetition

# . 1 lower bound on the

number of identical
items; if omitted 1
is assumed to be 0.

u upper bound on the
nunber of identical
items; if omitted u
is assumed to be »,

‘a number alone means: exact
number of repetition,

Network Working Group M. Elie
Request for Comments #51 4 May 70

Cs
-

2.5
2.5.1

label for further use within the same rule

assignment

conditional alternative

grouping ,

indicates a special value given to the following field name

plus
minus

Proposed standard beads
Alphanumeric beads
Character: CHAR

A character is composed of one eight bit field (which has the
same name). Many special patterns, corresponding to currently
used special characters are defined; they are indicated in
table 2.5.1, as well as some subsets of CHAR. The basic char~
acter code is declared as standard ASCII

: standard EBCDIC
or by the name CODE
followed by the 128 characters in this code corresponding to
the 128 ASCII characters. If no code declaration is specified,
the ASCII code is assumed by default.

- Number representation

Normally the kernel of a program stays in the server's HOST
and the user's HOST should have no arithmetic operations to
perform on the data. In this case, the principles involved
in the arithmetic unit conception of a HOST do not need to
be described. But the fomnat of fixed and floating point
numbers has to be described.

~- in thé case when user and server HOST's have the same
nunber representation,for instance the standard
representation,the transmission of data in their
number representation reduces the data flow between
then.

- if the server HOST has a different number representation

than the standard representation, depending on the data
transmitted, there are two alternatives:

Network Working Group M. Elie
Request for Camments #51 4 May 70

+ the numerical data is exchanged as decimal numbers in the
standard code

+ the fixed and floating point format are defined to the
Network Machine and the user HOST performs

either a'direct transcoding fran the server binary
representation to decimal representation and vice
versa.

or a transcoding from the server binary representation
to its om binary representation and vice versa.

As most of the numbers exchanged are to be printed in decimal or
are given as decimal input, it is felt that when there is incompati-

bility between binary representations of corresponding HOSTs,
exchanges in decimal representation would be the easiest.

Thus are defined:

a) \Number in decimal representation which is not a bead but
a string of characters (see 2.3.1)

b) Fixed point numbers single precision FXPNUML
double precision FXPNUM2

Field definition BYTE 8 SIGN 1
SBYTE 7

FXP NUM1<-SIGN + SBYTE + {pyre}?
FXP NUM2<—FXPNUM 1 + = © {Byrn}

c) Floating point numbers single precision FLPNUML
double precision FLPNUM2

FLP NUM1 <— SIGN + SBYTE + {pyre}?
FLP NUM2<— FLPNUML + (ayre}4

This only expresses the syntax of the floating point number.
The semantics should say: in FLPNUML

SIGN is the sign of the numker of format {evre}? which is
the mantissa

SBYTE is the exponent, and its value is based by a value
of 416 to insure positive exponents. In fact, FXPNUML

and FLPNUM1 differ by their semantics,

Network Working Group M. Elie
Request for Camments #51 . *4 May 70

These properties will be expressed by special field
definition:

_EXP £~ SBYTE @ '40H'SBYTE
Manr <—- SIGN @ {Eyre}?

and a floating point number is defined as:
FLP = Mant 22?

Network Working Group M. Elie
Request for Camments #51 4 May 70

# 1. Special Characters

Transmission Control Characters

SOH
STXx
EIX
For
ENQ
ACK
DLE
NAK
SYN
ETB
ESC

Printer Control Characters

'OX1' CHAR

horizontal tabulation HT +

vertical tabulation VI + ‘OBX' CHAR

new line NL + ‘OAX' CHAR

end of message EQM + '08X' CHAR
Teletype Control Characters

Carriage return CR oan “ODX!* CHAR

shift out so coal ‘OEX' CHAR

shift in - Sl + ‘OFX' CHAR
: BS 7

Device Control Characters
pel
pc2
vc3
pe4

Table 2.3.1

Network Working Group M. Elie
Request for Caments #51 4 May 70

# 2. Subsets of Characters

Numeric characters 'r1st
NUM + . CHAR
Printable characters NUM
ALPH
PRCHAR + - CHAR

in colum CHAR

Intermediate characters ‘(characters !'
ITCHAR + é

Final Characters

FIN CHAR + CHAR ©) ITCHAR
Transmission Control
Characters* ‘(NUL)' CHAR
TRACHAR + . \
Derra Control Characters ven? Teletype control character
DCCHAR to ‘-DCl)' CHAR TYCCHAR cRo
~ pc2 sO fa
DC3 si \
DC4 .
Alphabetic characters nr an
Printer Control ~
Characters HT)
vr
PCCHAR + we { CHAR
EOM /

Table 2.3.1: Special ASCII characters and groups of ASCII
characters.

*gee USACII standards

Network Working Group M. Elie
Request. for Caments 751 4 May 70

2.5.2: Graphic Beads

As proposed in RFC #5 by J. Rulifson, the screen of any graphical
display is taken to be a square; the coordinates of points are
nomalized fron ~1/2 to +1/2 on both axes. The position of the
first point of a structure is determined by the deflection fram
the origin which is the rest point of the beam; following points
are determined by their deflections (AX,AY) fran the last beam
position. |

Thus, only two data fields need to be defined:

DEFLECTION which is a 12 bit field: the deflection is
defined by a number between - 1 and +1 with
the precision usual to the server.

ANGLE which is a 15 bit field defining an angle from 0
to 2M in radians between the horizontal axis and
an axis passing through the origin. The first bit
of it indicates if the angle must be taken clock-
wise or counterclockwise.

The data beads are:

MOVE

Depending on the parameters which are set when this bead appears,
MOVE may specify:

- an invisible movement of the beam; in this case the beam
intensity is null

- anew point: in this case the beam intensity is on only
when the beam has reached the new point.

~ avector: in this case thebeam intensity is set to a certain
non zero value

MOVE « {DEFLECTION}?
Arc of circle: ARC

An arc of circle is defined by its center, followed by its start-
ing point and the angle of its ending axis.

ARC + (DEFLECTION) “4ancrE

Network Working Group . M. Elie
Request for Camments #51 4 May 70

2.6
2.6.1

2.6.2

Proposed parameter fields.
Character strings. ;

In character strings sane of the control characters are really
parameter fields: they act as an operator on the following
string of characters. i.e.:

lower shift
upper shift
new line
escape

But as the code and use of these characters are determined in

the standard codes, they are not included in parameter definition.
It may be taken advantage that these characters are in the two
left columns of the ASCII or EBCDIC standard code: they correspond
to codes with the first three bits null in EBCDIC and the first
two bits null in ASCII.

Graphics parameters

The following parameter fields are defined:

scale SCALE 4

beam intesity Int 4
light pen sensivity SENS. + SWITCH
blinking BLINK + SWITCH
beam BEAM + SWITCH

2.7

2.7.1

SWITCH is.a 1 bit field which may take the values:

ON <-'1' = SWITCH
OFF <-'0' SWITCH

A switch parameter stays ‘ON, as long as it is not reset to
OFF.

The beam intensity is expressed by a number from 0 tol. 0 is
black and 1 as light as the display can go. Numbers in between
specify the relative log of the intensity difference. BEAM
permits to switch the BEAM on or off without changing the
Current INT parameter.

Structures

Structure definition.

The structure definition consits mainly in the specification of
the topological relations between data beads:

- sequential relations; no pointer field necessary
- links through a number of pointers.

Network Working Group M. Elie
Request for Comnents #51 4 May 70

2.7.2

2.8

2.8.1

Standard structure type.
Two basic standard structure types are chosen

VECTOR to represent sequence of data beads (strings, arrays,
tables...)

PLEX. to represent any kind of directed graph, tree, ring...)
VECTOR (C;N,. +N) * VECTORHDR + VECTORBODY

VECTORBODY*+ (=C#1: {defined bea} + [VECTORBODY]

VECTORHDR *'VECTOR' IDENTIFICATION + C + Ny +... 4N
Cis the number of parts (colums) in the vector? 1 Le part hav=
ing Ne elements.

It is also probably interesting to define a compressed vector
COMPVECTOR in which sequence of the identical elenents*are trans-
mitted as 1 element +a special bead + the number of identical
elements in sequence.

PLEX (M)
The first bit of a pointer field indicates if the pointer points

to a teminal element or not. If it is the case, forward
pointer fields are not added to the data element,

M is the number of data elements in the structure.
Objects
object definition.

An object is defined by a semantic rule including, on the right
hand side a name to identify the object
a set of parameters of the object definition.
operands: name of thebeads used as data elements
on the lef .
hand side i parameter fields
structure of the data beads,

i.e. The definition of a new object called SQUARE is: SQUARE “~
(A,LA8) ROTUXANGLE€) (VECTOR(1,4) (BEAM'OFF'+

MOVE (A) + BEAM 'ON' + MOVE (0, Ly) + MOVE (L,0) +

MOVE (0,€L) + MOVE (€%.,0))

Where ROT refers to a transformation defined in the data manipul~
ation language, and VECTOR is defined as a stardard structure.

Network Working Group . M. Elie
Request for Carments #51 4 May 70

2.8.2

The identifier of the ew structure is SQUARE

“The structure type used is VECTOR with dimension 1 and 4 elements

The elements of the VECTOR are standard beads MOVE
The parameters are A, L, and AG
Parameter fields BEAM 'OFF' and PEAM 'ON' are used.

Alphanumeric standard objects.
Compressed character string (COMSTRING)

ie
COMSTRING < VECTOR (1) ( [PRCHAR]”™ + “mao ) .
VIENUM EOF)
ESCHCI
NL
FOP

A compressed string of characters is any number of times a
string of any number of printable characters followed by one of
the following characters

- horizontal tabulation followed by the number of correspond~
ing blanks to be added

- vertical tabulation followed by the mmber of lines to
be skipped. .

- escape followed by any character

~ new line
- end of page

The compressed string is ended by an EOF character.

- Code table (CODE) 128
CODE<-VECTOR (1;128) CHAR)

CODE is the name of the translation table assumed for a given
program. When defined by the user, he must give fram

column 1 to column 8 the 8 bit pattern equivalent to the
corresponding ASCII code. :

18.

Network Working Group M. Elie
Request for Comments #51 4 May 70

- Binary card image
B CARD ¢VECTOR (1;120) {cur} 320

Packed decimal number HNUM 4 bits field

A x} ‘fo xu}!
c Xx '
t
peteney © ENUM «PNM €— jf , ENUM
BX oH
DX
lénl
pow ¢— {ovat + DSIGN

- Decimal mmber (unpacked or zoned
_, Wne3h
peut ¢— {xuM} + D sien pom

‘19
