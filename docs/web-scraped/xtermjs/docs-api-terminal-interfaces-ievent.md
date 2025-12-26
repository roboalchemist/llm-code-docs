# Source: https://xtermjs.org/docs/api/terminal/interfaces/ievent/

<div>

</div>

# Interface: IEvent ‹**T, U**›

An event that can be listened to.

## Type parameters

▪ **T**

▪ **U**

## Hierarchy

-   **IEvent**

## Callable

▸ (`listener`: function): *[IDisposable](/docs/api/terminal/interfaces/idisposable/)*

*Defined in [xterm.d.ts:461](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L461)*

An event that can be listened to.

**Parameters:**

▪ **listener**: *function*

▸ (`arg1`: T, `arg2`: U): *any*

**Parameters:**

  Name                                             Type
  ------------------------------------------------ ------
  `arg1`   T
  `arg2`   U

**Returns:** *[IDisposable](/docs/api/terminal/interfaces/idisposable/)*

an `IDisposable` to stop listening.