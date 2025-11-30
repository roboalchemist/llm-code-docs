# Source: https://www.electronjs.org/docs/latest/tutorial/ipc

On this page

# Inter-Process Communication

Inter-process communication (IPC) is a key part of building feature-rich desktop applications in Electron. Because the main and renderer processes have different responsibilities in Electron\'s process model, IPC is the only way to perform many common tasks, such as calling a native API from your UI or triggering changes in your web contents from native menus.

## IPC channels[â€‹](#ipc-channels "Direct link to IPC channels") 

In Electron, processes communicate by passing messages through developer-defined \"channels\" with the [`ipcMain`](/docs/latest/api/ipc-main) and [`ipcRenderer`](/docs/latest/api/ipc-renderer) modules. These channels are **arbitrary** (you can name them anything you want) and **bidirectional** (you can use the same channel name for both modules).

In this guide, we\'ll be going over some fundamental IPC patterns with concrete examples that you can use as a reference for your app code.

## Understanding context-isolated processes[â€‹](#understanding-context-isolated-processes "Direct link to Understanding context-isolated processes") 

Before proceeding to implementation details, you should be familiar with the idea of using a [preload script](/docs/latest/tutorial/process-model#preload-scripts) to import Node.js and Electron modules in a context-isolated renderer process.

- For a full overview of Electron\'s process model, you can read the [process model docs](/docs/latest/tutorial/process-model).
- For a primer into exposing APIs from your preload script using the `contextBridge` module, check out the [context isolation tutorial](/docs/latest/tutorial/context-isolation).

## Pattern 1: Renderer to main (one-way)[â€‹](#pattern-1-renderer-to-main-one-way "Direct link to Pattern 1: Renderer to main (one-way)") 

To fire a one-way IPC message from a renderer process to the main process, you can use the [`ipcRenderer.send`](/docs/latest/api/ipc-renderer) API to send a message that is then received by the [`ipcMain.on`](/docs/latest/api/ipc-main) API.

You usually use this pattern to call a main process API from your web contents. We\'ll demonstrate this pattern by creating a simple app that can programmatically change its window title.

For this demo, you\'ll need to add code to your main process, your renderer process, and a preload script. The full code is below, but we\'ll be explaining each file individually in the following sections.

[][][]

[docs/fiddles/ipc/pattern-1 (39.2.4)](https://github.com/electron/electron/tree/v39.2.4/docs/fiddles/ipc/pattern-1)[Open in Fiddle](https://fiddle.electronjs.org/launch?target=electron/v39.2.4/docs/fiddles/ipc/pattern-1)

- main.js
- preload.js
- index.html
- renderer.js

``` 
const  = require('electron/main')
const path = require('node:path')

function handleSetTitle (event, title) 

function createWindow () 
  })

  mainWindow.loadFile('index.html')
}

app.whenReady().then(() => )
})

app.on('window-all-closed', function () )
```

``` 
const  = require('electron/renderer')

contextBridge.exposeInMainWorld('electronAPI', )
```

``` 
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <!-- https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP -->
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'">
    <title>Hello World!</title>
  </head>
  <body>
    Title: <input id="title"/>
    <button id="btn" type="button">Set</button>
    <script src="./renderer.js"></script>
  </body>
</html>
```

``` 
const setButton = document.getElementById('btn')
const titleInput = document.getElementById('title')
setButton.addEventListener('click', () => )
```

### 1. Listen for events with `ipcMain.on`[â€‹](#1-listen-for-events-with-ipcmainon "Direct link to 1-listen-for-events-with-ipcmainon") 

In the main process, set an IPC listener on the `set-title` channel with the `ipcMain.on` API:

main.js (Main Process)

``` 
const  = require('electron')

const path = require('node:path')

// ...

function handleSetTitle (event, title) 

function createWindow () 
  })
  mainWindow.loadFile('index.html')
}

app.whenReady().then(() => )
// ...
```

The above `handleSetTitle` callback has two parameters: an [IpcMainEvent](/docs/latest/api/structures/ipc-main-event) structure and a `title` string. Whenever a message comes through the `set-title` channel, this function will find the BrowserWindow instance attached to the message sender and use the `win.setTitle` API on it.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)]info

