# Source: https://xtermjs.org/docs/api/terminal/interfaces/ilink/

<div>

</div>

# Interface: ILink

A link within the terminal.

## Hierarchy

-   **ILink**

## Index

### Properties

-   [decorations](/docs/api/terminal/interfaces/ilink/#optional-decorations)
-   [range](/docs/api/terminal/interfaces/ilink/#range)
-   [text](/docs/api/terminal/interfaces/ilink/#text)

### Methods

-   [activate](/docs/api/terminal/interfaces/ilink/#activate)
-   [dispose](/docs/api/terminal/interfaces/ilink/#optional-dispose)
-   [hover](/docs/api/terminal/interfaces/ilink/#optional-hover)
-   [leave](/docs/api/terminal/interfaces/ilink/#optional-leave)

## Properties

### `Optional` decorations

• **decorations**? : *[ILinkDecorations](/docs/api/terminal/interfaces/ilinkdecorations/)*

*Defined in [xterm.d.ts:1381](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1381)*

What link decorations to show when hovering the link, this property is tracked and changes made after the link is provided will trigger changes. If not set, all decroations will be enabled.

------------------------------------------------------------------------

### range

• **range**: *[IBufferRange](/docs/api/terminal/interfaces/ibufferrange/)*

*Defined in [xterm.d.ts:1369](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1369)*

The buffer range of the link.

------------------------------------------------------------------------

### text

• **text**: *string*

*Defined in [xterm.d.ts:1374](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1374)*

The text of the link.

## Methods

### activate

▸ **activate**(`event`: MouseEvent, `text`: string): *void*

*Defined in [xterm.d.ts:1388](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1388)*

Calls when the link is activated.

**Parameters:**

  Name                                              Type         Description
  ------------------------------------------------- ------------ ------------------------------------------
  `event`   MouseEvent   The mouse event triggering the callback.
  `text`    string       The text of the link.

**Returns:** *void*

------------------------------------------------------------------------

### `Optional` dispose

▸ **dispose**(): *void*

*Defined in [xterm.d.ts:1410](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1410)*

Called when the link is released and no longer used by xterm.js.

**Returns:** *void*

------------------------------------------------------------------------

### `Optional` hover

▸ **hover**(`event`: MouseEvent, `text`: string): *void*

*Defined in [xterm.d.ts:1398](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1398)*

Called when the mouse hovers the link. To use this to create a DOM-based hover tooltip, create the hover element within `Terminal.element` and add the `xterm-hover` class to it, that will cause mouse events to not fall through and activate other links.

**Parameters:**

  Name                                              Type         Description
  ------------------------------------------------- ------------ ------------------------------------------
  `event`   MouseEvent   The mouse event triggering the callback.
  `text`    string       The text of the link.

**Returns:** *void*

------------------------------------------------------------------------

### `Optional` leave

▸ **leave**(`event`: MouseEvent, `text`: string): *void*

*Defined in [xterm.d.ts:1405](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1405)*

Called when the mouse leaves the link.

**Parameters:**

  Name                                              Type         Description
  ------------------------------------------------- ------------ ------------------------------------------
  `event`   MouseEvent   The mouse event triggering the callback.
  `text`    string       The text of the link.

**Returns:** *void*