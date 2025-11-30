# Source: https://www.electronjs.org/docs/latest/api/service-worker-main

On this page

# Class: ServiceWorkerMain

## Class: ServiceWorkerMain[â€‹](#class-serviceworkermain "Direct link to Class: ServiceWorkerMain") 

> An instance of a Service Worker representing a version of a script for a given scope.

Process: [Main](/docs/latest/glossary#main-process)\
*This class is not exported from the `'electron'` module. It is only available as a return value of other methods in the Electron API.*

### Instance Methods[â€‹](#instance-methods "Direct link to Instance Methods") 

#### `serviceWorker.isDestroyed()` *Experimental*[â€‹](#serviceworkerisdestroyed-experimental "Direct link to serviceworkerisdestroyed-experimental") 

Returns `boolean` - Whether the service worker has been destroyed.

#### `serviceWorker.send(channel, ...args)` *Experimental*[â€‹](#serviceworkersendchannel-args-experimental "Direct link to serviceworkersendchannel-args-experimental") 

- `channel` string
- `...args` any\[\]

Send an asynchronous message to the service worker process via `channel`, along with arguments. Arguments will be serialized with the [Structured Clone Algorithm](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm), just like [`postMessage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage), so prototype chains will not be included. Sending Functions, Promises, Symbols, WeakMaps, or WeakSets will throw an exception.

The service worker process can handle the message by listening to `channel` with the [`ipcRenderer`](/docs/latest/api/ipc-renderer) module.

#### `serviceWorker.startTask()` *Experimental*[â€‹](#serviceworkerstarttask-experimental "Direct link to serviceworkerstarttask-experimental") 

Returns `Object`:

- `end` Function - Method to call when the task has ended. If never called, the service won\'t terminate while otherwise idle.

Initiate a task to keep the service worker alive until ended.

### Instance Properties[â€‹](#instance-properties "Direct link to Instance Properties") 

#### `serviceWorker.ipc` *Readonly* *Experimental*[â€‹](#serviceworkeripc-readonly-experimental "Direct link to serviceworkeripc-readonly-experimental") 

An [`IpcMainServiceWorker`](/docs/latest/api/ipc-main-service-worker) instance scoped to the service worker.

#### `serviceWorker.scope` *Readonly* *Experimental*[â€‹](#serviceworkerscope-readonly-experimental "Direct link to serviceworkerscope-readonly-experimental") 

A `string` representing the scope URL of the service worker.

#### `serviceWorker.scriptURL` *Readonly* *Experimental*[â€‹](#serviceworkerscripturl-readonly-experimental "Direct link to serviceworkerscripturl-readonly-experimental") 

A `string` representing the script URL of the service worker.

#### `serviceWorker.versionId` *Readonly* *Experimental*[â€‹](#serviceworkerversionid-readonly-experimental "Direct link to serviceworkerversionid-readonly-experimental") 

A `number` representing the ID of the specific version of the service worker script in its scope.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/service-worker-main.md)