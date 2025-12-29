---
rfc: 553
title: "Draft design for a text/graphics protocol"
date: July 1973
---
..., Xn,Yn)

Replaces the unit by a line unit.

Errors: Subpicture does not exist illegal mode; some X or
Y is outside the subpicture.

DOT-UNIT(Subpicture,Unit,Target-Key,Type,Mode,X0,Y0,X1,Y1, ...,
Xn,Yn)

Replaces the unit by a dot unit.

Errors: Subpicture does not exist; illegal mode; some X or Y
is outside the subpicture.

SPECIAL-POINTS-UNIT(Subpicture,Unit,Target-Key,Type,Mode,X1,Y1,
..., Xn,Yn)

Replaces the unit by a special-points unit.

Errors: Subpicture does not exist; illegal mode; some X or Y
is outside the subpicture.

RFC 553        Draft design for a text/graphics protocol    14 July 1973

CALL-UNIT(Subpicture,Unit,Target-Key,Called-
Subpicture,Parameters)

Replaces the unit by a call unit.

Parameters:

Master-Instance rectangles

rotation

mode

Errors: Subpicture does not exist; Called-Subpicture does
not exist; parameter errors.

TTY-UNIT(Subpicture, unit, mode, rectangle, lines)

Creates a unit which will behave as a tty-simulation area
with "lines" lines distributed within the specified
rectangle.

Errors: Subpicture does not exist.

DEVICE-SPECIFIC-UNIT(Subpicture, Unit, Target-Key, device,
commands)

Creates a unit of device specific commands.  The action of
the commands should leave alone (or at least restore) any
global modes, e.g., the standout mode (see below).

APPEND-STRING-TO-UNIT(Subpicture, Unit, Text)

Appends the specified text to the specific commands.  This only
makes sense if the specified unit is a string or tty unit.

Errors: Subpicture does not exist, unit does not exist, not a
string or tty unit.

DELETE-UNIT(Subpicture, Unit)

Deletes a unit.

RFC 553        Draft design for a text/graphics protocol    14 July 1973

VISIBLE-UNIT(Subpicture, Unit, Flag)

Makes the Unit visible or invisible as specified by Flag.  If a
unit which is target sensitive is made invisible, it is no
longer target sensitive.  However, in the absence of a
subsequent modifying target sensitive command, the unit becomes
target sensitive again if it should be made visible.

Errors: Subpicture does not exist, unit does not exist.

SET-TARGET-KEY(Subpicture, Unit, Target-Key)

Sets the target key for the specified unit to the specified
value.

SET-STANDOUT-MODE(mode)

Sets the mode that will be used to make text and/or units stand
out to blinking, underlining, etc.

If the terminal does not support the specified mode, the
terminal should make a best effort or use another method to
make things stand out.

STANDOUT-UNIT(Subpicture, unit, yesno)

makes the specified unit stand out (according to the mode set
by SET-STANDOUT-MODE) or not, according to "yesno".  If the
unit which is to stand out is a call-unit, the instance of the
subpicture which is the result of the call (all the way to the
terminal nodes) is made to stand out.

STANDOUT-TEXT(Subpicture, unit, begin-char-count, end-char-count,
yesno)

Unit must refer to a string unit.

Makes the specified text stand out (according to the mode set
by SET-STANDOUT-MODE) or not, according to "yesno".

UPDATE-STRUCTURED-DISPLAY()

This causes any changes that have been made to the display
file, since the last update or since ICP, to be reflected on
the screen.

RFC 553        Draft design for a text/graphics protocol    14 July 1973

TTY(parameters)

parameters are:

position rectangle, visible/invisible, number of lines, mode
of characters

This refers to the ICP TTY simulation

USE-TTY-UNITS(Subpicture1, unit1, ..., Subpicturen, unitn)

Unescorted characters are to be appended only to the specified
tty units.

Errors: Subpicture, unit does not exist.

RESET(How)

Case How Of

=  Permanent

Immediately resets the terminal to its initial ICP state

=  Temporary

Immediately resets the terminal to its initial ICP state
without destroying the previous state.

=  Restore state saved from last RESET(Temporary).

Direct Feedback

