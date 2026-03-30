# Source: https://firebase.google.com/docs/database/web/offline-capabilities.md.txt

Firebase applications work even if your app loses its network connection temporarily. We provide several tools for monitoring presence and synchronizing local state with server state, which are introduced in this document.

## Managing Presence


In realtime applications it is often useful to detect when clients
connect and disconnect. For example, you may
want to mark a user as 'offline' when their client disconnects.


Firebase Database clients provide simple primitives that you can use to
write to the database when a client disconnects from the Firebase Database
servers. These updates occur whether the client disconnects cleanly or not,
so you can rely on them to clean up data even if a connection is dropped
or a client crashes. All write operations, including setting,
updating, and removing, can be performed upon a disconnection.


Here is a simple example of writing data upon disconnection by using the
`onDisconnect` primitive:

### Web

```javascript
import { getDatabase, ref, onDisconnect } from "firebase/database";

const db = getDatabase();
const presenceRef = ref(db, "disconnectmessage");
// Write a string when this client loses connection
onDisconnect(presenceRef).set("I disconnected!");
```

### Web

```javascript
var presenceRef = firebase.database().ref("disconnectmessage");
// Write a string when this client loses connection
presenceRef.onDisconnect().set("I disconnected!");
```

### How onDisconnect Works


When you establish an `onDisconnect()` operation, the operation
lives on the Firebase Realtime Database server. The server checks security to
make sure the user can perform the write event requested, and informs
your app if it is invalid. The server then
monitors the connection. If at any point the connection times out, or is
actively closed by the Realtime Database client, the server checks security a
second time (to make sure the operation is still valid) and then invokes
the event.

Your app can use the callback on the write operation
to ensure the `onDisconnect` was correctly attached:

### Web

```javascript
onDisconnect(presenceRef).remove().catch((err) => {
  if (err) {
    console.error("could not establish onDisconnect event", err);
  }
});
```

### Web

```javascript
presenceRef.onDisconnect().remove((err) => {
  if (err) {
    console.error("could not establish onDisconnect event", err);
  }
});
```

An `onDisconnect` event can also be canceled by calling `.cancel()`:

### Web

```javascript
const onDisconnectRef = onDisconnect(presenceRef);
onDisconnectRef.set("I disconnected");
// some time later when we change our minds
onDisconnectRef.cancel();
```

### Web

```javascript
var onDisconnectRef = presenceRef.onDisconnect();
onDisconnectRef.set("I disconnected");
// some time later when we change our minds
onDisconnectRef.cancel();
```

## Detecting Connection State


For many presence-related features, it is useful for your app
to know when it is online or offline. Firebase Realtime Database
provides a special location at `/.info/connected` which
is updated every time the Firebase Realtime Database client's connection state
changes. Here is an example:

### Web

```javascript
import { getDatabase, ref, onValue } from "firebase/database";

const db = getDatabase();
const connectedRef = ref(db, ".info/connected");
onValue(connectedRef, (snap) => {
  if (snap.val() === true) {
    console.log("connected");
  } else {
    console.log("not connected");
  }
});
```

### Web

```javascript
var connectedRef = firebase.database().ref(".info/connected");
connectedRef.on("value", (snap) => {
  if (snap.val() === true) {
    console.log("connected");
  } else {
    console.log("not connected");
  }
});
```


`/.info/connected` is a boolean value which is not
synchronized between Realtime Database clients because the value is
dependent on the state of the client. In other words, if one client
reads `/.info/connected` as false, this is no
guarantee that a separate client will also read false.

## Handling Latency

### Server Timestamps


The Firebase Realtime Database servers provide a mechanism to insert
timestamps generated on the server as data. This feature, combined with
`onDisconnect`, provides an easy way to reliably make note of
the time at which a Realtime Database client disconnected:

### Web

```javascript
import { getDatabase, ref, onDisconnect, serverTimestamp } from "firebase/database";

const db = getDatabase();
const userLastOnlineRef = ref(db, "users/joe/lastOnline");
onDisconnect(userLastOnlineRef).set(serverTimestamp());
```

