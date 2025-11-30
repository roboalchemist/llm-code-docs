# Source: https://www.electronjs.org/docs/latest/api/parent-port

On this page

# parentPort

> Interface for communication with parent process.

Process: [Utility](/docs/latest/glossary#utility-process)

`parentPort` is an [EventEmitter](https://nodejs.org/api/events.html#events_class_eventemitter). *This object is not exported from the `'electron'` module. It is only available as a property of the process object in the Electron API.*

``` 
// Main process
const child = utilityProcess.fork(path.join(__dirname, 'test.js'))
child.postMessage()
child.on('message', (data) => )

// Child process
process.parentPort.on('message', (e) =>  world!`)
})
```

## Events[â€‹](#events "Direct link to Events") 

The `parentPort` object emits the following events:

### Event: \'message\'[â€‹](#event-message "Direct link to Event: 'message'") 

Returns:

- `messageEvent` Object
  - `data` any
  - `ports` MessagePortMain\[\]

Emitted when the process receives a message. Messages received on this port will be queued up until a handler is registered for this event.

## Methods[â€‹](#methods "Direct link to Methods") 

### `parentPort.postMessage(message)`[â€‹](#parentportpostmessagemessage "Direct link to parentportpostmessagemessage") 

- `message` any

Sends a message from the process to its parent.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/parent-port.md)