It seems extremely desirable, given network speeds, to allow the
using host to perform direct feedback to the user without
intervention from the application program in the serving host.  This
is already done in telnet with local echoing.  We propose extending
this capability to graphics by allowing "dragging" (attaching a
subpicture's origin to the position of the cursor), "tracking"
(following the movement of the mouse, stylus, or light pen with a
distinctive mark on the screen), "inking" (plotting the trail of the
cursor on the screen) and "rubber banding" (a straight line attached
to a fixed point on one end the cursor location on the other).

These should be seen as allowable extensions of the protocol rather
than as requirements.  There should, however, be commands available
in the protocol for determining their existence and controlling them.

RFC 553        Draft design for a text/graphics protocol    14 July 1973

Data input primitives

Input Control

TARGET-SENSATIVE(key1, ..., keyn)

Arms the units which have the specified keys for target
selection.

SET-INPUT-MODE(Device, parameters)

Selects the mode in which a logical device shall produce input
and under what conditions.

the logical devices are specified below as well as their
possible input formats and conditions.

Errors: no such device.

Keyboard input

The keyboard has only one input mode, in which it sends a
character whenever a key is struck.

Binary devices

Unless otherwise specified, binary devices act as an extension of
the keyboard and produce 8-bit characters which are not
distinguishable from keyboard characters by the serving host.

The algorithm for translating binary devices into characters is
not specified, but something like the NLS accumulation
algorithm for mouse-keyset chords is intended.

Binary devices may also input binary data (according to their
up/down states), which is transmitted on state changes.  Examples
of this type of device are function keys and overlay cards, mouse
and keyset (used independently or together), pen-up/pen/down,
light pen buttons, etc.

Coordinate input

Coordinates may be sent according to any subset of the following
criteria: with every character in some designated set (e.g.
control characters, or all characters); with every binary device
state change input; after some time interval has elapsed; after a
position change P > (y1-y0) ^2+(x1-x0)^2, etc.

RFC 553        Draft design for a text/graphics protocol    14 July 1973

Coordinates may be sent in either or both of "X-Y" or "target"
format.

X-Y format is just the location of the cursor relative to the
screen region assigned to the host.

Target format is the "call stack" (logical path from the root
unit - the ICP SUBPICTURE - to the closest unit) plus the
target-key of that unit plus the count of the closest character
within the string or the closest line segment or dot or special
point if appropriate.

Target input is unavailable for segmented display files.

In the event of overlapping target sensitive units, it is
not specified which of the units selected will be returned
as the hit unit.

Time input

Since hosts may wish to consider two events happening sufficiently
close together to be simultaneous, or to keep detailed interaction
statistics, it must be possible to request time information to be
sent with some reasonable subnet of other types of input.

Interrogations

It must be possible for the serving host to discover its environment
(e.g. screen size, available devices) and to read back state
information (display file).

This is very desirable both for debugging and for redirecting a
displayed image to another device (e.g. a plotter).

Environment

Terminal parameters: screen size and resolution, available input
devices, terminal type (for device specific control), number of
lines in the ICP TTY-UNIT.

Character parameters: available character sizes, special (non-
ASCII) characters, font characteristics, sub- and super-scripting
facilities.

State

Display file or display file components.

RFC 553        Draft design for a text/graphics protocol    14 July 1973

Cursor Position

It should be possible for the application program to read the
cursor position at any time.

Display File Support

It should be possible to find out if this user process supports
only segmented or structured display files, or both.

Command support

It should be possible to get a matrix from the user process
which indicates which commands are implemented.  This is a
necessity to find out which, if any, of the direct feedback
features are supported, and might be nice to allow for, e.g.,
the possibility of a text only or graphics only subset of the
protocol to be implemented.

Encoding Principles

Commands will have the format : BGC OPCODE DATA EGC where:

BGC (Begin Graphics Command) places the telnet connection into a
"read graphics command" mode,

OPCODE DATA is the specific graphics command and data, and

EGC (End Graphics Command) restores the telnet connection to its
normal state.

Note: This may all have to be bracketed by telnet Begin-8-bit-
transparent-mode and End-8-bit-transparent-mode commands.

Numbers in general will have have 7-bits of significance in each byte
-- if the high order of a byte is on, then the significant bits from
the next byte should be concatenated onto the low-order end of the
bits collected so far, etc..

Subpicture names - shall be 14-bit numbers, assigned by the serving
host.

Unit names - shall be 14-bit numbers, assigned by the serving host.

Strings - shall be 8-bit characters, with an escape convention to
represent changes of font and mode.

RFC 553        Draft design for a text/graphics protocol    14 July 1973

Since the channel is 8-bits wide, there is room for many more than
128 displayable characters.  However, the interpretation of codes
200B and above is not standardized!

Coordinates should be as described in RFC 493.

Rectangles - shall be specified by the coordinates of the endpoints
of one of the diagonal.

Encoding

The actual encoding of this protocol is forthcoming.  Since we expect
some changes to come about because of the upcoming Network Graphics
Group Meeting, we have postponed the actual encoding until after this
meeting.

[This RFC was put into machine readable form for entry]

```
           [into the online RFC archives by Via Genie, 12/1999]

```