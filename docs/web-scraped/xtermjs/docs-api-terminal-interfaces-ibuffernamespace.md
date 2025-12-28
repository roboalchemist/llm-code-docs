# Source: https://xtermjs.org/docs/api/terminal/interfaces/ibuffernamespace/

<div>

</div>

# Interface: IBufferNamespace

Represents the terminal's set of buffers.

## Hierarchy

-   **IBufferNamespace**

## Index

### Properties

-   [active](/docs/api/terminal/interfaces/ibuffernamespace/#readonly-active)
-   [alternate](/docs/api/terminal/interfaces/ibuffernamespace/#readonly-alternate)
-   [normal](/docs/api/terminal/interfaces/ibuffernamespace/#readonly-normal)
-   [onBufferChange](/docs/api/terminal/interfaces/ibuffernamespace/#onbufferchange)

## Properties

### `Readonly` active

• **active**: *[IBuffer](/docs/api/terminal/interfaces/ibuffer/)*

*Defined in [xterm.d.ts:1531](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1531)*

The active buffer, this will either be the normal or alternate buffers.

------------------------------------------------------------------------

### `Readonly` alternate

• **alternate**: *[IBuffer](/docs/api/terminal/interfaces/ibuffer/)*

*Defined in [xterm.d.ts:1542](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1542)*

The alternate buffer, this becomes the active buffer when an application enters this mode via DECSET (`CSI ? 4 7 h`)

------------------------------------------------------------------------

### `Readonly` normal

• **normal**: *[IBuffer](/docs/api/terminal/interfaces/ibuffer/)*

*Defined in [xterm.d.ts:1536](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1536)*

The normal buffer.

------------------------------------------------------------------------

### onBufferChange

• **onBufferChange**: *[IEvent](/docs/api/terminal/interfaces/ievent/)‹[IBuffer](/docs/api/terminal/interfaces/ibuffer/)›*

*Defined in [xterm.d.ts:1548](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1548)*

Adds an event listener for when the active buffer changes.

**`returns`** an `IDisposable` to stop listening.