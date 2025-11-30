# Source: https://www.electronjs.org/docs/latest/tutorial/tutorial-preload

On this page

# Using Preload Scripts

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)]Follow along the tutorial

This is **part 3** of the Electron tutorial.

1.  [Prerequisites](/docs/latest/tutorial/tutorial-prerequisites)
2.  [Building your First App](/docs/latest/tutorial/tutorial-first-app)
3.  **[Using Preload Scripts](/docs/latest/tutorial/tutorial-preload)**
4.  [Adding Features](/docs/latest/tutorial/tutorial-adding-features)
5.  [Packaging Your Application](/docs/latest/tutorial/tutorial-packaging)
6.  [Publishing and Updating](/docs/latest/tutorial/tutorial-publishing-updating)

## Learning goals[â€‹](#learning-goals "Direct link to Learning goals") 

In this part of the tutorial, you will learn what a preload script is and how to use one to securely expose privileged APIs into the renderer process. You will also learn how to communicate between main and renderer processes with Electron\'s inter-process communication (IPC) modules.

## What is a preload script?[â€‹](#what-is-a-preload-script "Direct link to What is a preload script?") 

Electron\'s main process is a Node.js environment that has full operating system access. On top of [Electron modules](/docs/latest/api/app), you can also access [Node.js built-ins](https://nodejs.org/dist/latest/docs/api/), as well as any packages installed via npm. On the other hand, renderer processes run web pages and do not run Node.js by default for security reasons.

To bridge Electron\'s different process types together, we will need to use a special script called a **preload**.

## Augmenting the renderer with a preload script[â€‹](#augmenting-the-renderer-with-a-preload-script "Direct link to Augmenting the renderer with a preload script") 

A BrowserWindow\'s preload script runs in a context that has access to both the HTML DOM and a limited subset of Node.js and Electron APIs.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)]Preload script sandboxing

From Electron 20 onwards, preload scripts are **sandboxed** by default and no longer have access to a full Node.js environment. Practically, this means that you have a polyfilled `require` function that only has access to a limited set of APIs.

Available API

Details

Electron modules

Renderer process modules

Node.js modules

[`events`](https://nodejs.org/api/events.html), [`timers`](https://nodejs.org/api/timers.html), [`url`](https://nodejs.org/api/url.html)

Polyfilled globals

[`Buffer`](https://nodejs.org/api/buffer.html), [`process`](/docs/latest/api/process), [`clearImmediate`](https://nodejs.org/api/timers.html#timers_clearimmediate_immediate), [`setImmediate`](https://nodejs.org/api/timers.html#timers_setimmediate_callback_args)

For more information, check out the [Process Sandboxing](/docs/latest/tutorial/sandbox) guide.

Preload scripts are injected before a web page loads in the renderer, similar to a Chrome extension\'s [content scripts](https://developer.chrome.com/docs/extensions/mv3/content_scripts/). To add features to your renderer that require privileged access, you can define [global](https://developer.mozilla.org/en-US/docs/Glossary/Global_object) objects through the [contextBridge](/docs/latest/api/context-bridge) API.

To demonstrate this concept, you will create a preload script that exposes your app\'s versions of Chrome, Node, and Electron into the renderer.

Add a new `preload.js` script that exposes selected properties of Electron\'s `process.versions` object to the renderer process in a `versions` global variable.

preload.js

``` 
const  = require('electron')

contextBridge.exposeInMainWorld('versions', )
```

To attach this script to your renderer process, pass its path to the `webPreferences.preload` option in the BrowserWindow constructor:

main.js

``` 
const  = require('electron')

const path = require('node:path')

const createWindow = () => 
  })

  win.loadFile('index.html')
}

app.whenReady().then(() => )
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)]info

There are two Node.js concepts that are used here:

- The [`__dirname`](https://nodejs.org/api/modules.html#modules_dirname) string points to the path of the currently executing script (in this case, your project\'s root folder).
- The [`path.join`](https://nodejs.org/api/path.html#path_path_join_paths) API joins multiple path segments together, creating a combined path string that works across all platforms.

At this point, the renderer has access to the `versions` global, so let\'s display that information in the window. This variable can be accessed via `window.versions` or simply `versions`. Create a `renderer.js` script that uses the [`document.getElementById`](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById) DOM API to replace the displayed text for the HTML element with `info` as its `id` property.

renderer.js

``` 
const information = document.getElementById('info')
information.innerText = `This app is using Chrome (v$), Node.js (v$), and Electron (v$)`
```

Then, modify your `index.html` by adding a new element with `info` as its `id` property, and attach your `renderer.js` script:

index.html

``` 
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta
      http-equiv="Content-Security-Policy"
      content="default-src 'self'; script-src 'self'"
    />
    <meta
      http-equiv="X-Content-Security-Policy"
      content="default-src 'self'; script-src 'self'"
    />
    <title>Hello from Electron renderer!</title>
  </head>
  <body>
    <h1>Hello from Electron renderer!</h1>
    <p>ð</p>
    <p id="info"></p>
  </body>
  <script src="./renderer.js"></script>
</html>
```

After following the above steps, your app should look something like this:

![Electron app showing This app is using Chrome (v102.0.5005.63), Node.js (v16.14.2), and Electron (v19.0.3)](/assets/images/preload-example-f77948d27686974e427084fa94fe620c.png)

And the code should look like this:

[][][]

[docs/fiddles/tutorial-preload (39.2.4)](https://github.com/electron/electron/tree/v39.2.4/docs/fiddles/tutorial-preload)[Open in Fiddle](https://fiddle.electronjs.org/launch?target=electron/v39.2.4/docs/fiddles/tutorial-preload)

- main.js
- preload.js
- index.html
- renderer.js

``` 
const  = require('electron/main')
const path = require('node:path')

const createWindow = () => 
  })

  win.loadFile('index.html')
}

