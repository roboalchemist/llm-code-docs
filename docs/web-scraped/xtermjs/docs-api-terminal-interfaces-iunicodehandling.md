# Source: https://xtermjs.org/docs/api/terminal/interfaces/iunicodehandling/

<div>

</div>

# Interface: IUnicodeHandling

(EXPERIMENTAL) Unicode handling interface.

## Hierarchy

-   **IUnicodeHandling**

## Index

### Properties

-   [activeVersion](/docs/api/terminal/interfaces/iunicodehandling/#activeversion)
-   [versions](/docs/api/terminal/interfaces/iunicodehandling/#readonly-versions)

### Methods

-   [register](/docs/api/terminal/interfaces/iunicodehandling/#register)

## Properties

### activeVersion

• **activeVersion**: *string*

*Defined in [xterm.d.ts:1859](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1859)*

Getter/setter for active Unicode version.

------------------------------------------------------------------------

### `Readonly` versions

• **versions**: *ReadonlyArray‹string›*

*Defined in [xterm.d.ts:1854](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1854)*

Registered Unicode versions.

## Methods

### register

▸ **register**(`provider`: [IUnicodeVersionProvider](/docs/api/terminal/interfaces/iunicodeversionprovider/)): *void*

*Defined in [xterm.d.ts:1849](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1849)*

Register a custom Unicode version provider.

**Parameters:**

  Name                                                 Type
  ---------------------------------------------------- -----------------------------------------------------------------------------------
  `provider`   [IUnicodeVersionProvider](/docs/api/terminal/interfaces/iunicodeversionprovider/)

**Returns:** *void*