# Source: https://xtermjs.org/docs/api/terminal/interfaces/ilogger/

<div>

</div>

# Interface: ILogger

A replacement logger for `console`.

## Hierarchy

-   **ILogger**

## Index

### Methods

-   [debug](/docs/api/terminal/interfaces/ilogger/#debug)
-   [error](/docs/api/terminal/interfaces/ilogger/#error)
-   [info](/docs/api/terminal/interfaces/ilogger/#info)
-   [trace](/docs/api/terminal/interfaces/ilogger/#trace)
-   [warn](/docs/api/terminal/interfaces/ilogger/#warn)

## Methods

### debug

▸ **debug**(`message`: string, ...`args`: any\[\]): *void*

*Defined in [xterm.d.ts:432](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L432)*

Log a debug message, this will only be called if [ITerminalOptions.logLevel](/docs/api/terminal/interfaces/iterminaloptions/#optional-loglevel) is set to debug or below.

**Parameters:**

  Name                                                Type
  --------------------------------------------------- ---------
  `message`   string
  `...args`   any\[\]

**Returns:** *void*

------------------------------------------------------------------------

### error

  ----------------------------------------------------------------------- ----------------------------------------------------------------------------
  ▸ **error**(`message`: string   Error, ...`args`: any\[\]): *void*
  ----------------------------------------------------------------------- ----------------------------------------------------------------------------

*Defined in [xterm.d.ts:447](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L447)*

Log a debug message, this will only be called if [ITerminalOptions.logLevel](/docs/api/terminal/interfaces/iterminaloptions/#optional-loglevel) is set to error or below.

**Parameters:**

  Name                                                Type
  --------------------------------------------------- -----------------
  `message`   string \| Error
  `...args`   any\[\]

**Returns:** *void*

------------------------------------------------------------------------

### info

▸ **info**(`message`: string, ...`args`: any\[\]): *void*

*Defined in [xterm.d.ts:437](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L437)*

Log a debug message, this will only be called if [ITerminalOptions.logLevel](/docs/api/terminal/interfaces/iterminaloptions/#optional-loglevel) is set to info or below.

**Parameters:**

  Name                                                Type
  --------------------------------------------------- ---------
  `message`   string
  `...args`   any\[\]

**Returns:** *void*

------------------------------------------------------------------------

### trace

▸ **trace**(`message`: string, ...`args`: any\[\]): *void*

*Defined in [xterm.d.ts:427](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L427)*

Log a trace message, this will only be called if [ITerminalOptions.logLevel](/docs/api/terminal/interfaces/iterminaloptions/#optional-loglevel) is set to trace.

**Parameters:**

  Name                                                Type
  --------------------------------------------------- ---------
  `message`   string
  `...args`   any\[\]

**Returns:** *void*

------------------------------------------------------------------------

### warn

▸ **warn**(`message`: string, ...`args`: any\[\]): *void*

*Defined in [xterm.d.ts:442](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L442)*

Log a debug message, this will only be called if [ITerminalOptions.logLevel](/docs/api/terminal/interfaces/iterminaloptions/#optional-loglevel) is set to warn or below.

**Parameters:**

  Name                                                Type
  --------------------------------------------------- ---------
  `message`   string
  `...args`   any\[\]

**Returns:** *void*