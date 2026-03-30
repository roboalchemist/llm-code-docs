# Source: https://socket.io/docs/v4/client-api/

Title: Client API | Socket.IO

URL Source: https://socket.io/docs/v4/client-api/

Markdown Content:
The `io` method is bound to the global scope in the standalone build:

`<script src="/socket.io/socket.io.js"></script><script>  const socket = io();</script>`

An ESM bundle is also available since version [4.3.0](https://socket.io/blog/socket-io-4-3-0/):

`<script type="module">  import { io } from "https://cdn.socket.io/4.8.3/socket.io.esm.min.js";  const socket = io();</script>`

With an [import map](https://caniuse.com/import-maps):

`<script type="importmap">  {    "imports": {      "socket.io-client": "https://cdn.socket.io/4.8.3/socket.io.esm.min.js"    }  }</script><script type="module">  import { io } from "socket.io-client";  const socket = io();</script>`

Else, in all other cases (with some build tools, in Node.js or React Native), it can be imported from the `socket.io-client` package:

`// ES modulesimport { io } from "socket.io-client";// CommonJSconst { io } = require("socket.io-client");`

### io.protocol[​](https://socket.io/docs/v4/client-api/#ioprotocol "Direct link to io.protocol")

*   [`<number>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#number_type)

The protocol revision number (currently: 5).

The protocol defines the format of the packets exchanged between the client and the server. Both the client and the server must use the same revision in order to understand each other.

You can find more information [here](https://github.com/socketio/socket.io-protocol).

### io([url][, options])[​](https://socket.io/docs/v4/client-api/#iourl "Direct link to iourl")

*   `url`[`<string>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#string_type) (defaults to `window.location.host`)
*   `options`[`<Object>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
    *   `forceNew`[`<boolean>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#boolean_type) whether to create a new connection

*   **Returns**[`<Socket>`](https://socket.io/docs/v4/client-api/#socket)

Creates a new `Manager` for the given URL, and attempts to reuse an existing `Manager` for subsequent calls, unless the `multiplex` option is passed with `false`. Passing this option is the equivalent of passing `"force new connection": true` or `forceNew: true`.

A new `Socket` instance is returned for the namespace specified by the pathname in the URL, defaulting to `/`. For example, if the `url` is `http://localhost/users`, a transport connection will be established to `http://localhost` and a Socket.IO connection will be established to `/users`.

Query parameters can also be provided, either with the `query` option or directly in the url (example: `http://localhost/users?token=abc`).

To understand what happens under the hood, the following example:

`import { io } from "socket.io-client";const socket = io("ws://example.com/my-namespace", {  reconnectionDelayMax: 10000,  auth: {    token: "123"  },  query: {    "my-key": "my-value"  }});`

is the short version of:

`import { Manager } from "socket.io-client";const manager = new Manager("ws://example.com", {  reconnectionDelayMax: 10000,  query: {    "my-key": "my-value"  }});const socket = manager.socket("/my-namespace", {  auth: {    token: "123"  }});`

The complete list of available options can be found [here](https://socket.io/docs/v4/client-options/).

![Image 1: Manager in the class diagram for the client](https://socket.io/images/client-class-diagram-manager.png)![Image 2: Manager in the class diagram for the client](https://socket.io/images/client-class-diagram-manager-dark.png)

The `Manager`_manages_ the Engine.IO [client](https://github.com/socketio/engine.io-client/) instance, which is the low-level engine that establishes the connection to the server (by using transports like WebSocket or HTTP long-polling).

The `Manager` handles the reconnection logic.

A single `Manager` can be used by several [Sockets](https://socket.io/docs/v4/client-api/#socket). You can find more information about this multiplexing feature [here](https://socket.io/docs/v4/namespaces/).

Please note that, in most cases, you won't use the Manager directly but use the [Socket](https://socket.io/docs/v4/client-api/#socket) instance instead.

### Constructor[​](https://socket.io/docs/v4/client-api/#constructor "Direct link to Constructor")

#### new Manager(url[, options])[​](https://socket.io/docs/v4/client-api/#new-managerurl-options "Direct link to new-managerurl-options")

*   `url`[`<string>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#string_type)
*   `options`[`<Object>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
*   **Returns**[`<Manager>`](https://socket.io/docs/v4/client-api/#manager)

The complete list of available options can be found [here](https://socket.io/docs/v4/client-options/).

`import { Manager } from "socket.io-client";const manager = new Manager("https://example.com");const socket = manager.socket("/"); // main namespaceconst adminSocket = manager.socket("/admin"); // admin namespace`

### Events[​](https://socket.io/docs/v4/client-api/#events "Direct link to Events")

#### Event: 'error'[​](https://socket.io/docs/v4/client-api/#event-error "Direct link to Event: 'error'")

*   `error`[`<Error>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error) error object

Fired upon a connection error.

`socket.io.on("error", (error) => {  // ...});`

#### Event: 'ping'[​](https://socket.io/docs/v4/client-api/#event-ping "Direct link to Event: 'ping'")

Fired when a ping packet is received from the server.

`socket.io.on("ping", () => {  // ...});`

#### Event: 'reconnect'[​](https://socket.io/docs/v4/client-api/#event-reconnect "Direct link to Event: 'reconnect'")

*   `attempt`[`<number>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#number_type) reconnection attempt number

Fired upon a successful reconnection.

`socket.io.on("reconnect", (attempt) => {  // ...});`

#### Event: 'reconnect_attempt'[​](https://socket.io/docs/v4/client-api/#event-reconnect_attempt "Direct link to Event: 'reconnect_attempt'")

*   `attempt`[`<number>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#number_type) reconnection attempt number

Fired upon an attempt to reconnect.

`socket.io.on("reconnect_attempt", (attempt) => {  // ...});`

#### Event: 'reconnect_error'[​](https://socket.io/docs/v4/client-api/#event-reconnect_error "Direct link to Event: 'reconnect_error'")

*   `error`[`<Error>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error) error object

Fired upon a reconnection attempt error.

`socket.io.on("reconnect_error", (error) => {  // ...});`

#### Event: 'reconnect_failed'[​](https://socket.io/docs/v4/client-api/#event-reconnect_failed "Direct link to Event: 'reconnect_failed'")

Fired when couldn't reconnect within `reconnectionAttempts`.

`socket.io.on("reconnect_failed", () => {  // ...});`

### Methods[​](https://socket.io/docs/v4/client-api/#methods "Direct link to Methods")

#### manager.connect([callback])[​](https://socket.io/docs/v4/client-api/#managerconnectcallback "Direct link to managerconnectcallback")

Synonym of [manager.open([callback])](https://socket.io/docs/v4/client-api/#manageropencallback).

#### manager.open([callback])[​](https://socket.io/docs/v4/client-api/#manageropencallback "Direct link to manageropencallback")

*   `callback`[`<Function>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
*   **Returns**[`<Manager>`](https://socket.io/docs/v4/client-api/#manager)

If the manager was initiated with `autoConnect` to `false`, launch a new connection attempt.

The `callback` argument is optional and will be called once the attempt fails/succeeds.

`import { Manager } from "socket.io-client";const manager = new Manager("https://example.com", {  autoConnect: false});const socket = manager.socket("/");manager.open((err) => {  if (err) {    // an error has occurred  } else {    // the connection was successfully established  }});`

#### manager.reconnection([value])[​](https://socket.io/docs/v4/client-api/#managerreconnectionvalue "Direct link to managerreconnectionvalue")

*   `value`[`<boolean>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#boolean_type)
*   **Returns**[`<Manager>`](https://socket.io/docs/v4/client-api/#manager) | [`<boolean>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#boolean_type)

Sets the `reconnection` option, or returns it if no parameters are passed.

#### manager.reconnectionAttempts([value])[​](https://socket.io/docs/v4/client-api/#managerreconnectionattemptsvalue "Direct link to managerreconnectionattemptsvalue")

*   `value`[`<number>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#number_type)
*   **Returns**[`<Manager>`](https://socket.io/docs/v4/client-api/#manager) | [`<number>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#number_type)

Sets the `reconnectionAttempts` option, or returns it if no parameters are passed.

#### manager.reconnectionDelay([value])[​](https://socket.io/docs/v4/client-api/#managerreconnectiondelayvalue "Direct link to managerreconnectiondelayvalue")

*   `value`[`<number>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#number_type)
*   **Returns**[`<Manager>`](https://socket.io/docs/v4/client-api/#manager) | [`<number>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#number_type)

Sets the `reconnectionDelay` option, or returns it if no parameters are passed.

#### manager.reconnectionDelayMax([value])[​](https://socket.io/docs/v4/client-api/#managerreconnectiondelaymaxvalue "Direct link to managerreconnectiondelaymaxvalue")

*   `value`[`<number>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#number_type)
*   **Returns**[`<Manager>`](https://socket.io/docs/v4/client-api/#manager) | [`<number>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#number_type)

Sets the `reconnectionDelayMax` option, or returns it if no parameters are passed.

#### manager.socket(nsp, options)[​](https://socket.io/docs/v4/client-api/#managersocketnsp-options "Direct link to manager.socket(nsp, options)")

*   `nsp`[`<string>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#string_type)
*   `options`[`<Object>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
*   **Returns**[`<Socket>`](https://socket.io/docs/v4/client-api/#socket)

Creates a new `Socket` for the given namespace. Only `auth` (`{ auth: {key: "value"} }`) is read from the `options` object. Other keys will be ignored and should be passed when instancing a `new Manager(nsp, options)`.

#### manager.timeout([value])[​](https://socket.io/docs/v4/client-api/#managertimeoutvalue "Direct link to managertimeoutvalue")

*   `value`[`<number>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#number_type)
*   **Returns**[`<Manager>`](https://socket.io/docs/v4/client-api/#manager) | [`<number>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#number_type)

Sets the `timeout` option, or returns it if no parameters are passed.

![Image 3: Socket in the class diagram for the client](https://socket.io/images/client-class-diagram-socket.png)![Image 4: Socket in the class diagram for the client](https://socket.io/images/client-class-diagram-socket-dark.png)

A `Socket` is the fundamental class for interacting with the server. A `Socket` belongs to a certain [Namespace](https://socket.io/docs/v4/namespaces/) (by default `/`) and uses an underlying [Manager](https://socket.io/docs/v4/client-api/#manager) to communicate.

A `Socket` is basically an [EventEmitter](https://nodejs.org/api/events.html#events_class_eventemitter) which sends events to — and receive events from — the server over the network.

`socket.emit("hello", { a: "b", c: [] });socket.on("hey", (...args) => {  // ...});`

More information can be found [here](https://socket.io/docs/v4/client-socket-instance/).

### Events[​](https://socket.io/docs/v4/client-api/#events-1 "Direct link to Events")

#### Event: 'connect'[​](https://socket.io/docs/v4/client-api/#event-connect "Direct link to Event: 'connect'")

This event is fired by the Socket instance upon connection **and** reconnection.

`socket.on("connect", () => {  // ...});`

caution

Event handlers shouldn't be registered in the `connect` handler itself, as a new handler will be registered every time the socket instance reconnects:

BAD ⚠️

`socket.on("connect", () => {  socket.on("data", () => { /* ... */ });});`

GOOD 👍

`socket.on("connect", () => {  // ...});socket.on("data", () => { /* ... */ });`

#### Event: 'connect_error'[​](https://socket.io/docs/v4/client-api/#event-connect_error "Direct link to Event: 'connect_error'")

*   `error`[`<Error>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)

This event is fired upon connection failure.

| Reason | Automatic reconnection? |
| --- | --- |
| The low-level connection cannot be established (temporary failure) | ✅ YES |
| The connection was denied by the server in a [middleware function](https://socket.io/docs/v4/middlewares/) | ❌ NO |

The [`socket.active`](https://socket.io/docs/v4/client-api/#socketactive) attribute indicates whether the socket will automatically try to reconnect after a small [randomized delay](https://socket.io/docs/v4/client-options/#reconnectiondelay):

`socket.on("connect_error", (error) => {  if (socket.active) {    // temporary failure, the socket will automatically try to reconnect  } else {    // the connection was denied by the server    // in that case, `socket.connect()` must be manually called in order to reconnect    console.log(error.message);  }});`

#### Event: 'disconnect'[​](https://socket.io/docs/v4/client-api/#event-disconnect "Direct link to Event: 'disconnect'")

*   `reason`[`<string>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#string_type)
*   `details``<DisconnectDetails>`

This event is fired upon disconnection.

`socket.on("disconnect", (reason, details) => {  // ...});`

Here is the list of possible reasons:

| Reason | Description | Automatic reconnection? |
| --- | --- | --- |
| `io server disconnect` | The server has forcefully disconnected the socket with [socket.disconnect()](https://socket.io/docs/v4/server-api/#socketdisconnectclose) | ❌ NO |
| `io client disconnect` | The socket was manually disconnected using [socket.disconnect()](https://socket.io/docs/v4/client-api/#socketdisconnect) | ❌ NO |
| `ping timeout` | The server did not send a PING within the `pingInterval + pingTimeout` range | ✅ YES |
| `transport close` | The connection was closed (example: the user has lost connection, or the network was changed from WiFi to 4G) | ✅ YES |
| `transport error` | The connection has encountered an error (example: the server was killed during a HTTP long-polling cycle) | ✅ YES |

The [`socket.active`](https://socket.io/docs/v4/client-api/#socketactive) attribute indicates whether the socket will automatically try to reconnect after a small [randomized delay](https://socket.io/docs/v4/client-options/#reconnectiondelay):

`socket.on("disconnect", (reason) => {  if (socket.active) {    // temporary disconnection, the socket will automatically try to reconnect  } else {    // the connection was forcefully closed by the server or the client itself    // in that case, `socket.connect()` must be manually called in order to reconnect    console.log(reason);  }});`

### Attributes[​](https://socket.io/docs/v4/client-api/#attributes "Direct link to Attributes")

#### socket.active[​](https://socket.io/docs/v4/client-api/#socketactive "Direct link to socket.active")

*   [`<boolean>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#boolean_type)

Whether the socket will automatically try to reconnect.

This attribute can be used after a connection failure:

`socket.on("connect_error", (error) => {  if (socket.active) {    // temporary failure, the socket will automatically try to reconnect  } else {    // the connection was denied by the server    // in that case, `socket.connect()` must be manually called in order to reconnect    console.log(error.message);  }});`

Or after a disconnection:

`socket.on("disconnect", (reason) => {  if (socket.active) {    // temporary disconnection, the socket will automatically try to reconnect  } else {    // the connection was forcefully closed by the server or the client itself    // in that case, `socket.connect()` must be manually called in order to reconnect    console.log(reason);  }});`

#### socket.connected[​](https://socket.io/docs/v4/client-api/#socketconnected "Direct link to socket.connected")

*   [`<boolean>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#boolean_type)

Whether the socket is currently connected to the server.

`const socket = io();console.log(socket.connected); // falsesocket.on("connect", () => {  console.log(socket.connected); // true});`

#### socket.disconnected[​](https://socket.io/docs/v4/client-api/#socketdisconnected "Direct link to socket.disconnected")

*   [`<boolean>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#boolean_type)

Whether the socket is currently disconnected from the server.

`const socket = io();console.log(socket.disconnected); // truesocket.on("connect", () => {  console.log(socket.disconnected); // false});`

#### socket.id[​](https://socket.io/docs/v4/client-api/#socketid "Direct link to socket.id")

*   [`<string>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#string_type)

A unique identifier for the socket session. Set after the `connect` event is triggered, and updated after the `reconnect` event.

`const socket = io();console.log(socket.id); // undefinedsocket.on("connect", () => {  console.log(socket.id); // "G5p5..."});`

caution

The `id` attribute is an **ephemeral** ID that is not meant to be used in your application (or only for debugging purposes) because:

*   this ID is regenerated after each reconnection (for example when the WebSocket connection is severed, or when the user refreshes the page)
*   two different browser tabs will have two different IDs
*   there is no message queue stored for a given ID on the server (i.e. if the client is disconnected, the messages sent from the server to this ID are lost)

Please use a regular session ID instead (either sent in a cookie, or stored in the localStorage and sent in the [`auth`](https://socket.io/docs/v4/client-options/#auth) payload).

See also:

*   [Part II of our private message guide](https://socket.io/get-started/private-messaging-part-2/)
*   [How to deal with cookies](https://socket.io/how-to/deal-with-cookies)

#### socket.io[​](https://socket.io/docs/v4/client-api/#socketio "Direct link to socket.io")

*   [`<Manager>`](https://socket.io/docs/v4/client-api/#manager)

A reference to the underlying [Manager](https://socket.io/docs/v4/client-api/#manager).

`socket.on("connect", () => {  const engine = socket.io.engine;  console.log(engine.transport.name); // in most cases, prints "polling"  engine.once("upgrade", () => {    // called when the transport is upgraded (i.e. from HTTP long-polling to WebSocket)    console.log(engine.transport.name); // in most cases, prints "websocket"  });  engine.on("packet", ({ type, data }) => {    // called for each packet received  });  engine.on("packetCreate", ({ type, data }) => {    // called for each packet sent  });  engine.on("drain", () => {    // called when the write buffer is drained  });  engine.on("close", (reason) => {    // called when the underlying connection is closed  });});`

#### socket.recovered[​](https://socket.io/docs/v4/client-api/#socketrecovered "Direct link to socket.recovered")

_Added in v4.6.0_

*   [`<boolean>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#boolean_type)

Whether the connection state was successfully recovered during the last reconnection.

`socket.on("connect", () => {  if (socket.recovered) {    // any event missed during the disconnection period will be received now  } else {    // new or unrecoverable session  }});`

More information about this feature [here](https://socket.io/docs/v4/connection-state-recovery).

### Methods[​](https://socket.io/docs/v4/client-api/#methods-1 "Direct link to Methods")

#### socket.close()[​](https://socket.io/docs/v4/client-api/#socketclose "Direct link to socket.close()")

_Added in v1.0.0_

Synonym of [socket.disconnect()](https://socket.io/docs/v4/client-api/#socketdisconnect).

#### socket.compress(value)[​](https://socket.io/docs/v4/client-api/#socketcompressvalue "Direct link to socket.compress(value)")

*   `value`[`<boolean>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#boolean_type)
*   **Returns**[`<Socket>`](https://socket.io/docs/v4/client-api/#socket)

Sets a modifier for a subsequent event emission that the event data will only be _compressed_ if the value is `true`. Defaults to `true` when you don't call the method.

`socket.compress(false).emit("an event", { some: "data" });`

#### socket.connect()[​](https://socket.io/docs/v4/client-api/#socketconnect "Direct link to socket.connect()")

_Added in v1.0.0_

*   **Returns**`Socket`

Manually connects the socket.

`const socket = io({  autoConnect: false});// ...socket.connect();`

It can also be used to manually reconnect:

`socket.on("disconnect", () => {  socket.connect();});`

#### socket.disconnect()[​](https://socket.io/docs/v4/client-api/#socketdisconnect "Direct link to socket.disconnect()")

_Added in v1.0.0_

*   **Returns**[`<Socket>`](https://socket.io/docs/v4/client-api/#socket)

Manually disconnects the socket. In that case, the socket will not try to reconnect.

Associated disconnection reason:

*   client-side: `"io client disconnect"`
*   server-side: `"client namespace disconnect"`

If this is the last active Socket instance of the Manager, the low-level connection will be closed.

#### socket.emit(eventName[, ...args][, ack])[​](https://socket.io/docs/v4/client-api/#socketemiteventname-args "Direct link to socketemiteventname-args")

*   `eventName`[`<string>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#string_type) | [`<symbol>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#symbol_type)
*   `args``<any[]>`
*   `ack`[`<Function>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
*   **Returns**`true`

Emits an event to the socket identified by the string name. Any other parameters can be included. All serializable data structures are supported, including `Buffer`.

`socket.emit("hello", "world");socket.emit("with-binary", 1, "2", { 3: "4", 5: Buffer.from([6, 7, 8]) });`

The `ack` argument is optional and will be called with the server answer.

_Client_

`socket.emit("hello", "world", (response) => {  console.log(response); // "got it"});`

_Server_

`io.on("connection", (socket) => {  socket.on("hello", (arg, callback) => {    console.log(arg); // "world"    callback("got it");  });});`

#### socket.emitWithAck(eventName[, ...args])[​](https://socket.io/docs/v4/client-api/#socketemitwithackeventname-args "Direct link to socketemitwithackeventname-args")

_Added in v4.6.0_

*   `eventName`[`<string>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#string_type) | [`<symbol>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#symbol_type)
*   `args``any[]`
*   **Returns**[`Promise<any>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)

Promised-based version of emitting and expecting an acknowledgement from the server:

`// without timeoutconst response = await socket.emitWithAck("hello", "world");// with a specific timeouttry {  const response = await socket.timeout(10000).emitWithAck("hello", "world");} catch (err) {  // the server did not acknowledge the event in the given delay}`

The example above is equivalent to:

`// without timeoutsocket.emit("hello", "world", (val) => {  // ...});// with a specific timeoutsocket.timeout(10000).emit("hello", "world", (err, val) => {  // ...});`

And on the receiving side:

`io.on("connection", (socket) => {  socket.on("hello", (arg1, callback) => {    callback("got it"); // only one argument is expected  });});`

#### socket.listeners(eventName)[​](https://socket.io/docs/v4/client-api/#socketlistenerseventname "Direct link to socket.listeners(eventName)")

_Inherited from the [EventEmitter class](https://www.npmjs.com/package/@socket.io/component-emitter)._

*   `eventName`[`<string>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#string_type) | [`<symbol>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#symbol_type)
*   **Returns**[`<Function[]>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)

Returns the array of listeners for the event named `eventName`.

`socket.on("my-event", () => {  // ...});console.log(socket.listeners("my-event")); // prints [ [Function] ]`

#### socket.listenersAny()[​](https://socket.io/docs/v4/client-api/#socketlistenersany "Direct link to socket.listenersAny()")

_Added in v3.0.0_

*   **Returns**[`<Function[]>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)

Returns the list of registered catch-all listeners.

`const listeners = socket.listenersAny();`

#### socket.listenersAnyOutgoing()[​](https://socket.io/docs/v4/client-api/#socketlistenersanyoutgoing "Direct link to socket.listenersAnyOutgoing()")

_Added in v4.5.0_

*   **Returns**[`<Function[]>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)

Returns the list of registered catch-all listeners for outgoing packets.

`const listeners = socket.listenersAnyOutgoing();`

#### socket.off([eventName][, listener])[​](https://socket.io/docs/v4/client-api/#socketoffeventname "Direct link to socketoffeventname")

_Inherited from the [EventEmitter class](https://www.npmjs.com/package/@socket.io/component-emitter)._

*   `eventName`[`<string>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#string_type) | [`<symbol>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#symbol_type)
*   `listener`[`<Function>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
*   **Returns**[`<Socket>`](https://socket.io/docs/v4/client-api/#socket)

Removes the specified `listener` from the listener array for the event named `eventName`.

`const myListener = () => {  // ...}socket.on("my-event", myListener);// then latersocket.off("my-event", myListener);`

The `listener` argument can also be omitted:

`// remove all listeners for that eventsocket.off("my-event");// remove all listeners for all eventssocket.off();`

#### socket.offAny([listener])[​](https://socket.io/docs/v4/client-api/#socketoffanylistener "Direct link to socketoffanylistener")

_Added in v3.0.0_

*   `listener`[`<Function>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)

Removes the previously registered listener. If no listener is provided, all catch-all listeners are removed.

`const myListener = () => { /* ... */ };socket.onAny(myListener);// then, latersocket.offAny(myListener);socket.offAny();`

#### socket.offAnyOutgoing([listener])[​](https://socket.io/docs/v4/client-api/#socketoffanyoutgoinglistener "Direct link to socketoffanyoutgoinglistener")

_Added in v4.5.0_

*   `listener`[`<Function>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)

Removes the previously registered listener. If no listener is provided, all catch-all listeners are removed.

`const myListener = () => { /* ... */ };socket.onAnyOutgoing(myListener);// remove a single listenersocket.offAnyOutgoing(myListener);// remove all listenerssocket.offAnyOutgoing();`

#### socket.on(eventName, callback)[​](https://socket.io/docs/v4/client-api/#socketoneventname-callback "Direct link to socket.on(eventName, callback)")

_Inherited from the [EventEmitter class](https://www.npmjs.com/package/@socket.io/component-emitter)._

*   `eventName`[`<string>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#string_type) | [`<symbol>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#symbol_type)
*   `listener`[`<Function>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
*   **Returns**[`<Socket>`](https://socket.io/docs/v4/client-api/#socket)

Register a new handler for the given event.

`socket.on("news", (data) => {  console.log(data);});// with multiple argumentssocket.on("news", (arg1, arg2, arg3, arg4) => {  // ...});// with callbacksocket.on("news", (cb) => {  cb(0);});`

#### socket.onAny(callback)[​](https://socket.io/docs/v4/client-api/#socketonanycallback "Direct link to socket.onAny(callback)")

_Added in v3.0.0_

*   `callback`[`<Function>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)

Register a new catch-all listener.

`socket.onAny((event, ...args) => {  console.log(`got ${event}`);});`

caution

[Acknowledgements](https://socket.io/docs/v4/emitting-events/#acknowledgements) are not caught in the catch-all listener.

`socket.emit("foo", (value) => {  // ...});socket.onAnyOutgoing(() => {  // triggered when the event is sent});socket.onAny(() => {  // not triggered when the acknowledgement is received});`

#### socket.onAnyOutgoing(callback)[​](https://socket.io/docs/v4/client-api/#socketonanyoutgoingcallback "Direct link to socket.onAnyOutgoing(callback)")

_Added in v4.5.0_

*   `callback`[`<Function>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)

Register a new catch-all listener for outgoing packets.

`socket.onAnyOutgoing((event, ...args) => {  console.log(`got ${event}`);});`

caution

[Acknowledgements](https://socket.io/docs/v4/emitting-events/#acknowledgements) are not caught in the catch-all listener.

`socket.on("foo", (value, callback) => {  callback("OK");});socket.onAny(() => {  // triggered when the event is received});socket.onAnyOutgoing(() => {  // not triggered when the acknowledgement is sent});`

#### socket.once(eventName, callback)[​](https://socket.io/docs/v4/client-api/#socketonceeventname-callback "Direct link to socket.once(eventName, callback)")

_Inherited from the [EventEmitter class](https://www.npmjs.com/package/@socket.io/component-emitter)._

*   `eventName`[`<string>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#string_type) | [`<symbol>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#symbol_type)
*   `listener`[`<Function>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
*   **Returns**[`<Socket>`](https://socket.io/docs/v4/client-api/#socket)

Adds a one-time `listener` function for the event named `eventName`. The next time `eventName` is triggered, this listener is removed and then invoked.

`socket.once("my-event", () => {  // ...});`

#### socket.open()[​](https://socket.io/docs/v4/client-api/#socketopen "Direct link to socket.open()")

_Added in v1.0.0_

Synonym of [socket.connect()](https://socket.io/docs/v4/client-api/#socketconnect).

#### socket.prependAny(callback)[​](https://socket.io/docs/v4/client-api/#socketprependanycallback "Direct link to socket.prependAny(callback)")

_Added in v3.0.0_

*   `callback`[`<Function>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)

Register a new catch-all listener. The listener is added to the beginning of the listeners array.

`socket.prependAny((event, ...args) => {  console.log(`got ${event}`);});`

#### socket.prependAnyOutgoing(callback)[​](https://socket.io/docs/v4/client-api/#socketprependanyoutgoingcallback "Direct link to socket.prependAnyOutgoing(callback)")

_Added in v4.5.0_

*   `callback`[`<Function>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)

Register a new catch-all listener for outgoing packets. The listener is added to the beginning of the listeners array.

`socket.prependAnyOutgoing((event, ...args) => {  console.log(`got ${event}`);});`

#### socket.send([...args][, ack])[​](https://socket.io/docs/v4/client-api/#socketsendargs "Direct link to socketsendargs")

*   `args``<any[]>`
*   `ack`[`<Function>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
*   **Returns**[`<Socket>`](https://socket.io/docs/v4/client-api/#socket)

Sends a `message` event. See [socket.emit(eventName[, ...args][, ack])](https://socket.io/docs/v4/client-api/#socketemiteventname-args).

#### socket.timeout(value)[​](https://socket.io/docs/v4/client-api/#sockettimeoutvalue "Direct link to socket.timeout(value)")

_Added in v4.4.0_

*   `value`[`<number>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#number_type)
*   **Returns**[`<Socket>`](https://socket.io/docs/v4/client-api/#socket)

Sets a modifier for a subsequent event emission that the callback will be called with an error when the given number of milliseconds have elapsed without an acknowledgement from the server:

`socket.timeout(5000).emit("my-event", (err) => {  if (err) {    // the server did not acknowledge the event in the given delay  }});`

### Flags[​](https://socket.io/docs/v4/client-api/#flags "Direct link to Flags")

#### Flag: 'volatile'[​](https://socket.io/docs/v4/client-api/#flag-volatile "Direct link to Flag: 'volatile'")

_Added in v3.0.0_

Sets a modifier for the subsequent event emission indicating that the packet may be dropped if:

*   the socket is not connected
*   the low-level transport is not writable (for example, when a `POST` request is already running in HTTP long-polling mode)

`socket.volatile.emit(/* ... */); // the server may or may not receive it`
