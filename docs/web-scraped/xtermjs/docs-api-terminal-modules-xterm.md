# Source: https://xtermjs.org/docs/api/terminal/modules/xterm/

<div>

</div>

# Module: "xterm"

**`license`** MIT

This contains the type declarations for the xterm.js library. Note that some interfaces differ between this file and the actual implementation in src/, that's because this file declares the *public* API which is intended to be stable and consumed by external programs.

## Index

### Classes

-   [Terminal](/docs/api/terminal/classes/terminal/)

### Interfaces

-   [IBuffer](/docs/api/terminal/interfaces/ibuffer/)
-   [IBufferCell](/docs/api/terminal/interfaces/ibuffercell/)
-   [IBufferCellPosition](/docs/api/terminal/interfaces/ibuffercellposition/)
-   [IBufferElementProvider](/docs/api/terminal/interfaces/ibufferelementprovider/)
-   [IBufferLine](/docs/api/terminal/interfaces/ibufferline/)
-   [IBufferNamespace](/docs/api/terminal/interfaces/ibuffernamespace/)
-   [IBufferRange](/docs/api/terminal/interfaces/ibufferrange/)
-   [IDecoration](/docs/api/terminal/interfaces/idecoration/)
-   [IDecorationOptions](/docs/api/terminal/interfaces/idecorationoptions/)
-   [IDecorationOverviewRulerOptions](/docs/api/terminal/interfaces/idecorationoverviewruleroptions/)
-   [IDisposable](/docs/api/terminal/interfaces/idisposable/)
-   [IDisposableWithEvent](/docs/api/terminal/interfaces/idisposablewithevent/)
-   [IEvent](/docs/api/terminal/interfaces/ievent/)
-   [IFunctionIdentifier](/docs/api/terminal/interfaces/ifunctionidentifier/)
-   [ILink](/docs/api/terminal/interfaces/ilink/)
-   [ILinkDecorations](/docs/api/terminal/interfaces/ilinkdecorations/)
-   [ILinkHandler](/docs/api/terminal/interfaces/ilinkhandler/)
-   [ILinkProvider](/docs/api/terminal/interfaces/ilinkprovider/)
-   [ILocalizableStrings](/docs/api/terminal/interfaces/ilocalizablestrings/)
-   [ILogger](/docs/api/terminal/interfaces/ilogger/)
-   [IMarker](/docs/api/terminal/interfaces/imarker/)
-   [IModes](/docs/api/terminal/interfaces/imodes/)
-   [IParser](/docs/api/terminal/interfaces/iparser/)
-   [ITerminalAddon](/docs/api/terminal/interfaces/iterminaladdon/)
-   [ITerminalInitOnlyOptions](/docs/api/terminal/interfaces/iterminalinitonlyoptions/)
-   [ITerminalOptions](/docs/api/terminal/interfaces/iterminaloptions/)
-   [ITheme](/docs/api/terminal/interfaces/itheme/)
-   [IUnicodeHandling](/docs/api/terminal/interfaces/iunicodehandling/)
-   [IUnicodeVersionProvider](/docs/api/terminal/interfaces/iunicodeversionprovider/)
-   [IViewportRange](/docs/api/terminal/interfaces/iviewportrange/)
-   [IViewportRangePosition](/docs/api/terminal/interfaces/iviewportrangeposition/)
-   [IWindowOptions](/docs/api/terminal/interfaces/iwindowoptions/)
-   [IWindowsPty](/docs/api/terminal/interfaces/iwindowspty/)

### Type aliases

-   [FontWeight](/docs/api/terminal/modules/xterm/#fontweight)
-   [LogLevel](/docs/api/terminal/modules/xterm/#loglevel)

## Type aliases

### FontWeight

  ------------------------------ -------- ------- ------- ------- ------- ------- ------- ------- ------- ------- ----------
  Ƭ **FontWeight**: \*"normal"   "bold"   "100"   "200"   "300"   "400"   "500"   "600"   "700"   "800"   "900"   number\*
  ------------------------------ -------- ------- ------- ------- ------- ------- ------- ------- ------- ------- ----------

*Defined in [xterm.d.ts:16](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L16)*

A string or number representing text font weight.

------------------------------------------------------------------------

### LogLevel

  --------------------------- --------- -------- -------- --------- ---------
  Ƭ **LogLevel**: \*"trace"   "debug"   "info"   "warn"   "error"   "off"\*
  --------------------------- --------- -------- -------- --------- ---------

*Defined in [xterm.d.ts:21](https://github.com/xtermjs/xterm.js/blob/5.5.0/typings/xterm.d.ts#L21)*

A string representing log level.