Make sure you\'re loading the `index.html` and `preload.js` entry points for the following steps!

### 2. Expose `ipcRenderer.send` via preload[â€‹](#2-expose-ipcrenderersend-via-preload "Direct link to 2-expose-ipcrenderersend-via-preload") 

To send messages to the listener created above, you can use the `ipcRenderer.send` API. By default, the renderer process has no Node.js or Electron module access. As an app developer, you need to choose which APIs to expose from your preload script using the `contextBridge` API.

In your preload script, add the following code, which will expose a global `window.electronAPI` variable to your renderer process.

preload.js (Preload Script)

``` 
const  = require('electron')

contextBridge.exposeInMainWorld('electronAPI', )
```

At this point, you\'ll be able to use the `window.electronAPI.setTitle()` function in the renderer process.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)]Security warning

We don\'t directly expose the whole `ipcRenderer.send` API for [security reasons](/docs/latest/tutorial/context-isolation#security-considerations). Make sure to limit the renderer\'s access to Electron APIs as much as possible.

### 3. Build the renderer process UI[â€‹](#3-build-the-renderer-process-ui "Direct link to 3. Build the renderer process UI") 

In our BrowserWindow\'s loaded HTML file, add a basic user interface consisting of a text input and a button:

index.html

``` 
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <!-- https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP -->
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'">
    <title>Hello World!</title>
  </head>
  <body>
    Title: <input id="title"/>
    <button id="btn" type="button">Set</button>
    <script src="./renderer.js"></script>
  </body>
</html>
```

To make these elements interactive, we\'ll be adding a few lines of code in the imported `renderer.js` file that leverages the `window.electronAPI` functionality exposed from the preload script:

renderer.js (Renderer Process)

``` 
const setButton = document.getElementById('btn')
const titleInput = document.getElementById('title')
setButton.addEventListener('click', () => )
```

At this point, your demo should be fully functional. Try using the input field and see what happens to your BrowserWindow title!

## Pattern 2: Renderer to main (two-way)[â€‹](#pattern-2-renderer-to-main-two-way "Direct link to Pattern 2: Renderer to main (two-way)") 

