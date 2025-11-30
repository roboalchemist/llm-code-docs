# Source: https://www.electronjs.org/docs/latest/tutorial/custom-window-interactions

On this page

# Custom Window Interactions

## Custom draggable regions[â€‹](#custom-draggable-regions "Direct link to Custom draggable regions") 

By default, windows are dragged using the title bar provided by the OS chrome. Apps that remove the default title bar need to use the `app-region` CSS property to define specific areas that can be used to drag the window. Setting `app-region: drag` marks a rectagular area as draggable.

It is important to note that draggable areas ignore all pointer events. For example, a button element that overlaps a draggable region will not emit mouse clicks or mouse enter/exit events within that overlapping area. Setting `app-region: no-drag` reenables pointer events by excluding a rectagular area from a draggable region.

To make the whole window draggable, you can add `app-region: drag` as `body`\'s style:

styles.css

``` 
body 
```

And note that if you have made the whole window draggable, you must also mark buttons as non-draggable, otherwise it would be impossible for users to click on them:

styles.css

``` 
button 
```

If you\'re only setting a custom title bar as draggable, you also need to make all buttons in title bar non-draggable.

### Tip: disable text selection[â€‹](#tip-disable-text-selection "Direct link to Tip: disable text selection") 

When creating a draggable region, the dragging behavior may conflict with text selection. For example, when you drag the title bar, you may accidentally select its text contents. To prevent this, you need to disable text selection within a draggable area like this:

``` 
.titlebar 
```

### Tip: disable context menus[â€‹](#tip-disable-context-menus "Direct link to Tip: disable context menus") 

On some platforms, the draggable area will be treated as a non-client frame, so when you right click on it, a system menu will pop up. To make the context menu behave correctly on all platforms, you should never use a custom context menu on draggable areas.

## Click-through windows[â€‹](#click-through-windows "Direct link to Click-through windows") 

To create a click-through window, i.e. making the window ignore all mouse events, you can call the [win.setIgnoreMouseEvents(ignore)](/docs/latest/api/browser-window#winsetignoremouseeventsignore-options) API:

main.js

``` 
const  = require('electron')

const win = new BrowserWindow()
win.setIgnoreMouseEvents(true)
```

### Forward mouse events *macOS* *Windows*[â€‹](#forward-mouse-events-macos-windows "Direct link to forward-mouse-events-macos-windows") 

Ignoring mouse messages makes the web contents oblivious to mouse movement, meaning that mouse movement events will not be emitted. On Windows and macOS, an optional parameter can be used to forward mouse move messages to the web page, allowing events such as `mouseleave` to be emitted:

main.js

``` 
const  = require('electron')

const path = require('node:path')

const win = new BrowserWindow(
})

ipcMain.on('set-ignore-mouse-events', (event, ignore, options) => )
```

preload.js

``` 
window.addEventListener('DOMContentLoaded', () => )
  })
  el.addEventListener('mouseleave', () => )
})
```

This makes the web page click-through when over the `#clickThroughElement` element, and returns to normal outside it.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/tutorial/custom-window-interactions.md)