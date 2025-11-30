# Source: https://www.electronjs.org/docs/latest/api/tray

On this page

# Tray

## Class: Tray[â€‹](#class-tray "Direct link to Class: Tray") 

> Add icons and context menus to the system\'s notification area.

Process: [Main](/docs/latest/glossary#main-process)

`Tray` is an [EventEmitter](https://nodejs.org/api/events.html#events_class_eventemitter).

Creating a basic tray menu

``` 
const  = require('electron')

let tray = null
app.whenReady().then(() => ,
    ,
    ,
    
  ])
  tray.setToolTip('This is my application.')
  tray.setContextMenu(contextMenu)
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)]tip

See also: [A detailed guide about how to implement Tray menus](/docs/latest/tutorial/tray).

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)]warning

Electron\'s built-in classes cannot be subclassed in user code. For more information, see [the FAQ](/docs/latest/faq#class-inheritance-does-not-work-with-electron-built-in-modules).

**Platform Considerations**

**Linux**

- Tray icon uses [StatusNotifierItem](https://www.freedesktop.org/wiki/Specifications/StatusNotifierItem/) by default, when it is not available in user\'s desktop environment the `GtkStatusIcon` will be used instead.
- The `click` event is emitted when the tray icon receives activation from user, however the StatusNotifierItem spec does not specify which action would cause an activation, for some environments it is left mouse click, but for some it might be double left mouse click.
- In order for changes made to individual `MenuItem`s to take effect, you have to call `setContextMenu` again. For example:

``` 
const  = require('electron')

let appIcon = null
app.whenReady().then(() => ,
    
  ])

  // Make a change to the context menu
  contextMenu.items[1].checked = false

  // Call this again for Linux because we modified the context menu
  appIcon.setContextMenu(contextMenu)
})
```

**MacOS**

- Icons passed to the Tray constructor should be [Template Images](/docs/latest/api/native-image#template-image-macos).
- To make sure your icon isn\'t grainy on retina monitors, be sure your `@2x` image is 144dpi.
- If you are bundling your application (e.g., with webpack for development), be sure that the file names are not being mangled or hashed. The filename needs to end in Template, and the `@2x` image needs to have the same filename as the standard image, or MacOS will not magically invert your image\'s colors or use the high density image.
- 16x16 (72dpi) and 32x32@2x (144dpi) work well for most icons.

**Windows**

- It is recommended to use `ICO` icons to get best visual effects.

### `new Tray(image, [guid])`[â€‹](#new-trayimage-guid "Direct link to new-trayimage-guid") 

- `image` ([NativeImage](/docs/latest/api/native-image) \| string)
- `guid` string (optional) *Windows* *macOS* - A unique string used to identify the tray icon. Must adhere to [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) format.

**Windows**

On Windows, if the executable is signed and the signature contains an organization in the subject line then the GUID is permanently associated with that signature. OS level settings like the position of the tray icon in the system tray will persist even if the path to the executable changes. If the executable is not code-signed then the GUID is permanently associated with the path to the executable. Changing the path to the executable will break the creation of the tray icon and a new GUID must be used. However, it is highly recommended to use the GUID parameter only in conjunction with code-signed executable. If an App defines multiple tray icons then each icon must use a separate GUID.

**MacOS**

On macOS, the `guid` is a string used to uniquely identify the tray icon and allow it to retain its position between relaunches. Using the same string for a new tray item will create it in the same position as the previous tray item to use the string.

Creates a new tray icon associated with the `image`.

### Instance Events[â€‹](#instance-events "Direct link to Instance Events") 

The `Tray` module emits the following events:

#### Event: \'click\'[â€‹](#event-click "Direct link to Event: 'click'") 

Returns:

- `event` [KeyboardEvent](/docs/latest/api/structures/keyboard-event)
- `bounds` [Rectangle](/docs/latest/api/structures/rectangle) - The bounds of tray icon.
- `position` [Point](/docs/latest/api/structures/point) - The position of the event.

Emitted when the tray icon is clicked.

Note that on Linux this event is emitted when the tray icon receives an activation, which might not necessarily be left mouse click.

#### Event: \'right-click\' *macOS* *Windows*[â€‹](#event-right-click-macos-windows "Direct link to event-right-click-macos-windows") 

Returns:

- `event` [KeyboardEvent](/docs/latest/api/structures/keyboard-event)
- `bounds` [Rectangle](/docs/latest/api/structures/rectangle) - The bounds of tray icon.

Emitted when the tray icon is right clicked.

#### Event: \'double-click\' *macOS* *Windows*[â€‹](#event-double-click-macos-windows "Direct link to event-double-click-macos-windows") 

Returns:

- `event` [KeyboardEvent](/docs/latest/api/structures/keyboard-event)
- `bounds` [Rectangle](/docs/latest/api/structures/rectangle) - The bounds of tray icon.

Emitted when the tray icon is double clicked.

#### Event: \'middle-click\' *Windows*[â€‹](#event-middle-click-windows "Direct link to event-middle-click-windows") 

Returns:

- `event` [KeyboardEvent](/docs/latest/api/structures/keyboard-event)
- `bounds` [Rectangle](/docs/latest/api/structures/rectangle) - The bounds of tray icon.

Emitted when the tray icon is middle clicked.

#### Event: \'balloon-show\' *Windows*[â€‹](#event-balloon-show-windows "Direct link to event-balloon-show-windows") 

Emitted when the tray balloon shows.

#### Event: \'balloon-click\' *Windows*[â€‹](#event-balloon-click-windows "Direct link to event-balloon-click-windows") 

Emitted when the tray balloon is clicked.

#### Event: \'balloon-closed\' *Windows*[â€‹](#event-balloon-closed-windows "Direct link to event-balloon-closed-windows") 

Emitted when the tray balloon is closed because of timeout or user manually closes it.

#### Event: \'drop\' *macOS*[â€‹](#event-drop-macos "Direct link to event-drop-macos") 

Emitted when any dragged items are dropped on the tray icon.

#### Event: \'drop-files\' *macOS*[â€‹](#event-drop-files-macos "Direct link to event-drop-files-macos") 

Returns:

- `event` Event
- `files` string\[\] - The paths of the dropped files.

Emitted when dragged files are dropped in the tray icon.

#### Event: \'drop-text\' *macOS*[â€‹](#event-drop-text-macos "Direct link to event-drop-text-macos") 

Returns:

- `event` Event
- `text` string - the dropped text string.

Emitted when dragged text is dropped in the tray icon.

#### Event: \'drag-enter\' *macOS*[â€‹](#event-drag-enter-macos "Direct link to event-drag-enter-macos") 

Emitted when a drag operation enters the tray icon.

#### Event: \'drag-leave\' *macOS*[â€‹](#event-drag-leave-macos "Direct link to event-drag-leave-macos") 

Emitted when a drag operation exits the tray icon.

#### Event: \'drag-end\' *macOS*[â€‹](#event-drag-end-macos "Direct link to event-drag-end-macos") 

Emitted when a drag operation ends on the tray or ends at another location.

#### Event: \'mouse-up\' *macOS*[â€‹](#event-mouse-up-macos "Direct link to event-mouse-up-macos") 

Returns:

- `event` [KeyboardEvent](/docs/latest/api/structures/keyboard-event)
- `position` [Point](/docs/latest/api/structures/point) - The position of the event.

Emitted when the mouse is released from clicking the tray icon.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

This will not be emitted if you have set a context menu for your Tray using `tray.setContextMenu`, as a result of macOS-level constraints.

#### Event: \'mouse-down\' *macOS*[â€‹](#event-mouse-down-macos "Direct link to event-mouse-down-macos") 

Returns:

- `event` [KeyboardEvent](/docs/latest/api/structures/keyboard-event)
- `position` [Point](/docs/latest/api/structures/point) - The position of the event.

Emitted when the mouse clicks the tray icon.

#### Event: \'mouse-enter\' *macOS* *Windows*[â€‹](#event-mouse-enter-macos-windows "Direct link to event-mouse-enter-macos-windows") 

Returns:

- `event` [KeyboardEvent](/docs/latest/api/structures/keyboard-event)
- `position` [Point](/docs/latest/api/structures/point) - The position of the event.

Emitted when the mouse enters the tray icon.

#### Event: \'mouse-leave\' *macOS* *Windows*[â€‹](#event-mouse-leave-macos-windows "Direct link to event-mouse-leave-macos-windows") 

Returns:

- `event` [KeyboardEvent](/docs/latest/api/structures/keyboard-event)
- `position` [Point](/docs/latest/api/structures/point) - The position of the event.

Emitted when the mouse exits the tray icon.

#### Event: \'mouse-move\' *macOS* *Windows*[â€‹](#event-mouse-move-macos-windows "Direct link to event-mouse-move-macos-windows") 

Returns:

- `event` [KeyboardEvent](/docs/latest/api/structures/keyboard-event)
- `position` [Point](/docs/latest/api/structures/point) - The position of the event.

Emitted when the mouse moves in the tray icon.

### Instance Methods[â€‹](#instance-methods "Direct link to Instance Methods") 

The `Tray` class has the following methods:

#### `tray.destroy()`[â€‹](#traydestroy "Direct link to traydestroy") 

Destroys the tray icon immediately.

#### `tray.setImage(image)`[â€‹](#traysetimageimage "Direct link to traysetimageimage") 

- `image` ([NativeImage](/docs/latest/api/native-image) \| string)

Sets the `image` associated with this tray icon.

#### `tray.setPressedImage(image)` *macOS*[â€‹](#traysetpressedimageimage-macos "Direct link to traysetpressedimageimage-macos") 

- `image` ([NativeImage](/docs/latest/api/native-image) \| string)

Sets the `image` associated with this tray icon when pressed on macOS.

#### `tray.setToolTip(toolTip)`[â€‹](#traysettooltiptooltip "Direct link to traysettooltiptooltip") 

- `toolTip` string

Sets the hover text for this tray icon. Setting the text to an empty string will remove the tooltip.

#### `tray.setTitle(title[, options])` *macOS*[â€‹](#traysettitletitle-options-macos "Direct link to traysettitletitle-options-macos") 

- `title` string
- `options` Object (optional)
  - `fontType` string (optional) - The font family variant to display, can be `monospaced` or `monospacedDigit`. `monospaced` is available in macOS 10.15+ When left blank, the title uses the default system font.

Sets the title displayed next to the tray icon in the status bar (Support ANSI colors).

#### `tray.getTitle()` *macOS*[â€‹](#traygettitle-macos "Direct link to traygettitle-macos") 

Returns `string` - the title displayed next to the tray icon in the status bar

#### `tray.setIgnoreDoubleClickEvents(ignore)` *macOS*[â€‹](#traysetignoredoubleclickeventsignore-macos "Direct link to traysetignoredoubleclickeventsignore-macos") 

- `ignore` boolean

Sets the option to ignore double click events. Ignoring these events allows you to detect every individual click of the tray icon.

This value is set to false by default.

#### `tray.getIgnoreDoubleClickEvents()` *macOS*[â€‹](#traygetignoredoubleclickevents-macos "Direct link to traygetignoredoubleclickevents-macos") 

Returns `boolean` - Whether double click events will be ignored.

#### `tray.displayBalloon(options)` *Windows*[â€‹](#traydisplayballoonoptions-windows "Direct link to traydisplayballoonoptions-windows") 

- `options` Object
  - `icon` ([NativeImage](/docs/latest/api/native-image) \| string) (optional) - Icon to use when `iconType` is `custom`.
  - `iconType` string (optional) - Can be `none`, `info`, `warning`, `error` or `custom`. Default is `custom`.
  - `title` string
  - `content` string
  - `largeIcon` boolean (optional) - The large version of the icon should be used. Default is `true`. Maps to [`NIIF_LARGE_ICON`](https://learn.microsoft.com/en-us/windows/win32/api/shellapi/ns-shellapi-notifyicondataa#niif_large_icon-0x00000020).
  - `noSound` boolean (optional) - Do not play the associated sound. Default is `false`. Maps to [`NIIF_NOSOUND`](https://learn.microsoft.com/en-us/windows/win32/api/shellapi/ns-shellapi-notifyicondataa#niif_nosound-0x00000010).
  - `respectQuietTime` boolean (optional) - Do not display the balloon notification if the current user is in \"quiet time\". Default is `false`. Maps to [`NIIF_RESPECT_QUIET_TIME`](https://learn.microsoft.com/en-us/windows/win32/api/shellapi/ns-shellapi-notifyicondataa#niif_respect_quiet_time-0x00000080).

Displays a tray balloon.

#### `tray.removeBalloon()` *Windows*[â€‹](#trayremoveballoon-windows "Direct link to trayremoveballoon-windows") 

Removes a tray balloon.

#### `tray.focus()` *Windows*[â€‹](#trayfocus-windows "Direct link to trayfocus-windows") 

Returns focus to the taskbar notification area. Notification area icons should use this message when they have completed their UI operation. For example, if the icon displays a shortcut menu, but the user presses ESC to cancel it, use `tray.focus()` to return focus to the notification area.

#### `tray.popUpContextMenu([menu, position])` *macOS* *Windows*[â€‹](#traypopupcontextmenumenu-position-macos-windows "Direct link to traypopupcontextmenumenu-position-macos-windows") 

- `menu` Menu (optional)
- `position` [Point](/docs/latest/api/structures/point) (optional) - The pop up position.

Pops up the context menu of the tray icon. When `menu` is passed, the `menu` will be shown instead of the tray icon\'s context menu.

The `position` is only available on Windows, and it is (0, 0) by default.

#### `tray.closeContextMenu()` *macOS* *Windows*[â€‹](#trayclosecontextmenu-macos-windows "Direct link to trayclosecontextmenu-macos-windows") 

Closes an open context menu, as set by `tray.setContextMenu()`.

#### `tray.setContextMenu(menu)`[â€‹](#traysetcontextmenumenu "Direct link to traysetcontextmenumenu") 

- `menu` Menu \| null

Sets the context menu for this icon.

#### `tray.getBounds()` *macOS* *Windows*[â€‹](#traygetbounds-macos-windows "Direct link to traygetbounds-macos-windows") 

Returns [Rectangle](/docs/latest/api/structures/rectangle)

The `bounds` of this tray icon as `Object`.

#### `tray.getGUID()` *macOS* *Windows*[â€‹](#traygetguid-macos-windows "Direct link to traygetguid-macos-windows") 

Returns `string | null` - The GUID used to uniquely identify the tray icon and allow it to retain its position between relaunches, or null if none is set.

#### `tray.isDestroyed()`[â€‹](#trayisdestroyed "Direct link to trayisdestroyed") 

Returns `boolean` - Whether the tray icon is destroyed.

## Platform considerations[â€‹](#platform-considerations "Direct link to Platform considerations") 

### Linux[â€‹](#linux "Direct link to Linux") 

- Tray icon uses [StatusNotifierItem](https://www.freedesktop.org/wiki/Specifications/StatusNotifierItem/) by default, when it is not available in user\'s desktop environment the `GtkStatusIcon` will be used instead.
- The `click` event is emitted when the tray icon receives activation from user, however the StatusNotifierItem spec does not specify which action would cause an activation, for some environments it is left mouse click, but for some it might be double left mouse click.
- In order for changes made to individual `MenuItem`s to take effect, you have to call `setContextMenu` again. For example:

``` 
const  = require('electron')

let appIcon = null
app.whenReady().then(() => ,
    
  ])

  // Make a change to the context menu
  contextMenu.items[1].checked = false

  // Call this again for Linux because we modified the context menu
  appIcon.setContextMenu(contextMenu)
})
```

### macOS[â€‹](#macos "Direct link to macOS") 

- Icons passed to the Tray constructor should be [Template Images](/docs/latest/api/native-image#template-image-macos).
- To make sure your icon isn\'t grainy on retina monitors, be sure your `@2x` image is 144dpi.
- If you are bundling your application (e.g., with webpack for development), be sure that the file names are not being mangled or hashed. The filename needs to end in Template, and the `@2x` image needs to have the same filename as the standard image, or MacOS will not magically invert your image\'s colors or use the high density image.
- 16x16 (72dpi) and 32x32@2x (144dpi) work well for most icons.

### Windows[â€‹](#windows "Direct link to Windows") 

- It is recommended to use `ICO` icons to get best visual effects.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/tray.md)