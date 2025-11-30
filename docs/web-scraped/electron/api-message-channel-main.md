# Source: https://www.electronjs.org/docs/latest/api/message-channel-main

On this page

# MessageChannelMain

`MessageChannelMain` is the main-process-side equivalent of the DOM [`MessageChannel`](https://developer.mozilla.org/en-US/docs/Web/API/MessageChannel) object. Its singular function is to create a pair of connected [`MessagePortMain`](/docs/latest/api/message-port-main) objects.

See the [Channel Messaging API](https://developer.mozilla.org/en-US/docs/Web/API/Channel_Messaging_API) documentation for more information on using channel messaging.

## Class: MessageChannelMain[â€‹](#class-messagechannelmain "Direct link to Class: MessageChannelMain") 

> Channel interface for channel messaging in the main process.

Process: [Main](/docs/latest/glossary#main-process)

Example:

``` 
// Main process
const  = require('electron')

const w = new BrowserWindow()
const  = new MessageChannelMain()
w.webContents.postMessage('port', null, [port2])
port1.postMessage()

// Renderer process
const  = require('electron')

ipcRenderer.on('port', (e) => 
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)]warning

Electron\'s built-in classes cannot be subclassed in user code. For more information, see [the FAQ](/docs/latest/faq#class-inheritance-does-not-work-with-electron-built-in-modules).

### Instance Properties[â€‹](#instance-properties "Direct link to Instance Properties") 

#### `channel.port1`[â€‹](#channelport1 "Direct link to channelport1") 

A [`MessagePortMain`](/docs/latest/api/message-port-main) property.

#### `channel.port2`[â€‹](#channelport2 "Direct link to channelport2") 

A [`MessagePortMain`](/docs/latest/api/message-port-main) property.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/message-channel-main.md)