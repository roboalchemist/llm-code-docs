# Source: https://xtermjs.org/docs/api/terminal/interfaces/idisposablewithevent/

<div>

</div>

# Interface: IDisposableWithEvent

Represents a disposable that tracks is disposed state.

## Hierarchy

-   [IDisposable](/docs/api/terminal/interfaces/idisposable/)

    ↳ **IDisposableWithEvent**

    ↳ [IMarker](/docs/api/terminal/interfaces/imarker/)

    ↳ [IDecoration](/docs/api/terminal/interfaces/idecoration/)

## Index

### Properties

-   [isDisposed](/docs/api/terminal/interfaces/idisposablewithevent/#readonly-isdisposed)
-   [onDispose](/docs/api/terminal/interfaces/idisposablewithevent/#ondispose)

### Methods

-   [dispose](/docs/api/terminal/interfaces/idisposablewithevent/#dispose)

## Properties

### `Readonly` isDisposed

• **isDisposed**: *boolean*

*Defined in [xterm.d.ts:495](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L495)*

Whether this is disposed.

------------------------------------------------------------------------

### onDispose

• **onDispose**: *[IEvent](/docs/api/terminal/interfaces/ievent/)‹void›*

*Defined in [xterm.d.ts:490](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L490)*

Event listener to get notified when this gets disposed.

## Methods

### dispose

▸ **dispose**(): *void*

*Inherited from [IDisposable](/docs/api/terminal/interfaces/idisposable/).[dispose](/docs/api/terminal/interfaces/idisposable/#dispose)*

*Defined in [xterm.d.ts:454](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L454)*

**Returns:** *void*