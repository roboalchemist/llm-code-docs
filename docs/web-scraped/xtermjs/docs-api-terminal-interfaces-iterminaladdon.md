# Source: https://xtermjs.org/docs/api/terminal/interfaces/iterminaladdon/

<div>

</div>

# Interface: ITerminalAddon

An addon that can provide additional functionality to the terminal.

## Hierarchy

-   [IDisposable](/docs/api/terminal/interfaces/idisposable/)

    ↳ **ITerminalAddon**

## Index

### Methods

-   [activate](/docs/api/terminal/interfaces/iterminaladdon/#activate)
-   [dispose](/docs/api/terminal/interfaces/iterminaladdon/#dispose)

## Methods

### activate

▸ **activate**(`terminal`: [Terminal](/docs/api/terminal/classes/terminal/)): *void*

*Defined in [xterm.d.ts:1270](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1270)*

This is called when the addon is activated.

**Parameters:**

  Name                                                 Type
  ---------------------------------------------------- --------------------------------------------------
  `terminal`   [Terminal](/docs/api/terminal/classes/terminal/)

**Returns:** *void*

------------------------------------------------------------------------

### dispose

▸ **dispose**(): *void*

*Inherited from [IDisposable](/docs/api/terminal/interfaces/idisposable/).[dispose](/docs/api/terminal/interfaces/idisposable/#dispose)*

*Defined in [xterm.d.ts:454](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L454)*

**Returns:** *void*