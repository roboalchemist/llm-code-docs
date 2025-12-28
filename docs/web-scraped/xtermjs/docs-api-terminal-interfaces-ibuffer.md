# Source: https://xtermjs.org/docs/api/terminal/interfaces/ibuffer/

<div>

</div>

# Interface: IBuffer

Represents a terminal buffer.

## Hierarchy

-   **IBuffer**

## Index

### Properties

-   [baseY](/docs/api/terminal/interfaces/ibuffer/#readonly-basey)
-   [cursorX](/docs/api/terminal/interfaces/ibuffer/#readonly-cursorx)
-   [cursorY](/docs/api/terminal/interfaces/ibuffer/#readonly-cursory)
-   [length](/docs/api/terminal/interfaces/ibuffer/#readonly-length)
-   [type](/docs/api/terminal/interfaces/ibuffer/#readonly-type)
-   [viewportY](/docs/api/terminal/interfaces/ibuffer/#readonly-viewporty)

### Methods

-   [getLine](/docs/api/terminal/interfaces/ibuffer/#getline)
-   [getNullCell](/docs/api/terminal/interfaces/ibuffer/#getnullcell)

## Properties

### `Readonly` baseY

• **baseY**: *number*

*Defined in [xterm.d.ts:1489](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1489)*

The line within the buffer where the top of the bottom page is (when fully scrolled down).

------------------------------------------------------------------------

### `Readonly` cursorX

• **cursorX**: *number*

*Defined in [xterm.d.ts:1478](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1478)*

The x position of the cursor. This ranges between `0` (left side) and `Terminal.cols` (after last cell of the row).

------------------------------------------------------------------------

### `Readonly` cursorY

• **cursorY**: *number*

*Defined in [xterm.d.ts:1472](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1472)*

The y position of the cursor. This ranges between `0` (when the cursor is at baseY) and `Terminal.rows - 1` (when the cursor is on the last row).

------------------------------------------------------------------------

### `Readonly` length

• **length**: *number*

*Defined in [xterm.d.ts:1494](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1494)*

The amount of lines in the buffer.

------------------------------------------------------------------------

### `Readonly` type

  ------------------------ ---------------
  • **type**: \*"normal"   "alternate"\*
  ------------------------ ---------------

*Defined in [xterm.d.ts:1465](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1465)*

The type of the buffer.

------------------------------------------------------------------------

### `Readonly` viewportY

• **viewportY**: *number*

*Defined in [xterm.d.ts:1483](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1483)*

The line within the buffer where the top of the viewport is.

## Methods

### getLine

  --------------------------------------------------------------------------------------------------------------------------------- -------------
  ▸ **getLine**(`y`: number): \*[IBufferLine](/docs/api/terminal/interfaces/ibufferline/)   undefined\*
  --------------------------------------------------------------------------------------------------------------------------------- -------------

*Defined in [xterm.d.ts:1506](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1506)*

Gets a line from the buffer, or undefined if the line index does not exist.

Note that the result of this function should be used immediately after calling as when the terminal updates it could lead to unexpected behavior.

**Parameters:**

  Name                                          Type     Description
  --------------------------------------------- -------- ------------------------
  `y`   number   The line index to get.

  -------------------------------------------------------------------------- -------------
  **Returns:** \*[IBufferLine](/docs/api/terminal/interfaces/ibufferline/)   undefined\*
  -------------------------------------------------------------------------- -------------

------------------------------------------------------------------------

### getNullCell

▸ **getNullCell**(): *[IBufferCell](/docs/api/terminal/interfaces/ibuffercell/)*

*Defined in [xterm.d.ts:1513](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1513)*

Creates an empty cell object suitable as a cell reference in `line.getCell(x, cell)`. Use this to avoid costly recreation of cell objects when dealing with tons of cells.

**Returns:** *[IBufferCell](/docs/api/terminal/interfaces/ibuffercell/)*