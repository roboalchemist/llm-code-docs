# Source: https://xtermjs.org/docs/api/terminal/interfaces/idecorationoptions/

<div>

</div>

# Interface: IDecorationOptions

## Hierarchy

-   **IDecorationOptions**

## Index

### Properties

-   [anchor](/docs/api/terminal/interfaces/idecorationoptions/#optional-readonly-anchor)
-   [backgroundColor](/docs/api/terminal/interfaces/idecorationoptions/#optional-readonly-backgroundcolor)
-   [foregroundColor](/docs/api/terminal/interfaces/idecorationoptions/#optional-readonly-foregroundcolor)
-   [height](/docs/api/terminal/interfaces/idecorationoptions/#optional-readonly-height)
-   [layer](/docs/api/terminal/interfaces/idecorationoptions/#optional-readonly-layer)
-   [marker](/docs/api/terminal/interfaces/idecorationoptions/#readonly-marker)
-   [overviewRulerOptions](/docs/api/terminal/interfaces/idecorationoptions/#optional-overviewruleroptions)
-   [width](/docs/api/terminal/interfaces/idecorationoptions/#optional-readonly-width)
-   [x](/docs/api/terminal/interfaces/idecorationoptions/#optional-readonly-x)

## Properties

### `Optional` `Readonly` anchor

  --------------------------- ----------
  • **anchor**? : \*"right"   "left"\*
  --------------------------- ----------

*Defined in [xterm.d.ts:553](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L553)*

------------------------------------------------------------------------

### `Optional` `Readonly` backgroundColor

• **backgroundColor**? : *string*

*Defined in [xterm.d.ts:576](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L576)*

The background color of the cell(s). When 2 decorations both set the foreground color the last registered decoration will be used. Only the `#RRGGBB` format is supported.

------------------------------------------------------------------------

### `Optional` `Readonly` foregroundColor

• **foregroundColor**? : *string*

*Defined in [xterm.d.ts:583](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L583)*

The foreground color of the cell(s). When 2 decorations both set the foreground color the last registered decoration will be used. Only the `#RRGGBB` format is supported.

------------------------------------------------------------------------

### `Optional` `Readonly` height

• **height**? : *number*

*Defined in [xterm.d.ts:569](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L569)*

The height of the decoration in cells, defaults to 1.

------------------------------------------------------------------------

### `Optional` `Readonly` layer

  --------------------------- ---------
  • **layer**? : \*"bottom"   "top"\*
  --------------------------- ---------

*Defined in [xterm.d.ts:593](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L593)*

What layer to render the decoration at when [backgroundColor](/docs/api/terminal/interfaces/idecorationoptions/#optional-readonly-backgroundcolor) or [foregroundColor](/docs/api/terminal/interfaces/idecorationoptions/#optional-readonly-foregroundcolor) are used. `'bottom'` will render under the selection, `'top`' will render above the selection\*.

*\* The selection will render on top regardless of layer on the canvas renderer due to how it renders selection separately.*

------------------------------------------------------------------------

### `Readonly` marker

• **marker**: *[IMarker](/docs/api/terminal/interfaces/imarker/)*

*Defined in [xterm.d.ts:547](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L547)*

The line in the terminal where the decoration will be displayed

------------------------------------------------------------------------

### `Optional` overviewRulerOptions

• **overviewRulerOptions**? : *[IDecorationOverviewRulerOptions](/docs/api/terminal/interfaces/idecorationoverviewruleroptions/)*

*Defined in [xterm.d.ts:602](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L602)*

When defined, renders the decoration in the overview ruler to the right of the terminal. [ITerminalOptions.overviewRulerWidth](/docs/api/terminal/interfaces/iterminaloptions/#optional-overviewrulerwidth) must be set in order to see the overview ruler.

**`param`** The color of the decoration.

**`param`** The position of the decoration.

------------------------------------------------------------------------

### `Optional` `Readonly` width

• **width**? : *number*

*Defined in [xterm.d.ts:564](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L564)*

The width of the decoration in cells, defaults to 1.

------------------------------------------------------------------------

### `Optional` `Readonly` x

• **x**? : *number*

*Defined in [xterm.d.ts:558](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L558)*

The x position offset relative to the anchor