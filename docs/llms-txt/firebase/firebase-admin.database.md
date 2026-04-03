# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.database.md.txt

# firebase-admin.database package

## External API Re-exports

The following externally defined APIs are re-exported from this module entry point for convenience.

|                                                  Symbol                                                   |                              Description                               |
|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot)           | `DataSnapshot` type from the `@firebase/database-compat` package.      |
| [EventType](https://firebase.google.com/docs/reference/js/v8/firebase.database#eventtype)                 | `EventType` type from the `@firebase/database-compat` package.         |
| [OnDisconnect](https://firebase.google.com/docs/reference/js/v8/firebase.database.OnDisconnect)           | `OnDisconnect` type from the `@firebase/database-compat` package.      |
| [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query)                         | `Query` type from the `@firebase/database-compat` package.             |
| [Reference](https://firebase.google.com/docs/reference/js/v8/firebase.database.Reference)                 | `Reference` type from the `@firebase/database-compat` package.         |
| [ThenableReference](https://firebase.google.com/docs/reference/js/v8/firebase.database.ThenableReference) | `ThenableReference` type from the `@firebase/database-compat` package. |

Firebase Realtime Database.

## Functions

|                                                                  Function                                                                   |                                                                                                                                                                                                                                                                                                   Description                                                                                                                                                                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [getDatabase(app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database.md#getdatabase_8a40afc)                    | Gets the [Database](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database.database.md#database_interface) service for the default app or a given app.`getDatabase()` can be called with no arguments to access the default app's `Database` service or as `getDatabase(app)` to access the `Database` service associated with a specific app.                                                                                                                                                                                                                                           |
| [getDatabaseWithUrl(url, app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database.md#getdatabasewithurl_19a3502) | Gets the [Database](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database.database.md#database_interface) service for the default app or a given app.`getDatabaseWithUrl()` can be called with no arguments to access the default app's [Database](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database.database.md#database_interface) service or as `getDatabaseWithUrl(app)` to access the [Database](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database.database.md#database_interface) service associated with a specific app. |

## Classes

|                                                                            Class                                                                            |                             Description                             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| [FirebaseDatabaseError](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database.firebasedatabaseerror.md#firebasedatabaseerror_class) | Firebase Database error code structure. This extends FirebaseError. |

## Interfaces

|                                                        Interface                                                         |                                                                                                 Description                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Database](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database.database.md#database_interface) | The Firebase Database service interface. Extends the [Database](https://firebase.google.com/docs/reference/js/v8/firebase.database.Database) interface provided by the `@firebase/database-compat` package. |

## Variables

|                                                    Variable                                                     |                                                                       Description                                                                        |
|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [enableLogging](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database.md#enablelogging) | [enableLogging](https://firebase.google.com/docs/reference/js/v8/firebase.database#enablelogging) function from the `@firebase/database-compat` package. |
| [ServerValue](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database.md#servervalue)     | [ServerValue](https://firebase.google.com/docs/reference/js/v8/firebase.database.ServerValue) constant from the `@firebase/database-compat` package.     |

## getDatabase(app)

Gets the [Database](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database.database.md#database_interface) service for the default app or a given app.

`getDatabase()` can be called with no arguments to access the default app's `Database` service or as `getDatabase(app)` to access the `Database` service associated with a specific app.

**Signature:**  

    export declare function getDatabase(app?: App): Database;

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| app       | App  |             |

**Returns:**

[Database](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database.database.md#database_interface)

The default `Database` service if no app is provided or the `Database` service associated with the provided app.

### Example 1

    // Get the Database service for the default app
    const defaultDatabase = getDatabase();

### Example 2

    // Get the Database service for a specific app
    const otherDatabase = getDatabase(app);

## getDatabaseWithUrl(url, app)

Gets the [Database](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database.database.md#database_interface) service for the default app or a given app.

`getDatabaseWithUrl()` can be called with no arguments to access the default app's [Database](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database.database.md#database_interface) service or as `getDatabaseWithUrl(app)` to access the [Database](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database.database.md#database_interface) service associated with a specific app.

**Signature:**  

    export declare function getDatabaseWithUrl(url: string, app?: App): Database;

### Parameters

| Parameter |  Type  | Description |
|-----------|--------|-------------|
| url       | string |             |
| app       | App    |             |

**Returns:**

[Database](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database.database.md#database_interface)

The default `Database` service if no app is provided or the `Database` service associated with the provided app.

### Example 1

    // Get the Database service for the default app
    const defaultDatabase = getDatabaseWithUrl('https://example.firebaseio.com');

### Example 2

    // Get the Database service for a specific app
    const otherDatabase = getDatabaseWithUrl('https://example.firebaseio.com', app);

## enableLogging

[enableLogging](https://firebase.google.com/docs/reference/js/v8/firebase.database#enablelogging) function from the `@firebase/database-compat` package.

**Signature:**  

    enableLogging: typeof rtdb.enableLogging

## ServerValue

[ServerValue](https://firebase.google.com/docs/reference/js/v8/firebase.database.ServerValue) constant from the `@firebase/database-compat` package.

**Signature:**  

    ServerValue: rtdb.ServerValue