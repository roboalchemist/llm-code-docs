# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.database_n.md.txt

# database namespace

**Signature:**  

    export declare namespace database 

## Variables

|                                                         Variable                                                          |                                                                       Description                                                                        |
|---------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [enableLogging](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database_n.md#databaseenablelogging) | [enableLogging](https://firebase.google.com/docs/reference/js/v8/firebase.database#enablelogging) function from the `@firebase/database-compat` package. |
| [ServerValue](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database_n.md#databaseservervalue)     | [ServerValue](https://firebase.google.com/docs/reference/js/v8/firebase.database.ServerValue) constant from the `@firebase/database-compat` package.     |

## Type Aliases

|                                                            Type Alias                                                             |                                                                                Description                                                                                 |
|-----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Database](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database_n.md#databasedatabase)                   | Type alias to [Database](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database.database.md#database_interface).                                    |
| [DataSnapshot](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database_n.md#databasedatasnapshot)           | Type alias to [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot) type from the `@firebase/database-compat` package.           |
| [EventType](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database_n.md#databaseeventtype)                 | Type alias to the [EventType](https://firebase.google.com/docs/reference/js/v8/firebase.database#eventtype) type from the `@firebase/database-compat` package.             |
| [OnDisconnect](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database_n.md#databaseondisconnect)           | Type alias to [OnDisconnect](https://firebase.google.com/docs/reference/js/v8/firebase.database.OnDisconnect) type from the `@firebase/database-compat` package.           |
| [Query](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database_n.md#databasequery)                         | Type alias to [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query) type from the `@firebase/database-compat` package.                         |
| [Reference](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database_n.md#databasereference)                 | Type alias to [Reference](https://firebase.google.com/docs/reference/js/v8/firebase.database.Reference) type from the `@firebase/database-compat` package.                 |
| [ThenableReference](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database_n.md#databasethenablereference) | Type alias to [ThenableReference](https://firebase.google.com/docs/reference/js/v8/firebase.database.ThenableReference) type from the `@firebase/database-compat` package. |

## database.enableLogging

[enableLogging](https://firebase.google.com/docs/reference/js/v8/firebase.database#enablelogging) function from the `@firebase/database-compat` package.

**Signature:**  

    enableLogging: typeof rtdb.enableLogging

## database.ServerValue

[ServerValue](https://firebase.google.com/docs/reference/js/v8/firebase.database.ServerValue) constant from the `@firebase/database-compat` package.

**Signature:**  

    ServerValue: rtdb.ServerValue

## database.Database

Type alias to [Database](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database.database.md#database_interface).

**Signature:**  

    type Database = TDatabase;

## database.DataSnapshot

Type alias to [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot) type from the `@firebase/database-compat` package.

**Signature:**  

    type DataSnapshot = rtdb.DataSnapshot;

## database.EventType

Type alias to the [EventType](https://firebase.google.com/docs/reference/js/v8/firebase.database#eventtype) type from the `@firebase/database-compat` package.

**Signature:**  

    type EventType = rtdb.EventType;

## database.OnDisconnect

Type alias to [OnDisconnect](https://firebase.google.com/docs/reference/js/v8/firebase.database.OnDisconnect) type from the `@firebase/database-compat` package.

**Signature:**  

    type OnDisconnect = rtdb.OnDisconnect;

## database.Query

Type alias to [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query) type from the `@firebase/database-compat` package.

**Signature:**  

    type Query = rtdb.Query;

## database.Reference

Type alias to [Reference](https://firebase.google.com/docs/reference/js/v8/firebase.database.Reference) type from the `@firebase/database-compat` package.

**Signature:**  

    type Reference = rtdb.Reference;

## database.ThenableReference

Type alias to [ThenableReference](https://firebase.google.com/docs/reference/js/v8/firebase.database.ThenableReference) type from the `@firebase/database-compat` package.

**Signature:**  

    type ThenableReference = rtdb.ThenableReference;