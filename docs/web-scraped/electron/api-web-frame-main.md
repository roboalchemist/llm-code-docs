# Source: https://www.electronjs.org/docs/latest/api/web-frame-main

On this page

# webFrameMain

> Control web pages and iframes.

Process: [Main](/docs/latest/glossary#main-process)

The `webFrameMain` module can be used to lookup frames across existing [`WebContents`](/docs/latest/api/web-contents) instances. Navigation events are the common use case.

``` 
const  = require('electron')

const win = new BrowserWindow()
win.loadURL('https://twitter.com')

win.webContents.on(
  'did-frame-navigate',
  (event, url, httpResponseCode, httpStatusText, isMainFrame, frameProcessId, frameRoutingId) => 
  }
)
```

You can also access frames of existing pages by using the `mainFrame` property of [`WebContents`](/docs/latest/api/web-contents).

``` 
const  = require('electron')

async function main () )
  await win.loadURL('https://reddit.com')

  const youtubeEmbeds = win.webContents.mainFrame.frames.filter((frame) =>  catch 
  })

  console.log(youtubeEmbeds)
}

main()
```

## Methods[â€‹](#methods "Direct link to Methods") 

These methods can be accessed from the `webFrameMain` module:

### `webFrameMain.fromId(processId, routingId)`[â€‹](#webframemainfromidprocessid-routingid "Direct link to webframemainfromidprocessid-routingid") 

- `processId` Integer - An `Integer` representing the internal ID of the process which owns the frame.
- `routingId` Integer - An `Integer` representing the unique frame ID in the current renderer process. Routing IDs can be retrieved from `WebFrameMain` instances (`frame.routingId`) and are also passed by frame specific `WebContents` navigation events (e.g. `did-frame-navigate`).

Returns `WebFrameMain | undefined` - A frame with the given process and routing IDs, or `undefined` if there is no WebFrameMain associated with the given IDs.

### `webFrameMain.fromFrameToken(processId, frameToken)`[â€‹](#webframemainfromframetokenprocessid-frametoken "Direct link to webframemainfromframetokenprocessid-frametoken") 

- `processId` Integer - An `Integer` representing the internal ID of the process which owns the frame.
- `frameToken` string - A `string` token identifying the unique frame. Can also be retrieved in the renderer process via [`webFrame.frameToken`](/docs/latest/api/web-frame#webframeframetoken-readonly).

Returns `WebFrameMain | null` - A frame with the given process and frame token, or `null` if there is no WebFrameMain associated with the given IDs.

## Class: WebFrameMain[â€‹](#class-webframemain "Direct link to Class: WebFrameMain") 

Process: [Main](/docs/latest/glossary#main-process)\
*This class is not exported from the `'electron'` module. It is only available as a return value of other methods in the Electron API.*

### Instance Events[â€‹](#instance-events "Direct link to Instance Events") 

#### Event: \'dom-ready\'[â€‹](#event-dom-ready "Direct link to Event: 'dom-ready'") 

Emitted when the document is loaded.

### Instance Methods[â€‹](#instance-methods "Direct link to Instance Methods") 

#### `frame.executeJavaScript(code[, userGesture])`[â€‹](#frameexecutejavascriptcode-usergesture "Direct link to frameexecutejavascriptcode-usergesture") 

- `code` string
- `userGesture` boolean (optional) - Default is `false`.

Returns `Promise<unknown>` - A promise that resolves with the result of the executed code or is rejected if execution throws or results in a rejected promise.

Evaluates `code` in page.

In the browser window some HTML APIs like `requestFullScreen` can only be invoked by a gesture from the user. Setting `userGesture` to `true` will remove this limitation.

#### `frame.reload()`[â€‹](#framereload "Direct link to framereload") 

Returns `boolean` - Whether the reload was initiated successfully. Only results in `false` when the frame has no history.

#### `frame.isDestroyed()`[â€‹](#frameisdestroyed "Direct link to frameisdestroyed") 

Returns `boolean` - Whether the frame is destroyed.

#### `frame.send(channel, ...args)`[â€‹](#framesendchannel-args "Direct link to framesendchannel-args") 

- `channel` string
- `...args` any\[\]

Send an asynchronous message to the renderer process via `channel`, along with arguments. Arguments will be serialized with the [Structured Clone Algorithm](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm), just like [`postMessage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage), so prototype chains will not be included. Sending Functions, Promises, Symbols, WeakMaps, or WeakSets will throw an exception.

The renderer process can handle the message by listening to `channel` with the [`ipcRenderer`](/docs/latest/api/ipc-renderer) module.

#### `frame.postMessage(channel, message, [transfer])`[â€‹](#framepostmessagechannel-message-transfer "Direct link to framepostmessagechannel-message-transfer") 

- `channel` string
- `message` any
- `transfer` MessagePortMain\[\] (optional)

Send a message to the renderer process, optionally transferring ownership of zero or more [`MessagePortMain`](/docs/latest/api/message-port-main) objects.

The transferred `MessagePortMain` objects will be available in the renderer process by accessing the `ports` property of the emitted event. When they arrive in the renderer, they will be native DOM `MessagePort` objects.

For example:

``` 
// Main process
const win = new BrowserWindow()
const  = new MessageChannelMain()
win.webContents.mainFrame.postMessage('port', , [port1])

// Renderer process
ipcRenderer.on('port', (e, msg) => )
```

#### `frame.collectJavaScriptCallStack()` *Experimental*[â€‹](#framecollectjavascriptcallstack-experimental "Direct link to framecollectjavascriptcallstack-experimental") 

Returns `Promise<string> | Promise<void>` - A promise that resolves with the currently running JavaScript call stack. If no JavaScript runs in the frame, the promise will never resolve. In cases where the call stack is otherwise unable to be collected, it will return `undefined`.

This can be useful to determine why the frame is unresponsive in cases where there\'s long-running JavaScript. For more information, see the [proposed Crash Reporting API.](https://wicg.github.io/crash-reporting/)

``` 
const  = require('electron')

app.commandLine.appendSwitch('enable-features', 'DocumentPolicyIncludeJSCallStacksInCrashReports')

app.on('web-contents-created', (_, webContents) => )
})
```

### Instance Properties[â€‹](#instance-properties "Direct link to Instance Properties") 

#### `frame.ipc` *Readonly*[â€‹](#frameipc-readonly "Direct link to frameipc-readonly") 

An [`IpcMain`](/docs/latest/api/ipc-main) instance scoped to the frame.

IPC messages sent with `ipcRenderer.send`, `ipcRenderer.sendSync` or `ipcRenderer.postMessage` will be delivered in the following order:

1.  `contents.on('ipc-message')`
2.  `contents.mainFrame.on(channel)`
3.  `contents.ipc.on(channel)`
4.  `ipcMain.on(channel)`

Handlers registered with `invoke` will be checked in the following order. The first one that is defined will be called, the rest will be ignored.

1.  `contents.mainFrame.handle(channel)`
2.  `contents.handle(channel)`
3.  `ipcMain.handle(channel)`

In most cases, only the main frame of a WebContents can send or receive IPC messages. However, if the `nodeIntegrationInSubFrames` option is enabled, it is possible for child frames to send and receive IPC messages also. The [`WebContents.ipc`](/docs/latest/api/web-contents#contentsipc-readonly) interface may be more convenient when `nodeIntegrationInSubFrames` is not enabled.

#### `frame.url` *Readonly*[â€‹](#frameurl-readonly "Direct link to frameurl-readonly") 

A `string` representing the current URL of the frame.

#### `frame.origin` *Readonly*[â€‹](#frameorigin-readonly "Direct link to frameorigin-readonly") 

A `string` representing the current origin of the frame, serialized according to [RFC 6454](https://www.rfc-editor.org/rfc/rfc6454). This may be different from the URL. For instance, if the frame is a child window opened to `about:blank`, then `frame.origin` will return the parent frame\'s origin, while `frame.url` will return the empty string. Pages without a scheme/host/port triple origin will have the serialized origin of `"null"` (that is, the string containing the letters n, u, l, l).

#### `frame.top` *Readonly*[â€‹](#frametop-readonly "Direct link to frametop-readonly") 

A `WebFrameMain | null` representing top frame in the frame hierarchy to which `frame` belongs.

#### `frame.parent` *Readonly*[â€‹](#frameparent-readonly "Direct link to frameparent-readonly") 

A `WebFrameMain | null` representing parent frame of `frame`, the property would be `null` if `frame` is the top frame in the frame hierarchy.

#### `frame.frames` *Readonly*[â€‹](#frameframes-readonly "Direct link to frameframes-readonly") 

A `WebFrameMain[]` collection containing the direct descendents of `frame`.

#### `frame.framesInSubtree` *Readonly*[â€‹](#frameframesinsubtree-readonly "Direct link to frameframesinsubtree-readonly") 

A `WebFrameMain[]` collection containing every frame in the subtree of `frame`, including itself. This can be useful when traversing through all frames.

#### `frame.frameTreeNodeId` *Readonly*[â€‹](#frameframetreenodeid-readonly "Direct link to frameframetreenodeid-readonly") 

An `Integer` representing the id of the frame\'s internal FrameTreeNode instance. This id is browser-global and uniquely identifies a frame that hosts content. The identifier is fixed at the creation of the frame and stays constant for the lifetime of the frame. When the frame is removed, the id is not used again.

#### `frame.name` *Readonly*[â€‹](#framename-readonly "Direct link to framename-readonly") 

A `string` representing the frame name.

#### `frame.frameToken` *Readonly*[â€‹](#frameframetoken-readonly "Direct link to frameframetoken-readonly") 

A `string` which uniquely identifies the frame within its associated renderer process. This is equivalent to [`webFrame.frameToken`](/docs/latest/api/web-frame#webframeframetoken-readonly).

#### `frame.osProcessId` *Readonly*[â€‹](#frameosprocessid-readonly "Direct link to frameosprocessid-readonly") 

An `Integer` representing the operating system `pid` of the process which owns this frame.

#### `frame.processId` *Readonly*[â€‹](#frameprocessid-readonly "Direct link to frameprocessid-readonly") 

An `Integer` representing the Chromium internal `pid` of the process which owns this frame. This is not the same as the OS process ID; to read that use `frame.osProcessId`.

#### `frame.routingId` *Readonly*[â€‹](#frameroutingid-readonly "Direct link to frameroutingid-readonly") 

An `Integer` representing the unique frame id in the current renderer process. Distinct `WebFrameMain` instances that refer to the same underlying frame will have the same `routingId`.

#### `frame.visibilityState` *Readonly*[â€‹](#framevisibilitystate-readonly "Direct link to framevisibilitystate-readonly") 

A `string` representing the [visibility state](https://developer.mozilla.org/en-US/docs/Web/API/Document/visibilityState) of the frame.

See also how the [Page Visibility API](/docs/latest/api/browser-window#page-visibility) is affected by other Electron APIs.

#### `frame.detached` *Readonly*[â€‹](#framedetached-readonly "Direct link to framedetached-readonly") 

A `Boolean` representing whether the frame is detached from the frame tree. If a frame is accessed while the corresponding page is running any [unload](https://developer.mozilla.org/en-US/docs/Web/API/Window/unload_event) listeners, it may become detached as the newly navigated page replaced it in the frame tree.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/web-frame-main.md)