app.whenReady().then(() => 
  })
})

app.on('window-all-closed', () => 
})
```

``` 
const  = require('electron/renderer')

contextBridge.exposeInMainWorld('versions', )
```

``` 
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta
      http-equiv="Content-Security-Policy"
      content="default-src 'self'; script-src 'self'"
    />
    <meta
      http-equiv="X-Content-Security-Policy"
      content="default-src 'self'; script-src 'self'"
    />
    <title>Hello from Electron renderer!</title>
  </head>
  <body>
    <h1>Hello from Electron renderer!</h1>
    <p>ð</p>
    <p id="info"></p>
  </body>
  <script src="./renderer.js"></script>
</html>
```

``` 
const information = document.getElementById('info')
information.innerText = `This app is using Chrome (v$), Node.js (v$), and Electron (v$)`
```

## Communicating between processes[â€‹](#communicating-between-processes "Direct link to Communicating between processes") 

As we have mentioned above, Electron\'s main and renderer process have distinct responsibilities and are not interchangeable. This means it is not possible to access the Node.js APIs directly from the renderer process, nor the HTML Document Object Model (DOM) from the main process.

The solution for this problem is to use Electron\'s `ipcMain` and `ipcRenderer` modules for inter-process communication (IPC). To send a message from your web page to the main process, you can set up a main process handler with `ipcMain.handle` and then expose a function that calls `ipcRenderer.invoke` to trigger the handler in your preload script.

To illustrate, we will add a global function to the renderer called `ping()` that will return a string from the main process.

First, set up the `invoke` call in your preload script:

preload.js

``` 
const  = require('electron')

contextBridge.exposeInMainWorld('versions', )
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)]IPC security

Notice how we wrap the `ipcRenderer.invoke('ping')` call in a helper function rather than expose the `ipcRenderer` module directly via context bridge. You **never** want to directly expose the entire `ipcRenderer` module via preload. This would give your renderer the ability to send arbitrary IPC messages to the main process, which becomes a powerful attack vector for malicious code.

Then, set up your `handle` listener in the main process. We do this *before* loading the HTML file so that the handler is guaranteed to be ready before you send out the `invoke` call from the renderer.

main.js

``` 
const  = require('electron/main')

const path = require('node:path')

const createWindow = () => 
  })
  win.loadFile('index.html')
}
app.whenReady().then(() => )
```

Once you have the sender and receiver set up, you can now send messages from the renderer to the main process through the `'ping'` channel you just defined.

renderer.js

``` 
const func = async () => 

func()
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)]info

For more in-depth explanations on using the `ipcRenderer` and `ipcMain` modules, check out the full [Inter-Process Communication](/docs/latest/tutorial/ipc) guide.

## Summary[â€‹](#summary "Direct link to Summary") 

A preload script contains code that runs before your web page is loaded into the browser window. It has access to both DOM APIs and Node.js environment, and is often used to expose privileged APIs to the renderer via the `contextBridge` API.

Because the main and renderer processes have very different responsibilities, Electron apps often use the preload script to set up inter-process communication (IPC) interfaces to pass arbitrary messages between the two kinds of processes.

In the next part of the tutorial, we will be showing you resources on adding more functionality to your app, then teaching you how to distribute your app to users.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/tutorial/tutorial-3-preload.md)