# Source: https://xtermjs.org/docs/api/terminal/interfaces/imodes/

<div>

</div>

# Interface: IModes

Terminal modes as set by SM/DECSET.

## Hierarchy

-   **IModes**

## Index

### Properties

-   [applicationCursorKeysMode](/docs/api/terminal/interfaces/imodes/#readonly-applicationcursorkeysmode)
-   [applicationKeypadMode](/docs/api/terminal/interfaces/imodes/#readonly-applicationkeypadmode)
-   [bracketedPasteMode](/docs/api/terminal/interfaces/imodes/#readonly-bracketedpastemode)
-   [insertMode](/docs/api/terminal/interfaces/imodes/#readonly-insertmode)
-   [mouseTrackingMode](/docs/api/terminal/interfaces/imodes/#readonly-mousetrackingmode)
-   [originMode](/docs/api/terminal/interfaces/imodes/#readonly-originmode)
-   [reverseWraparoundMode](/docs/api/terminal/interfaces/imodes/#readonly-reversewraparoundmode)
-   [sendFocusMode](/docs/api/terminal/interfaces/imodes/#readonly-sendfocusmode)
-   [wraparoundMode](/docs/api/terminal/interfaces/imodes/#readonly-wraparoundmode)

## Properties

### `Readonly` applicationCursorKeysMode

• **applicationCursorKeysMode**: *boolean*

*Defined in [xterm.d.ts:1869](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1869)*

Application Cursor Keys (DECCKM): `CSI ? 1 h`

------------------------------------------------------------------------

### `Readonly` applicationKeypadMode

• **applicationKeypadMode**: *boolean*

*Defined in [xterm.d.ts:1873](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1873)*

Application Keypad Mode (DECNKM): `CSI ? 6 6 h`

------------------------------------------------------------------------

### `Readonly` bracketedPasteMode

• **bracketedPasteMode**: *boolean*

*Defined in [xterm.d.ts:1877](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1877)*

Bracketed Paste Mode: `CSI ? 2 0 0 4 h`

------------------------------------------------------------------------

### `Readonly` insertMode

• **insertMode**: *boolean*

*Defined in [xterm.d.ts:1881](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1881)*

Insert Mode (IRM): `CSI 4 h`

------------------------------------------------------------------------

### `Readonly` mouseTrackingMode

  ----------------------------------- ------- --------- -------- ---------
  • **mouseTrackingMode**: \*"none"   "x10"   "vt200"   "drag"   "any"\*
  ----------------------------------- ------- --------- -------- ---------

*Defined in [xterm.d.ts:1890](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1890)*

Mouse Tracking, this can be one of the following:

-   none: This is the default value and can be reset with DECRST
-   x10: Send Mouse X & Y on button press `CSI ? 9 h`
-   vt200: Send Mouse X & Y on button press and release `CSI ? 1 0 0 0 h`
-   drag: Use Cell Motion Mouse Tracking `CSI ? 1 0 0 2 h`
-   any: Use All Motion Mouse Tracking `CSI ? 1 0 0 3 h`

------------------------------------------------------------------------

### `Readonly` originMode

• **originMode**: *boolean*

*Defined in [xterm.d.ts:1894](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1894)*

Origin Mode (DECOM): `CSI ? 6 h`

------------------------------------------------------------------------

### `Readonly` reverseWraparoundMode

• **reverseWraparoundMode**: *boolean*

*Defined in [xterm.d.ts:1898](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1898)*

Reverse-wraparound Mode: `CSI ? 4 5 h`

------------------------------------------------------------------------

### `Readonly` sendFocusMode

• **sendFocusMode**: *boolean*

*Defined in [xterm.d.ts:1902](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1902)*

Send FocusIn/FocusOut events: `CSI ? 1 0 0 4 h`

------------------------------------------------------------------------

### `Readonly` wraparoundMode

• **wraparoundMode**: *boolean*

*Defined in [xterm.d.ts:1906](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1906)*

Auto-Wrap Mode (DECAWM): `CSI ? 7 h`