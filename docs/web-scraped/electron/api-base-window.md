# Source: https://www.electronjs.org/docs/latest/api/base-window

On this page

# BaseWindow

> Create and control windows.

Process: [Main](/docs/latest/glossary#main-process)

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

`BaseWindow` provides a flexible way to compose multiple web views in a single window. For windows with only a single, full-size web view, the [`BrowserWindow`](/docs/latest/api/browser-window) class may be a simpler option.

This module cannot be used until the `ready` event of the `app` module is emitted.

``` 
// In the main process.
const  = require('electron')

const win = new BaseWindow()

const leftView = new WebContentsView()
leftView.webContents.loadURL('https://electronjs.org')
win.contentView.addChildView(leftView)

const rightView = new WebContentsView()
rightView.webContents.loadURL('https://github.com/electron/electron')
win.contentView.addChildView(rightView)

leftView.setBounds()
rightView.setBounds()
```

## Parent and child windows[â€‹](#parent-and-child-windows "Direct link to Parent and child windows") 

By using `parent` option, you can create child windows:

``` 
const  = require('electron')

const parent = new BaseWindow()
const child = new BaseWindow()
```

The `child` window will always show on top of the `parent` window.

## Modal windows[â€‹](#modal-windows "Direct link to Modal windows") 

A modal window is a child window that disables parent window. To create a modal window, you have to set both the `parent` and `modal` options:

``` 
const  = require('electron')

const parent = new BaseWindow()
const child = new BaseWindow()
```

## Platform notices[â€‹](#platform-notices "Direct link to Platform notices") 

- On macOS modal windows will be displayed as sheets attached to the parent window.
- On macOS the child windows will keep the relative position to parent window when parent window moves, while on Windows and Linux child windows will not move.
- On Linux the type of modal windows will be changed to `dialog`.
- On Linux many desktop environments do not support hiding a modal window.

## Resource management[â€‹](#resource-management "Direct link to Resource management") 

When you add a [`WebContentsView`](/docs/latest/api/web-contents-view) to a `BaseWindow` and the `BaseWindow` is closed, the [`webContents`](/docs/latest/api/web-contents) of the `WebContentsView` are not destroyed automatically.

It is your responsibility to close the `webContents` when you no longer need them, e.g. when the `BaseWindow` is closed:

``` 
const  = require('electron')

const win = new BaseWindow()

const view = new WebContentsView()
win.contentView.addChildView(view)

win.on('closed', () => )
```

Unlike with a [`BrowserWindow`](/docs/latest/api/browser-window), if you don\'t explicitly close the `webContents`, you\'ll encounter memory leaks.

## Class: BaseWindow[â€‹](#class-basewindow "Direct link to Class: BaseWindow") 

> Create and control windows.

Process: [Main](/docs/latest/glossary#main-process)

`BaseWindow` is an [EventEmitter](https://nodejs.org/api/events.html#events_class_eventemitter).

It creates a new `BaseWindow` with native properties as set by the `options`.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)]warning

Electron\'s built-in classes cannot be subclassed in user code. For more information, see [the FAQ](/docs/latest/faq#class-inheritance-does-not-work-with-electron-built-in-modules).

### `new BaseWindow([options])`[â€‹](#new-basewindowoptions "Direct link to new-basewindowoptions") 

- `options` [BaseWindowConstructorOptions](/docs/latest/api/structures/base-window-options) (optional)

  - `width` Integer (optional) - Window\'s width in pixels. Default is `800`.
  - `height` Integer (optional) - Window\'s height in pixels. Default is `600`.
  - `x` Integer (optional) - (**required** if y is used) Window\'s left offset from screen. Default is to center the window.
  - `y` Integer (optional) - (**required** if x is used) Window\'s top offset from screen. Default is to center the window.
  - `useContentSize` boolean (optional) - The `width` and `height` would be used as web page\'s size, which means the actual window\'s size will include window frame\'s size and be slightly larger. Default is `false`.
  - `center` boolean (optional) - Show window in the center of the screen. Default is `false`.
  - `minWidth` Integer (optional) - Window\'s minimum width. Default is `0`.
  - `minHeight` Integer (optional) - Window\'s minimum height. Default is `0`.
  - `maxWidth` Integer (optional) - Window\'s maximum width. Default is no limit.
  - `maxHeight` Integer (optional) - Window\'s maximum height. Default is no limit.
  - `resizable` boolean (optional) - Whether window is resizable. Default is `true`.
  - `movable` boolean (optional) *macOS* *Windows* - Whether window is movable. This is not implemented on Linux. Default is `true`.
  - `minimizable` boolean (optional) *macOS* *Windows* - Whether window is minimizable. This is not implemented on Linux. Default is `true`.
  - `maximizable` boolean (optional) *macOS* *Windows* - Whether window is maximizable. This is not implemented on Linux. Default is `true`.
  - `closable` boolean (optional) *macOS* *Windows* - Whether window is closable. This is not implemented on Linux. Default is `true`.
  - `focusable` boolean (optional) - Whether the window can be focused. Default is `true`. On Windows setting `focusable: false` also implies setting `skipTaskbar: true`. On Linux setting `focusable: false` makes the window stop interacting with wm, so the window will always stay on top in all workspaces.
  - `alwaysOnTop` boolean (optional) - Whether the window should always stay on top of other windows. Default is `false`.
  - `fullscreen` boolean (optional) - Whether the window should show in fullscreen. When explicitly set to `false` the fullscreen button will be hidden or disabled on macOS. Default is `false`.
  - `fullscreenable` boolean (optional) - Whether the window can be put into fullscreen mode. On macOS, also whether the maximize/zoom button should toggle full screen mode or maximize window. Default is `true`.
  - `simpleFullscreen` boolean (optional) *macOS* - Use pre-Lion fullscreen on macOS. Default is `false`.
  - `skipTaskbar` boolean (optional) *macOS* *Windows* - Whether to show the window in taskbar. Default is `false`.
  - `hiddenInMissionControl` boolean (optional) *macOS* - Whether window should be hidden when the user toggles into mission control.
  - `kiosk` boolean (optional) - Whether the window is in kiosk mode. Default is `false`.
  - `title` string (optional) - Default window title. Default is `"Electron"`. If the HTML tag `<title>` is defined in the HTML file loaded by `loadURL()`, this property will be ignored.
  - `icon` ([NativeImage](/docs/latest/api/native-image) \| string) (optional) - The window icon. On Windows it is recommended to use `ICO` icons to get best visual effects, you can also leave it undefined so the executable\'s icon will be used.
  - `show` boolean (optional) - Whether window should be shown when created. Default is `true`.
  - `frame` boolean (optional) - Specify `false` to create a [frameless window](/docs/latest/tutorial/custom-window-styles#frameless-windows). Default is `true`.
  - `parent` BaseWindow (optional) - Specify parent window. Default is `null`.
  - `modal` boolean (optional) - Whether this is a modal window. This only works when the window is a child window. Default is `false`.
  - `acceptFirstMouse` boolean (optional) *macOS* - Whether clicking an inactive window will also click through to the web contents. Default is `false` on macOS. This option is not configurable on other platforms.
  - `disableAutoHideCursor` boolean (optional) - Whether to hide cursor when typing. Default is `false`.
  - `autoHideMenuBar` boolean (optional) *Linux* *Windows* - Auto hide the menu bar unless the `Alt` key is pressed. Default is `false`.
  - `enableLargerThanScreen` boolean (optional) *macOS* - Enable the window to be resized larger than screen. Only relevant for macOS, as other OSes allow larger-than-screen windows by default. Default is `false`.
  - `backgroundColor` string (optional) - The window\'s background color in Hex, RGB, RGBA, HSL, HSLA or named CSS color format. Alpha in #AARRGGBB format is supported if `transparent` is set to `true`. Default is `#FFF` (white). See [win.setBackgroundColor](/docs/latest/api/browser-window#winsetbackgroundcolorbackgroundcolor) for more information.
  - `hasShadow` boolean (optional) - Whether window should have a shadow. Default is `true`.
  - `opacity` number (optional) *macOS* *Windows* - Set the initial opacity of the window, between 0.0 (fully transparent) and 1.0 (fully opaque). This is only implemented on Windows and macOS.
  - `darkTheme` boolean (optional) - Forces using dark theme for the window, only works on some GTK+3 desktop environments. Default is `false`.
  - `transparent` boolean (optional) - Makes the window [transparent](/docs/latest/tutorial/custom-window-styles#transparent-windows). Default is `false`. On Windows, does not work unless the window is frameless. When you add a [`View`](/docs/latest/api/view) to a `BaseWindow`, you\'ll need to call [`view.setBackgroundColor`](/docs/latest/api/view#viewsetbackgroundcolorcolor) with a transparent background color on that view to make its background transparent as well.
  - `type` string (optional) - The type of window, default is normal window. See more about this below.
  - `visualEffectState` string (optional) *macOS* - Specify how the material appearance should reflect window activity state on macOS. Must be used with the `vibrancy` property. Possible values are:
    - `followWindow` - The backdrop should automatically appear active when the window is active, and inactive when it is not. This is the default.
    - `active` - The backdrop should always appear active.
    - `inactive` - The backdrop should always appear inactive.
  - `titleBarStyle` string (optional) - The style of window title bar. Default is `default`. Possible values are:
    - `default` - Results in the standard title bar for macOS or Windows respectively.
    - `hidden` - Results in a hidden title bar and a full size content window. On macOS, the window still has the standard window controls (â€œtraffic lightsâ€?) in the top left. On Windows and Linux, when combined with `titleBarOverlay: true` it will activate the Window Controls Overlay (see `titleBarOverlay` for more information), otherwise no window controls will be shown.
    - `hiddenInset` *macOS* - Results in a hidden title bar with an alternative look where the traffic light buttons are slightly more inset from the window edge.
    - `customButtonsOnHover` *macOS* - Results in a hidden title bar and a full size content window, the traffic light buttons will display when being hovered over in the top left of the window. **Note:** This option is currently experimental.
  - `titleBarOverlay` Object \| Boolean (optional) - When using a frameless window in conjunction with `win.setWindowButtonVisibility(true)` on macOS or using a `titleBarStyle` so that the standard window controls (\"traffic lights\" on macOS) are visible, this property enables the Window Controls Overlay [JavaScript APIs](https://github.com/WICG/window-controls-overlay/blob/main/explainer.md#javascript-apis) and [CSS Environment Variables](https://github.com/WICG/window-controls-overlay/blob/main/explainer.md#css-environment-variables). Specifying `true` will result in an overlay with default system colors. Default is `false`.
    - `color` String (optional) *Windows* *Linux* - The CSS color of the Window Controls Overlay when enabled. Default is the system color.
    - `symbolColor` String (optional) *Windows* *Linux* - The CSS color of the symbols on the Window Controls Overlay when enabled. Default is the system color.
    - `height` Integer (optional) - The height of the title bar and Window Controls Overlay in pixels. Default is system height.
  - `accentColor` boolean \| string (optional) *Windows* - The accent color for the window. By default, follows user preference in System Settings. Set to `false` to explicitly disable, or set the color in Hex, RGB, RGBA, HSL, HSLA or named CSS color format. Alpha values will be ignored.
  - `trafficLightPosition` [Point](/docs/latest/api/structures/point) (optional) *macOS* - Set a custom position for the traffic light buttons in frameless windows.
  - `roundedCorners` boolean (optional) *macOS* *Windows* - Whether frameless window should have rounded corners. Default is `true`. Setting this property to `false` will prevent the window from being fullscreenable on macOS. On Windows versions older than Windows 11 Build 22000 this property has no effect, and frameless windows will not have rounded corners.
  - `thickFrame` boolean (optional) *Windows* - Use `WS_THICKFRAME` style for frameless windows on Windows, which adds the standard window frame. Setting it to `false` will remove window shadow and window animations, and disable window resizing via dragging the window edges. Default is `true`.
  - `vibrancy` string (optional) *macOS* - Add a type of vibrancy effect to the window, only on macOS. Can be `appearance-based`, `titlebar`, `selection`, `menu`, `popover`, `sidebar`, `header`, `sheet`, `window`, `hud`, `fullscreen-ui`, `tooltip`, `content`, `under-window`, or `under-page`.
  - `backgroundMaterial` string (optional) *Windows* - Set the window\'s system-drawn background material, including behind the non-client area. Can be `auto`, `none`, `mica`, `acrylic` or `tabbed`. See [win.setBackgroundMaterial](/docs/latest/api/browser-window#winsetbackgroundmaterialmaterial-windows) for more information.
  - `zoomToPageWidth` boolean (optional) *macOS* - Controls the behavior on macOS when option-clicking the green stoplight button on the toolbar or by clicking the Window \> Zoom menu item. If `true`, the window will grow to the preferred width of the web page when zoomed, `false` will cause it to zoom to the width of the screen. This will also affect the behavior when calling `maximize()` directly. Default is `false`.
  - `tabbingIdentifier` string (optional) *macOS* - Tab group name, allows opening the window as a native tab. Windows with the same tabbing identifier will be grouped together. This also adds a native new tab button to your window\'s tab bar and allows your `app` and window to receive the `new-window-for-tab` event.

  When setting minimum or maximum window size with `minWidth`/`maxWidth`/ `minHeight`/`maxHeight`, it only constrains the users. It won\'t prevent you from passing a size that does not follow size constraints to `setBounds`/`setSize` or to the constructor of `BrowserWindow`.

  The possible values and behaviors of the `type` option are platform dependent. Possible values are:

  - On Linux, possible types are `desktop`, `dock`, `toolbar`, `splash`, `notification`.
    - The `desktop` type places the window at the desktop background window level (kCGDesktopWindowLevel - 1). However, note that a desktop window will not receive focus, keyboard, or mouse events. You can still use globalShortcut to receive input sparingly.
    - The `dock` type creates a dock-like window behavior.
    - The `toolbar` type creates a window with a toolbar appearance.
    - The `splash` type behaves in a specific way. It is not draggable, even if the CSS styling of the window\'s body contains -webkit-app-region: drag. This type is commonly used for splash screens.
    - The `notification` type creates a window that behaves like a system notification.
  - On macOS, possible types are `desktop`, `textured`, `panel`.
    - The `textured` type adds metal gradient appearance. This option is **deprecated**.
    - The `desktop` type places the window at the desktop background window level (`kCGDesktopWindowLevel - 1`). Note that desktop window will not receive focus, keyboard or mouse events, but you can use `globalShortcut` to receive input sparingly.
    - The `panel` type enables the window to float on top of full-screened apps by adding the `NSWindowStyleMaskNonactivatingPanel` style mask, normally reserved for NSPanel, at runtime. Also, the window will appear on all spaces (desktops).
  - On Windows, possible type is `toolbar`.

### Instance Events[â€‹](#instance-events "Direct link to Instance Events") 

Objects created with `new BaseWindow` emit the following events:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

Some events are only available on specific operating systems and are labeled as such.

#### Event: \'close\'[â€‹](#event-close "Direct link to Event: 'close'") 

Returns:

- `event` Event

Emitted when the window is going to be closed. It\'s emitted before the `beforeunload` and `unload` event of the DOM. Calling `event.preventDefault()` will cancel the close.

Usually you would want to use the `beforeunload` handler to decide whether the window should be closed, which will also be called when the window is reloaded. In Electron, returning any value other than `undefined` would cancel the close. For example:

``` 
window.onbeforeunload = (e) => 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

There is a subtle difference between the behaviors of `window.onbeforeunload = handler` and `window.addEventListener('beforeunload', handler)`. It is recommended to always set the `event.returnValue` explicitly, instead of only returning a value, as the former works more consistently within Electron.

#### Event: \'closed\'[â€‹](#event-closed "Direct link to Event: 'closed'") 

Emitted when the window is closed. After you have received this event you should remove the reference to the window and avoid using it any more.

#### Event: \'query-session-end\' *Windows*[â€‹](#event-query-session-end-windows "Direct link to event-query-session-end-windows") 

Returns:

- `event` [WindowSessionEndEvent](/docs/latest/api/structures/window-session-end-event)

Emitted when a session is about to end due to a shutdown, machine restart, or user log-off. Calling `event.preventDefault()` can delay the system shutdown, though itâ€™s generally best to respect the userâ€™s choice to end the session. However, you may choose to use it if ending the session puts the user at risk of losing data.

#### Event: \'session-end\' *Windows*[â€‹](#event-session-end-windows "Direct link to event-session-end-windows") 

Returns:

- `event` [WindowSessionEndEvent](/docs/latest/api/structures/window-session-end-event)

Emitted when a session is about to end due to a shutdown, machine restart, or user log-off. Once this event fires, there is no way to prevent the session from ending.

#### Event: \'blur\'[â€‹](#event-blur "Direct link to Event: 'blur'") 

Returns:

- `event` Event

Emitted when the window loses focus.

#### Event: \'focus\'[â€‹](#event-focus "Direct link to Event: 'focus'") 

Returns:

- `event` Event

Emitted when the window gains focus.

#### Event: \'show\'[â€‹](#event-show "Direct link to Event: 'show'") 

Emitted when the window is shown.

#### Event: \'hide\'[â€‹](#event-hide "Direct link to Event: 'hide'") 

Emitted when the window is hidden.

#### Event: \'maximize\'[â€‹](#event-maximize "Direct link to Event: 'maximize'") 

Emitted when window is maximized.

#### Event: \'unmaximize\'[â€‹](#event-unmaximize "Direct link to Event: 'unmaximize'") 

Emitted when the window exits from a maximized state.

#### Event: \'minimize\'[â€‹](#event-minimize "Direct link to Event: 'minimize'") 

Emitted when the window is minimized.

#### Event: \'restore\'[â€‹](#event-restore "Direct link to Event: 'restore'") 

Emitted when the window is restored from a minimized state.

#### Event: \'will-resize\' *macOS* *Windows*[â€‹](#event-will-resize-macos-windows "Direct link to event-will-resize-macos-windows") 

Returns:

- `event` Event
- `newBounds` [Rectangle](/docs/latest/api/structures/rectangle) - Size the window is being resized to.
- `details` Object
  - `edge` (string) - The edge of the window being dragged for resizing. Can be `bottom`, `left`, `right`, `top-left`, `top-right`, `bottom-left` or `bottom-right`.

Emitted before the window is resized. Calling `event.preventDefault()` will prevent the window from being resized.

Note that this is only emitted when the window is being resized manually. Resizing the window with `setBounds`/`setSize` will not emit this event.

The possible values and behaviors of the `edge` option are platform dependent. Possible values are:

- On Windows, possible values are `bottom`, `top`, `left`, `right`, `top-left`, `top-right`, `bottom-left`, `bottom-right`.
- On macOS, possible values are `bottom` and `right`.
  - The value `bottom` is used to denote vertical resizing.
  - The value `right` is used to denote horizontal resizing.

#### Event: \'resize\'[â€‹](#event-resize "Direct link to Event: 'resize'") 

Emitted after the window has been resized.

#### Event: \'resized\' *macOS* *Windows*[â€‹](#event-resized-macos-windows "Direct link to event-resized-macos-windows") 

Emitted once when the window has finished being resized.

This is usually emitted when the window has been resized manually. On macOS, resizing the window with `setBounds`/`setSize` and setting the `animate` parameter to `true` will also emit this event once resizing has finished.

#### Event: \'will-move\' *macOS* *Windows*[â€‹](#event-will-move-macos-windows "Direct link to event-will-move-macos-windows") 

Returns:

- `event` Event
- `newBounds` [Rectangle](/docs/latest/api/structures/rectangle) - Location the window is being moved to.

Emitted before the window is moved. On Windows, calling `event.preventDefault()` will prevent the window from being moved.

Note that this is only emitted when the window is being moved manually. Moving the window with `setPosition`/`setBounds`/`center` will not emit this event.

#### Event: \'move\'[â€‹](#event-move "Direct link to Event: 'move'") 

Emitted when the window is being moved to a new position.

#### Event: \'moved\' *macOS* *Windows*[â€‹](#event-moved-macos-windows "Direct link to event-moved-macos-windows") 

Emitted once when the window is moved to a new position.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

On macOS, this event is an alias of `move`.

#### Event: \'enter-full-screen\'[â€‹](#event-enter-full-screen "Direct link to Event: 'enter-full-screen'") 

Emitted when the window enters a full-screen state.

#### Event: \'leave-full-screen\'[â€‹](#event-leave-full-screen "Direct link to Event: 'leave-full-screen'") 

Emitted when the window leaves a full-screen state.

#### Event: \'always-on-top-changed\'[â€‹](#event-always-on-top-changed "Direct link to Event: 'always-on-top-changed'") 

Returns:

- `event` Event
- `isAlwaysOnTop` boolean

Emitted when the window is set or unset to show always on top of other windows.

#### Event: \'app-command\' *Windows* *Linux*[â€‹](#event-app-command-windows-linux "Direct link to event-app-command-windows-linux") 

Returns:

- `event` Event
- `command` string

Emitted when an [App Command](https://learn.microsoft.com/en-us/windows/win32/inputdev/wm-appcommand) is invoked. These are typically related to keyboard media keys or browser commands, as well as the \"Back\" button built into some mice on Windows.

Commands are lowercased, underscores are replaced with hyphens, and the `APPCOMMAND_` prefix is stripped off. e.g. `APPCOMMAND_BROWSER_BACKWARD` is emitted as `browser-backward`.

``` 
const  = require('electron')

const win = new BaseWindow()
win.on('app-command', (e, cmd) => 
})
```

The following app commands are explicitly supported on Linux:

- `browser-backward`
- `browser-forward`

#### Event: \'swipe\' *macOS*[â€‹](#event-swipe-macos "Direct link to event-swipe-macos") 

Returns:

- `event` Event
- `direction` string

Emitted on 3-finger swipe. Possible directions are `up`, `right`, `down`, `left`.

The method underlying this event is built to handle older macOS-style trackpad swiping, where the content on the screen doesn\'t move with the swipe. Most macOS trackpads are not configured to allow this kind of swiping anymore, so in order for it to emit properly the \'Swipe between pages\' preference in `System Preferences > Trackpad > More Gestures` must be set to \'Swipe with two or three fingers\'.

#### Event: \'rotate-gesture\' *macOS*[â€‹](#event-rotate-gesture-macos "Direct link to event-rotate-gesture-macos") 

Returns:

- `event` Event
- `rotation` Float

Emitted on trackpad rotation gesture. Continually emitted until rotation gesture is ended. The `rotation` value on each emission is the angle in degrees rotated since the last emission. The last emitted event upon a rotation gesture will always be of value `0`. Counter-clockwise rotation values are positive, while clockwise ones are negative.

#### Event: \'sheet-begin\' *macOS*[â€‹](#event-sheet-begin-macos "Direct link to event-sheet-begin-macos") 

Emitted when the window opens a sheet.

#### Event: \'sheet-end\' *macOS*[â€‹](#event-sheet-end-macos "Direct link to event-sheet-end-macos") 

Emitted when the window has closed a sheet.

#### Event: \'new-window-for-tab\' *macOS*[â€‹](#event-new-window-for-tab-macos "Direct link to event-new-window-for-tab-macos") 

Emitted when the native new tab button is clicked.

#### Event: \'system-context-menu\' *Windows* *Linux*[â€‹](#event-system-context-menu-windows-linux "Direct link to event-system-context-menu-windows-linux") 

Returns:

- `event` Event
- `point` [Point](/docs/latest/api/structures/point) - The screen coordinates where the context menu was triggered.

Emitted when the system context menu is triggered on the window, this is normally only triggered when the user right clicks on the non-client area of your window. This is the window titlebar or any area you have declared as `-webkit-app-region: drag` in a frameless window.

Calling `event.preventDefault()` will prevent the menu from being displayed.

To convert `point` to DIP, use [`screen.screenToDipPoint(point)`](/docs/latest/api/screen#screenscreentodippointpoint-windows-linux).

### Static Methods[â€‹](#static-methods "Direct link to Static Methods") 

The `BaseWindow` class has the following static methods:

#### `BaseWindow.getAllWindows()`[â€‹](#basewindowgetallwindows "Direct link to basewindowgetallwindows") 

Returns `BaseWindow[]` - An array of all opened browser windows.

#### `BaseWindow.getFocusedWindow()`[â€‹](#basewindowgetfocusedwindow "Direct link to basewindowgetfocusedwindow") 

Returns `BaseWindow | null` - The window that is focused in this application, otherwise returns `null`.

#### `BaseWindow.fromId(id)`[â€‹](#basewindowfromidid "Direct link to basewindowfromidid") 

- `id` Integer

Returns `BaseWindow | null` - The window with the given `id`.

### Instance Properties[â€‹](#instance-properties "Direct link to Instance Properties") 

Objects created with `new BaseWindow` have the following properties:

``` 
const  = require('electron')
// In this example `win` is our instance
const win = new BaseWindow()
```

#### `win.id` *Readonly*[â€‹](#winid-readonly "Direct link to winid-readonly") 

A `Integer` property representing the unique ID of the window. Each ID is unique among all `BaseWindow` instances of the entire Electron application.

#### `win.contentView`[â€‹](#wincontentview "Direct link to wincontentview") 

A `View` property for the content view of the window.

#### `win.tabbingIdentifier` *macOS* *Readonly*[â€‹](#wintabbingidentifier-macos-readonly "Direct link to wintabbingidentifier-macos-readonly") 

A `string` (optional) property that is equal to the `tabbingIdentifier` passed to the `BrowserWindow` constructor or `undefined` if none was set.

#### `win.autoHideMenuBar` *Linux* *Windows*[â€‹](#winautohidemenubar-linux-windows "Direct link to winautohidemenubar-linux-windows") 

A `boolean` property that determines whether the window menu bar should hide itself automatically. Once set, the menu bar will only show when users press the single `Alt` key.

If the menu bar is already visible, setting this property to `true` won\'t hide it immediately.

#### `win.simpleFullScreen`[â€‹](#winsimplefullscreen "Direct link to winsimplefullscreen") 

A `boolean` property that determines whether the window is in simple (pre-Lion) fullscreen mode.

#### `win.fullScreen`[â€‹](#winfullscreen "Direct link to winfullscreen") 

A `boolean` property that determines whether the window is in fullscreen mode.

#### `win.focusable` *Windows* *macOS*[â€‹](#winfocusable-windows-macos "Direct link to winfocusable-windows-macos") 

A `boolean` property that determines whether the window is focusable.

#### `win.visibleOnAllWorkspaces` *macOS* *Linux*[â€‹](#winvisibleonallworkspaces-macos-linux "Direct link to winvisibleonallworkspaces-macos-linux") 

A `boolean` property that determines whether the window is visible on all workspaces.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

Always returns false on Windows.

#### `win.shadow`[â€‹](#winshadow "Direct link to winshadow") 

A `boolean` property that determines whether the window has a shadow.

#### `win.menuBarVisible` *Windows* *Linux*[â€‹](#winmenubarvisible-windows-linux "Direct link to winmenubarvisible-windows-linux") 

A `boolean` property that determines whether the menu bar should be visible.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

If the menu bar is auto-hide, users can still bring up the menu bar by pressing the single `Alt` key.

#### `win.kiosk`[â€‹](#winkiosk "Direct link to winkiosk") 

A `boolean` property that determines whether the window is in kiosk mode.

#### `win.documentEdited` *macOS*[â€‹](#windocumentedited-macos "Direct link to windocumentedited-macos") 

A `boolean` property that specifies whether the windowâ€™s document has been edited.

The icon in title bar will become gray when set to `true`.

#### `win.representedFilename` *macOS*[â€‹](#winrepresentedfilename-macos "Direct link to winrepresentedfilename-macos") 

A `string` property that determines the pathname of the file the window represents, and the icon of the file will show in window\'s title bar.

#### `win.title`[â€‹](#wintitle "Direct link to wintitle") 

A `string` property that determines the title of the native window.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

The title of the web page can be different from the title of the native window.

#### `win.minimizable` *macOS* *Windows*[â€‹](#winminimizable-macos-windows "Direct link to winminimizable-macos-windows") 

A `boolean` property that determines whether the window can be manually minimized by user.

On Linux the setter is a no-op, although the getter returns `true`.

#### `win.maximizable` *macOS* *Windows*[â€‹](#winmaximizable-macos-windows "Direct link to winmaximizable-macos-windows") 

A `boolean` property that determines whether the window can be manually maximized by user.

On Linux the setter is a no-op, although the getter returns `true`.

#### `win.fullScreenable`[â€‹](#winfullscreenable "Direct link to winfullscreenable") 

A `boolean` property that determines whether the maximize/zoom window button toggles fullscreen mode or maximizes the window.

#### `win.resizable`[â€‹](#winresizable "Direct link to winresizable") 

A `boolean` property that determines whether the window can be manually resized by user.

#### `win.closable` *macOS* *Windows*[â€‹](#winclosable-macos-windows "Direct link to winclosable-macos-windows") 

A `boolean` property that determines whether the window can be manually closed by user.

On Linux the setter is a no-op, although the getter returns `true`.

#### `win.movable` *macOS* *Windows*[â€‹](#winmovable-macos-windows "Direct link to winmovable-macos-windows") 

A `boolean` property that determines Whether the window can be moved by user.

On Linux the setter is a no-op, although the getter returns `true`.

#### `win.excludedFromShownWindowsMenu` *macOS*[â€‹](#winexcludedfromshownwindowsmenu-macos "Direct link to winexcludedfromshownwindowsmenu-macos") 

A `boolean` property that determines whether the window is excluded from the applicationâ€™s Windows menu. `false` by default.

``` 
const  = require('electron')

const win = new BaseWindow()

const template = [
  
]

win.excludedFromShownWindowsMenu = true

const menu = Menu.buildFromTemplate(template)
Menu.setApplicationMenu(menu)
```

#### `win.accessibleTitle`[â€‹](#winaccessibletitle "Direct link to winaccessibletitle") 

A `string` property that defines an alternative title provided only to accessibility tools such as screen readers. This string is not directly visible to users.

#### `win.snapped` *Windows* *Readonly*[â€‹](#winsnapped-windows-readonly "Direct link to winsnapped-windows-readonly") 

A `boolean` property that indicates whether the window is arranged via [Snap.](https://support.microsoft.com/en-us/windows/snap-your-windows-885a9b1e-a983-a3b1-16cd-c531795e6241)

### Instance Methods[â€‹](#instance-methods "Direct link to Instance Methods") 

Objects created with `new BaseWindow` have the following instance methods:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

Some methods are only available on specific operating systems and are labeled as such.

#### `win.setContentView(view)`[â€‹](#winsetcontentviewview "Direct link to winsetcontentviewview") 

- `view` [View](/docs/latest/api/view)

Sets the content view of the window.

#### `win.getContentView()`[â€‹](#wingetcontentview "Direct link to wingetcontentview") 

Returns [`View`](/docs/latest/api/view) - The content view of the window.

#### `win.destroy()`[â€‹](#windestroy "Direct link to windestroy") 

Force closing the window, the `unload` and `beforeunload` event won\'t be emitted for the web page, and `close` event will also not be emitted for this window, but it guarantees the `closed` event will be emitted.

#### `win.close()`[â€‹](#winclose "Direct link to winclose") 

Try to close the window. This has the same effect as a user manually clicking the close button of the window. The web page may cancel the close though. See the [close event](#event-close).

#### `win.focus()`[â€‹](#winfocus "Direct link to winfocus") 

Focuses on the window.

#### `win.blur()`[â€‹](#winblur "Direct link to winblur") 

Removes focus from the window.

#### `win.isFocused()`[â€‹](#winisfocused "Direct link to winisfocused") 

Returns `boolean` - Whether the window is focused.

#### `win.isDestroyed()`[â€‹](#winisdestroyed "Direct link to winisdestroyed") 

Returns `boolean` - Whether the window is destroyed.

#### `win.show()`[â€‹](#winshow "Direct link to winshow") 

Shows and gives focus to the window.

#### `win.showInactive()`[â€‹](#winshowinactive "Direct link to winshowinactive") 

Shows the window but doesn\'t focus on it.

#### `win.hide()`[â€‹](#winhide "Direct link to winhide") 

Hides the window.

#### `win.isVisible()`[â€‹](#winisvisible "Direct link to winisvisible") 

Returns `boolean` - Whether the window is visible to the user in the foreground of the app.

#### `win.isModal()`[â€‹](#winismodal "Direct link to winismodal") 

Returns `boolean` - Whether current window is a modal window.

#### `win.maximize()`[â€‹](#winmaximize "Direct link to winmaximize") 

Maximizes the window. This will also show (but not focus) the window if it isn\'t being displayed already.

#### `win.unmaximize()`[â€‹](#winunmaximize "Direct link to winunmaximize") 

Unmaximizes the window.

#### `win.isMaximized()`[â€‹](#winismaximized "Direct link to winismaximized") 

Returns `boolean` - Whether the window is maximized.

#### `win.minimize()`[â€‹](#winminimize "Direct link to winminimize") 

Minimizes the window. On some platforms the minimized window will be shown in the Dock.

#### `win.restore()`[â€‹](#winrestore "Direct link to winrestore") 

Restores the window from minimized state to its previous state.

#### `win.isMinimized()`[â€‹](#winisminimized "Direct link to winisminimized") 

Returns `boolean` - Whether the window is minimized.

#### `win.setFullScreen(flag)`[â€‹](#winsetfullscreenflag "Direct link to winsetfullscreenflag") 

- `flag` boolean

Sets whether the window should be in fullscreen mode.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

On macOS, fullscreen transitions take place asynchronously. If further actions depend on the fullscreen state, use the [\'enter-full-screen\'](/docs/latest/api/base-window#event-enter-full-screen) or \> [\'leave-full-screen\'](/docs/latest/api/base-window#event-leave-full-screen) events.

#### `win.isFullScreen()`[â€‹](#winisfullscreen "Direct link to winisfullscreen") 

Returns `boolean` - Whether the window is in fullscreen mode.

#### `win.setSimpleFullScreen(flag)` *macOS*[â€‹](#winsetsimplefullscreenflag-macos "Direct link to winsetsimplefullscreenflag-macos") 

- `flag` boolean

Enters or leaves simple fullscreen mode.

Simple fullscreen mode emulates the native fullscreen behavior found in versions of macOS prior to Lion (10.7).

#### `win.isSimpleFullScreen()` *macOS*[â€‹](#winissimplefullscreen-macos "Direct link to winissimplefullscreen-macos") 

Returns `boolean` - Whether the window is in simple (pre-Lion) fullscreen mode.

#### `win.isNormal()`[â€‹](#winisnormal "Direct link to winisnormal") 

Returns `boolean` - Whether the window is in normal state (not maximized, not minimized, not in fullscreen mode).

#### `win.setAspectRatio(aspectRatio[, extraSize])`[â€‹](#winsetaspectratioaspectratio-extrasize "Direct link to winsetaspectratioaspectratio-extrasize") 

- `aspectRatio` Float - The aspect ratio to maintain for some portion of the content view.
- `extraSize` [Size](/docs/latest/api/structures/size) (optional) *macOS* - The extra size not to be included while maintaining the aspect ratio.

This will make a window maintain an aspect ratio. The extra size allows a developer to have space, specified in pixels, not included within the aspect ratio calculations. This API already takes into account the difference between a window\'s size and its content size.

Consider a normal window with an HD video player and associated controls. Perhaps there are 15 pixels of controls on the left edge, 25 pixels of controls on the right edge and 50 pixels of controls below the player. In order to maintain a 16:9 aspect ratio (standard aspect ratio for HD \@1920x1080) within the player itself we would call this function with arguments of 16/9 and . The second argument doesn\'t care where the extra width and height are within the content view\--only that they exist. Sum any extra width and height areas you have within the overall content view.

The aspect ratio is not respected when window is resized programmatically with APIs like `win.setSize`.

To reset an aspect ratio, pass 0 as the `aspectRatio` value: `win.setAspectRatio(0)`.

#### `win.setBackgroundColor(backgroundColor)`[â€‹](#winsetbackgroundcolorbackgroundcolor "Direct link to winsetbackgroundcolorbackgroundcolor") 

- `backgroundColor` string - Color in Hex, RGB, RGBA, HSL, HSLA or named CSS color format. The alpha channel is optional for the hex type.

Examples of valid `backgroundColor` values:

- Hex
  - #fff (shorthand RGB)
  - #ffff (shorthand ARGB)
  - #ffffff (RGB)
  - #ffffffff (ARGB)
- RGB
  - `rgb\(([\d]+),\s*([\d]+),\s*([\d]+)\)`
    - e.g. rgb(255, 255, 255)
- RGBA
  - `rgba\(([\d]+),\s*([\d]+),\s*([\d]+),\s*([\d.]+)\)`
    - e.g. rgba(255, 255, 255, 1.0)
- HSL
  - `hsl\((-?[\d.]+),\s*([\d.]+)%,\s*([\d.]+)%\)`
    - e.g. hsl(200, 20%, 50%)
- HSLA
  - `hsla\((-?[\d.]+),\s*([\d.]+)%,\s*([\d.]+)%,\s*([\d.]+)\)`
    - e.g. hsla(200, 20%, 50%, 0.5)
- Color name
  - Options are listed in [SkParseColor.cpp](https://source.chromium.org/chromium/chromium/src/+/main:third_party/skia/src/utils/SkParseColor.cpp;l=11-152;drc=eea4bf52cb0d55e2a39c828b017c80a5ee054148)
  - Similar to CSS Color Module Level 3 keywords, but case-sensitive.
    - e.g. `blueviolet` or `red`

Sets the background color of the window. See [Setting `backgroundColor`](/docs/latest/api/browser-window#setting-the-backgroundcolor-property).

#### `win.previewFile(path[, displayName])` *macOS*[â€‹](#winpreviewfilepath-displayname-macos "Direct link to winpreviewfilepath-displayname-macos") 

- `path` string - The absolute path to the file to preview with QuickLook. This is important as Quick Look uses the file name and file extension on the path to determine the content type of the file to open.
- `displayName` string (optional) - The name of the file to display on the Quick Look modal view. This is purely visual and does not affect the content type of the file. Defaults to `path`.

Uses [Quick Look](https://en.wikipedia.org/wiki/Quick_Look) to preview a file at a given path.

#### `win.closeFilePreview()` *macOS*[â€‹](#winclosefilepreview-macos "Direct link to winclosefilepreview-macos") 

Closes the currently open [Quick Look](https://en.wikipedia.org/wiki/Quick_Look) panel.

#### `win.setBounds(bounds[, animate])`[â€‹](#winsetboundsbounds-animate "Direct link to winsetboundsbounds-animate") 

- `bounds` Partial\<[Rectangle](/docs/latest/api/structures/rectangle)\>
- `animate` boolean (optional) *macOS*

Resizes and moves the window to the supplied bounds. Any properties that are not supplied will default to their current values.

``` 
const  = require('electron')

const win = new BaseWindow()

// set all bounds properties
win.setBounds()

// set a single bounds property
win.setBounds()

// 
console.log(win.getBounds())
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

On macOS, the y-coordinate value cannot be smaller than the [Tray](/docs/latest/api/tray) height. The tray height has changed over time and depends on the operating system, but is between 20-40px. Passing a value lower than the tray height will result in a window that is flush to the tray.

#### `win.getBounds()`[â€‹](#wingetbounds "Direct link to wingetbounds") 

Returns [Rectangle](/docs/latest/api/structures/rectangle) - The `bounds` of the window as `Object`.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

On macOS, the y-coordinate value returned will be at minimum the [Tray](/docs/latest/api/tray) height. For example, calling `win.setBounds()` with a tray height of 38 means that `win.getBounds()` will return ``.

#### `win.getBackgroundColor()`[â€‹](#wingetbackgroundcolor "Direct link to wingetbackgroundcolor") 

Returns `string` - Gets the background color of the window in Hex (`#RRGGBB`) format.

See [Setting `backgroundColor`](/docs/latest/api/browser-window#setting-the-backgroundcolor-property).

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

The alpha value is *not* returned alongside the red, green, and blue values.

#### `win.setContentBounds(bounds[, animate])`[â€‹](#winsetcontentboundsbounds-animate "Direct link to winsetcontentboundsbounds-animate") 

- `bounds` [Rectangle](/docs/latest/api/structures/rectangle)
- `animate` boolean (optional) *macOS*

Resizes and moves the window\'s client area (e.g. the web page) to the supplied bounds.

#### `win.getContentBounds()`[â€‹](#wingetcontentbounds "Direct link to wingetcontentbounds") 

Returns [Rectangle](/docs/latest/api/structures/rectangle) - The `bounds` of the window\'s client area as `Object`.

#### `win.getNormalBounds()`[â€‹](#wingetnormalbounds "Direct link to wingetnormalbounds") 

Returns [Rectangle](/docs/latest/api/structures/rectangle) - Contains the window bounds of the normal state

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

Whatever the current state of the window : maximized, minimized or in fullscreen, this function always returns the position and size of the window in normal state. In normal state, getBounds and getNormalBounds returns the same [Rectangle](/docs/latest/api/structures/rectangle).

#### `win.setEnabled(enable)`[â€‹](#winsetenabledenable "Direct link to winsetenabledenable") 

- `enable` boolean

Disable or enable the window.

#### `win.isEnabled()`[â€‹](#winisenabled "Direct link to winisenabled") 

Returns `boolean` - whether the window is enabled.

#### `win.setSize(width, height[, animate])`[â€‹](#winsetsizewidth-height-animate "Direct link to winsetsizewidth-height-animate") 

- `width` Integer
- `height` Integer
- `animate` boolean (optional) *macOS*

Resizes the window to `width` and `height`. If `width` or `height` are below any set minimum size constraints the window will snap to its minimum size.

#### `win.getSize()`[â€‹](#wingetsize "Direct link to wingetsize") 

Returns `Integer[]` - Contains the window\'s width and height.

#### `win.setContentSize(width, height[, animate])`[â€‹](#winsetcontentsizewidth-height-animate "Direct link to winsetcontentsizewidth-height-animate") 

- `width` Integer
- `height` Integer
- `animate` boolean (optional) *macOS*

Resizes the window\'s client area (e.g. the web page) to `width` and `height`.

#### `win.getContentSize()`[â€‹](#wingetcontentsize "Direct link to wingetcontentsize") 

Returns `Integer[]` - Contains the window\'s client area\'s width and height.

#### `win.setMinimumSize(width, height)`[â€‹](#winsetminimumsizewidth-height "Direct link to winsetminimumsizewidth-height") 

- `width` Integer
- `height` Integer

Sets the minimum size of window to `width` and `height`.

#### `win.getMinimumSize()`[â€‹](#wingetminimumsize "Direct link to wingetminimumsize") 

Returns `Integer[]` - Contains the window\'s minimum width and height.

#### `win.setMaximumSize(width, height)`[â€‹](#winsetmaximumsizewidth-height "Direct link to winsetmaximumsizewidth-height") 

- `width` Integer
- `height` Integer

Sets the maximum size of window to `width` and `height`.

#### `win.getMaximumSize()`[â€‹](#wingetmaximumsize "Direct link to wingetmaximumsize") 

Returns `Integer[]` - Contains the window\'s maximum width and height.

#### `win.setResizable(resizable)`[â€‹](#winsetresizableresizable "Direct link to winsetresizableresizable") 

- `resizable` boolean

Sets whether the window can be manually resized by the user.

#### `win.isResizable()`[â€‹](#winisresizable "Direct link to winisresizable") 

Returns `boolean` - Whether the window can be manually resized by the user.

#### `win.setMovable(movable)` *macOS* *Windows*[â€‹](#winsetmovablemovable-macos-windows "Direct link to winsetmovablemovable-macos-windows") 

- `movable` boolean

Sets whether the window can be moved by user. On Linux does nothing.

#### `win.isMovable()` *macOS* *Windows*[â€‹](#winismovable-macos-windows "Direct link to winismovable-macos-windows") 

Returns `boolean` - Whether the window can be moved by user.

On Linux always returns `true`.

#### `win.setMinimizable(minimizable)` *macOS* *Windows*[â€‹](#winsetminimizableminimizable-macos-windows "Direct link to winsetminimizableminimizable-macos-windows") 

- `minimizable` boolean

Sets whether the window can be manually minimized by user. On Linux does nothing.

#### `win.isMinimizable()` *macOS* *Windows*[â€‹](#winisminimizable-macos-windows "Direct link to winisminimizable-macos-windows") 

Returns `boolean` - Whether the window can be manually minimized by the user.

On Linux always returns `true`.

#### `win.setMaximizable(maximizable)` *macOS* *Windows*[â€‹](#winsetmaximizablemaximizable-macos-windows "Direct link to winsetmaximizablemaximizable-macos-windows") 

- `maximizable` boolean

Sets whether the window can be manually maximized by user. On Linux does nothing.

#### `win.isMaximizable()` *macOS* *Windows*[â€‹](#winismaximizable-macos-windows "Direct link to winismaximizable-macos-windows") 

Returns `boolean` - Whether the window can be manually maximized by user.

On Linux always returns `true`.

#### `win.setFullScreenable(fullscreenable)`[â€‹](#winsetfullscreenablefullscreenable "Direct link to winsetfullscreenablefullscreenable") 

- `fullscreenable` boolean

Sets whether the maximize/zoom window button toggles fullscreen mode or maximizes the window.

#### `win.isFullScreenable()`[â€‹](#winisfullscreenable "Direct link to winisfullscreenable") 

Returns `boolean` - Whether the maximize/zoom window button toggles fullscreen mode or maximizes the window.

#### `win.setClosable(closable)` *macOS* *Windows*[â€‹](#winsetclosableclosable-macos-windows "Direct link to winsetclosableclosable-macos-windows") 

- `closable` boolean

Sets whether the window can be manually closed by user. On Linux does nothing.

#### `win.isClosable()` *macOS* *Windows*[â€‹](#winisclosable-macos-windows "Direct link to winisclosable-macos-windows") 

Returns `boolean` - Whether the window can be manually closed by user.

On Linux always returns `true`.

#### `win.setHiddenInMissionControl(hidden)` *macOS*[â€‹](#winsethiddeninmissioncontrolhidden-macos "Direct link to winsethiddeninmissioncontrolhidden-macos") 

- `hidden` boolean

Sets whether the window will be hidden when the user toggles into mission control.

#### `win.isHiddenInMissionControl()` *macOS*[â€‹](#winishiddeninmissioncontrol-macos "Direct link to winishiddeninmissioncontrol-macos") 

Returns `boolean` - Whether the window will be hidden when the user toggles into mission control.

#### `win.setAlwaysOnTop(flag[, level][, relativeLevel])`[â€‹](#winsetalwaysontopflag-level-relativelevel "Direct link to winsetalwaysontopflag-level-relativelevel") 

- `flag` boolean
- `level` string (optional) *macOS* *Windows* - Values include `normal`, `floating`, `torn-off-menu`, `modal-panel`, `main-menu`, `status`, `pop-up-menu`, `screen-saver`, and ~~`dock`~~ (Deprecated). The default is `floating` when `flag` is true. The `level` is reset to `normal` when the flag is false. Note that from `floating` to `status` included, the window is placed below the Dock on macOS and below the taskbar on Windows. From `pop-up-menu` to a higher it is shown above the Dock on macOS and above the taskbar on Windows. See the [macOS docs](https://developer.apple.com/documentation/appkit/nswindow/level) for more details.
- `relativeLevel` Integer (optional) *macOS* - The number of layers higher to set this window relative to the given `level`. The default is `0`. Note that Apple discourages setting levels higher than 1 above `screen-saver`.

Sets whether the window should show always on top of other windows. After setting this, the window is still a normal window, not a toolbox window which can not be focused on.

#### `win.isAlwaysOnTop()`[â€‹](#winisalwaysontop "Direct link to winisalwaysontop") 

Returns `boolean` - Whether the window is always on top of other windows.

#### `win.moveAbove(mediaSourceId)`[â€‹](#winmoveabovemediasourceid "Direct link to winmoveabovemediasourceid") 

- `mediaSourceId` string - Window id in the format of DesktopCapturerSource\'s id. For example \"window:1869:0\".

Moves window above the source window in the sense of z-order. If the `mediaSourceId` is not of type window or if the window does not exist then this method throws an error.

#### `win.moveTop()`[â€‹](#winmovetop "Direct link to winmovetop") 

Moves window to top(z-order) regardless of focus

#### `win.center()`[â€‹](#wincenter "Direct link to wincenter") 

Moves window to the center of the screen.

#### `win.setPosition(x, y[, animate])`[â€‹](#winsetpositionx-y-animate "Direct link to winsetpositionx-y-animate") 

- `x` Integer
- `y` Integer
- `animate` boolean (optional) *macOS*

Moves window to `x` and `y`.

#### `win.getPosition()`[â€‹](#wingetposition "Direct link to wingetposition") 

Returns `Integer[]` - Contains the window\'s current position.

#### `win.setTitle(title)`[â€‹](#winsettitletitle "Direct link to winsettitletitle") 

- `title` string

Changes the title of native window to `title`.

#### `win.getTitle()`[â€‹](#wingettitle "Direct link to wingettitle") 

Returns `string` - The title of the native window.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

The title of the web page can be different from the title of the native window.

#### `win.setSheetOffset(offsetY[, offsetX])` *macOS*[â€‹](#winsetsheetoffsetoffsety-offsetx-macos "Direct link to winsetsheetoffsetoffsety-offsetx-macos") 

- `offsetY` Float
- `offsetX` Float (optional)

Changes the attachment point for sheets on macOS. By default, sheets are attached just below the window frame, but you may want to display them beneath a HTML-rendered toolbar. For example:

``` 
const  = require('electron')

const win = new BaseWindow()

const toolbarRect = document.getElementById('toolbar').getBoundingClientRect()
win.setSheetOffset(toolbarRect.height)
```

#### `win.flashFrame(flag)`[â€‹](#winflashframeflag "Direct link to winflashframeflag") 

History

Version(s)

Changes

    None

[](/docs/latest/breaking-changes#behavior-changed-windowflashframebool-will-flash-dock-icon-continuously-on-macos)

`window.flashFrame(bool)` will flash dock icon continuously on macOS

    None

``` api-added_XqIp
API ADDED
```

- `flag` boolean

Starts or stops flashing the window to attract user\'s attention.

#### `win.setSkipTaskbar(skip)` *macOS* *Windows*[â€‹](#winsetskiptaskbarskip-macos-windows "Direct link to winsetskiptaskbarskip-macos-windows") 

- `skip` boolean

Makes the window not show in the taskbar.

#### `win.setKiosk(flag)`[â€‹](#winsetkioskflag "Direct link to winsetkioskflag") 

- `flag` boolean

Enters or leaves kiosk mode.

#### `win.isKiosk()`[â€‹](#winiskiosk "Direct link to winiskiosk") 

Returns `boolean` - Whether the window is in kiosk mode.

#### `win.isTabletMode()` *Windows*[â€‹](#winistabletmode-windows "Direct link to winistabletmode-windows") 

Returns `boolean` - Whether the window is in Windows 10 tablet mode.

Since Windows 10 users can [use their PC as tablet](https://support.microsoft.com/en-us/help/17210/windows-10-use-your-pc-like-a-tablet), under this mode apps can choose to optimize their UI for tablets, such as enlarging the titlebar and hiding titlebar buttons.

This API returns whether the window is in tablet mode, and the `resize` event can be be used to listen to changes to tablet mode.

#### `win.getMediaSourceId()`[â€‹](#wingetmediasourceid "Direct link to wingetmediasourceid") 

Returns `string` - Window id in the format of DesktopCapturerSource\'s id. For example \"window:1324:0\".

More precisely the format is `window:id:other_id` where `id` is `HWND` on Windows, `CGWindowID` (`uint64_t`) on macOS and `Window` (`unsigned long`) on Linux. `other_id` is used to identify web contents (tabs) so within the same top level window.

#### `win.getNativeWindowHandle()`[â€‹](#wingetnativewindowhandle "Direct link to wingetnativewindowhandle") 

Returns `Buffer` - The platform-specific handle of the window.

The native type of the handle is `HWND` on Windows, `NSView*` on macOS, and `Window` (`unsigned long`) on Linux.

#### `win.hookWindowMessage(message, callback)` *Windows*[â€‹](#winhookwindowmessagemessage-callback-windows "Direct link to winhookwindowmessagemessage-callback-windows") 

- `message` Integer
- `callback` Function
  - `wParam` Buffer - The `wParam` provided to the WndProc
  - `lParam` Buffer - The `lParam` provided to the WndProc

Hooks a windows message. The `callback` is called when the message is received in the WndProc.

#### `win.isWindowMessageHooked(message)` *Windows*[â€‹](#winiswindowmessagehookedmessage-windows "Direct link to winiswindowmessagehookedmessage-windows") 

- `message` Integer

Returns `boolean` - `true` or `false` depending on whether the message is hooked.

#### `win.unhookWindowMessage(message)` *Windows*[â€‹](#winunhookwindowmessagemessage-windows "Direct link to winunhookwindowmessagemessage-windows") 

- `message` Integer

Unhook the window message.

#### `win.unhookAllWindowMessages()` *Windows*[â€‹](#winunhookallwindowmessages-windows "Direct link to winunhookallwindowmessages-windows") 

Unhooks all of the window messages.

#### `win.setRepresentedFilename(filename)` *macOS*[â€‹](#winsetrepresentedfilenamefilename-macos "Direct link to winsetrepresentedfilenamefilename-macos") 

- `filename` string

Sets the pathname of the file the window represents, and the icon of the file will show in window\'s title bar.

#### `win.getRepresentedFilename()` *macOS*[â€‹](#wingetrepresentedfilename-macos "Direct link to wingetrepresentedfilename-macos") 

Returns `string` - The pathname of the file the window represents.

#### `win.setDocumentEdited(edited)` *macOS*[â€‹](#winsetdocumenteditededited-macos "Direct link to winsetdocumenteditededited-macos") 

- `edited` boolean

Specifies whether the windowâ€™s document has been edited, and the icon in title bar will become gray when set to `true`.

#### `win.isDocumentEdited()` *macOS*[â€‹](#winisdocumentedited-macos "Direct link to winisdocumentedited-macos") 

Returns `boolean` - Whether the window\'s document has been edited.

#### `win.setMenu(menu)` *Linux* *Windows*[â€‹](#winsetmenumenu-linux-windows "Direct link to winsetmenumenu-linux-windows") 

- `menu` Menu \| null

Sets the `menu` as the window\'s menu bar.

#### `win.removeMenu()` *Linux* *Windows*[â€‹](#winremovemenu-linux-windows "Direct link to winremovemenu-linux-windows") 

Remove the window\'s menu bar.

#### `win.setProgressBar(progress[, options])`[â€‹](#winsetprogressbarprogress-options "Direct link to winsetprogressbarprogress-options") 

- `progress` Double
- `options` Object (optional)
  - `mode` string *Windows* - Mode for the progress bar. Can be `none`, `normal`, `indeterminate`, `error` or `paused`.

Sets progress value in progress bar. Valid range is \[0, 1.0\].

Remove progress bar when progress \< 0; Change to indeterminate mode when progress \> 1.

On Linux platform, only supports Unity desktop environment, you need to specify the `*.desktop` file name to `desktopName` field in `package.json`. By default, it will assume `.desktop`.

On Windows, a mode can be passed. Accepted values are `none`, `normal`, `indeterminate`, `error`, and `paused`. If you call `setProgressBar` without a mode set (but with a value within the valid range), `normal` will be assumed.

#### `win.setOverlayIcon(overlay, description)` *Windows*[â€‹](#winsetoverlayiconoverlay-description-windows "Direct link to winsetoverlayiconoverlay-description-windows") 

- `overlay` [NativeImage](/docs/latest/api/native-image) \| null - the icon to display on the bottom right corner of the taskbar icon. If this parameter is `null`, the overlay is cleared
- `description` string - a description that will be provided to Accessibility screen readers

Sets a 16 x 16 pixel overlay onto the current taskbar icon, usually used to convey some sort of application status or to passively notify the user.

#### `win.invalidateShadow()` *macOS*[â€‹](#wininvalidateshadow-macos "Direct link to wininvalidateshadow-macos") 

Invalidates the window shadow so that it is recomputed based on the current window shape.

`BaseWindow`s that are transparent can sometimes leave behind visual artifacts on macOS. This method can be used to clear these artifacts when, for example, performing an animation.

#### `win.setHasShadow(hasShadow)`[â€‹](#winsethasshadowhasshadow "Direct link to winsethasshadowhasshadow") 

- `hasShadow` boolean

Sets whether the window should have a shadow.

#### `win.hasShadow()`[â€‹](#winhasshadow "Direct link to winhasshadow") 

Returns `boolean` - Whether the window has a shadow.

#### `win.setOpacity(opacity)` *Windows* *macOS*[â€‹](#winsetopacityopacity-windows-macos "Direct link to winsetopacityopacity-windows-macos") 

- `opacity` number - between 0.0 (fully transparent) and 1.0 (fully opaque)

Sets the opacity of the window. On Linux, does nothing. Out of bound number values are clamped to the \[0, 1\] range.

#### `win.getOpacity()`[â€‹](#wingetopacity "Direct link to wingetopacity") 

Returns `number` - between 0.0 (fully transparent) and 1.0 (fully opaque). On Linux, always returns 1.

#### `win.setShape(rects)` *Windows* *Linux* *Experimental*[â€‹](#winsetshaperects-windows-linux-experimental "Direct link to winsetshaperects-windows-linux-experimental") 

- `rects` [Rectangle\[\]](/docs/latest/api/structures/rectangle) - Sets a shape on the window. Passing an empty list reverts the window to being rectangular.

Setting a window shape determines the area within the window where the system permits drawing and user interaction. Outside of the given region, no pixels will be drawn and no mouse events will be registered. Mouse events outside of the region will not be received by that window, but will fall through to whatever is behind the window.

#### `win.setThumbarButtons(buttons)` *Windows*[â€‹](#winsetthumbarbuttonsbuttons-windows "Direct link to winsetthumbarbuttonsbuttons-windows") 

- `buttons` [ThumbarButton\[\]](/docs/latest/api/structures/thumbar-button)

Returns `boolean` - Whether the buttons were added successfully

Add a thumbnail toolbar with a specified set of buttons to the thumbnail image of a window in a taskbar button layout. Returns a `boolean` object indicates whether the thumbnail has been added successfully.

The number of buttons in thumbnail toolbar should be no greater than 7 due to the limited room. Once you setup the thumbnail toolbar, the toolbar cannot be removed due to the platform\'s limitation. But you can call the API with an empty array to clean the buttons.

The `buttons` is an array of `Button` objects:

- `Button` Object
  - `icon` [NativeImage](/docs/latest/api/native-image) - The icon showing in thumbnail toolbar.
  - `click` Function
  - `tooltip` string (optional) - The text of the button\'s tooltip.
  - `flags` string\[\] (optional) - Control specific states and behaviors of the button. By default, it is `['enabled']`.

The `flags` is an array that can include following `string`s:

- `enabled` - The button is active and available to the user.
- `disabled` - The button is disabled. It is present, but has a visual state indicating it will not respond to user action.
- `dismissonclick` - When the button is clicked, the thumbnail window closes immediately.
- `nobackground` - Do not draw a button border, use only the image.
- `hidden` - The button is not shown to the user.
- `noninteractive` - The button is enabled but not interactive; no pressed button state is drawn. This value is intended for instances where the button is used in a notification.

#### `win.setThumbnailClip(region)` *Windows*[â€‹](#winsetthumbnailclipregion-windows "Direct link to winsetthumbnailclipregion-windows") 

- `region` [Rectangle](/docs/latest/api/structures/rectangle) - Region of the window

Sets the region of the window to show as the thumbnail image displayed when hovering over the window in the taskbar. You can reset the thumbnail to be the entire window by specifying an empty region: ``.

#### `win.setThumbnailToolTip(toolTip)` *Windows*[â€‹](#winsetthumbnailtooltiptooltip-windows "Direct link to winsetthumbnailtooltiptooltip-windows") 

- `toolTip` string

Sets the toolTip that is displayed when hovering over the window thumbnail in the taskbar.

#### `win.setAppDetails(options)` *Windows*[â€‹](#winsetappdetailsoptions-windows "Direct link to winsetappdetailsoptions-windows") 

- `options` Object
  - `appId` string (optional) - Window\'s [App User Model ID](https://learn.microsoft.com/en-us/windows/win32/shell/appids). It has to be set, otherwise the other options will have no effect.
  - `appIconPath` string (optional) - Window\'s [Relaunch Icon](https://learn.microsoft.com/en-us/windows/win32/properties/props-system-appusermodel-relaunchiconresource).
  - `appIconIndex` Integer (optional) - Index of the icon in `appIconPath`. Ignored when `appIconPath` is not set. Default is `0`.
  - `relaunchCommand` string (optional) - Window\'s [Relaunch Command](https://learn.microsoft.com/en-us/windows/win32/properties/props-system-appusermodel-relaunchcommand).
  - `relaunchDisplayName` string (optional) - Window\'s [Relaunch Display Name](https://learn.microsoft.com/en-us/windows/win32/properties/props-system-appusermodel-relaunchdisplaynameresource).

Sets the properties for the window\'s taskbar button.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

`relaunchCommand` and `relaunchDisplayName` must always be set together. If one of those properties is not set, then neither will be used.

#### `win.setAccentColor(accentColor)` *Windows*[â€‹](#winsetaccentcoloraccentcolor-windows "Direct link to winsetaccentcoloraccentcolor-windows") 

- `accentColor` boolean \| string \| null - The accent color for the window. By default, follows user preference in System Settings. To reset to system default, pass `null`.

Sets the system accent color and highlighting of active window border.

The `accentColor` parameter accepts the following values:

- **Color string** - Like `true`, but sets a custom accent color using standard CSS color formats (Hex, RGB, RGBA, HSL, HSLA, or named colors). Alpha values in RGBA/HSLA formats are ignored and the color is treated as fully opaque.
- **`true`** - Enable accent color highlighting for the window with the system accent color regardless of whether accent colors are enabled for windows in System `Settings.`
- **`false`** - Disable accent color highlighting for the window regardless of whether accent colors are currently enabled for windows in System Settings.
- **`null`** - Reset window accent color behavior to follow behavior set in System Settings.

Examples:

``` 
const win = new BrowserWindow()

// Set red accent color.
win.setAccentColor('#ff0000')

// RGB format (alpha ignored if present).
win.setAccentColor('rgba(255,0,0,0.5)')

// Enable accent color, using the color specified in System Settings.
win.setAccentColor(true)

// Disable accent color.
win.setAccentColor(false)

// Reset window accent color behavior to follow behavior set in System Settings.
win.setAccentColor(null)
```

#### `win.getAccentColor()` *Windows*[â€‹](#wingetaccentcolor-windows "Direct link to wingetaccentcolor-windows") 

Returns `string | boolean` - the system accent color and highlighting of active window border in Hex RGB format.

If a color has been set for the window that differs from the system accent color, the window accent color will be returned. Otherwise, a boolean will be returned, with `true` indicating that the window uses the global system accent color, and `false` indicating that accent color highlighting is disabled for this window.

#### `win.setIcon(icon)` *Windows* *Linux*[â€‹](#winseticonicon-windows-linux "Direct link to winseticonicon-windows-linux") 

- `icon` [NativeImage](/docs/latest/api/native-image) \| string

Changes window icon.

#### `win.setWindowButtonVisibility(visible)` *macOS*[â€‹](#winsetwindowbuttonvisibilityvisible-macos "Direct link to winsetwindowbuttonvisibilityvisible-macos") 

- `visible` boolean

Sets whether the window traffic light buttons should be visible.

#### `win.setAutoHideMenuBar(hide)` *Windows* *Linux*[â€‹](#winsetautohidemenubarhide-windows-linux "Direct link to winsetautohidemenubarhide-windows-linux") 

- `hide` boolean

Sets whether the window menu bar should hide itself automatically. Once set the menu bar will only show when users press the single `Alt` key.

If the menu bar is already visible, calling `setAutoHideMenuBar(true)` won\'t hide it immediately.

#### `win.isMenuBarAutoHide()` *Windows* *Linux*[â€‹](#winismenubarautohide-windows-linux "Direct link to winismenubarautohide-windows-linux") 

Returns `boolean` - Whether menu bar automatically hides itself.

#### `win.setMenuBarVisibility(visible)` *Windows* *Linux*[â€‹](#winsetmenubarvisibilityvisible-windows-linux "Direct link to winsetmenubarvisibilityvisible-windows-linux") 

- `visible` boolean

Sets whether the menu bar should be visible. If the menu bar is auto-hide, users can still bring up the menu bar by pressing the single `Alt` key.

#### `win.isMenuBarVisible()` *Windows* *Linux*[â€‹](#winismenubarvisible-windows-linux "Direct link to winismenubarvisible-windows-linux") 

Returns `boolean` - Whether the menu bar is visible.

#### `win.isSnapped()` *Windows*[â€‹](#winissnapped-windows "Direct link to winissnapped-windows") 

Returns `boolean` - whether the window is arranged via [Snap.](https://support.microsoft.com/en-us/windows/snap-your-windows-885a9b1e-a983-a3b1-16cd-c531795e6241)

The window is snapped via buttons shown when the mouse is hovered over window maximize button, or by dragging it to the edges of the screen.

#### `win.setVisibleOnAllWorkspaces(visible[, options])` *macOS* *Linux*[â€‹](#winsetvisibleonallworkspacesvisible-options-macos-linux "Direct link to winsetvisibleonallworkspacesvisible-options-macos-linux") 

- `visible` boolean
- `options` Object (optional)
  - `visibleOnFullScreen` boolean (optional) *macOS* - Sets whether the window should be visible above fullscreen windows.
  - `skipTransformProcessType` boolean (optional) *macOS* - Calling setVisibleOnAllWorkspaces will by default transform the process type between UIElementApplication and ForegroundApplication to ensure the correct behavior. However, this will hide the window and dock for a short time every time it is called. If your window is already of type UIElementApplication, you can bypass this transformation by passing true to skipTransformProcessType.

Sets whether the window should be visible on all workspaces.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

This API does nothing on Windows.

#### `win.isVisibleOnAllWorkspaces()` *macOS* *Linux*[â€‹](#winisvisibleonallworkspaces-macos-linux "Direct link to winisvisibleonallworkspaces-macos-linux") 

Returns `boolean` - Whether the window is visible on all workspaces.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

This API always returns false on Windows.

#### `win.setIgnoreMouseEvents(ignore[, options])`[â€‹](#winsetignoremouseeventsignore-options "Direct link to winsetignoremouseeventsignore-options") 

- `ignore` boolean
- `options` Object (optional)
  - `forward` boolean (optional) *macOS* *Windows* - If true, forwards mouse move messages to Chromium, enabling mouse related events such as `mouseleave`. Only used when `ignore` is true. If `ignore` is false, forwarding is always disabled regardless of this value.

Makes the window ignore all mouse events.

All mouse events happened in this window will be passed to the window below this window, but if this window has focus, it will still receive keyboard events.

#### `win.setContentProtection(enable)` *macOS* *Windows*[â€‹](#winsetcontentprotectionenable-macos-windows "Direct link to winsetcontentprotectionenable-macos-windows") 

- `enable` boolean

Prevents the window contents from being captured by other apps.

On macOS it sets the NSWindow\'s sharingType to NSWindowSharingNone. On Windows it calls SetWindowDisplayAffinity with `WDA_EXCLUDEFROMCAPTURE`. For Windows 10 version 2004 and up the window will be removed from capture entirely, older Windows versions behave as if `WDA_MONITOR` is applied capturing a black window.

#### `win.isContentProtected()` *macOS* *Windows*[â€‹](#winiscontentprotected-macos-windows "Direct link to winiscontentprotected-macos-windows") 

Returns `boolean` - whether or not content protection is currently enabled.

#### `win.setFocusable(focusable)` *macOS* *Windows*[â€‹](#winsetfocusablefocusable-macos-windows "Direct link to winsetfocusablefocusable-macos-windows") 

- `focusable` boolean

Changes whether the window can be focused.

On macOS it does not remove the focus from the window.

#### `win.isFocusable()` *macOS* *Windows*[â€‹](#winisfocusable-macos-windows "Direct link to winisfocusable-macos-windows") 

Returns `boolean` - Whether the window can be focused.

#### `win.setParentWindow(parent)`[â€‹](#winsetparentwindowparent "Direct link to winsetparentwindowparent") 

- `parent` BaseWindow \| null

Sets `parent` as current window\'s parent window, passing `null` will turn current window into a top-level window.

#### `win.getParentWindow()`[â€‹](#wingetparentwindow "Direct link to wingetparentwindow") 

Returns `BaseWindow | null` - The parent window or `null` if there is no parent.

#### `win.getChildWindows()`[â€‹](#wingetchildwindows "Direct link to wingetchildwindows") 

Returns `BaseWindow[]` - All child windows.

#### `win.setAutoHideCursor(autoHide)` *macOS*[â€‹](#winsetautohidecursorautohide-macos "Direct link to winsetautohidecursorautohide-macos") 

- `autoHide` boolean

Controls whether to hide cursor when typing.

#### `win.selectPreviousTab()` *macOS*[â€‹](#winselectprevioustab-macos "Direct link to winselectprevioustab-macos") 

Selects the previous tab when native tabs are enabled and there are other tabs in the window.

#### `win.selectNextTab()` *macOS*[â€‹](#winselectnexttab-macos "Direct link to winselectnexttab-macos") 

Selects the next tab when native tabs are enabled and there are other tabs in the window.

#### `win.showAllTabs()` *macOS*[â€‹](#winshowalltabs-macos "Direct link to winshowalltabs-macos") 

Shows or hides the tab overview when native tabs are enabled.

#### `win.mergeAllWindows()` *macOS*[â€‹](#winmergeallwindows-macos "Direct link to winmergeallwindows-macos") 

Merges all windows into one window with multiple tabs when native tabs are enabled and there is more than one open window.

#### `win.moveTabToNewWindow()` *macOS*[â€‹](#winmovetabtonewwindow-macos "Direct link to winmovetabtonewwindow-macos") 

Moves the current tab into a new window if native tabs are enabled and there is more than one tab in the current window.

#### `win.toggleTabBar()` *macOS*[â€‹](#wintoggletabbar-macos "Direct link to wintoggletabbar-macos") 

Toggles the visibility of the tab bar if native tabs are enabled and there is only one tab in the current window.

#### `win.addTabbedWindow(baseWindow)` *macOS*[â€‹](#winaddtabbedwindowbasewindow-macos "Direct link to winaddtabbedwindowbasewindow-macos") 

- `baseWindow` BaseWindow

Adds a window as a tab on this window, after the tab for the window instance.

#### `win.setVibrancy(type)` *macOS*[â€‹](#winsetvibrancytype-macos "Direct link to winsetvibrancytype-macos") 

- `type` string \| null - Can be `titlebar`, `selection`, `menu`, `popover`, `sidebar`, `header`, `sheet`, `window`, `hud`, `fullscreen-ui`, `tooltip`, `content`, `under-window`, or `under-page`. See the [macOS documentation](https://developer.apple.com/documentation/appkit/nsvisualeffectview?preferredLanguage=objc) for more details.

Adds a vibrancy effect to the window. Passing `null` or an empty string will remove the vibrancy effect on the window.

#### `win.setBackgroundMaterial(material)` *Windows*[â€‹](#winsetbackgroundmaterialmaterial-windows "Direct link to winsetbackgroundmaterialmaterial-windows") 

- `material` string
  - `auto` - Let the Desktop Window Manager (DWM) automatically decide the system-drawn backdrop material for this window. This is the default.
  - `none` - Don\'t draw any system backdrop.
  - `mica` - Draw the backdrop material effect corresponding to a long-lived window.
  - `acrylic` - Draw the backdrop material effect corresponding to a transient window.
  - `tabbed` - Draw the backdrop material effect corresponding to a window with a tabbed title bar.

This method sets the browser window\'s system-drawn background material, including behind the non-client area.

See the [Windows documentation](https://learn.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwm_systembackdrop_type) for more details.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

This method is only supported on Windows 11 22H2 and up.

#### `win.setWindowButtonPosition(position)` *macOS*[â€‹](#winsetwindowbuttonpositionposition-macos "Direct link to winsetwindowbuttonpositionposition-macos") 

- `position` [Point](/docs/latest/api/structures/point) \| null

Set a custom position for the traffic light buttons in frameless window. Passing `null` will reset the position to default.

#### `win.getWindowButtonPosition()` *macOS*[â€‹](#wingetwindowbuttonposition-macos "Direct link to wingetwindowbuttonposition-macos") 

Returns `Point | null` - The custom position for the traffic light buttons in frameless window, `null` will be returned when there is no custom position.

#### `win.setTouchBar(touchBar)` *macOS*[â€‹](#winsettouchbartouchbar-macos "Direct link to winsettouchbartouchbar-macos") 

- `touchBar` TouchBar \| null

Sets the touchBar layout for the current window. Specifying `null` or `undefined` clears the touch bar. This method only has an effect if the machine has a touch bar.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

The TouchBar API is currently experimental and may change or be removed in future Electron releases.

#### `win.setTitleBarOverlay(options)` *Windows* *Linux*[â€‹](#winsettitlebaroverlayoptions-windows-linux "Direct link to winsettitlebaroverlayoptions-windows-linux") 

- `options` Object
  - `color` String (optional) - The CSS color of the Window Controls Overlay when enabled.
  - `symbolColor` String (optional) - The CSS color of the symbols on the Window Controls Overlay when enabled.
  - `height` Integer (optional) - The height of the title bar and Window Controls Overlay in pixels.

On a Window with Window Controls Overlay already enabled, this method updates the style of the title bar overlay.

On Linux, the `symbolColor` is automatically calculated to have minimum accessible contrast to the `color` if not explicitly set.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/base-window.md)