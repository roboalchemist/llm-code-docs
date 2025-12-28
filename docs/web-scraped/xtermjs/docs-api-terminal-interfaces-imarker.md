# Source: https://xtermjs.org/docs/api/terminal/interfaces/imarker/

<div>

</div>

# Interface: IMarker

Represents a specific line in the terminal that is tracked when scrollback is trimmed and lines are added or removed. This is a single line that may be part of a larger wrapped line.

## Hierarchy

↳ [IDisposableWithEvent](/docs/api/terminal/interfaces/idisposablewithevent/)

↳ **IMarker**

## Index

### Properties

-   [id](/docs/api/terminal/interfaces/imarker/#readonly-id)
-   [isDisposed](/docs/api/terminal/interfaces/imarker/#readonly-isdisposed)
-   [line](/docs/api/terminal/interfaces/imarker/#readonly-line)
-   [onDispose](/docs/api/terminal/interfaces/imarker/#ondispose)

### Methods

-   [dispose](/docs/api/terminal/interfaces/imarker/#dispose)

## Properties

### `Readonly` id

• **id**: *number*

*Defined in [xterm.d.ts:474](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L474)*

A unique identifier for this marker.

------------------------------------------------------------------------

### `Readonly` isDisposed

• **isDisposed**: *boolean*

*Inherited from [IMarker](/docs/api/terminal/interfaces/imarker/).[isDisposed](/docs/api/terminal/interfaces/imarker/#readonly-isdisposed)*

*Defined in [xterm.d.ts:495](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L495)*

Whether this is disposed.

------------------------------------------------------------------------

### `Readonly` line

• **line**: *number*

*Defined in [xterm.d.ts:480](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L480)*

The actual line index in the buffer at this point in time. This is set to -1 if the marker has been disposed.

------------------------------------------------------------------------

### onDispose

• **onDispose**: *[IEvent](/docs/api/terminal/interfaces/ievent/)‹void›*

*Inherited from [IMarker](/docs/api/terminal/interfaces/imarker/).[onDispose](/docs/api/terminal/interfaces/imarker/#ondispose)*

*Defined in [xterm.d.ts:490](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L490)*

Event listener to get notified when this gets disposed.

## Methods

### dispose

▸ **dispose**(): *void*

*Inherited from [IDisposable](/docs/api/terminal/interfaces/idisposable/).[dispose](/docs/api/terminal/interfaces/idisposable/#dispose)*

*Defined in [xterm.d.ts:454](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L454)*

**Returns:** *void*