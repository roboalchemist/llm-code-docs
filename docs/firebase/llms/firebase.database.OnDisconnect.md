# Source: https://firebase.google.com/docs/reference/js/v8/firebase.database.OnDisconnect.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.database.OnDisconnect.md.txt

# OnDisconnect | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/node/firebase).
- [database](https://firebase.google.com/docs/reference/node/firebase.database).
- OnDisconnect

The `onDisconnect` class allows you to write or clear data when your client
disconnects from the Database server. These updates occur whether your
client disconnects cleanly or not, so you can rely on them to clean up data
even if a connection is dropped or a client crashes.

The `onDisconnect` class is most commonly used to manage presence in
applications where it is useful to detect how many clients are connected and
when other clients disconnect. See
[Enabling Offline Capabilities in JavaScript](https://firebase.google.com/docs/database/web/offline-capabilities) for more information.

To avoid problems when a connection is dropped before the requests can be
transferred to the Database server, these functions should be called before
writing any data.

Note that `onDisconnect` operations are only triggered once. If you want an
operation to occur each time a disconnect occurs, you'll need to re-establish
the `onDisconnect` operations each time you reconnect.

## Index

### Methods

- [cancel](https://firebase.google.com/docs/reference/node/firebase.database.OnDisconnect#cancel)
- [remove](https://firebase.google.com/docs/reference/node/firebase.database.OnDisconnect#remove)
- [set](https://firebase.google.com/docs/reference/node/firebase.database.OnDisconnect#set)
- [setWithPriority](https://firebase.google.com/docs/reference/node/firebase.database.OnDisconnect#setwithpriority)
- [update](https://firebase.google.com/docs/reference/node/firebase.database.OnDisconnect#update)

## Methods

### cancel

- cancel ( onComplete ? : ( a : [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null ) =\> any ) : Promise \< any \>
- Cancels all previously queued `onDisconnect()` set or update events for this
  location and all children.

  If a write has been queued for this location via a `set()` or `update()` at a
  parent location, the write at this location will be canceled, though writes
  to sibling locations will still occur.

  example
  :

          var ref = firebase.database().ref("onlineState");
          ref.onDisconnect().set(false);
          // ... sometime later
          ref.onDisconnect().cancel();


  #### Parameters

  -

    ##### Optional onComplete: (a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null) =\> any

    An optional callback function that will
    be called when synchronization to the server has completed. The callback
    will be passed a single parameter: null for success, or an Error object
    indicating a failure.
    -
      - (a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null): any

      <!-- -->

      -

        #### Parameters

        -

          ##### a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null

        #### Returns any

  #### Returns Promise\<any\>

  Resolves when synchronization to the server
  is complete.

### remove

- remove ( onComplete ? : ( a : [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null ) =\> any ) : Promise \< any \>
- Ensures the data at this location is deleted when the client is disconnected
  (due to closing the browser, navigating to a new page, or network issues).

  #### Parameters

  -

    ##### Optional onComplete: (a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null) =\> any

    An optional callback function that will
    be called when synchronization to the server has completed. The callback
    will be passed a single parameter: null for success, or an Error object
    indicating a failure.
    -
      - (a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null): any

      <!-- -->

      -

        #### Parameters

        -

          ##### a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null

        #### Returns any

  #### Returns Promise\<any\>

  Resolves when synchronization to the server
  is complete.

### set

- set ( value : any , onComplete ? : ( a : [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null ) =\> any ) : Promise \< any \>
- Ensures the data at this location is set to the specified value when the
  client is disconnected (due to closing the browser, navigating to a new page,
  or network issues).

  `set()` is especially useful for implementing "presence" systems, where a
  value should be changed or cleared when a user disconnects so that they
  appear "offline" to other users. See
  [Enabling Offline Capabilities in JavaScript](https://firebase.google.com/docs/database/web/offline-capabilities) for more information.

  Note that `onDisconnect` operations are only triggered once. If you want an
  operation to occur each time a disconnect occurs, you'll need to re-establish
  the `onDisconnect` operations each time.

  example
  :

          var ref = firebase.database().ref("users/ada/status");
          ref.onDisconnect().set("I disconnected!");


  #### Parameters

  -

    ##### value: any

    The value to be written to this location on
    disconnect (can be an object, array, string, number, boolean, or null).
  -

    ##### Optional onComplete: (a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null) =\> any

    An optional callback function that
    will be called when synchronization to the Database server has completed.
    The callback will be passed a single parameter: null for success, or an
    `Error` object indicating a failure.
    -
      - (a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null): any

      <!-- -->

      -

        #### Parameters

        -

          ##### a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null

        #### Returns any

  #### Returns Promise\<any\>

  Resolves when synchronization to the
  Database is complete.

### setWithPriority

- setWithPriority ( value : any , priority : number \| string \| null , onComplete ? : ( a : [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null ) =\> any ) : Promise \< any \>
- Ensures the data at this location is set to the specified value and priority
  when the client is disconnected (due to closing the browser, navigating to a
  new page, or network issues).

  #### Parameters

  -

    ##### value: any

  -

    ##### priority: number \| string \| null

  -

    ##### Optional onComplete: (a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null) =\> any

    -
      - (a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null): any

      <!-- -->

      -

        #### Parameters

        -

          ##### a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null

        #### Returns any

  #### Returns Promise\<any\>

### update

- update ( values : Object , onComplete ? : ( a : [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null ) =\> any ) : Promise \< any \>
- Writes multiple values at this location when the client is disconnected (due
  to closing the browser, navigating to a new page, or network issues).

  The `values` argument contains multiple property-value pairs that will be
  written to the Database together. Each child property can either be a simple
  property (for example, "name") or a relative path (for example, "name/first")
  from the current location to the data to update.

  As opposed to the `set()` method, `update()` can be use to selectively update
  only the referenced properties at the current location (instead of replacing
  all the child properties at the current location).

  See more examples using the connected version of
  [`update()`](https://firebase.google.com/docs/reference/node/firebase.database.Reference#update).

  example
  :

          var ref = firebase.database().ref("users/ada");
          ref.update({
             onlineState: true,
             status: "I'm online."
          });
          ref.onDisconnect().update({
            onlineState: false,
            status: "I'm offline."
          });


  #### Parameters

  -

    ##### values: Object

    Object containing multiple values.
  -

    ##### Optional onComplete: (a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null) =\> any

    An optional callback function that will
    be called when synchronization to the server has completed. The
    callback will be passed a single parameter: null for success, or an Error
    object indicating a failure.
    -
      - (a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null): any

      <!-- -->

      -

        #### Parameters

        -

          ##### a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null

        #### Returns any

  #### Returns Promise\<any\>

  Resolves when synchronization to the
Database is complete.