# Source: https://www.electronjs.org/docs/latest/api/screen

On this page

# screen

> Retrieve information about screen size, displays, cursor position, etc.

Process: [Main](/docs/latest/glossary#main-process)

This module cannot be used until the `ready` event of the `app` module is emitted.

`screen` is an [EventEmitter](https://nodejs.org/api/events.html#events_class_eventemitter).

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

In the renderer / DevTools, `window.screen` is a reserved DOM property, so writing `let  = require('electron')` will not work.

An example of creating a window that fills the whole screen:

[][][]

[docs/fiddles/screen/fit-screen (39.2.4)](https://github.com/electron/electron/tree/v39.2.4/docs/fiddles/screen/fit-screen)[Open in Fiddle](https://fiddle.electronjs.org/launch?target=electron/v39.2.4/docs/fiddles/screen/fit-screen)

- main.js

``` 
// Retrieve information about screen size, displays, cursor position, etc.
//
// For more info, see:
// https://www.electronjs.org/docs/latest/api/screen

const  = require('electron/main')

let mainWindow = null

app.whenReady().then(() =>  = primaryDisplay.workAreaSize

  mainWindow = new BrowserWindow()
  mainWindow.loadURL('https://electronjs.org')
})
```

Another example of creating a window in the external display:

``` 
const  = require('electron')

let win

app.whenReady().then(() => )

  if (externalDisplay) )
    win.loadURL('https://github.com')
  }
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

Screen coordinates used by this module are [Point](/docs/latest/api/structures/point) structures. There are two kinds of coordinates available to the process:

- **Physical screen points** are raw hardware pixels on a display.
- **Device-independent pixel (DIP) points** are virtualized screen points scaled based on the DPI (dots per inch) of the display.

## Events[â€‹](#events "Direct link to Events") 

The `screen` module emits the following events:

### Event: \'display-added\'[â€‹](#event-display-added "Direct link to Event: 'display-added'") 

Returns:

- `event` Event
- `newDisplay` [Display](/docs/latest/api/structures/display)

Emitted when `newDisplay` has been added.

### Event: \'display-removed\'[â€‹](#event-display-removed "Direct link to Event: 'display-removed'") 

Returns:

- `event` Event
- `oldDisplay` [Display](/docs/latest/api/structures/display)

Emitted when `oldDisplay` has been removed.

### Event: \'display-metrics-changed\'[â€‹](#event-display-metrics-changed "Direct link to Event: 'display-metrics-changed'") 

Returns:

- `event` Event
- `display` [Display](/docs/latest/api/structures/display)
- `changedMetrics` string\[\]

Emitted when one or more metrics change in a `display`. The `changedMetrics` is an array of strings that describe the changes. Possible changes are `bounds`, `workArea`, `scaleFactor` and `rotation`.

## Methods[â€‹](#methods "Direct link to Methods") 

The `screen` module has the following methods:

### `screen.getCursorScreenPoint()`[â€‹](#screengetcursorscreenpoint "Direct link to screengetcursorscreenpoint") 

Returns [Point](/docs/latest/api/structures/point)

The current absolute position of the mouse pointer.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

The return value is a DIP point, not a screen physical point.

### `screen.getPrimaryDisplay()`[â€‹](#screengetprimarydisplay "Direct link to screengetprimarydisplay") 

Returns [Display](/docs/latest/api/structures/display) - The primary display.

### `screen.getAllDisplays()`[â€‹](#screengetalldisplays "Direct link to screengetalldisplays") 

Returns [Display\[\]](/docs/latest/api/structures/display) - An array of displays that are currently available.

### `screen.getDisplayNearestPoint(point)`[â€‹](#screengetdisplaynearestpointpoint "Direct link to screengetdisplaynearestpointpoint") 

- `point` [Point](/docs/latest/api/structures/point)

Returns [Display](/docs/latest/api/structures/display) - The display nearest the specified point.

### `screen.getDisplayMatching(rect)`[â€‹](#screengetdisplaymatchingrect "Direct link to screengetdisplaymatchingrect") 

- `rect` [Rectangle](/docs/latest/api/structures/rectangle)

Returns [Display](/docs/latest/api/structures/display) - The display that most closely intersects the provided bounds.

### `screen.screenToDipPoint(point)` *Windows* *Linux*[â€‹](#screenscreentodippointpoint-windows-linux "Direct link to screenscreentodippointpoint-windows-linux") 

- `point` [Point](/docs/latest/api/structures/point)

Returns [Point](/docs/latest/api/structures/point)

Converts a screen physical point to a screen DIP point. The DPI scale is performed relative to the display containing the physical point.

Not currently supported on Wayland - if used there it will return the point passed in with no changes.

### `screen.dipToScreenPoint(point)` *Windows* *Linux*[â€‹](#screendiptoscreenpointpoint-windows-linux "Direct link to screendiptoscreenpointpoint-windows-linux") 

- `point` [Point](/docs/latest/api/structures/point)

Returns [Point](/docs/latest/api/structures/point)

Converts a screen DIP point to a screen physical point. The DPI scale is performed relative to the display containing the DIP point.

Not currently supported on Wayland.

### `screen.screenToDipRect(window, rect)` *Windows*[â€‹](#screenscreentodiprectwindow-rect-windows "Direct link to screenscreentodiprectwindow-rect-windows") 

- `window` [BrowserWindow](/docs/latest/api/browser-window) \| null
- `rect` [Rectangle](/docs/latest/api/structures/rectangle)

Returns [Rectangle](/docs/latest/api/structures/rectangle)

Converts a screen physical rect to a screen DIP rect. The DPI scale is performed relative to the display nearest to `window`. If `window` is null, scaling will be performed to the display nearest to `rect`.

### `screen.dipToScreenRect(window, rect)` *Windows*[â€‹](#screendiptoscreenrectwindow-rect-windows "Direct link to screendiptoscreenrectwindow-rect-windows") 

- `window` [BrowserWindow](/docs/latest/api/browser-window) \| null
- `rect` [Rectangle](/docs/latest/api/structures/rectangle)

Returns [Rectangle](/docs/latest/api/structures/rectangle)

Converts a screen DIP rect to a screen physical rect. The DPI scale is performed relative to the display nearest to `window`. If `window` is null, scaling will be performed to the display nearest to `rect`.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/screen.md)