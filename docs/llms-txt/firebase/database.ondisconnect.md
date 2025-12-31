# Source: https://firebase.google.com/docs/reference/js/database.ondisconnect.md.txt

# OnDisconnect class

The `onDisconnect` class allows you to write or clear data when your client disconnects from the Database server. These updates occur whether your client disconnects cleanly or not, so you can rely on them to clean up data even if a connection is dropped or a client crashes.

The `onDisconnect` class is most commonly used to manage presence in applications where it is useful to detect how many clients are connected and when other clients disconnect. See [Enabling Offline Capabilities in JavaScript](https://firebase.google.com/docs/database/web/offline-capabilities) for more information.

To avoid problems when a connection is dropped before the requests can be transferred to the Database server, these functions should be called before writing any data.

Note that `onDisconnect` operations are only triggered once. If you want an operation to occur each time a disconnect occurs, you'll need to re-establish the `onDisconnect` operations each time you reconnect.

**Signature:**  

    export declare class OnDisconnect 

## Methods

|                                                                 Method                                                                 | Modifiers |                                                                                                                                                                                                                                                                                                                                                Description                                                                                                                                                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [cancel()](https://firebase.google.com/docs/reference/js/database.ondisconnect.md#ondisconnectcancel)                                  |           | Cancels all previously queued `onDisconnect()` set or update events for this location and all children.If a write has been queued for this location via a `set()` or `update()` at a parent location, the write at this location will be canceled, though writes to sibling locations will still occur.                                                                                                                                                                                                                                                                                                                                                                                                    |
| [remove()](https://firebase.google.com/docs/reference/js/database.ondisconnect.md#ondisconnectremove)                                  |           | Ensures the data at this location is deleted when the client is disconnected (due to closing the browser, navigating to a new page, or network issues).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [set(value)](https://firebase.google.com/docs/reference/js/database.ondisconnect.md#ondisconnectset)                                   |           | Ensures the data at this location is set to the specified value when the client is disconnected (due to closing the browser, navigating to a new page, or network issues).`set()` is especially useful for implementing "presence" systems, where a value should be changed or cleared when a user disconnects so that they appear "offline" to other users. See [Enabling Offline Capabilities in JavaScript](https://firebase.google.com/docs/database/web/offline-capabilities) for more information.Note that `onDisconnect` operations are only triggered once. If you want an operation to occur each time a disconnect occurs, you'll need to re-establish the `onDisconnect` operations each time. |
| [setWithPriority(value, priority)](https://firebase.google.com/docs/reference/js/database.ondisconnect.md#ondisconnectsetwithpriority) |           | Ensures the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [update(values)](https://firebase.google.com/docs/reference/js/database.ondisconnect.md#ondisconnectupdate)                            |           | Writes multiple values at this location when the client is disconnected (due to closing the browser, navigating to a new page, or network issues).The `values` argument contains multiple property-value pairs that will be written to the Database together. Each child property can either be a simple property (for example, "name") or a relative path (for example, "name/first") from the current location to the data to update.As opposed to the `set()` method, `update()` can be use to selectively update only the referenced properties at the current location (instead of replacing all the child properties at the current location).                                                       |

## OnDisconnect.cancel()

Cancels all previously queued `onDisconnect()` set or update events for this location and all children.

If a write has been queued for this location via a `set()` or `update()` at a parent location, the write at this location will be canceled, though writes to sibling locations will still occur.

**Signature:**  

    cancel(): Promise<void>;

**Returns:**

Promise\<void\>

Resolves when synchronization to the server is complete.

## OnDisconnect.remove()

Ensures the data at this location is deleted when the client is disconnected (due to closing the browser, navigating to a new page, or network issues).

**Signature:**  

    remove(): Promise<void>;

**Returns:**

Promise\<void\>

Resolves when synchronization to the server is complete.

## OnDisconnect.set()

Ensures the data at this location is set to the specified value when the client is disconnected (due to closing the browser, navigating to a new page, or network issues).

`set()` is especially useful for implementing "presence" systems, where a value should be changed or cleared when a user disconnects so that they appear "offline" to other users. See [Enabling Offline Capabilities in JavaScript](https://firebase.google.com/docs/database/web/offline-capabilities) for more information.

Note that `onDisconnect` operations are only triggered once. If you want an operation to occur each time a disconnect occurs, you'll need to re-establish the `onDisconnect` operations each time.

**Signature:**  

    set(value: unknown): Promise<void>;

#### Parameters

| Parameter |  Type   |                                                     Description                                                     |
|-----------|---------|---------------------------------------------------------------------------------------------------------------------|
| value     | unknown | The value to be written to this location on disconnect (can be an object, array, string, number, boolean, or null). |

**Returns:**

Promise\<void\>

Resolves when synchronization to the Database is complete.

## OnDisconnect.setWithPriority()

Ensures the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues).

**Signature:**  

    setWithPriority(value: unknown, priority: number | string | null): Promise<void>;

#### Parameters

| Parameter |           Type           |                                                     Description                                                     |
|-----------|--------------------------|---------------------------------------------------------------------------------------------------------------------|
| value     | unknown                  | The value to be written to this location on disconnect (can be an object, array, string, number, boolean, or null). |
| priority  | number \| string \| null | The priority to be written (string, number, or null).                                                               |

**Returns:**

Promise\<void\>

Resolves when synchronization to the Database is complete.

## OnDisconnect.update()

Writes multiple values at this location when the client is disconnected (due to closing the browser, navigating to a new page, or network issues).

The `values` argument contains multiple property-value pairs that will be written to the Database together. Each child property can either be a simple property (for example, "name") or a relative path (for example, "name/first") from the current location to the data to update.

As opposed to the `set()` method, `update()` can be use to selectively update only the referenced properties at the current location (instead of replacing all the child properties at the current location).

**Signature:**  

    update(values: object): Promise<void>;

#### Parameters

| Parameter |  Type  |            Description             |
|-----------|--------|------------------------------------|
| values    | object | Object containing multiple values. |

**Returns:**

Promise\<void\>

Resolves when synchronization to the Database is complete.