### Web

```javascript
var userLastOnlineRef = firebase.database().ref("users/joe/lastOnline");
userLastOnlineRef.onDisconnect().set(firebase.database.ServerValue.TIMESTAMP);
```

### Clock Skew


While `firebase.database.ServerValue.TIMESTAMP` is much more
accurate, and preferable for most read/write operations,
it can occasionally be useful to estimate the client's clock skew with
respect to the Firebase Realtime Database's servers. You
can attach a callback to the location `/.info/serverTimeOffset`
to obtain the value, in milliseconds, that Firebase Realtime Database clients
add to the local reported time (epoch time in milliseconds) to estimate
the server time. Note that this offset's accuracy can be affected by
networking latency, and so is useful primarily for discovering
large (\> 1 second) discrepancies in clock time.

### Web

```javascript
import { getDatabase, ref, onValue } from "firebase/database";

const db = getDatabase();
const offsetRef = ref(db, ".info/serverTimeOffset");
onValue(offsetRef, (snap) => {
  const offset = snap.val();
  const estimatedServerTimeMs = new Date().getTime() + offset;
});
```

### Web

```javascript
var offsetRef = firebase.database().ref(".info/serverTimeOffset");
offsetRef.on("value", (snap) => {
  var offset = snap.val();
  var estimatedServerTimeMs = new Date().getTime() + offset;
});
```

## Sample Presence App


By combining disconnect operations with connection state monitoring and
server timestamps, you can build a user presence system. In this system,
each user stores data at a database location to indicate whether or not a
Realtime Database client is online. Clients set this location to true when
they come online and a timestamp when they disconnect. This timestamp
indicates the last time the given user was online.


Note that your app should queue the disconnect operations before a user is
marked online, to avoid any race conditions in the event that the client's
network connection is lost before both commands can be sent to the server.

Here is a simple user presence system:

### Web

```javascript
import { getDatabase, ref, onValue, push, onDisconnect, set, serverTimestamp } from "firebase/database";

// Since I can connect from multiple devices or browser tabs, we store each connection instance separately
// any time that connectionsRef's value is null (i.e. has no children) I am offline
const db = getDatabase();
const myConnectionsRef = ref(db, 'users/joe/connections');

// stores the timestamp of my last disconnect (the last time I was seen online)
const lastOnlineRef = ref(db, 'users/joe/lastOnline');

const connectedRef = ref(db, '.info/connected');
onValue(connectedRef, (snap) => {
  if (snap.val() === true) {
    // We're connected (or reconnected)! Do anything here that should happen only if online (or on reconnect)
    const con = push(myConnectionsRef);

    // When I disconnect, remove this device
    onDisconnect(con).remove();

    // Add this device to my connections list
    // this value could contain info about the device or a timestamp too
    set(con, true);

    // When I disconnect, update the last time I was seen online
    onDisconnect(lastOnlineRef).set(serverTimestamp());
  }
});
```

### Web

```javascript
// Since I can connect from multiple devices or browser tabs, we store each connection instance separately
// any time that connectionsRef's value is null (i.e. has no children) I am offline
var myConnectionsRef = firebase.database().ref('users/joe/connections');

// stores the timestamp of my last disconnect (the last time I was seen online)
var lastOnlineRef = firebase.database().ref('users/joe/lastOnline');

var connectedRef = firebase.database().ref('.info/connected');
connectedRef.on('value', (snap) => {
  if (snap.val() === true) {
    // We're connected (or reconnected)! Do anything here that should happen only if online (or on reconnect)
    var con = myConnectionsRef.push();

    // When I disconnect, remove this device
    con.onDisconnect().remove();

    // Add this device to my connections list
    // this value could contain info about the device or a timestamp too
    con.set(true);

    // When I disconnect, update the last time I was seen online
    lastOnlineRef.onDisconnect().set(firebase.database.ServerValue.TIMESTAMP);
  }
});
```