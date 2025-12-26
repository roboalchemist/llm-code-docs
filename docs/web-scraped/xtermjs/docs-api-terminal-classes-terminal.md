# Source: https://xtermjs.org/docs/api/terminal/classes/terminal/

<div>

</div>

# Class: Terminal

The class that represents an xterm.js terminal.

## Hierarchy

-   **Terminal**

## Implements

-   [IDisposable](/docs/api/terminal/interfaces/idisposable/)

## Index

### Constructors

-   [constructor](/docs/api/terminal/classes/terminal/#constructor)

### Properties

-   [buffer](/docs/api/terminal/classes/terminal/#readonly-buffer)
-   [cols](/docs/api/terminal/classes/terminal/#readonly-cols)
-   [element](/docs/api/terminal/classes/terminal/#readonly-element)
-   [markers](/docs/api/terminal/classes/terminal/#readonly-markers)
-   [modes](/docs/api/terminal/classes/terminal/#readonly-modes)
-   [onBell](/docs/api/terminal/classes/terminal/#onbell)
-   [onBinary](/docs/api/terminal/classes/terminal/#onbinary)
-   [onCursorMove](/docs/api/terminal/classes/terminal/#oncursormove)
-   [onData](/docs/api/terminal/classes/terminal/#ondata)
-   [onKey](/docs/api/terminal/classes/terminal/#onkey)
-   [onLineFeed](/docs/api/terminal/classes/terminal/#onlinefeed)
-   [onRender](/docs/api/terminal/classes/terminal/#onrender)
-   [onResize](/docs/api/terminal/classes/terminal/#onresize)
-   [onScroll](/docs/api/terminal/classes/terminal/#onscroll)
-   [onSelectionChange](/docs/api/terminal/classes/terminal/#onselectionchange)
-   [onTitleChange](/docs/api/terminal/classes/terminal/#ontitlechange)
-   [onWriteParsed](/docs/api/terminal/classes/terminal/#onwriteparsed)
-   [options](/docs/api/terminal/classes/terminal/#options)
-   [parser](/docs/api/terminal/classes/terminal/#readonly-parser)
-   [rows](/docs/api/terminal/classes/terminal/#readonly-rows)
-   [textarea](/docs/api/terminal/classes/terminal/#readonly-textarea)
-   [unicode](/docs/api/terminal/classes/terminal/#readonly-unicode)
-   [strings](/docs/api/terminal/classes/terminal/#static-strings)

### Methods

-   [attachCustomKeyEventHandler](/docs/api/terminal/classes/terminal/#attachcustomkeyeventhandler)
-   [attachCustomWheelEventHandler](/docs/api/terminal/classes/terminal/#attachcustomwheeleventhandler)
-   [blur](/docs/api/terminal/classes/terminal/#blur)
-   [clear](/docs/api/terminal/classes/terminal/#clear)
-   [clearSelection](/docs/api/terminal/classes/terminal/#clearselection)
-   [clearTextureAtlas](/docs/api/terminal/classes/terminal/#cleartextureatlas)
-   [deregisterCharacterJoiner](/docs/api/terminal/classes/terminal/#deregistercharacterjoiner)
-   [dispose](/docs/api/terminal/classes/terminal/#dispose)
-   [focus](/docs/api/terminal/classes/terminal/#focus)
-   [getSelection](/docs/api/terminal/classes/terminal/#getselection)
-   [getSelectionPosition](/docs/api/terminal/classes/terminal/#getselectionposition)
-   [hasSelection](/docs/api/terminal/classes/terminal/#hasselection)
-   [input](/docs/api/terminal/classes/terminal/#input)
-   [loadAddon](/docs/api/terminal/classes/terminal/#loadaddon)
-   [open](/docs/api/terminal/classes/terminal/#open)
-   [paste](/docs/api/terminal/classes/terminal/#paste)
-   [refresh](/docs/api/terminal/classes/terminal/#refresh)
-   [registerCharacterJoiner](/docs/api/terminal/classes/terminal/#registercharacterjoiner)
-   [registerDecoration](/docs/api/terminal/classes/terminal/#registerdecoration)
-   [registerLinkProvider](/docs/api/terminal/classes/terminal/#registerlinkprovider)
-   [registerMarker](/docs/api/terminal/classes/terminal/#registermarker)
-   [reset](/docs/api/terminal/classes/terminal/#reset)
-   [resize](/docs/api/terminal/classes/terminal/#resize)
-   [scrollLines](/docs/api/terminal/classes/terminal/#scrolllines)
-   [scrollPages](/docs/api/terminal/classes/terminal/#scrollpages)
-   [scrollToBottom](/docs/api/terminal/classes/terminal/#scrolltobottom)
-   [scrollToLine](/docs/api/terminal/classes/terminal/#scrolltoline)
-   [scrollToTop](/docs/api/terminal/classes/terminal/#scrolltotop)
-   [select](/docs/api/terminal/classes/terminal/#select)
-   [selectAll](/docs/api/terminal/classes/terminal/#selectall)
-   [selectLines](/docs/api/terminal/classes/terminal/#selectlines)
-   [write](/docs/api/terminal/classes/terminal/#write)
-   [writeln](/docs/api/terminal/classes/terminal/#writeln)

## Constructors

### constructor

\+ **new Terminal**(`options?`: [ITerminalOptions](/docs/api/terminal/interfaces/iterminaloptions/) & [ITerminalInitOnlyOptions](/docs/api/terminal/interfaces/iterminalinitonlyoptions/)): *[Terminal](/docs/api/terminal/classes/terminal/)*

*Defined in [xterm.d.ts:872](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L872)*

Creates a new `Terminal` object.

**Parameters:**

  Name                                                 Type                                                                                                                                                        Description
  ---------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------
  `options?`   [ITerminalOptions](/docs/api/terminal/interfaces/iterminaloptions/) & [ITerminalInitOnlyOptions](/docs/api/terminal/interfaces/iterminalinitonlyoptions/)   An object containing a set of options.

**Returns:** *[Terminal](/docs/api/terminal/classes/terminal/)*

## Properties

### `Readonly` buffer

• **buffer**: *[IBufferNamespace](/docs/api/terminal/interfaces/ibuffernamespace/)*

*Defined in [xterm.d.ts:809](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L809)*

Access to the terminal's normal and alt buffer.

------------------------------------------------------------------------

### `Readonly` cols

• **cols**: *number*

*Defined in [xterm.d.ts:804](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L804)*

The number of columns in the terminal's viewport. Use `ITerminalOptions.cols` to set this in the constructor and `Terminal.resize` for when the terminal exists.

------------------------------------------------------------------------

### `Readonly` element

  ------------------------------ -------------
  • **element**: \*HTMLElement   undefined\*
  ------------------------------ -------------

*Defined in [xterm.d.ts:785](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L785)*

The element containing the terminal.

------------------------------------------------------------------------

### `Readonly` markers

• **markers**: *ReadonlyArray‹[IMarker](/docs/api/terminal/interfaces/imarker/)›*

*Defined in [xterm.d.ts:815](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L815)*

(EXPERIMENTAL) Get all markers registered against the buffer. If the alt buffer is active this will always return \[\].

------------------------------------------------------------------------

### `Readonly` modes

• **modes**: *[IModes](/docs/api/terminal/interfaces/imodes/)*

*Defined in [xterm.d.ts:831](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L831)*

Gets the terminal modes as set by SM/DECSET.

------------------------------------------------------------------------

### onBell

• **onBell**: *[IEvent](/docs/api/terminal/interfaces/ievent/)‹void›*

*Defined in [xterm.d.ts:885](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L885)*

Adds an event listener for when the bell is triggered.

**`returns`** an `IDisposable` to stop listening.

------------------------------------------------------------------------

### onBinary

• **onBinary**: *[IEvent](/docs/api/terminal/interfaces/ievent/)‹string›*

*Defined in [xterm.d.ts:896](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L896)*

Adds an event listener for when a binary event fires. This is used to enable non UTF-8 conformant binary messages to be sent to the backend. Currently this is only used for a certain type of mouse reports that happen to be not UTF-8 compatible. The event value is a JS string, pass it to the underlying pty as binary data, e.g. `pty.write(Buffer.from(data, 'binary'))`.

**`returns`** an `IDisposable` to stop listening.

------------------------------------------------------------------------

### onCursorMove

• **onCursorMove**: *[IEvent](/docs/api/terminal/interfaces/ievent/)‹void›*

*Defined in [xterm.d.ts:902](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L902)*

Adds an event listener for the cursor moves.

**`returns`** an `IDisposable` to stop listening.

------------------------------------------------------------------------

### onData

• **onData**: *[IEvent](/docs/api/terminal/interfaces/ievent/)‹string›*

*Defined in [xterm.d.ts:911](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L911)*

Adds an event listener for when a data event fires. This happens for example when the user types or pastes into the terminal. The event value is whatever `string` results, in a typical setup, this should be passed on to the backing pty.

**`returns`** an `IDisposable` to stop listening.

------------------------------------------------------------------------

### onKey

• **onKey**: *[IEvent](/docs/api/terminal/interfaces/ievent/)‹object›*

*Defined in [xterm.d.ts:919](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L919)*

Adds an event listener for when a key is pressed. The event value contains the string that will be sent in the data event as well as the DOM event that triggered it.

**`returns`** an `IDisposable` to stop listening.

------------------------------------------------------------------------

### onLineFeed

• **onLineFeed**: *[IEvent](/docs/api/terminal/interfaces/ievent/)‹void›*

*Defined in [xterm.d.ts:925](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L925)*

Adds an event listener for when a line feed is added.

**`returns`** an `IDisposable` to stop listening.

------------------------------------------------------------------------

### onRender

• **onRender**: *[IEvent](/docs/api/terminal/interfaces/ievent/)‹object›*

*Defined in [xterm.d.ts:933](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L933)*

Adds an event listener for when rows are rendered. The event value contains the start row and end rows of the rendered area (ranges from `0` to `Terminal.rows - 1`).

**`returns`** an `IDisposable` to stop listening.

------------------------------------------------------------------------

### onResize

• **onResize**: *[IEvent](/docs/api/terminal/interfaces/ievent/)‹object›*

*Defined in [xterm.d.ts:951](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L951)*

Adds an event listener for when the terminal is resized. The event value contains the new size.

**`returns`** an `IDisposable` to stop listening.

------------------------------------------------------------------------

### onScroll

• **onScroll**: *[IEvent](/docs/api/terminal/interfaces/ievent/)‹number›*

*Defined in [xterm.d.ts:958](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L958)*

Adds an event listener for when a scroll occurs. The event value is the new position of the viewport.

**`returns`** an `IDisposable` to stop listening.

------------------------------------------------------------------------

### onSelectionChange

• **onSelectionChange**: *[IEvent](/docs/api/terminal/interfaces/ievent/)‹void›*

*Defined in [xterm.d.ts:964](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L964)*

Adds an event listener for when a selection change occurs.

**`returns`** an `IDisposable` to stop listening.

------------------------------------------------------------------------

### onTitleChange

• **onTitleChange**: *[IEvent](/docs/api/terminal/interfaces/ievent/)‹string›*

*Defined in [xterm.d.ts:971](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L971)*

Adds an event listener for when an OSC 0 or OSC 2 title change occurs. The event value is the new title.

**`returns`** an `IDisposable` to stop listening.

------------------------------------------------------------------------

### onWriteParsed

• **onWriteParsed**: *[IEvent](/docs/api/terminal/interfaces/ievent/)‹void›*

*Defined in [xterm.d.ts:944](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L944)*

Adds an event listener for when data has been parsed by the terminal, after [write](/docs/api/terminal/classes/terminal/#write) is called. This event is useful to listen for any changes in the buffer.

This fires at most once per frame, after data parsing completes. Note that this can fire when there are still writes pending if there is a lot of data.

------------------------------------------------------------------------

### options

• **options**: *[ITerminalOptions](/docs/api/terminal/interfaces/iterminaloptions/)*

*Defined in [xterm.d.ts:867](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L867)*

Gets or sets the terminal options. This supports setting multiple options.

**`example`** Get a single option

``` highlight
console.log(terminal.options.fontSize);
```

**`example`** Set a single option:

``` highlight
terminal.options.fontSize = 12;
```

Note that for options that are object, a new object must be used in order to take effect as a reference comparison will be done:

``` highlight
const newValue = terminal.options.theme;
newValue.background = '#000000';

// This won't work
terminal.options.theme = newValue;

// This will work
terminal.options.theme = ;
```

**`example`** Set multiple options

``` highlight
terminal.options = ;
```

------------------------------------------------------------------------

### `Readonly` parser

• **parser**: *[IParser](/docs/api/terminal/interfaces/iparser/)*

*Defined in [xterm.d.ts:820](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L820)*

Get the parser interface to register custom escape sequence handlers.

------------------------------------------------------------------------

### `Readonly` rows

• **rows**: *number*

*Defined in [xterm.d.ts:797](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L797)*

The number of rows in the terminal's viewport. Use `ITerminalOptions.rows` to set this in the constructor and `Terminal.resize` for when the terminal exists.

------------------------------------------------------------------------

### `Readonly` textarea

  --------------------------------------- -------------
  • **textarea**: \*HTMLTextAreaElement   undefined\*
  --------------------------------------- -------------

*Defined in [xterm.d.ts:790](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L790)*

The textarea that accepts input for the terminal.

------------------------------------------------------------------------

### `Readonly` unicode

• **unicode**: *[IUnicodeHandling](/docs/api/terminal/interfaces/iunicodehandling/)*

*Defined in [xterm.d.ts:826](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L826)*

(EXPERIMENTAL) Get the Unicode handling interface to register and switch Unicode version.

------------------------------------------------------------------------

### `Static` strings

▪ **strings**: *[ILocalizableStrings](/docs/api/terminal/interfaces/ilocalizablestrings/)*

*Defined in [xterm.d.ts:872](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L872)*

Natural language strings that can be localized.

## Methods

### attachCustomKeyEventHandler

▸ **attachCustomKeyEventHandler**(`customKeyEventHandler`: function): *void*

*Defined in [xterm.d.ts:1040](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1040)*

Attaches a custom key event handler which is run before keys are processed, giving consumers of xterm.js ultimate control as to what keys should be processed by the terminal and what keys should not.

**`example`** A custom keymap that overrides the backspace key

``` highlight
const keymap = [
  ,
  
];
term.attachCustomKeyEventHandler(ev => 
    }
  }
});
```

**Parameters:**

▪ **customKeyEventHandler**: *function*

The custom KeyboardEvent handler to attach. This is a function that takes a KeyboardEvent, allowing consumers to stop propagation and/or prevent the default action. The function returns whether the event should be processed by xterm.js.

▸ (`event`: KeyboardEvent): *boolean*

**Parameters:**

  Name                                              Type
  ------------------------------------------------- ---------------
  `event`   KeyboardEvent

**Returns:** *void*

------------------------------------------------------------------------

### attachCustomWheelEventHandler

▸ **attachCustomWheelEventHandler**(`customWheelEventHandler`: function): *void*

*Defined in [xterm.d.ts:1062](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1062)*

Attaches a custom wheel event handler which is run before keys are processed, giving consumers of xterm.js control over whether to proceed or cancel terminal wheel events.

**`example`** A handler that prevents all wheel events while ctrl is held from being processed.

``` highlight
term.attachCustomWheelEventHandler(ev => 
  return true;
});
```

**Parameters:**

▪ **customWheelEventHandler**: *function*

The custom WheelEvent handler to attach. This is a function that takes a WheelEvent, allowing consumers to stop propagation and/or prevent the default action. The function returns whether the event should be processed by xterm.js.

▸ (`event`: WheelEvent): *boolean*

**Parameters:**

  Name                                              Type
  ------------------------------------------------- ------------
  `event`   WheelEvent

**Returns:** *void*

------------------------------------------------------------------------

### blur

▸ **blur**(): *void*

*Defined in [xterm.d.ts:976](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L976)*

Unfocus the terminal.

**Returns:** *void*

------------------------------------------------------------------------

### clear

▸ **clear**(): *void*

*Defined in [xterm.d.ts:1206](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1206)*

Clear the entire buffer, making the prompt line the new first line.

**Returns:** *void*

------------------------------------------------------------------------

### clearSelection

▸ **clearSelection**(): *void*

*Defined in [xterm.d.ts:1146](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1146)*

Clears the current terminal selection.

**Returns:** *void*

------------------------------------------------------------------------

### clearTextureAtlas

▸ **clearTextureAtlas**(): *void*

*Defined in [xterm.d.ts:1249](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1249)*

Clears the texture atlas of the canvas renderer if it's active. Doing this will force a redraw of all glyphs which can workaround issues causing the texture to become corrupt, for example Chromium/Nvidia has an issue where the texture gets messed up when resuming the OS from sleep.

**Returns:** *void*

------------------------------------------------------------------------

### deregisterCharacterJoiner

▸ **deregisterCharacterJoiner**(`joinerId`: number): *void*

*Defined in [xterm.d.ts:1108](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1108)*

(EXPERIMENTAL) Deregisters the character joiner if one was registered. NOTE: character joiners are only used by the canvas renderer.

**Parameters:**

  Name                                                 Type     Description
  ---------------------------------------------------- -------- -----------------------------------------------------
  `joinerId`   number   The character joiner's ID (returned after register)

**Returns:** *void*

------------------------------------------------------------------------

### dispose

▸ **dispose**(): *void*

*Implementation of [IDisposable](/docs/api/terminal/interfaces/idisposable/)*

*Defined in [xterm.d.ts:1173](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1173)*

**Returns:** *void*

------------------------------------------------------------------------

### focus

▸ **focus**(): *void*

*Defined in [xterm.d.ts:981](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L981)*

Focus the terminal.

**Returns:** *void*

------------------------------------------------------------------------

### getSelection

▸ **getSelection**(): *string*

*Defined in [xterm.d.ts:1136](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1136)*

Gets the terminal's current selection, this is useful for implementing copy behavior outside of xterm.js.

**Returns:** *string*

------------------------------------------------------------------------

### getSelectionPosition

  --------------------------------------------------------------------------------------------- -------------
  ▸ **getSelectionPosition**(): \*[IBufferRange](/docs/api/terminal/interfaces/ibufferrange/)   undefined\*
  --------------------------------------------------------------------------------------------- -------------

*Defined in [xterm.d.ts:1141](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1141)*

Gets the selection position or undefined if there is no selection.

  ---------------------------------------------------------------------------- -------------
  **Returns:** \*[IBufferRange](/docs/api/terminal/interfaces/ibufferrange/)   undefined\*
  ---------------------------------------------------------------------------- -------------

------------------------------------------------------------------------

### hasSelection

▸ **hasSelection**(): *boolean*

*Defined in [xterm.d.ts:1130](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1130)*

Gets whether the terminal has an active selection.

**Returns:** *boolean*

------------------------------------------------------------------------

### input

▸ **input**(`data`: string, `wasUserInput?`: boolean): *void*

*Defined in [xterm.d.ts:993](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L993)*

Input data to application side. The data is treated the same way input typed into the terminal would (ie. the [onData](/docs/api/terminal/classes/terminal/#ondata) event will fire).

**Parameters:**

  Name                                                      Type      Description
  --------------------------------------------------------- --------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `data`            string    The data to forward to the application.
  `wasUserInput?`   boolean   Whether the input is genuine user input. This is true by default and triggers additionalbehavior like focus or selection clearing. Set this to false if the data sent should not be treated like user input would, for example passing an escape sequence to the application.

**Returns:** *void*

------------------------------------------------------------------------

### loadAddon

▸ **loadAddon**(`addon`: [ITerminalAddon](/docs/api/terminal/interfaces/iterminaladdon/)): *void*

*Defined in [xterm.d.ts:1260](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1260)*

Loads an addon into this instance of xterm.js.

**Parameters:**

  Name                                              Type                                                              Description
  ------------------------------------------------- ----------------------------------------------------------------- --------------------
  `addon`   [ITerminalAddon](/docs/api/terminal/interfaces/iterminaladdon/)   The addon to load.

**Returns:** *void*

------------------------------------------------------------------------

### open

▸ **open**(`parent`: HTMLElement): *void*

*Defined in [xterm.d.ts:1011](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1011)*

Opens the terminal within an element. This should also be called if the xterm.js element ever changes browser window.

**Parameters:**

  Name                                               Type          Description
  -------------------------------------------------- ------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `parent`   HTMLElement   The element to create the terminal within. This element must be visible (have dimensions) when `open` is called as several DOM- based measurements need to be performed when this function is called.

**Returns:** *void*

------------------------------------------------------------------------

### paste

▸ **paste**(`data`: string): *void*

*Defined in [xterm.d.ts:1233](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1233)*

Writes text to the terminal, performing the necessary transformations for pasted text.

**Parameters:**

  Name                                             Type     Description
  ------------------------------------------------ -------- ------------------------------------
  `data`   string   The text to write to the terminal.

**Returns:** *void*

------------------------------------------------------------------------

### refresh

▸ **refresh**(`start`: number, `end`: number): *void*

*Defined in [xterm.d.ts:1241](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1241)*

Tells the renderer to refresh terminal content between two rows (inclusive) at the next opportunity.

**Parameters:**

  Name                                              Type     Description
  ------------------------------------------------- -------- ------------------------------------------------------
  `start`   number   The row to start from (between 0 and this.rows - 1).
  `end`     number   The row to end at (between start and this.rows - 1).

**Returns:** *void*

------------------------------------------------------------------------

### registerCharacterJoiner

▸ **registerCharacterJoiner**(`handler`: function): *number*

*Defined in [xterm.d.ts:1101](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1101)*

(EXPERIMENTAL) Registers a character joiner, allowing custom sequences of characters to be rendered as a single unit. This is useful in particular for rendering ligatures and graphemes, among other things.

Each registered character joiner is called with a string of text representing a portion of a line in the terminal that can be rendered as a single unit. The joiner must return a sorted array, where each entry is itself an array of length two, containing the start (inclusive) and end (exclusive) index of a substring of the input that should be rendered as a single unit. When multiple joiners are provided, the results of each are collected. If there are any overlapping substrings between them, they are combined into one larger unit that is drawn together.

All character joiners that are registered get called every time a line is rendered in the terminal, so it is essential for the handler function to run as quickly as possible to avoid slowdowns when rendering. Similarly, joiners should strive to return the smallest possible substrings to render together, since they aren't drawn as optimally as individual characters.

NOTE: character joiners are only used by the canvas renderer.

**Parameters:**

▪ **handler**: *function*

The function that determines character joins. It is called with a string of text that is eligible for joining and returns an array where each entry is an array containing the start (inclusive) and end (exclusive) indexes of ranges that should be rendered as a single unit.

▸ (`text`: string): *\[\]\[\]*

**Parameters:**

  Name                                             Type
  ------------------------------------------------ --------
  `text`   string

**Returns:** *number*

The ID of the new joiner, this can be used to deregister

------------------------------------------------------------------------

### registerDecoration

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------
  ▸ **registerDecoration**(`decorationOptions`: [IDecorationOptions](/docs/api/terminal/interfaces/idecorationoptions/)): \*[IDecoration](/docs/api/terminal/interfaces/idecoration/)   undefined\*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------

*Defined in [xterm.d.ts:1125](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1125)*

(EXPERIMENTAL) Adds a decoration to the terminal using

**`throws`** when options include a negative x offset.

**Parameters:**

  Name                                                          Type
  ------------------------------------------------------------- -------------------------------------------------------------------------
  `decorationOptions`   [IDecorationOptions](/docs/api/terminal/interfaces/idecorationoptions/)

  -------------------------------------------------------------------------- -------------
  **Returns:** \*[IDecoration](/docs/api/terminal/interfaces/idecoration/)   undefined\*
  -------------------------------------------------------------------------- -------------

------------------------------------------------------------------------

### registerLinkProvider

▸ **registerLinkProvider**(`linkProvider`: [ILinkProvider](/docs/api/terminal/interfaces/ilinkprovider/)): *[IDisposable](/docs/api/terminal/interfaces/idisposable/)*

*Defined in [xterm.d.ts:1070](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1070)*

Registers a link provider, allowing a custom parser to be used to match and handle links. Multiple link providers can be used, they will be asked in the order in which they are registered.

**Parameters:**

  Name                                                     Type                                                            Description
  -------------------------------------------------------- --------------------------------------------------------------- -------------------------------------------
  `linkProvider`   [ILinkProvider](/docs/api/terminal/interfaces/ilinkprovider/)   The link provider to use to detect links.

**Returns:** *[IDisposable](/docs/api/terminal/interfaces/idisposable/)*

------------------------------------------------------------------------

### registerMarker

▸ **registerMarker**(`cursorYOffset?`: number): *[IMarker](/docs/api/terminal/interfaces/imarker/)*

*Defined in [xterm.d.ts:1115](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1115)*

Adds a marker to the normal buffer and returns it.

**Parameters:**

  Name                                                       Type     Description
  ---------------------------------------------------------- -------- ------------------------------------------------------
  `cursorYOffset?`   number   The y position offset of the marker from the cursor.

**Returns:** *[IMarker](/docs/api/terminal/interfaces/imarker/)*

The new marker or undefined.

------------------------------------------------------------------------

### reset

▸ **reset**(): *void*

*Defined in [xterm.d.ts:1254](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1254)*

Perform a full reset (RIS, aka '\\x1bc').

**Returns:** *void*

------------------------------------------------------------------------

### resize

▸ **resize**(`columns`: number, `rows`: number): *void*

*Defined in [xterm.d.ts:1002](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1002)*

Resizes the terminal. It's best practice to debounce calls to resize, this will help ensure that the pty can respond to the resize event before another one occurs.

**Parameters:**

  Name                                                Type
  --------------------------------------------------- --------
  `columns`   number
  `rows`      number

**Returns:** *void*

------------------------------------------------------------------------

### scrollLines

▸ **scrollLines**(`amount`: number): *void*

*Defined in [xterm.d.ts:1179](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1179)*

Scroll the display of the terminal

**Parameters:**

  Name                                               Type     Description
  -------------------------------------------------- -------- ----------------------------------------------------------
  `amount`   number   The number of lines to scroll down (negative scroll up).

**Returns:** *void*

------------------------------------------------------------------------

### scrollPages

▸ **scrollPages**(`pageCount`: number): *void*

*Defined in [xterm.d.ts:1185](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1185)*

Scroll the display of the terminal by a number of pages.

**Parameters:**

  Name                                                  Type     Description
  ----------------------------------------------------- -------- ------------------------------------------------------
  `pageCount`   number   The number of pages to scroll (negative scrolls up).

**Returns:** *void*

------------------------------------------------------------------------

### scrollToBottom

▸ **scrollToBottom**(): *void*

*Defined in [xterm.d.ts:1195](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1195)*

Scrolls the display of the terminal to the bottom.

**Returns:** *void*

------------------------------------------------------------------------

### scrollToLine

▸ **scrollToLine**(`line`: number): *void*

*Defined in [xterm.d.ts:1201](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1201)*

Scrolls to a line within the buffer.

**Parameters:**

  Name                                             Type     Description
  ------------------------------------------------ -------- --------------------------------------
  `line`   number   The 0-based line index to scroll to.

**Returns:** *void*

------------------------------------------------------------------------

### scrollToTop

▸ **scrollToTop**(): *void*

*Defined in [xterm.d.ts:1190](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1190)*

Scrolls the display of the terminal to the top.

**Returns:** *void*

------------------------------------------------------------------------

### select

▸ **select**(`column`: number, `row`: number, `length`: number): *void*

*Defined in [xterm.d.ts:1154](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1154)*

Selects text within the terminal.

**Parameters:**

  Name                                               Type     Description
  -------------------------------------------------- -------- -------------------------------------
  `column`   number   The column the selection starts at.
  `row`      number   The row the selection starts at.
  `length`   number   The length of the selection.

**Returns:** *void*

------------------------------------------------------------------------

### selectAll

▸ **selectAll**(): *void*

*Defined in [xterm.d.ts:1159](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1159)*

Selects all text within the terminal.

**Returns:** *void*

------------------------------------------------------------------------

### selectLines

▸ **selectLines**(`start`: number, `end`: number): *void*

*Defined in [xterm.d.ts:1166](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1166)*

Selects text in the buffer between 2 lines.

**Parameters:**

  Name                                              Type     Description
  ------------------------------------------------- -------- ----------------------------------------------------
  `start`   number   The 0-based line index to select from (inclusive).
  `end`     number   The 0-based line index to select to (inclusive).

**Returns:** *void*

------------------------------------------------------------------------

### write

  -------------------------------------------------------------------- ------------------------------------------------------------------------------------
  ▸ **write**(`data`: string   Uint8Array, `callback?`: function): *void*
  -------------------------------------------------------------------- ------------------------------------------------------------------------------------

*Defined in [xterm.d.ts:1216](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1216)*

Write data to the terminal.

**Parameters:**

  ---------------------- --------------
  ▪ **data**: \*string   Uint8Array\*
  ---------------------- --------------

The data to write to the terminal. This can either be raw bytes given as Uint8Array from the pty or a string. Raw bytes will always be treated as UTF-8 encoded, string data as UTF-16.

▪`Optional` **callback**: *function*

Optional callback that fires when the data was processed by the parser.

▸ (): *void*

**Returns:** *void*

------------------------------------------------------------------------

### writeln

  ---------------------------------------------------------------------- ------------------------------------------------------------------------------------
  ▸ **writeln**(`data`: string   Uint8Array, `callback?`: function): *void*
  ---------------------------------------------------------------------- ------------------------------------------------------------------------------------

*Defined in [xterm.d.ts:1226](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L1226)*

Writes data to the terminal, followed by a break line character (\\n).

**Parameters:**

  ---------------------- --------------
  ▪ **data**: \*string   Uint8Array\*
  ---------------------- --------------

The data to write to the terminal. This can either be raw bytes given as Uint8Array from the pty or a string. Raw bytes will always be treated as UTF-8 encoded, string data as UTF-16.

▪`Optional` **callback**: *function*

Optional callback that fires when the data was processed by the parser.

▸ (): *void*

**Returns:** *void*