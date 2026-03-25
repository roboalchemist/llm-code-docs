iced
# Module advanced 
Source Available on **crate feature `advanced`** only.
## Re-exports§
`pub use crate::renderer::graphics;`
## Modules§
clipboardAccess the clipboard.imageLoad and draw raster graphics.input_methodListen to input method events.layoutPosition your widgets properly.mouseHandle mouse events.overlayDisplay interactive elements on top of other widgets.rendererWrite your own renderer.subscriptionWrite your own subscriptions.svgLoad and draw vector graphics.textDraw and interact with text.widgetCreate custom widgets and operate on them.
## Structs§
LayoutThe bounds of a `Node` and its children, using absolute coordinates.ShellA connection to the state of a shell.TextA paragraph.
## Enums§
InputMethodThe input method strategy of a widget.
## Traits§
ClipboardA buffer for short-term storage and transfer within and between
applications.OverlayAn interactive component that can be displayed on top of other widgets.RendererA component that can be used by widgets to draw themselves on a screen.WidgetA component that displays information and allows interaction.