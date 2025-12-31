# Source: https://firebase.google.com/docs/reference/node/firebase.database.Database.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.database.Database.md.txt

# Database | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [database](https://firebase.google.com/docs/reference/js/v8/firebase.database).
- Database

The Firebase Database service interface.

Do not call this constructor directly. Instead, use
[`firebase.database()`](https://firebase.google.com/docs/reference/js/v8/firebase.database).

See
[Installation \& Setup in JavaScript](https://firebase.google.com/docs/database/web/start/)
for a full guide on how to use the Firebase Database service.

## Index

### Properties

- [INTERNAL](https://firebase.google.com/docs/reference/js/v8/firebase.database.Database#internal)
- [app](https://firebase.google.com/docs/reference/js/v8/firebase.database.Database#app)

### Methods

- [goOffline](https://firebase.google.com/docs/reference/js/v8/firebase.database.Database#gooffline)
- [goOnline](https://firebase.google.com/docs/reference/js/v8/firebase.database.Database#goonline)
- [ref](https://firebase.google.com/docs/reference/js/v8/firebase.database.Database#ref)
- [refFromURL](https://firebase.google.com/docs/reference/js/v8/firebase.database.Database#reffromurl)
- [useEmulator](https://firebase.google.com/docs/reference/js/v8/firebase.database.Database#useemulator)

## Properties

### INTERNAL

INTERNAL: { forceLongPolling: () =\> void; forceWebSockets: () =\> void }  
Additional methods for debugging and special cases.  

#### Type declaration

-

  ##### forceLongPolling: () =\> void

  Force the use of long polling instead of WebSockets. This will be ignored if the WebSocket protocol is used in `databaseURL`.
  -
    - (): void

    <!-- -->

    -

      #### Returns void

-

  ##### forceWebSockets: () =\> void

  Force the use of WebSockets instead of long polling.
  -
    - (): void

    <!-- -->

    -

      #### Returns void

### app

app: [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App)  
The [app](https://firebase.google.com/docs/reference/js/v8/firebase.app.App) associated with the `Database` service
instance.

example
:

        var app = database.app;


## Methods

### goOffline

- goOffline ( ) : any
- Disconnects from the server (all Database operations will be completed
  offline).

  The client automatically maintains a persistent connection to the Database
  server, which will remain active indefinitely and reconnect when
  disconnected. However, the `goOffline()` and `goOnline()` methods may be used
  to control the client connection in cases where a persistent connection is
  undesirable.

  While offline, the client will no longer receive data updates from the
  Database. However, all Database operations performed locally will continue to
  immediately fire events, allowing your application to continue behaving
  normally. Additionally, each operation performed locally will automatically
  be queued and retried upon reconnection to the Database server.

  To reconnect to the Database and begin receiving remote events, see
  `goOnline()`.

  example
  :

          firebase.database().goOffline();


  #### Returns any

### goOnline

- goOnline ( ) : any
- Reconnects to the server and synchronizes the offline Database state
  with the server state.

  This method should be used after disabling the active connection with
  `goOffline()`. Once reconnected, the client will transmit the proper data
  and fire the appropriate events so that your client "catches up"
  automatically.

  example
  :

          firebase.database().goOnline();


  #### Returns any

### ref

- ref ( path ? : string ) : [Reference](https://firebase.google.com/docs/reference/js/v8/firebase.database.Reference)
- Returns a `Reference` representing the location in the Database
  corresponding to the provided path. If no path is provided, the `Reference`
  will point to the root of the Database.

  example
  :

          // Get a reference to the root of the Database
          var rootRef = firebase.database().ref();


  example
  :

          // Get a reference to the /users/ada node
          var adaRef = firebase.database().ref("users/ada");
          // The above is shorthand for the following operations:
          //var rootRef = firebase.database().ref();
          //var adaRef = rootRef.child("users/ada");


  #### Parameters

  -

    ##### Optional path: string

    Optional path representing the location the returned
    `Reference` will point. If not provided, the returned `Reference` will
    point to the root of the Database.

  #### Returns [Reference](https://firebase.google.com/docs/reference/js/v8/firebase.database.Reference)

  If a path is provided, a `Reference`
  pointing to the provided path. Otherwise, a `Reference` pointing to the
  root of the Database.

### refFromURL

- refFromURL ( url : string ) : [Reference](https://firebase.google.com/docs/reference/js/v8/firebase.database.Reference)
- Returns a `Reference` representing the location in the Database
  corresponding to the provided Firebase URL.

  An exception is thrown if the URL is not a valid Firebase Database URL or it
  has a different domain than the current `Database` instance.

  Note that all query parameters (`orderBy`, `limitToLast`, etc.) are ignored
  and are not applied to the returned `Reference`.

  example
  :

          // Get a reference to the root of the Database
          var rootRef = firebase.database().ref("https://<DATABASE_NAME>.firebaseio.com");


  example
  :

          // Get a reference to the /users/ada node
          var adaRef = firebase.database().ref("https://<DATABASE_NAME>.firebaseio.com/users/ada");


  #### Parameters

  -

    ##### url: string

    The Firebase URL at which the returned `Reference` will
    point.

  #### Returns [Reference](https://firebase.google.com/docs/reference/js/v8/firebase.database.Reference)

  A `Reference` pointing to the provided
  Firebase URL.

### useEmulator

- useEmulator ( host : string , port : number , options ? : { mockUserToken ?: [EmulatorMockTokenOptions](https://firebase.google.com/docs/reference/js/v8/firebase.database#emulatormocktokenoptions) \| string } ) : void
- Modify this instance to communicate with the Realtime Database emulator.

  Note: This method must be called before performing any other operation.

  #### Parameters

  -

    ##### host: string

    the emulator host (ex: localhost)
  -

    ##### port: number

    the emulator port (ex: 8080)
  -

    ##### Optional options: { mockUserToken?: [EmulatorMockTokenOptions](https://firebase.google.com/docs/reference/js/v8/firebase.database#emulatormocktokenoptions) \| string }

    -

      ##### Optional mockUserToken?: [EmulatorMockTokenOptions](https://firebase.google.com/docs/reference/js/v8/firebase.database#emulatormocktokenoptions) \| string

      the mock auth token to use for unit testing Security Rules

  #### Returns void