# Source: https://www.electronjs.org/docs/latest/tutorial/keyboard-shortcuts

On this page

# Keyboard Shortcuts

## Accelerators[â€‹](#accelerators "Direct link to Accelerators") 

Accelerators are strings that can be used to represent keyboard shortcuts throughout your Electron. These strings can contain multiple modifiers keys and a single key code joined by the `+` character.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

Accelerators are **case-insensitive**.

### Available modifiers[â€‹](#available-modifiers "Direct link to Available modifiers") 

- `Command` (or `Cmd` for short)
- `Control` (or `Ctrl` for short)
- `CommandOrControl` (or `CmdOrCtrl` for short)
- `Alt`
- `Option`
- `AltGr`
- `Shift`
- `Super` (or `Meta` as alias)

### Available key codes[â€‹](#available-key-codes "Direct link to Available key codes") 

- `0` to `9`
- `A` to `Z`
- `F1` to `F24`
- Various Punctuation: `)`, `!`, `@`, `#`, `$`, `%`, `^`, `&`, `*`, `(`, `:`, `;`, `:`, `+`, `=`, `<`, `,`, `_`, `-`, `>`, `.`, `?`, `/`, `~`, `` ` ``, ``, `"`
- `Plus`
- `Space`
- `Tab`
- `Capslock`
- `Numlock`
- `Scrolllock`
- `Backspace`
- `Delete`
- `Insert`
- `Return` (or `Enter` as alias)
- `Up`, `Down`, `Left` and `Right`
- `Home` and `End`
- `PageUp` and `PageDown`
- `Escape` (or `Esc` for short)
- `VolumeUp`, `VolumeDown` and `VolumeMute`
- `MediaNextTrack`, `MediaPreviousTrack`, `MediaStop` and `MediaPlayPause`
- `PrintScreen`
- NumPad Keys
  - `num0` - `num9`
  - `numdec` - decimal key
  - `numadd` - numpad `+` key
  - `numsub` - numpad `-` key
  - `nummult` - numpad `*` key
  - `numdiv` - numpad `Ã·` key

### Cross-platform modifiers[â€‹](#cross-platform-modifiers "Direct link to Cross-platform modifiers") 

Many modifier accelerators map to different keys between operating systems.

Modifier

macOS

Windows and Linux

`CommandOrControl`

Command (âŒ˜)

Control

`Command`

Command (âŒ˜)

N/A

`Control`

Control (\^)

Control

`Alt`

Option (âŒ¥)

Alt

`Option`

Option (âŒ¥)

N/A

`Super` (`Meta`)

Command (âŒ˜)

Windows (âŠž)

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)]info

- On Linux and Windows, the `Command` modifier does not have any effect. In general, you should use the `CommandOrControl` modifier instead, which represents [âŒ˜ Cmd] on macOS and [Ctrl] on Linux and Windows.
- Use `Alt` instead of `Option`. The [âŒ¥ Opt] key only exists on macOS, whereas the `Alt` will map to the appropriate modifier on all platforms.

#### Examples[â€‹](#examples "Direct link to Examples") 

Here are some examples of cross-platform Electron accelerators for common editing operations:

- Copy: `CommandOrControl+C`
- Paste: `CommandOrControl+V`
- Undo: `CommandOrControl+Z`
- Redo: `CommandOrControl+Shift+Z`

## Local shortcuts[â€‹](#local-shortcuts "Direct link to Local shortcuts") 

**Local** keyboard shortcuts are triggered only when the application is focused. These shortcuts map to specific menu items within the app\'s main [application menu](/docs/latest/tutorial/application-menu).

To define a local keyboard shortcut, you need to configure the `accelerator` property when creating a [MenuItem](/docs/latest/api/menu-item). Then, the `click` event associated to that menu item will trigger upon using that accelerator.

Opening a dialog via accelerator (local)

``` 
const  = require('electron/main')

const menu = new Menu()

// The first submenu needs to be the app menu on macOS
if (process.platform === 'darwin') )
  menu.append(appMenu)
}

const submenu = Menu.buildFromTemplate([),
  accelerator: 'CommandOrControl+Alt+R'
}])
menu.append(new MenuItem())

Menu.setApplicationMenu(menu)
```

