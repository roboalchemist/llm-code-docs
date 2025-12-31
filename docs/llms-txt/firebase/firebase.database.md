# Source: https://firebase.google.com/docs/reference/node/firebase.database.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.database.md.txt

# database | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- database

### Callable

- database ( app ? : [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App) ) : [Database](https://firebase.google.com/docs/reference/js/v8/firebase.database.Database)
- Gets the [`Database`](https://firebase.google.com/docs/reference/js/v8/firebase.database.Database) service for the
  default app or a given app.

  `firebase.database()` can be called with no arguments to access the default
  app's [`Database`](https://firebase.google.com/docs/reference/js/v8/firebase.database.Database) service or as
  `firebase.database(app)` to access the
  [`Database`](https://firebase.google.com/docs/reference/js/v8/firebase.database.Database) service associated with a
  specific app.

  `firebase.database` is also a namespace that can be used to access global
  constants and methods associated with the `Database` service.

  example
  :

          // Get the Database service for the default app
          var defaultDatabase = firebase.database();


  example
  :

          // Get the Database service for a specific app
          var otherDatabase = firebase.database(app);


  namespace
  :

  #### Parameters

  -

    ##### Optional app: [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App)

    Optional app whose Database service to
    return. If not provided, the default Database service will be returned.

  #### Returns [Database](https://firebase.google.com/docs/reference/js/v8/firebase.database.Database)

  The default Database service if no app
  is provided or the Database service associated with the provided app.

## Index

### Modules

- [ServerValue](https://firebase.google.com/docs/reference/js/v8/firebase.database.ServerValue)

### Interfaces

- [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot)
- [Database](https://firebase.google.com/docs/reference/js/v8/firebase.database.Database)
- [IteratedDataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.iterateddatasnapshot)
- [OnDisconnect](https://firebase.google.com/docs/reference/js/v8/firebase.database.OnDisconnect)
- [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query)
- [Reference](https://firebase.google.com/docs/reference/js/v8/firebase.database.Reference)
- [ThenableReference](https://firebase.google.com/docs/reference/js/v8/firebase.database.ThenableReference)
- [TransactionResult](https://firebase.google.com/docs/reference/js/v8/firebase.database.TransactionResult)

### Type aliases

- [EmulatorMockTokenOptions](https://firebase.google.com/docs/reference/js/v8/firebase.database#emulatormocktokenoptions)
- [EventType](https://firebase.google.com/docs/reference/js/v8/firebase.database#eventtype)

### Functions

- [enableLogging](https://firebase.google.com/docs/reference/js/v8/firebase.database#enablelogging)

## Type aliases

### EmulatorMockTokenOptions

EmulatorMockTokenOptions: [EmulatorMockTokenOptions](https://firebase.google.com/docs/reference/js/v8/firebase#emulatormocktokenoptions)

### EventType

EventType: "value" \| "child_added" \| "child_changed" \| "child_moved" \| "child_removed"

## Functions

### enableLogging

- enableLogging ( logger ? : boolean \| ( ( a : string ) =\> any ) , persistent ? : boolean ) : any
- Logs debugging information to the console.

  example
  :

          // Enable logging
          firebase.database.enableLogging(true);


  example
  :

          // Disable logging
          firebase.database.enableLogging(false);


  example
  :

          // Enable logging across page refreshes
          firebase.database.enableLogging(true, true);


  example
  :

          // Provide custom logger which prefixes log statements with "[FIREBASE]"
          firebase.database.enableLogging(function(message) {
            console.log("[FIREBASE]", message);
          });


  #### Parameters

  -

    ##### Optional logger: boolean \| ((a: string) =\> any)

    Enables logging if `true`;
    disables logging if `false`. You can also provide a custom logger function
    to control how things get logged.
  -

    ##### Optional persistent: boolean

    Remembers the logging state between page
    refreshes if `true`.

  #### Returns any