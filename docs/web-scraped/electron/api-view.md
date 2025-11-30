# Source: https://www.electronjs.org/docs/latest/api/view

On this page

# View

> Create and layout native views.

Process: [Main](/docs/latest/glossary#main-process)

This module cannot be used until the `ready` event of the `app` module is emitted.

``` 
const  = require('electron')

const win = new BaseWindow()
const view = new View()

view.setBackgroundColor('red')
view.setBounds()
win.contentView.addChildView(view)
```

## Class: View[â€‹](#class-view "Direct link to Class: View") 

> A basic native view.

Process: [Main](/docs/latest/glossary#main-process)

`View` is an [EventEmitter](https://nodejs.org/api/events.html#events_class_eventemitter).

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)]warning

Electron\'s built-in classes cannot be subclassed in user code. For more information, see [the FAQ](/docs/latest/faq#class-inheritance-does-not-work-with-electron-built-in-modules).

### `new View()`[â€‹](#new-view "Direct link to new-view") 

Creates a new `View`.

### Instance Events[â€‹](#instance-events "Direct link to Instance Events") 

Objects created with `new View` emit the following events:

#### Event: \'bounds-changed\'[â€‹](#event-bounds-changed "Direct link to Event: 'bounds-changed'") 

Emitted when the view\'s bounds have changed in response to being laid out. The new bounds can be retrieved with [`view.getBounds()`](#viewgetbounds).

### Instance Methods[â€‹](#instance-methods "Direct link to Instance Methods") 

Objects created with `new View` have the following instance methods:

#### `view.addChildView(view[, index])`[â€‹](#viewaddchildviewview-index "Direct link to viewaddchildviewview-index") 

- `view` View - Child view to add.
- `index` Integer (optional) - Index at which to insert the child view. Defaults to adding the child at the end of the child list.

If the same View is added to a parent which already contains it, it will be reordered such that it becomes the topmost view.

#### `view.removeChildView(view)`[â€‹](#viewremovechildviewview "Direct link to viewremovechildviewview") 

- `view` View - Child view to remove.

If the view passed as a parameter is not a child of this view, this method is a no-op.

#### `view.setBounds(bounds)`[â€‹](#viewsetboundsbounds "Direct link to viewsetboundsbounds") 

- `bounds` [Rectangle](/docs/latest/api/structures/rectangle) - New bounds of the View.

#### `view.getBounds()`[â€‹](#viewgetbounds "Direct link to viewgetbounds") 

Returns [Rectangle](/docs/latest/api/structures/rectangle) - The bounds of this View, relative to its parent.

#### `view.setBackgroundColor(color)`[â€‹](#viewsetbackgroundcolorcolor "Direct link to viewsetbackgroundcolorcolor") 

- `color` string - Color in Hex, RGB, ARGB, HSL, HSLA or named CSS color format. The alpha channel is optional for the hex type.

Examples of valid `color` values:

- Hex
  - `#fff` (RGB)
  - `#ffff` (ARGB)
  - `#ffffff` (RRGGBB)
  - `#ffffffff` (AARRGGBB)
- RGB
  - `rgb\(([\d]+),\s*([\d]+),\s*([\d]+)\)`
    - e.g. `rgb(255, 255, 255)`
- RGBA
  - `rgba\(([\d]+),\s*([\d]+),\s*([\d]+),\s*([\d.]+)\)`
    - e.g. `rgba(255, 255, 255, 1.0)`
- HSL
  - `hsl\((-?[\d.]+),\s*([\d.]+)%,\s*([\d.]+)%\)`
    - e.g. `hsl(200, 20%, 50%)`
- HSLA
  - `hsla\((-?[\d.]+),\s*([\d.]+)%,\s*([\d.]+)%,\s*([\d.]+)\)`
    - e.g. `hsla(200, 20%, 50%, 0.5)`
- Color name
  - Options are listed in [SkParseColor.cpp](https://source.chromium.org/chromium/chromium/src/+/main:third_party/skia/src/utils/SkParseColor.cpp;l=11-152;drc=eea4bf52cb0d55e2a39c828b017c80a5ee054148)
  - Similar to CSS Color Module Level 3 keywords, but case-sensitive.
    - e.g. `blueviolet` or `red`

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

Hex format with alpha takes `AARRGGBB` or `ARGB`, *not* `RRGGBBAA` or `RGB`.

#### `view.setBorderRadius(radius)`[â€‹](#viewsetborderradiusradius "Direct link to viewsetborderradiusradius") 

- `radius` Integer - Border radius size in pixels.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

The area cutout of the view\'s border still captures clicks.

#### `view.setVisible(visible)`[â€‹](#viewsetvisiblevisible "Direct link to viewsetvisiblevisible") 

- `visible` boolean - If false, the view will be hidden from display.

#### `view.getVisible()`[â€‹](#viewgetvisible "Direct link to viewgetvisible") 

Returns `boolean` - Whether the view should be drawn. Note that this is different from whether the view is visible on screenâ€"it may still be obscured or out of view.

### Instance Properties[â€‹](#instance-properties "Direct link to Instance Properties") 

Objects created with `new View` have the following properties:

#### `view.children` *Readonly*[â€‹](#viewchildren-readonly "Direct link to viewchildren-readonly") 

A `View[]` property representing the child views of this view.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/view.md)