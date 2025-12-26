# Source: https://xtermjs.org/docs/api/terminal/interfaces/ibuffercell/

<div>

</div>

# Interface: IBufferCell

Represents a single cell in the terminal's buffer.

## Hierarchy

-   **IBufferCell**

## Index

### Methods

-   [getBgColor](/docs/api/terminal/interfaces/ibuffercell/#getbgcolor)
-   [getBgColorMode](/docs/api/terminal/interfaces/ibuffercell/#getbgcolormode)
-   [getChars](/docs/api/terminal/interfaces/ibuffercell/#getchars)
-   [getCode](/docs/api/terminal/interfaces/ibuffercell/#getcode)
-   [getFgColor](/docs/api/terminal/interfaces/ibuffercell/#getfgcolor)
-   [getFgColorMode](/docs/api/terminal/interfaces/ibuffercell/#getfgcolormode)
-   [getWidth](/docs/api/terminal/interfaces/ibuffercell/#getwidth)
-   [isAttributeDefault](/docs/api/terminal/interfaces/ibuffercell/#isattributedefault)
-   [isBgDefault](/docs/api/terminal/interfaces/ibuffercell/#isbgdefault)
-   [isBgPalette](/docs/api/terminal/interfaces/ibuffercell/#isbgpalette)
-   [isBgRGB](/docs/api/terminal/interfaces/ibuffercell/#isbgrgb)
-   [isBlink](/docs/api/terminal/interfaces/ibuffercell/#isblink)
-   [isBold](/docs/api/terminal/interfaces/ibuffercell/#isbold)
-   [isDim](/docs/api/terminal/interfaces/ibuffercell/#isdim)
-   [isFgDefault](/docs/api/terminal/interfaces/ibuffercell/#isfgdefault)
-   [isFgPalette](/docs/api/terminal/interfaces/ibuffercell/#isfgpalette)
-   [isFgRGB](/docs/api/terminal/interfaces/ibuffercell/#isfgrgb)
-   [isInverse](/docs/api/terminal/interfaces/ibuffercell/#isinverse)
-   [isInvisible](/docs/api/terminal/interfaces/ibuffercell/#isinvisible)
-   [isItalic](/docs/api/terminal/interfaces/ibuffercell/#isitalic)
-   [isOverline](/docs/api/terminal/interfaces/ibuffercell/#isoverline)
-   [isStrikethrough](/docs/api/terminal/interfaces/ibuffercell/#isstrikethrough)
-   [isUnderline](/docs/api/terminal/interfaces/ibuffercell/#isunderline)

## Methods

### getBgColor

▸ **getBgColor**(): *number*

*Defined in [xterm.d.ts:1661](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1661)*

Gets a cell's background color number, this differs depending on what the color mode of the cell is:

-   Default: This should be 0, representing the default background color (CSI 49 m).
-   Palette: This is a number from 0 to 255 of ANSI colors (CSI 4(0-7) m, CSI 10(0-7) m, CSI 48 ; 5 ; 0-255 m).
-   RGB: A hex value representing a 'true color': 0xRRGGBB (CSI 4 8 ; 2 ; Pi ; Pr ; Pg ; Pb)

**Returns:** *number*

------------------------------------------------------------------------

### getBgColorMode

▸ **getBgColorMode**(): *number*

*Defined in [xterm.d.ts:1635](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1635)*

Gets the number representation of the background color mode, this can be used to perform quick comparisons of 2 cells to see if they're the same. Use `isBgRGB`, `isBgPalette` and `isBgDefault` to check what color mode a cell is.

**Returns:** *number*

------------------------------------------------------------------------

### getChars

▸ **getChars**(): *string*

*Defined in [xterm.d.ts:1613](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1613)*

The character(s) within the cell. Examples of what this can contain:

-   A normal width character
-   A wide character (eg. CJK)
-   An emoji

**Returns:** *string*

------------------------------------------------------------------------

### getCode

▸ **getCode**(): *number*

*Defined in [xterm.d.ts:1619](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1619)*

Gets the UTF32 codepoint of single characters, if content is a combined string it returns the codepoint of the last character in the string.

**Returns:** *number*

------------------------------------------------------------------------

### getFgColor

▸ **getFgColor**(): *number*

*Defined in [xterm.d.ts:1648](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1648)*

Gets a cell's foreground color number, this differs depending on what the color mode of the cell is:

-   Default: This should be 0, representing the default foreground color (CSI 39 m).
-   Palette: This is a number from 0 to 255 of ANSI colors (CSI 3(0-7) m, CSI 9(0-7) m, CSI 38 ; 5 ; 0-255 m).
-   RGB: A hex value representing a 'true color': 0xRRGGBB. (CSI 3 8 ; 2 ; Pi ; Pr ; Pg ; Pb)

**Returns:** *number*

------------------------------------------------------------------------

### getFgColorMode

▸ **getFgColorMode**(): *number*

*Defined in [xterm.d.ts:1627](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1627)*

Gets the number representation of the foreground color mode, this can be used to perform quick comparisons of 2 cells to see if they're the same. Use `isFgRGB`, `isFgPalette` and `isFgDefault` to check what color mode a cell is.

**Returns:** *number*

------------------------------------------------------------------------

### getWidth

▸ **getWidth**(): *number*

*Defined in [xterm.d.ts:1604](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1604)*

The width of the character. Some examples:

-   `1` for most cells.
-   `2` for wide character like CJK glyphs.
-   `0` for cells immediately following cells with a width of `2`.

**Returns:** *number*

------------------------------------------------------------------------

### isAttributeDefault

▸ **isAttributeDefault**(): *boolean*

*Defined in [xterm.d.ts:1696](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1696)*

Whether the cell has the default attribute (no color or style).

**Returns:** *boolean*

------------------------------------------------------------------------

### isBgDefault

▸ **isBgDefault**(): *boolean*

*Defined in [xterm.d.ts:1693](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1693)*

Whether the cell is using the default background color mode.

**Returns:** *boolean*

------------------------------------------------------------------------

### isBgPalette

▸ **isBgPalette**(): *boolean*

*Defined in [xterm.d.ts:1689](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1689)*

Whether the cell is using the palette background color mode.

**Returns:** *boolean*

------------------------------------------------------------------------

### isBgRGB

▸ **isBgRGB**(): *boolean*

*Defined in [xterm.d.ts:1685](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1685)*

Whether the cell is using the RGB background color mode.

**Returns:** *boolean*

------------------------------------------------------------------------

### isBlink

▸ **isBlink**(): *number*

*Defined in [xterm.d.ts:1672](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1672)*

Whether the cell has the blink attribute (CSI 5 m).

**Returns:** *number*

------------------------------------------------------------------------

### isBold

▸ **isBold**(): *number*

*Defined in [xterm.d.ts:1664](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1664)*

Whether the cell has the bold attribute (CSI 1 m).

**Returns:** *number*

------------------------------------------------------------------------

### isDim

▸ **isDim**(): *number*

*Defined in [xterm.d.ts:1668](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1668)*

Whether the cell has the dim attribute (CSI 2 m).

**Returns:** *number*

------------------------------------------------------------------------

### isFgDefault

▸ **isFgDefault**(): *boolean*

*Defined in [xterm.d.ts:1691](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1691)*

Whether the cell is using the default foreground color mode.

**Returns:** *boolean*

------------------------------------------------------------------------

### isFgPalette

▸ **isFgPalette**(): *boolean*

*Defined in [xterm.d.ts:1687](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1687)*

Whether the cell is using the palette foreground color mode.

**Returns:** *boolean*

------------------------------------------------------------------------

### isFgRGB

▸ **isFgRGB**(): *boolean*

*Defined in [xterm.d.ts:1683](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1683)*

Whether the cell is using the RGB foreground color mode.

**Returns:** *boolean*

------------------------------------------------------------------------

### isInverse

▸ **isInverse**(): *number*

*Defined in [xterm.d.ts:1674](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1674)*

Whether the cell has the inverse attribute (CSI 7 m).

**Returns:** *number*

------------------------------------------------------------------------

### isInvisible

▸ **isInvisible**(): *number*

*Defined in [xterm.d.ts:1676](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1676)*

Whether the cell has the invisible attribute (CSI 8 m).

**Returns:** *number*

------------------------------------------------------------------------

### isItalic

▸ **isItalic**(): *number*

*Defined in [xterm.d.ts:1666](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1666)*

Whether the cell has the italic attribute (CSI 3 m).

**Returns:** *number*

------------------------------------------------------------------------

### isOverline

▸ **isOverline**(): *number*

*Defined in [xterm.d.ts:1680](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1680)*

Whether the cell has the overline attribute (CSI 53 m).

**Returns:** *number*

------------------------------------------------------------------------

### isStrikethrough

▸ **isStrikethrough**(): *number*

*Defined in [xterm.d.ts:1678](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1678)*

Whether the cell has the strikethrough attribute (CSI 9 m).

**Returns:** *number*

------------------------------------------------------------------------

### isUnderline

▸ **isUnderline**(): *number*

*Defined in [xterm.d.ts:1670](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1670)*

Whether the cell has the underline attribute (CSI 4 m).

**Returns:** *number*