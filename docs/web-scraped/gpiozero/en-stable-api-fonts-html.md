# Source: https://gpiozero.readthedocs.io/en/stable/api_fonts.html

Title: Fonts — gpiozero 2.0.1 Documentation

URL Source: https://gpiozero.readthedocs.io/en/stable/api_fonts.html

Markdown Content:
21. API - Fonts[](https://gpiozero.readthedocs.io/en/stable/api_fonts.html#module-gpiozero.fonts "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------

GPIO Zero includes a concept of “fonts” which is somewhat different to that you may be familiar with. While a typical printing font determines how a particular character is rendered on a page, a GPIO Zero font determines how a particular character is rendered by a series of lights, like LED segments (e.g. with [`LEDCharDisplay`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCharDisplay "gpiozero.LEDCharDisplay") or [`LEDMultiCharDisplay`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDMultiCharDisplay "gpiozero.LEDMultiCharDisplay")).

As a result, GPIO Zero’s fonts are quite crude affairs, being little more than mappings of characters to tuples of LED states. Still, it helps to have a “friendly” format for creating such fonts, and in this module the library provides several routines for this purpose.

The module itself is typically imported as follows:

from gpiozero import fonts

21.1. Font Parsing[](https://gpiozero.readthedocs.io/en/stable/api_fonts.html#font-parsing "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

gpiozero.fonts.load_font_7seg(_filename\_or\_obj_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/fonts.html#load_font_7seg)[](https://gpiozero.readthedocs.io/en/stable/api_fonts.html#gpiozero.fonts.load_font_7seg "Link to this definition")
Given a filename or a file-like object, parse it as an font definition for a [7-segment display](https://en.wikipedia.org/wiki/Seven-segment_display), returning a [`dict`](https://docs.python.org/3.9/library/stdtypes.html#dict "(in Python v3.9)") suitable for use with [`LEDCharDisplay`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCharDisplay "gpiozero.LEDCharDisplay").

The file-format is a simple text-based format in which blank and #-prefixed lines are ignored. All other lines are assumed to be groups of character definitions which are cells of 3x3 characters laid out as follows:

Ca
fgb
edc

Where C is the character being defined, and a-g define the states of the LEDs for that position. a, d, and g are on if they are “_”. b, c, e, and f are on if they are “|”. Any other character in these positions is considered off. For example, you might define the following characters:

 .  0_  1.  2_  3_  4.  5_  6_  7_  8_  9_
... |.| ..| ._| ._| |_| |_. |_. ..| |_| |_|
... |_| ..| |_. ._| ..| ._| |_| ..| |_| ._|

In the example above, empty locations are marked with “.” but could mostly be left as spaces. However, the first item defines the space (” “) character and needs _some_ non-space characters in its definition as the parser also strips empty columns (as typically occur between character definitions). This is also why the definition for “1” must include something to fill the middle column.

gpiozero.fonts.load_font_14seg(_filename\_or\_obj_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/fonts.html#load_font_14seg)[](https://gpiozero.readthedocs.io/en/stable/api_fonts.html#gpiozero.fonts.load_font_14seg "Link to this definition")
Given a filename or a file-like object, parse it as a font definition for a [14-segment display](https://en.wikipedia.org/wiki/Fourteen-segment_display), returning a [`dict`](https://docs.python.org/3.9/library/stdtypes.html#dict "(in Python v3.9)") suitable for use with [`LEDCharDisplay`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCharDisplay "gpiozero.LEDCharDisplay").

The file-format is a simple text-based format in which blank and #-prefixed lines are ignored. All other lines are assumed to be groups of character definitions which are cells of 5x5 characters laid out as follows:

X.a..
fijkb
.g.h.
elmnc
..d..

Where X is the character being defined, and a-n define the states of the LEDs for that position. a, d, g, and h are on if they are “-”. b, c, e, f, j, and m are on if they are “|”. i and n are on if they are “". Finally, k and l are on if they are “/”. Any other character in these positions is considered off. For example, you might define the following characters:

 .... 0---  1..   2---  3---  4     5---  6---  7---. 8---  9---
..... |  /|    /|     |     | |   | |     |        /  |   | |   |
..... | / |     |  ---    --   ---|  ---  |---    |    ---   ---|
..... |/  |     | |         |     |     | |   |   |   |   |     |
.....  ---         ---   ---         ---   ---         ---

In the example above, several locations have extraneous characters. For example, the “/” in the center of the “0” definition, or the “-” in the middle of the “8”. These locations are ignored, but filled in nonetheless to make the shape more obvious.

These extraneous locations could equally well be left as spaces. However, the first item defines the space (” “) character and needs _some_ non-space characters in its definition as the parser also strips empty columns (as typically occur between character definitions) and verifies that definitions are 5 columns wide and 5 rows high.

This also explains why place-holder characters (“.”) have been inserted at the top of the definition of the “1” character. Otherwise the parser will strip these empty columns and decide the definition is invalid (as the result is only 3 columns wide).

gpiozero.fonts.load_segment_font(_filename\_or\_obj_, _width_, _height_, _pins_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/fonts.html#load_segment_font)[](https://gpiozero.readthedocs.io/en/stable/api_fonts.html#gpiozero.fonts.load_segment_font "Link to this definition")
A generic function for parsing segment font definition files.

If you’re working with “standard” [7-segment](https://en.wikipedia.org/wiki/Seven-segment_display) or [14-segment](https://en.wikipedia.org/wiki/Fourteen-segment_display) displays you _don’t_ want this function; see [`load_font_7seg()`](https://gpiozero.readthedocs.io/en/stable/api_fonts.html#gpiozero.fonts.load_font_7seg "gpiozero.fonts.load_font_7seg") or [`load_font_14seg()`](https://gpiozero.readthedocs.io/en/stable/api_fonts.html#gpiozero.fonts.load_font_14seg "gpiozero.fonts.load_font_14seg") instead. However, if you are working with another style of segmented display and wish to construct a parser for a custom format, this is the function you want.

The _filename\_or\_obj_ parameter is simply the file-like object or filename to load. This is typically passed in from the calling function.

The _width_ and _height_ parameters give the width and height in characters of each character definition. For example, these are 3 and 3 for 7-segment displays. Finally, _pins_ is a list of tuples that defines the position of each pin definition in the character array, and the character that marks that position “active”.

For example, for 7-segment displays this function is called as follows:

load_segment_font(filename_or_obj, width=3, height=3, pins=[
    (1, '_'), (5, '|'), (8, '|'), (7, '_'),
    (6, '|'), (3, '|'), (4, '_')])

This dictates that each character will be defined by a 3x3 character grid which will be converted into a nine-character string like so:

012
345  ==>  '012345678'
678

Position 0 is always assumed to be the character being defined. The _pins_ list then specifies: the first pin is the character at position 1 which will be “on” when that character is “_”. The second pin is the character at position 5 which will be “on” when that character is “|”, and so on.
