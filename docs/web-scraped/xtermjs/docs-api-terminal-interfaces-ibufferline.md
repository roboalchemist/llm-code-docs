# Source: https://xtermjs.org/docs/api/terminal/interfaces/ibufferline/

<div>

</div>

# Interface: IBufferLine

Represents a line in the terminal's buffer.

## Hierarchy

-   **IBufferLine**

## Index

### Properties

-   [isWrapped](/docs/api/terminal/interfaces/ibufferline/#readonly-iswrapped)
-   [length](/docs/api/terminal/interfaces/ibufferline/#readonly-length)

### Methods

-   [getCell](/docs/api/terminal/interfaces/ibufferline/#getcell)
-   [translateToString](/docs/api/terminal/interfaces/ibufferline/#translatetostring)

## Properties

### `Readonly` isWrapped

• **isWrapped**: *boolean*

*Defined in [xterm.d.ts:1558](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1558)*

Whether the line is wrapped from the previous line.

------------------------------------------------------------------------

### `Readonly` length

• **length**: *number*

*Defined in [xterm.d.ts:1566](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1566)*

The length of the line, all call to getCell beyond the length will result in `undefined`. Note that this may exceed columns as the line array may not be trimmed after a resize, compare against [Terminal.cols](/docs/api/terminal/classes/terminal/#readonly-cols) to get the actual maximum length of a line.

## Methods

### getCell

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------
  ▸ **getCell**(`x`: number, `cell?`: [IBufferCell](/docs/api/terminal/interfaces/ibuffercell/)): \*[IBufferCell](/docs/api/terminal/interfaces/ibuffercell/)   undefined\*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------

*Defined in [xterm.d.ts:1580](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1580)*

Gets a cell from the line, or undefined if the line index does not exist.

Note that the result of this function should be used immediately after calling as when the terminal updates it could lead to unexpected behavior.

**Parameters:**

  Name                                              Type                                                        Description
  ------------------------------------------------- ----------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `x`       number                                                      The character index to get.
  `cell?`   [IBufferCell](/docs/api/terminal/interfaces/ibuffercell/)   Optional cell object to load data into for performance reasons. This is mainly useful when every cell in the buffer is being looped over to avoid creating new objects for every cell.

  -------------------------------------------------------------------------- -------------
  **Returns:** \*[IBufferCell](/docs/api/terminal/interfaces/ibuffercell/)   undefined\*
  -------------------------------------------------------------------------- -------------

------------------------------------------------------------------------

### translateToString

▸ **translateToString**(`trimRight?`: boolean, `startColumn?`: number, `endColumn?`: number): *string*

*Defined in [xterm.d.ts:1590](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1590)*

Gets the line as a string. Note that this is gets only the string for the line, not taking isWrapped into account.

**Parameters:**

  Name                                                     Type      Description
  -------------------------------------------------------- --------- ----------------------------------------------------------
  `trimRight?`     boolean   Whether to trim any whitespace at the right of the line.
  `startColumn?`   number    The column to start from (inclusive).
  `endColumn?`     number    The column to end at (exclusive).

**Returns:** *string*