A common application for two-way IPC is calling a main process module from your renderer process code and waiting for a result. This can be done by using [`ipcRenderer.invoke`](/docs/latest/api/ipc-renderer#ipcrendererinvokechannel-args) paired with [`ipcMain.handle`](/docs/latest/api/ipc-main#ipcmainhandlechannel-listener).

In the following example, we\'ll be opening a native file dialog from the renderer process and returning the selected file\'s path.

For this demo, you\'ll need to add code to your main process, your renderer process, and a preload script. The full code is below, but we\'ll be explaining each file individually in the following sections.

[][][]

[docs/fiddles/ipc/pattern-2 (39.2.4)](https://github.com/electron/electron/tree/v39.2.4/docs/fiddles/ipc/pattern-2)[Open in Fiddle](https://fiddle.electronjs.org/launch?target=electron/v39.2.4/docs/fiddles/ipc/pattern-2)

- main.js
- preload.js
- index.html
- renderer.js

``` 
const  = require('electron/main')
const path = require('node:path')

async function handleFileOpen ()  = await dialog.showOpenDialog()
  if (!canceled) 
}

function createWindow () 
  })
  mainWindow.loadFile('index.html')
}

app.whenReady().then(() => )
})

app.on('window-all-closed', function () )
```

``` 
const  = require('electron/renderer')

contextBridge.exposeInMainWorld('electronAPI', )
```

``` 
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <!-- https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP -->
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'">
    <title>Dialog</title>
  </head>
  <body>
    <button type="button" id="btn">Open a File</button>
    File path: <strong id="filePath"></strong>
    <script src='./renderer.js'></script>
  </body>
</html>
```

``` 
const btn = document.getElementById('btn')
const filePathElement = document.getElementById('filePath')

btn.addEventListener('click', async () => )
```

### 1. Listen for events with `ipcMain.handle`[â€‹](#1-listen-for-events-with-ipcmainhandle "Direct link to 1-listen-for-events-with-ipcmainhandle") 

In the main process, we\'ll be creating a `handleFileOpen()` function that calls `dialog.showOpenDialog` and returns the value of the file path selected by the user. This function is used as a callback whenever an `ipcRender.invoke` message is sent through the `dialog:openFile` channel from the renderer process. The return value is then returned as a Promise to the original `invoke` call.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)]A word on error handling

Errors thrown through `handle` in the main process are not transparent as they are serialized and only the `message` property from the original error is provided to the renderer process. Please refer to [#24427](https://github.com/electron/electron/issues/24427) for details.

main.js (Main Process)

``` 
const  = require('electron')

const path = require('node:path')

// ...

async function handleFileOpen ()  = await dialog.showOpenDialog()
  if (!canceled) 
}

function createWindow () 
  })
  mainWindow.loadFile('index.html')
}

app.whenReady().then(() => )
// ...
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)]on channel names

The `dialog:` prefix on the IPC channel name has no effect on the code. It only serves as a namespace that helps with code readability.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)]info

Make sure you\'re loading the `index.html` and `preload.js` entry points for the following steps!

### 2. Expose `ipcRenderer.invoke` via preload[â€‹](#2-expose-ipcrendererinvoke-via-preload "Direct link to 2-expose-ipcrendererinvoke-via-preload") 

In the preload script, we expose a one-line `openFile` function that calls and returns the value of `ipcRenderer.invoke('dialog:openFile')`. We\'ll be using this API in the next step to call the native dialog from our renderer\'s user interface.

preload.js (Preload Script)

``` 
const  = require('electron')

contextBridge.exposeInMainWorld('electronAPI', )
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)]Security warning

We don\'t directly expose the whole `ipcRenderer.invoke` API for [security reasons](/docs/latest/tutorial/context-isolation#security-considerations). Make sure to limit the renderer\'s access to Electron APIs as much as possible.

### 3. Build the renderer process UI[â€‹](#3-build-the-renderer-process-ui-1 "Direct link to 3. Build the renderer process UI") 

Finally, let\'s build the HTML file that we load into our BrowserWindow.

index.html

``` 
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <!-- https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP -->
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'">
    <title>Dialog</title>
  </head>
  <body>
    <button type="button" id="btn">Open a File</button>
    File path: <strong id="filePath"></strong>
    <script src='./renderer.js'></script>
  </body>
</html>
```

The UI consists of a single `#btn` button element that will be used to trigger our preload API, and a `#filePath` element that will be used to display the path of the selected file. Making these pieces work will take a few lines of code in the renderer process script:

renderer.js (Renderer Process)

``` 
const btn = document.getElementById('btn')
const filePathElement = document.getElementById('filePath')

btn.addEventListener('click', async () => )
```

In the above snippet, we listen for clicks on the `#btn` button, and call our `window.electronAPI.openFile()` API to activate the native Open File dialog. We then display the selected file path in the `#filePath` element.

### Note: legacy approaches[â€‹](#note-legacy-approaches "Direct link to Note: legacy approaches") 

The `ipcRenderer.invoke` API was added in Electron 7 as a developer-friendly way to tackle two-way IPC from the renderer process. However, a couple of alternative approaches to this IPC pattern exist.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)]Avoid legacy approaches if possible

We recommend using `ipcRenderer.invoke` whenever possible. The following two-way renderer-to-main patterns are documented for historical purposes.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)]info

For the following examples, we\'re calling `ipcRenderer` directly from the preload script to keep the code samples small.

#### Using `ipcRenderer.send`[â€‹](#using-ipcrenderersend "Direct link to using-ipcrenderersend") 

The `ipcRenderer.send` API that we used for single-way communication can also be leveraged to perform two-way communication. This was the recommended way for asynchronous two-way communication via IPC prior to Electron 7.

preload.js (Preload Script)

``` 
// You can also put expose this code to the renderer
// process with the `contextBridge` API
const  = require('electron')

ipcRenderer.on('asynchronous-reply', (_event, arg) => )
ipcRenderer.send('asynchronous-message', 'ping')
```

main.js (Main Process)

``` 
ipcMain.on('asynchronous-message', (event, arg) => )
```

There are a couple downsides to this approach:

