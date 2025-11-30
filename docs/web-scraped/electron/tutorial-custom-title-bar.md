# Source: https://www.electronjs.org/docs/latest/tutorial/custom-title-bar

On this page

# Custom Title Bar

## Basic tutorial[â€‹](#basic-tutorial "Direct link to Basic tutorial") 

Application windows have a default [chrome](https://developer.mozilla.org/en-US/docs/Glossary/Chrome) applied by the OS. Not to be confused with the Google Chrome browser, windowÂ *chrome*Â refers to the parts of the window (e.g. title bar, toolbars, controls) that are not a part of the main web content. While the default title bar provided by the OS chrome is sufficient for simple use cases, many applications opt to remove it. Implementing a custom title bar can help your application feel more modern and consistent across platforms.

You can follow along with this tutorial by opening Fiddle with the following starter code.

[][][]

[docs/fiddles/features/window-customization/custom-title-bar/starter-code (39.2.4)](https://github.com/electron/electron/tree/v39.2.4/docs/fiddles/features/window-customization/custom-title-bar/starter-code)[Open in Fiddle](https://fiddle.electronjs.org/launch?target=electron/v39.2.4/docs/fiddles/features/window-customization/custom-title-bar/starter-code)

- main.js

``` 
const  = require('electron')

function createWindow () )
  win.loadURL('https://example.com')
}

app.whenReady().then(() => )
```

### Remove the default title bar[â€‹](#remove-the-default-title-bar "Direct link to Remove the default title bar") 

Letâ€™s start by configuring a window with native window controls and a hidden title bar. To remove the default title bar, set the [BaseWindowContructorOptions](/docs/latest/api/structures/base-window-options) `titleBarStyle` param in theÂ `BrowserWindow`Â constructor to `'hidden'`.

[][][]

[docs/fiddles/features/window-customization/custom-title-bar/remove-title-bar (39.2.4)](https://github.com/electron/electron/tree/v39.2.4/docs/fiddles/features/window-customization/custom-title-bar/remove-title-bar)[Open in Fiddle](https://fiddle.electronjs.org/launch?target=electron/v39.2.4/docs/fiddles/features/window-customization/custom-title-bar/remove-title-bar)

- main.js

``` 
const  = require('electron')

function createWindow () )
  win.loadURL('https://example.com')
}

app.whenReady().then(() => )
```

### Add native window controls *Windows* *Linux*[â€‹](#add-native-window-controls-windows-linux "Direct link to add-native-window-controls-windows-linux") 

On macOS, setting `titleBarStyle: 'hidden'` removes the title bar while keeping the windowâ€™s traffic light controls available in the upper left hand corner. However on Windows and Linux, youâ€™ll need to add window controls back into your `BrowserWindow` by setting the [BaseWindowContructorOptions](/docs/latest/api/structures/base-window-options) `titleBarOverlay` param in theÂ `BrowserWindow`Â constructor.

[][][]

[docs/fiddles/features/window-customization/custom-title-bar/native-window-controls (39.2.4)](https://github.com/electron/electron/tree/v39.2.4/docs/fiddles/features/window-customization/custom-title-bar/native-window-controls)[Open in Fiddle](https://fiddle.electronjs.org/launch?target=electron/v39.2.4/docs/fiddles/features/window-customization/custom-title-bar/native-window-controls)

- main.js

``` 
const  = require('electron')

function createWindow ()  : )
  })
  win.loadURL('https://example.com')
}

app.whenReady().then(() => )
```

Setting `titleBarOverlay: true` is the simplest way to expose window controls back into your `BrowserWindow`. If youâ€™re interested in customizing the window controls further, check out the sections [Custom traffic lights](#custom-traffic-lights-macos) and [Custom window controls](#custom-window-controls) that cover this in more detail.

### Create a custom title bar[â€‹](#create-a-custom-title-bar "Direct link to Create a custom title bar") 

Now, letâ€™s implement a simple custom title bar in the `webContents` of our `BrowserWindow`. Thereâ€™s nothing fancy here, just HTML and CSS!

[][][]

[docs/fiddles/features/window-customization/custom-title-bar/custom-title-bar (39.2.4)](https://github.com/electron/electron/tree/v39.2.4/docs/fiddles/features/window-customization/custom-title-bar/custom-title-bar)[Open in Fiddle](https://fiddle.electronjs.org/launch?target=electron/v39.2.4/docs/fiddles/features/window-customization/custom-title-bar/custom-title-bar)

- main.js
- index.html
- styles.css

``` 
const  = require('electron')

function createWindow ()  : )
  })

  win.loadFile('index.html')
}

app.whenReady().then(() => )
```

``` 
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <!-- https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP -->
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'">
    <link href="./styles.css" rel="stylesheet">
    <title>Custom Titlebar App</title>
  </head>
  <body>
      <!-- mount your title bar at the top of you application's body tag -->
    <div class="titlebar">Cool titlebar</div>
  </body>
</html>
```

``` 
body 

.titlebar 
```

Currently our application window canâ€™t be moved. Since weâ€™ve removed the default title bar, the application needs to tell Electron which regions are draggable. Weâ€™ll do this by adding the CSS style `app-region: drag` to the custom title bar. Now we can drag the custom title bar to reposition our app window!

[][][]

[docs/fiddles/features/window-customization/custom-title-bar/custom-drag-region (39.2.4)](https://github.com/electron/electron/tree/v39.2.4/docs/fiddles/features/window-customization/custom-title-bar/custom-drag-region)[Open in Fiddle](https://fiddle.electronjs.org/launch?target=electron/v39.2.4/docs/fiddles/features/window-customization/custom-title-bar/custom-drag-region)

- main.js
- index.html
- styles.css

``` 
const  = require('electron')

function createWindow ()  : )
  })

  win.loadFile('index.html')
}

app.whenReady().then(() => )
```

``` 
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <!-- https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP -->
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'">
    <link href="./styles.css" rel="stylesheet">
    <title>Custom Titlebar App</title>
  </head>
  <body>
    <!-- mount your title bar at the top of you application's body tag -->
    <div class="titlebar">Cool titlebar</div>
  </body>
</html>
```

``` 
body 
.titlebar 
```

For more information around how to manage drag regions defined by your electron application, see the [Custom draggable regions](/docs/latest/tutorial/custom-window-interactions#custom-draggable-regions) section below.

Congratulations, you\'ve just implemented a basic custom title bar!

## Advanced window customization[â€‹](#advanced-window-customization "Direct link to Advanced window customization") 

### Custom traffic lights *macOS*[â€‹](#custom-traffic-lights-macos "Direct link to custom-traffic-lights-macos") 

#### Customize the look of your traffic lights *macOS*[â€‹](#customize-the-look-of-your-traffic-lights-macos "Direct link to customize-the-look-of-your-traffic-lights-macos") 

The `customButtonsOnHover` title bar style will hide the traffic lights until you hover over them. This is useful if you want to create custom traffic lights in your HTML but still use the native UI to control the window.

``` 
const  = require('electron')

const win = new BrowserWindow()
```

#### Customize the traffic light position *macOS*[â€‹](#customize-the-traffic-light-position-macos "Direct link to customize-the-traffic-light-position-macos") 

To modify the position of the traffic light window controls, there are two configuration options available.

Applying `hiddenInset` title bar style will shift the vertical inset of the traffic lights by a fixed amount.

main.js

``` 
const  = require('electron')

const win = new BrowserWindow()
```

If you need more granular control over the positioning of the traffic lights, you can pass a set of coordinates to the `trafficLightPosition` option in the `BrowserWindow` constructor.

main.js

``` 
const  = require('electron')

const win = new BrowserWindow(
})
```

#### Show and hide the traffic lights programmatically *macOS*[â€‹](#show-and-hide-the-traffic-lights-programmatically-macos "Direct link to show-and-hide-the-traffic-lights-programmatically-macos") 

You can also show and hide the traffic lights programmatically from the main process. The `win.setWindowButtonVisibility` forces traffic lights to be show or hidden depending on the value of its boolean parameter.

main.js

``` 
const  = require('electron')

const win = new BrowserWindow()
// hides the traffic lights
win.setWindowButtonVisibility(false)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

Given the number of APIs available, there are many ways of achieving this. For instance, combining `frame: false` with `win.setWindowButtonVisibility(true)` will yield the same layout outcome as setting `titleBarStyle: 'hidden'`.

#### Custom window controls[â€‹](#custom-window-controls "Direct link to Custom window controls") 

The [Window Controls Overlay API](https://github.com/WICG/window-controls-overlay/blob/main/explainer.md) is a web standard that gives web apps the ability to customize their title bar region when installed on desktop. Electron exposes this API through the `titleBarOverlay` option in the `BrowserWindow` constructor. When `titleBarOverlay` is enabled, the window controls become exposed in their default position, and DOM elements cannot use the area underneath this region.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

`titleBarOverlay` requires the `titleBarStyle` param in the `BrowserWindow` constructor to have a value other than `default`.

The custom title bar tutorial covers a [basic example](#add-native-window-controls-windows-linux) of exposing window controls by setting `titleBarOverlay: true`. The height, color (*Windows* *Linux*), and symbol colors (*Windows*) of the window controls can be customized further by setting `titleBarOverlay` to an object.

The value passed to the `height` property must be an integer. The `color` and `symbolColor` properties accept `rgba()`, `hsla()`, and `#RRGGBBAA` color formats and support transparency. If a color option is not specified, the color will default to its system color for the window control buttons. Similarly, if the height option is not specified, the window controls will default to the standard system height:

main.js

``` 
const  = require('electron')

const win = new BrowserWindow(
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

Once your title bar overlay is enabled from the main process, you can access the overlay\'s color and dimension values from a renderer using a set of readonly [JavaScript APIs](https://github.com/WICG/window-controls-overlay/blob/main/explainer.md#javascript-apis) and [CSS Environment Variables](https://github.com/WICG/window-controls-overlay/blob/main/explainer.md#css-environment-variables).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/tutorial/custom-title-bar.md)