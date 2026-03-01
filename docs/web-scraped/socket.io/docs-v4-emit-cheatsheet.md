# Source: https://socket.io/docs/v4/emit-cheatsheet/

Title: Emit cheatsheet | Socket.IO

URL Source: https://socket.io/docs/v4/emit-cheatsheet/

Markdown Content:
Version: 4.x

caution

The following event names are reserved and must not be used in your application:

*   `connect`
*   `connect_error`
*   `disconnect`
*   `disconnecting`
*   `newListener`
*   `removeListener`

`// BAD, will throw an errorsocket.emit("disconnecting");`

### Single client[​](https://socket.io/docs/v4/emit-cheatsheet/#single-client "Direct link to Single client")

#### Basic emit[​](https://socket.io/docs/v4/emit-cheatsheet/#basic-emit "Direct link to Basic emit")

`io.on("connection", (socket) => {  socket.emit("hello", 1, "2", { 3: "4", 5: Buffer.from([6]) });});`

#### Acknowledgement[​](https://socket.io/docs/v4/emit-cheatsheet/#acknowledgement "Direct link to Acknowledgement")

*   Callback
*   Promise

`io.on("connection", (socket) => {  socket.emit("hello", "world", (arg1, arg2, arg3) => {    // ...  });});`

#### Acknowledgement and timeout[​](https://socket.io/docs/v4/emit-cheatsheet/#acknowledgement-and-timeout "Direct link to Acknowledgement and timeout")

*   Callback
*   Promise

`io.on("connection", (socket) => {  socket.timeout(5000).emit("hello", "world", (err, arg1, arg2, arg3) => {    if (err) {      // the client did not acknowledge the event in the given delay    } else {      // ...    }  });});`

### Broadcasting[​](https://socket.io/docs/v4/emit-cheatsheet/#broadcasting "Direct link to Broadcasting")

#### To all connected clients[​](https://socket.io/docs/v4/emit-cheatsheet/#to-all-connected-clients "Direct link to To all connected clients")

`io.emit("hello");`

#### Except the sender[​](https://socket.io/docs/v4/emit-cheatsheet/#except-the-sender "Direct link to Except the sender")

`io.on("connection", (socket) => {  socket.broadcast.emit("hello");});`

#### Acknowledgements[​](https://socket.io/docs/v4/emit-cheatsheet/#acknowledgements "Direct link to Acknowledgements")

*   Callback
*   Promise

`io.timeout(5000).emit("hello", "world", (err, responses) => {  if (err) {    // some clients did not acknowledge the event in the given delay  } else {    console.log(responses); // one response per client  }});`

#### In a room[​](https://socket.io/docs/v4/emit-cheatsheet/#in-a-room "Direct link to In a room")

*   to all connected clients in the room named "my room"

`io.to("my room").emit("hello");`

*   to all connected clients except the ones in the room named "my room"

`io.except("my room").emit("hello");`

*   with multiple clauses

`io.to("room1").to(["room2", "room3"]).except("room4").emit("hello");`

#### In a namespace[​](https://socket.io/docs/v4/emit-cheatsheet/#in-a-namespace "Direct link to In a namespace")

`io.of("/my-namespace").emit("hello");`

tip

The modifiers can absolutely be chained:

`io.of("/my-namespace").on("connection", (socket) => {  socket    .timeout(5000)    .to("room1")    .to(["room2", "room3"])    .except("room4")    .emit("hello", (err, responses) => {      // ...    });});`

This will emit a "hello" event to all connected clients:

*   in the namespace named `my-namespace`
*   in at least one of the rooms named `room1`, `room2` and `room3`, but not in `room4`
*   except the sender

And expect an acknowledgement in the next 5 seconds.

### Between servers[​](https://socket.io/docs/v4/emit-cheatsheet/#between-servers "Direct link to Between servers")

#### Basic emit[​](https://socket.io/docs/v4/emit-cheatsheet/#basic-emit-1 "Direct link to Basic emit")

`io.serverSideEmit("hello", "world");`

Receiving side:

`io.on("hello", (value) => {  console.log(value); // "world"});`

#### Acknowledgements[​](https://socket.io/docs/v4/emit-cheatsheet/#acknowledgements-1 "Direct link to Acknowledgements")

*   Callback
*   Promise

`io.serverSideEmit("hello", "world", (err, responses) => {  if (err) {    // some servers did not acknowledge the event in the given delay  } else {    console.log(responses); // one response per server (except the current one)  }});`

Receiving side:

`io.on("hello", (value, callback) => {  console.log(value); // "world"  callback("hi");});`

### Basic emit[​](https://socket.io/docs/v4/emit-cheatsheet/#basic-emit-2 "Direct link to Basic emit")

`socket.emit("hello", 1, "2", { 3: "4", 5: Uint8Array.from([6]) });`

### Acknowledgement[​](https://socket.io/docs/v4/emit-cheatsheet/#acknowledgement-1 "Direct link to Acknowledgement")

*   Callback
*   Promise

`socket.emit("hello", "world", (arg1, arg2, arg3) => {  // ...});`

### Acknowledgement and timeout[​](https://socket.io/docs/v4/emit-cheatsheet/#acknowledgement-and-timeout-1 "Direct link to Acknowledgement and timeout")

*   Callback
*   Promise

`socket.timeout(5000).emit("hello", "world", (err, arg1, arg2, arg3) => {  if (err) {    // the server did not acknowledge the event in the given delay  } else {    // ...  }});`