- You need to set up a second `ipcRenderer.on` listener to handle the response in the renderer process. With `invoke`, you get the response value returned as a Promise to the original API call.
- There\'s no obvious way to pair the `asynchronous-reply` message to the original `asynchronous-message` one. If you have very frequent messages going back and forth through these channels, you would need to add additional app code to track each call and response individually.

#### Using `ipcRenderer.sendSync`[â€‹](#using-ipcrenderersendsync "Direct link to using-ipcrenderersendsync") 

The `ipcRenderer.sendSync` API sends a message to the main process and waits *synchronously* for a response.

main.js (Main Process)

``` 
const  = require('electron')

ipcMain.on('synchronous-message', (event, arg) => )
```

preload.js (Preload Script)

``` 
// You can also put expose this code to the renderer
// process with the `contextBridge` API
const  = require('electron')

const result = ipcRenderer.sendSync('synchronous-message', 'ping')
console.log(result) // prints "pong" in the DevTools console
```

The structure of this code is very similar to the `invoke` model, but we recommend **avoiding this API** for performance reasons. Its synchronous nature means that it\'ll block the renderer process until a reply is received.

## Pattern 3: Main to renderer[â€‹](#pattern-3-main-to-renderer "Direct link to Pattern 3: Main to renderer") 

When sending a message from the main process to a renderer process, you need to specify which renderer is receiving the message. Messages need to be sent to a renderer process via its [`WebContents`](/docs/latest/api/web-contents) instance. This WebContents instance contains a [`send`](/docs/latest/api/web-contents#contentssendchannel-args) method that can be used in the same way as `ipcRenderer.send`.

To demonstrate this pattern, we\'ll be building a number counter controlled by the native operating system menu.

For this demo, you\'ll need to add code to your main process, your renderer process, and a preload script. The full code is below, but we\'ll be explaining each file individually in the following sections.

[][][]

[docs/fiddles/ipc/pattern-3 (39.2.4)](https://github.com/electron/electron/tree/v39.2.4/docs/fiddles/ipc/pattern-3)[Open in Fiddle](https://fiddle.electronjs.org/launch?target=electron/v39.2.4/docs/fiddles/ipc/pattern-3)

- main.js
- preload.js
- index.html
- renderer.js

``` 
const  = require('electron/main')
const path = require('node:path')

function createWindow () 
  })

  const menu = Menu.buildFromTemplate([
    ,
        
      ]
    }

  ])

  Menu.setApplicationMenu(menu)
  mainWindow.loadFile('index.html')

  // Open the DevTools.
  mainWindow.webContents.openDevTools()
}

app.whenReady().then(() => )
  createWindow()

  app.on('activate', function () )
})

app.on('window-all-closed', function () )
```

``` 
const  = require('electron/renderer')

contextBridge.exposeInMainWorld('electronAPI', )
```

``` 
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <!-- https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP -->
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'">
    <title>Menu Counter</title>
  </head>
  <body>
    Current value: <strong id="counter">0</strong>
    <script src="./renderer.js"></script>
  </body>
</html>
```

``` 
const counter = document.getElementById('counter')

window.electronAPI.onUpdateCounter((value) => )
```

### 1. Send messages with the `webContents` module[â€‹](#1-send-messages-with-the-webcontents-module "Direct link to 1-send-messages-with-the-webcontents-module") 

For this demo, we\'ll need to first build a custom menu in the main process using Electron\'s `Menu` module that uses the `webContents.send` API to send an IPC message from the main process to the target renderer.

main.js (Main Process)

``` 
const  = require('electron')

const path = require('node:path')

function createWindow () 
  })

  const menu = Menu.buildFromTemplate([
    ,
        
      ]
    }
  ])
  Menu.setApplicationMenu(menu)

  mainWindow.loadFile('index.html')
}
// ...
```

For the purposes of the tutorial, it\'s important to note that the `click` handler sends a message (either `1` or `-1`) to the renderer process through the `update-counter` channel.

``` 
click: () => mainWindow.webContents.send('update-counter', -1)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)]info

Make sure you\'re loading the `index.html` and `preload.js` entry points for the following steps!

### 2. Expose `ipcRenderer.on` via preload[â€‹](#2-expose-ipcrendereron-via-preload "Direct link to 2-expose-ipcrendereron-via-preload") 

Like in the previous renderer-to-main example, we use the `contextBridge` and `ipcRenderer` modules in the preload script to expose IPC functionality to the renderer process:

preload.js (Preload Script)

``` 
const  = require('electron')

contextBridge.exposeInMainWorld('electronAPI', )
```

After loading the preload script, your renderer process should have access to the `window.electronAPI.onUpdateCounter()` listener function.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)]Security warning

We don\'t directly expose the whole `ipcRenderer.on` API for [security reasons](/docs/latest/tutorial/context-isolation#security-considerations). Make sure to limit the renderer\'s access to Electron APIs as much as possible. Also don\'t just pass the callback to `ipcRenderer.on` as this will leak `ipcRenderer` via `event.sender`. Use a custom handler that invoke the `callback` only with the desired arguments.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)]info

In the case of this minimal example, you can call `ipcRenderer.on` directly in the preload script rather than exposing it over the context bridge.

preload.js (Preload Script)

``` 
const  = require('electron')

window.addEventListener('DOMContentLoaded', () => )
})
```

However, this approach has limited flexibility compared to exposing your preload APIs over the context bridge, since your listener can\'t directly interact with your renderer code.

### 3. Build the renderer process UI[â€‹](#3-build-the-renderer-process-ui-2 "Direct link to 3. Build the renderer process UI") 

To tie it all together, we\'ll create an interface in the loaded HTML file that contains a `#counter` element that we\'ll use to display the values:

