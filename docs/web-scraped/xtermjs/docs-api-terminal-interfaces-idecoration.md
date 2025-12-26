# Source: https://xtermjs.org/docs/api/terminal/interfaces/idecoration/

<div>

</div>

# Interface: IDecoration

Represents a decoration in the terminal that is associated with a particular marker and DOM element.

## Hierarchy

↳ [IDisposableWithEvent](/docs/api/terminal/interfaces/idisposablewithevent/)

↳ **IDecoration**

## Index

### Properties

-   [element](/docs/api/terminal/interfaces/idecoration/#element)
-   [isDisposed](/docs/api/terminal/interfaces/idecoration/#readonly-isdisposed)
-   [marker](/docs/api/terminal/interfaces/idecoration/#readonly-marker)
-   [onDispose](/docs/api/terminal/interfaces/idecoration/#ondispose)
-   [onRender](/docs/api/terminal/interfaces/idecoration/#readonly-onrender)
-   [options](/docs/api/terminal/interfaces/idecoration/#options)

### Methods

-   [dispose](/docs/api/terminal/interfaces/idecoration/#dispose)

## Properties

### element

  ------------------------------ -------------
  • **element**: \*HTMLElement   undefined\*
  ------------------------------ -------------

*Defined in [xterm.d.ts:520](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L520)*

The element that the decoration is rendered to. This will be undefined until it is rendered for the first time by [IDecoration.onRender](/docs/api/terminal/interfaces/idecoration/#readonly-onrender). that.

------------------------------------------------------------------------

### `Readonly` isDisposed

• **isDisposed**: *boolean*

*Inherited from [IMarker](/docs/api/terminal/interfaces/imarker/).[isDisposed](/docs/api/terminal/interfaces/imarker/#readonly-isdisposed)*

*Defined in [xterm.d.ts:495](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L495)*

Whether this is disposed.

------------------------------------------------------------------------

### `Readonly` marker

• **marker**: *[IMarker](/docs/api/terminal/interfaces/imarker/)*

*Defined in [xterm.d.ts:506](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L506)*

------------------------------------------------------------------------

### onDispose

• **onDispose**: *[IEvent](/docs/api/terminal/interfaces/ievent/)‹void›*

*Inherited from [IMarker](/docs/api/terminal/interfaces/imarker/).[onDispose](/docs/api/terminal/interfaces/imarker/#ondispose)*

*Defined in [xterm.d.ts:490](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L490)*

Event listener to get notified when this gets disposed.

------------------------------------------------------------------------

### `Readonly` onRender

• **onRender**: *[IEvent](/docs/api/terminal/interfaces/ievent/)‹HTMLElement›*

*Defined in [xterm.d.ts:513](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L513)*

An event fired when the decoration is rendered, returns the dom element associated with the decoration.

------------------------------------------------------------------------

### options

• **options**: *Pick‹[IDecorationOptions](/docs/api/terminal/interfaces/idecorationoptions/), "overviewRulerOptions"›*

*Defined in [xterm.d.ts:527](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L527)*

The options for the overview ruler that can be updated. This will only take effect when [IDecorationOptions.overviewRulerOptions](/docs/api/terminal/interfaces/idecorationoptions/#optional-overviewruleroptions) were provided initially.

## Methods

### dispose

▸ **dispose**(): *void*

*Inherited from [IDisposable](/docs/api/terminal/interfaces/idisposable/).[dispose](/docs/api/terminal/interfaces/idisposable/#dispose)*

*Defined in [xterm.d.ts:454](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L454)*

**Returns:** *void*