In the above example, a native \"Hello World\" dialog will open when pressing [âŒ˜ Cmd]+[âŒ¥ Opt]+[R] on macOS or [Ctrl]+[Alt]+[R] on other platforms.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)]tip

Accelerators can work even when menu items are hidden. On macOS, this feature can be disabled by setting `acceleratorWorksWhenHidden: false` when building a `MenuItem`.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)]tip

On Windows and Linux, the `registerAccelerator` property of the `MenuItem` can be set to `false` so that the accelerator is visible in the system menu but not enabled.

## Global shortcuts[â€‹](#global-shortcuts "Direct link to Global shortcuts") 

**Global** keyboard shortcuts work even when your app is out of focus. To configure a global keyboard shortcut, you can use the [`globalShortcut.register`](/docs/latest/api/global-shortcut#globalshortcutregisteraccelerator-callback) function to specify shortcuts.

Opening a dialog via accelerator (global)

``` 
const  = require('electron/main')

globalShortcut.register('CommandOrControl+Alt+R', () => )
})
```

To later unregister a shortcut, you can use the [`globalShortcut.unregisterAccelerator`](/docs/latest/api/global-shortcut#globalshortcutunregisteraccelerator) function.

Opening a dialog via accelerator (global)

``` 
const  = require('electron/main')

globalShortcut.unregister('CommandOrControl+Alt+R')
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)]warning

On macOS, there\'s a long-standing bug with `globalShortcut` that prevents it from working with keyboard layouts other than QWERTY ([electron/electron#19747](https://github.com/electron/electron/issues/19747)).

## Shortcuts within a window[â€‹](#shortcuts-within-a-window "Direct link to Shortcuts within a window") 

### In the renderer process[â€‹](#in-the-renderer-process "Direct link to In the renderer process") 

If you want to handle keyboard shortcuts within a [BaseWindow](/docs/latest/api/base-window), you can listen for the [`keyup`](https://developer.mozilla.org/en-US/docs/Web/API/Element/keyup_event) and [`keydown`](https://developer.mozilla.org/en-US/docs/Web/API/Element/keydown_event) DOM Events inside the renderer process using the [addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener) API.

[][][]

[docs/fiddles/features/keyboard-shortcuts/web-apis (39.2.4)](https://github.com/electron/electron/tree/v39.2.4/docs/fiddles/features/keyboard-shortcuts/web-apis)[Open in Fiddle](https://fiddle.electronjs.org/launch?target=electron/v39.2.4/docs/fiddles/features/keyboard-shortcuts/web-apis)

- main.js
- index.html
- renderer.js

``` 
// Modules to control application life and create native browser window
const  = require('electron/main')

function createWindow () )

  // and load the index.html of the app.
  mainWindow.loadFile('index.html')
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(() => )
})

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', function () )
```

``` 
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <!-- https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP -->
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'">
    <meta http-equiv="X-Content-Security-Policy" content="default-src 'self'; script-src 'self'">
    <title>Hello World!</title>
  </head>
  <body>
    <h1>Hello World!</h1>

    <p>Hit any key with this window focused to see it captured here.</p>
    <div><span>Last Key Pressed: </span><span id="last-keypress"></span></div>
    <script src="./renderer.js"></script>
  </body>
</html>
```

``` 
function handleKeyPress (event) `)
}

window.addEventListener('keyup', handleKeyPress, true)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

The third parameter `true` indicates that the listener will always receive key presses before other listeners so they can\'t have `stopPropagation()` called on them.

#### Intercepting events in the main process[â€‹](#intercepting-events-in-the-main-process "Direct link to Intercepting events in the main process") 

The [`before-input-event`](/docs/latest/api/web-contents#event-before-input-event) event is emitted before dispatching `keydown` and `keyup` events in the renderer process. It can be used to catch and handle custom shortcuts that are not visible in the menu.

Intercepting the Ctrl+I event from the main process

``` 
const  = require('electron/main')

app.whenReady().then(() => 
  })
})
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/tutorial/keyboard-shortcuts.md)