index.html

``` 
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <!-- https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP -->
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'">
    <title>Menu Counter</title>
  </head>
  <body>
    Current value: <strong id="counter">0</strong>
    <script src="./renderer.js"></script>
  </body>
</html>
```

Finally, to make the values update in the HTML document, we\'ll add a few lines of DOM manipulation so that the value of the `#counter` element is updated whenever we fire an `update-counter` event.

renderer.js (Renderer Process)

``` 
const counter = document.getElementById('counter')

window.electronAPI.onUpdateCounter((value) => )
```

In the above code, we\'re passing in a callback to the `window.electronAPI.onUpdateCounter` function exposed from our preload script. The second `value` parameter corresponds to the `1` or `-1` we were passing in from the `webContents.send` call from the native menu.

### Optional: returning a reply[â€‹](#optional-returning-a-reply "Direct link to Optional: returning a reply") 

There\'s no equivalent for `ipcRenderer.invoke` for main-to-renderer IPC. Instead, you can send a reply back to the main process from within the `ipcRenderer.on` callback.

We can demonstrate this with slight modifications to the code from the previous example. In the renderer process, expose another API to send a reply back to the main process through the `counter-value` channel.

preload.js (Preload Script)

``` 
const  = require('electron')

contextBridge.exposeInMainWorld('electronAPI', )
```

renderer.js (Renderer Process)

``` 
const counter = document.getElementById('counter')

window.electronAPI.onUpdateCounter((value) => )
```

In the main process, listen for `counter-value` events and handle them appropriately.

main.js (Main Process)

``` 
// ...
ipcMain.on('counter-value', (_event, value) => )
// ...
```

## Pattern 4: Renderer to renderer[â€‹](#pattern-4-renderer-to-renderer "Direct link to Pattern 4: Renderer to renderer") 

There\'s no direct way to send messages between renderer processes in Electron using the `ipcMain` and `ipcRenderer` modules. To achieve this, you have two options:

- Use the main process as a message broker between renderers. This would involve sending a message from one renderer to the main process, which would forward the message to the other renderer.
- Pass a [MessagePort](/docs/latest/tutorial/message-ports) from the main process to both renderers. This will allow direct communication between renderers after the initial setup.

## Object serialization[â€‹](#object-serialization "Direct link to Object serialization") 

Electron\'s IPC implementation uses the HTML standard [Structured Clone Algorithm](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm) to serialize objects passed between processes, meaning that only certain types of objects can be passed through IPC channels.

In particular, DOM objects (e.g. `Element`, `Location` and `DOMMatrix`), Node.js objects backed by C++ classes (e.g. `process.env`, some members of `Stream`), and Electron objects backed by C++ classes (e.g. `WebContents`, `BrowserWindow` and `WebFrame`) are not serializable with Structured Clone.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/tutorial/ipc.md)