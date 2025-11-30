# Source: https://www.electronjs.org/docs/latest/tutorial/message-ports

On this page

# MessagePorts in Electron

[`MessagePort`](https://developer.mozilla.org/en-US/docs/Web/API/MessagePort)s are a web feature that allow passing messages between different contexts. It\'s like `window.postMessage`, but on different channels. The goal of this document is to describe how Electron extends the Channel Messaging model, and to give some examples of how you might use MessagePorts in your app.

Here is a very brief example of what a MessagePort is and how it works:

renderer.js (Renderer Process)

``` 
// MessagePorts are created in pairs. A connected pair of message ports is
// called a channel.
const channel = new MessageChannel()

// The only difference between port1 and port2 is in how you use them. Messages
// sent to port1 will be received by port2 and vice-versa.
const port1 = channel.port1
const port2 = channel.port2

// It's OK to send a message on the channel before the other end has registered
// a listener. Messages will be queued until a listener is registered.
port2.postMessage()

// Here we send the other end of the channel, port1, to the main process. It's
// also possible to send MessagePorts to other frames, or to Web Workers, etc.
ipcRenderer.postMessage('port', null, [port1])
```

main.js (Main Process)

``` 
// In the main process, we receive the port.
ipcMain.on('port', (event) => 
    const data = event.data
  })

  // MessagePortMain queues messages until the .start() method has been called.
  port.start()
})
```

The [Channel Messaging API](https://developer.mozilla.org/en-US/docs/Web/API/Channel_Messaging_API) documentation is a great way to learn more about how MessagePorts work.

## MessagePorts in the main process[â€‹](#messageports-in-the-main-process "Direct link to MessagePorts in the main process") 

In the renderer, the `MessagePort` class behaves exactly as it does on the web. The main process is not a web page, thoughâ€"it has no Blink integrationâ€"and so it does not have the `MessagePort` or `MessageChannel` classes. In order to handle and interact with MessagePorts in the main process, Electron adds two new classes: [`MessagePortMain`](/docs/latest/api/message-port-main) and [`MessageChannelMain`](/docs/latest/api/message-channel-main). These behave similarly to the analogous classes in the renderer.

`MessagePort` objects can be created in either the renderer or the main process, and passed back and forth using the [`ipcRenderer.postMessage`](/docs/latest/api/ipc-renderer#ipcrendererpostmessagechannel-message-transfer) and [`WebContents.postMessage`](/docs/latest/api/web-contents#contentspostmessagechannel-message-transfer) methods. Note that the usual IPC methods like `send` and `invoke` cannot be used to transfer `MessagePort`s, only the `postMessage` methods can transfer `MessagePort`s.

By passing `MessagePort`s via the main process, you can connect two pages that might not otherwise be able to communicate (e.g. due to same-origin restrictions).

## Extension: `close` event[â€‹](#extension-close-event "Direct link to extension-close-event") 

Electron adds one feature to `MessagePort` that isn\'t present on the web, in order to make MessagePorts more useful. That is the `close` event, which is emitted when the other end of the channel is closed. Ports can also be implicitly closed by being garbage-collected.

In the renderer, you can listen for the `close` event either by assigning to `port.onclose` or by calling `port.addEventListener('close', ...)`. In the main process, you can listen for the `close` event by calling `port.on('close', ...)`.

## Example use cases[â€‹](#example-use-cases "Direct link to Example use cases") 

### Setting up a MessageChannel between two renderers[â€‹](#setting-up-a-messagechannel-between-two-renderers "Direct link to Setting up a MessageChannel between two renderers") 

In this example, the main process sets up a MessageChannel, then sends each port to a different renderer. This allows renderers to send messages to each other without needing to use the main process as an in-between.

main.js (Main Process)

``` 
const  = require('electron')

app.whenReady().then(async () => 
  })

  const secondaryWindow = new BrowserWindow(
  })

  // set up the channel.
  const  = new MessageChannelMain()

  // once the webContents are ready, send a port to each webContents with postMessage.
  mainWindow.once('ready-to-show', () => )

  secondaryWindow.once('ready-to-show', () => )
})
```

Then, in your preload scripts you receive the port through IPC and set up the listeners.

preloadMain.js and preloadSecondary.js (Preload scripts)

``` 
const  = require('electron')

ipcRenderer.on('port', e => 
})
```

In this example messagePort is bound to the `window` object directly. It is better to use `contextIsolation` and set up specific contextBridge calls for each of your expected messages, but for the simplicity of this example we don\'t. You can find an example of context isolation further down this page at [Communicating directly between the main process and the main world of a context-isolated page](#communicating-directly-between-the-main-process-and-the-main-world-of-a-context-isolated-page)

That means window.electronMessagePort is globally available and you can call `postMessage` on it from anywhere in your app to send a message to the other renderer.

renderer.js (Renderer Process)

``` 
// elsewhere in your code to send a message to the other renderers message handler
window.electronMessagePort.postMessage('ping')
```

### Worker process[â€‹](#worker-process "Direct link to Worker process") 

In this example, your app has a worker process implemented as a hidden window. You want the app page to be able to communicate directly with the worker process, without the performance overhead of relaying via the main process.

main.js (Main Process)

``` 
const  = require('electron')

app.whenReady().then(async () => 
  })
  await worker.loadFile('worker.html')

  // The main window will send work to the worker process and receive results
  // over a MessagePort.
  const mainWindow = new BrowserWindow(
  })
  mainWindow.loadFile('app.html')

  // We can't use ipcMain.handle() here, because the reply needs to transfer a
  // MessagePort.
  // Listen for message sent from the top-level frame
  mainWindow.webContents.mainFrame.ipc.on('request-worker-channel', (event) =>  = new MessageChannelMain()
    // ... send one end to the worker ...
    worker.webContents.postMessage('new-client', null, [port1])
    // ... and the other end to the main window.
    event.senderFrame.postMessage('provide-worker-channel', null, [port2])
    // Now the main window and the worker can communicate with each other
    // without going through the main process!
  })
})
```

worker.html

``` 
<script>
const  = require('electron')

const doWork = (input) => 

// We might get multiple clients, for instance if there are multiple windows,
// or if the main window reloads.
ipcRenderer.on('new-client', (event) => 
})
</script>
```

app.html

``` 
<script>
const  = require('electron')

// We request that the main process sends us a channel we can use to
// communicate with the worker.
ipcRenderer.send('request-worker-channel')

ipcRenderer.once('provide-worker-channel', (event) => 
  // ... and start sending it work!
  port.postMessage(21)
})
</script>
```

### Reply streams[â€‹](#reply-streams "Direct link to Reply streams") 

Electron\'s built-in IPC methods only support two modes: fire-and-forget (e.g. `send`), or request-response (e.g. `invoke`). Using MessageChannels, you can implement a \"response stream\", where a single request responds with a stream of data.

renderer.js (Renderer Process)

``` 
const makeStreamingRequest = (element, callback) =>  = new MessageChannel()

  // We send one end of the port to the main process ...
  ipcRenderer.postMessage(
    'give-me-a-stream',
    ,
    [port2]
  )

  // ... and we hang on to the other end. The main process will send messages
  // to its end of the port, and close it when it's finished.
  port1.onmessage = (event) => 
  port1.onclose = () => 
}

makeStreamingRequest(42, (data) => )
// We will see "got response data: 42" 10 times.
```

main.js (Main Process)

``` 
ipcMain.on('give-me-a-stream', (event, msg) => 

  // We close the port when we're done to indicate to the other end that we
  // won't be sending any more messages. This isn't strictly necessary--if we
  // didn't explicitly close the port, it would eventually be garbage
  // collected, which would also trigger the 'close' event in the renderer.
  replyPort.close()
})
```

### Communicating directly between the main process and the main world of a context-isolated page[â€‹](#communicating-directly-between-the-main-process-and-the-main-world-of-a-context-isolated-page "Direct link to Communicating directly between the main process and the main world of a context-isolated page") 

When [context isolation](/docs/latest/tutorial/context-isolation) is enabled, IPC messages from the main process to the renderer are delivered to the isolated world, rather than to the main world. Sometimes you want to deliver messages to the main world directly, without having to step through the isolated world.

main.js (Main Process)

``` 
const  = require('electron')

const path = require('node:path')

app.whenReady().then(async () => 
  })
  bw.loadURL('index.html')

  // We'll be sending one end of this channel to the main world of the
  // context-isolated page.
  const  = new MessageChannelMain()

  // It's OK to send a message on the channel before the other end has
  // registered a listener. Messages will be queued until a listener is
  // registered.
  port2.postMessage()

  // We can also receive messages from the main world of the renderer.
  port2.on('message', (event) => )
  port2.start()

  // The preload script will receive this IPC message and transfer the port
  // over to the main world.
  bw.webContents.postMessage('main-world-port', null, [port1])
})
```

preload.js (Preload Script)

``` 
const  = require('electron')

// We need to wait until the main world is ready to receive the message before
// sending the port. We create this promise in the preload so it's guaranteed
// to register the onload listener before the load event is fired.
const windowLoaded = new Promise(resolve => )

ipcRenderer.on('main-world-port', async (event) => )
```

index.html

``` 
<script>
window.onmessage = (event) => 
  }
}
</script>
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/tutorial/message-ports.md)