# Source: https://firebase.google.com/docs/cli/database-profile.md.txt

## Firebase Realtime Databaseprofiler command

To generate a report of the speed and bandwidth usage for operations in yourRealtime Databaseinstance, use the following command:  

```
firebase database:profile
```

|                    Flag options                    |                                       Description                                       |
|----------------------------------------------------|-----------------------------------------------------------------------------------------|
| `-h, --help`                                       | Output usage information.                                                               |
| `-o, --output `<var translate="no">FILENAME</var>  | Save the output to the specified file.                                                  |
| `-i, --input `<var translate="no">FILENAME</var>   | Generate the report based on the specified file instead of stream logs from the server. |
| `-d, --duration `<var translate="no">SECONDS</var> | Collect database usage information for the specified number of seconds.                 |
| `--raw `                                           | Output the raw stats collected as new-line delimited JSON.                              |

## Operation types

### concurrent-connect

This operation reflects realtime connections to the database (for example, when a new client connects via an SDK). RESTful connections are not reflected in concurrent-connect operations.  

```javascript
{
    "name": "concurrent-connect",
    "timestamp": 1484776334900
}
```

### concurrent-disconnect

Concurrent-disconnects reflect a connection that has disconnected from the database (for example, when a client disconnects or signs off).  

```javascript
{
    "name": "concurrent-disconnect",
    "timestamp": 1484776341844
}
```

### realtime-write

Write requests from realtime connections. For example,`set()`and`push()`operations for web clients. Delete requests are also counted as`realtime-write`operations, and reflect writes of 0 bytes.  

```javascript
{
    "allowed": true, // If security rules allow the operation
    "bytes": 1,
    "millis": 2,
    "name": "realtime-write",
    "path": [
        "foo"
    ],
    "timestamp": 1484776538763
}
```

### realtime-transaction

This operation type includes transactions conducted through realtime connections. Repeat transactions may be the result of failed attempts and retries.  

```javascript
{
    "allowed": true,
    "bytes": 20,
    "millis": 2,
    "name": "realtime-transaction",
    "path": [
        "foo"
    ],
    "timestamp": 1484776854610
}
```

### realtime-update

These realtime operations for updates reflect overwites of specific data, not the more general write operations in`realtime-write`.  

```javascript
{
    "allowed": true,
    "bytes": 5,
    "millis": 2,
    "name": "realtime-update",
    "path": [
        "foo"
    ],
    "timestamp": 1484776538769
}
```

### listener-listen

These operations reflect the initial ask for data at a specific location from a client. For example, the`on()`or`once()`methods for web clients.  

```javascript
{
    "allowed": true,
    "bytes": 0,
    "millis": 26,
    "name": "listener-listen",
    "path": [
        "foo"
    ],
    "querySet": [],
    "timestamp": 1484776335024,
    "unIndexed": false
}
```

### listener-broadcast

This operation covers the data sent from the server to any and all clients that are listening at a given location following every write and update operation. The change to the data leads to a broadcast operation. However, you may see 0 updates if there aren't any clients listening.  

```javascript
{
    "bytes": 56, // Total bytes sent across clients
    "clientsUpdated": 3, // This may be 0 if no clients are listening
    "millis": 17,
    "name": "listener-broadcast",
    "path": [
        "baz",
        "mar"
    ],
    "timestamp": 1484775969928
}
```

### listener-unlisten

These operations reflect listening clients that sign off or stop listening through the detach methods (for example,`off()`for web, or`removeAllObservers`for iOS).  

```javascript
{
    "name": "listener-unlisten",
    "path": [
        "foo"
    ],
    "timestamp": 1484776335044
}
```

### rest-read

[`GET`](https://firebase.google.com/docs/reference/rest/database#section-get)requests through the REST API.  

```javascript
{
    "allowed": true,
    "bytes": 348, // This would be 0 if the read data was null
    "millis": 26,
    "name": "rest-read",
    "path": [],
    "querySet": [
        {
            "default": true,
            "endIndexValue": "[MAX_NAME]",
            "equality": false,
            "index": {},
            "limit": null,
            "range": false,
            "simpleLimit": false,
            "startIndexValue": "[MIN_NAME]",
            "viewFrom": null
        }
    ],
    "timestamp": 1484775747416
}
```

### rest-write

[`PUT`](https://firebase.google.com/docs/reference/rest/database#section-put)and[`POST`](https://firebase.google.com/docs/reference/rest/database#section-post)requests through the REST API.[`DELETE`](https://firebase.google.com/docs/reference/rest/database#section-delete)requests reflect`rest-write`operations of 0 bytes.  

```javascript
{
    "allowed": true,
    "bytes": 13,
    "millis": 116,
    "name": "rest-write",
    "path": [],
    "timestamp": 1484775917216
}
```

### rest-transaction

For transaction-like behavior, use[conditional Requests](https://firebase.google.com/docs/database/rest/save-data#section-conditional-requests). The`rest-transaction`operation captures requests using`Etag`or`if-match`headers.  

```javascript
{
    "allowed": true,
    "bytes": 13,
    "millis": 116,
    "name": "rest-transaction",
    "path": [],
    "timestamp": 1484775917216
}
```

### rest-update

Updates through the REST API reflect[`PATCH`](https://firebase.google.com/docs/reference/rest/database#section-patch)requests.  

```javascript
{
    "allowed": true,
    "bytes": 5,
    "millis": 11,
    "name": "rest-update",
    "path": [
        "baz",
        "mar"
    ],
    "timestamp": 1484775969930
}
```

### on-disconnect-put

These operations reflect the addition of`onDisconnect`listeners to write operations. For example, when you use`onDisconnect().setValue()`.  

```javascript
{
    "allowed": true,
    "bytes": 4,
    "millis": 2,
    "name": "on-disconnect-put",
    "path": [
        "baz",
        "mar"
    ],
    "timestamp": 1484775969930
}
```

### on-disconnect-update

These operations reflect the addition of`onDisconnect`listeners to update operations. For example, when you use`onDisconnect().updateChildren()`.  

```javascript
{
    "allowed": true,
    "bytes": 4,
    "millis": 2,
    "name": "on-disconnect-update",
    "path": [
        "baz",
        "mar"
    ],
    "timestamp": 1484775969930
}
```

### on-disconnect-cancel

These operations reflect the removal of onDisconnect listeners. For example, when you use`onDisconnect().set().cancel()`.  

```javascript
{
    "millis": 2,
    "name": "on-disconnect-cancel",
    "path": [
        "baz",
        "mar"
    ],
    "timestamp": 1484775969930
}
```

### run-on-disconnect

These operations reflect the triggering of`onDisconnect`listeners. When a realtime client disconnects after adding at least one`onDisconnect`listener, the profiler records a single`run-on-disconnect`operation to reflect the aggregated bytes and time of all the`onDisconnect`listeners triggered.  

```javascript
{
    "bytes": 4,
    "millis": 2,
    "name": "run-on-disconnect",
    "timestamp": 1484775969930
}
```