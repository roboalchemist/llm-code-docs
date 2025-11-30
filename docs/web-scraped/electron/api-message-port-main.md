# Source: https://www.electronjs.org/docs/latest/api/message-port-main

On this page

# MessagePortMain

`MessagePortMain` is the main-process-side equivalent of the DOM [`MessagePort`](https://developer.mozilla.org/en-US/docs/Web/API/MessagePort) object. It behaves similarly to the DOM version, with the exception that it uses the Node.js `EventEmitter` event system, instead of the DOM `EventTarget` system. This means you should use `port.on('message', ...)` to listen for events, instead of `port.onmessage = ...` or `port.addEventListener('message', ...)`

See the [Channel Messaging API](https://developer.mozilla.org/en-US/docs/Web/API/Channel_Messaging_API) documentation for more information on using channel messaging.

`MessagePortMain` is an [EventEmitter](https://nodejs.org/api/events.html#events_class_eventemitter).

## Class: MessagePortMain[â€‹](#class-messageportmain "Direct link to Class: MessagePortMain") 

> Port interface for channel messaging in the main process.

Process: [Main](/docs/latest/glossary#main-process)\
*This class is not exported from the `'electron'` module. It is only available as a return value of other methods in the Electron API.*

### Instance Methods[â€‹](#instance-methods "Direct link to Instance Methods") 

#### `port.postMessage(message, [transfer])`[â€‹](#portpostmessagemessage-transfer "Direct link to portpostmessagemessage-transfer") 

- `message` any
- `transfer` MessagePortMain\[\] (optional)

Sends a message from the port, and optionally, transfers ownership of objects to other browsing contexts.

#### `port.start()`[â€‹](#portstart "Direct link to portstart") 

Starts the sending of messages queued on the port. Messages will be queued until this method is called.

#### `port.close()`[â€‹](#portclose "Direct link to portclose") 

Disconnects the port, so it is no longer active.

### Instance Events[â€‹](#instance-events "Direct link to Instance Events") 

#### Event: \'message\'[â€‹](#event-message "Direct link to Event: 'message'") 

Returns:

- `messageEvent` Object
  - `data` any
  - `ports` MessagePortMain\[\]

Emitted when a MessagePortMain object receives a message.

#### Event: \'close\'[â€‹](#event-close "Direct link to Event: 'close'") 

Emitted when the remote end of a MessagePortMain object becomes disconnected.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/message-port-main.md)