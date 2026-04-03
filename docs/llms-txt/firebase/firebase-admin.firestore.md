# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.firestore.md.txt

# firebase-admin.firestore package

## External API Re-exports

The following externally defined APIs are re-exported from this module entry point for convenience.

|                                                          Symbol                                                          |                                Description                                |
|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| [BulkWriter](https://cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/bulkwriter)                       | `BulkWriter` type from the `@google-cloud/firestore` package.             |
| [AggregateField](https://cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/aggregatefield)               | `AggregateField` type from the `@google-cloud/firestore` package.         |
| [BulkWriterOptions](https://cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/bulkwriter)                | `BulkWriterOptions` type from the `@google-cloud/firestore` package.      |
| [BundleBuilder](https://googleapis.dev/nodejs/firestore/latest/BundleBuilder.html)                                       | `BundleBuilder` type from the `@google-cloud/firestore` package.          |
| [CollectionGroup](https://cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/collectiongroup)             | `CollectionGroup` type from the `@google-cloud/firestore` package.        |
| [CollectionReference](https://cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/collectionreference)     | `CollectionReference` type from the `@google-cloud/firestore` package.    |
| [DocumentChange](https://cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentchange)               | `DocumentChange` type from the `@google-cloud/firestore` package.         |
| [DocumentData](https://googleapis.dev/nodejs/firestore/latest/global.html#DocumentData)                                  | `DocumentData` type from the `@google-cloud/firestore` package.           |
| [DocumentReference](https://cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentreference)         | `DocumentReference` type from the `@google-cloud/firestore` package.      |
| [DocumentSnapshot](https://cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentsnapshot)           | `DocumentSnapshot` type from the `@google-cloud/firestore` package.       |
| [FieldPath](https://cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldpath)                         | `FieldPath` type from the `@google-cloud/firestore` package.              |
| [FieldValue](https://cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldvalue)                       | `FieldValue` type from the `@google-cloud/firestore` package.             |
| [Filter](https://cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/filter)                               | `Filter` type from the `@google-cloud/firestore` package.                 |
| [Firestore](https://cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/firestore)                         | `Firestore` type from the `@google-cloud/firestore` package.              |
| [FirestoreDataConverter](https://googleapis.dev/nodejs/firestore/latest/global.html#FirestoreDataConverter)              | `FirestoreDataConverter` type from the `@google-cloud/firestore` package. |
| [GeoPoint](https://cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/geopoint)                           | `GeoPoint` type from the `@google-cloud/firestore` package.               |
| [GrpcStatus](https://googleapis.dev/nodejs/firestore/latest/global.html#GrpcStatus)                                      | `GrpcStatus` type from the `@google-cloud/firestore` package.             |
| [Precondition](https://googleapis.dev/nodejs/firestore/latest/global.html#Precondition)                                  | `Precondition` type from the `@google-cloud/firestore` package.           |
| [Query](https://cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query)                                 | `Query` type from the `@google-cloud/firestore` package.                  |
| [QueryDocumentSnapshot](https://cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querydocumentsnapshot) | `QueryDocumentSnapshot` type from the `@google-cloud/firestore` package.  |
| [QueryPartition](https://cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querypartition)               | `QueryPartition` type from the `@google-cloud/firestore` package.         |
| [QuerySnapshot](https://cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querysnapshot)                 | `QuerySnapshot` type from the `@google-cloud/firestore` package.          |
| [ReadOptions](https://googleapis.dev/nodejs/firestore/latest/global.html#ReadOptions)                                    | `ReadOptions` type from the `@google-cloud/firestore` package.            |
| [SetOptions](https://googleapis.dev/nodejs/firestore/latest/global.html#SetOptions)                                      | `SetOptions` type from the `@google-cloud/firestore` package.             |
| [Timestamp](https://cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/timestamp)                         | `Timestamp` type from the `@google-cloud/firestore` package.              |
| [Transaction](https://cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/transaction)                     | `Transaction` type from the `@google-cloud/firestore` package.            |
| [WriteBatch](https://cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/writebatch)                       | `WriteBatch` type from the `@google-cloud/firestore` package.             |
| [WriteResult](https://cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/writeresult)                     | `WriteResult` type from the `@google-cloud/firestore` package.            |
| [setLogFunction](https://googleapis.dev/nodejs/firestore/latest/global.html#setLogFunction)                              | `setLogFunction` function from the `@google-cloud/firestore` package.     |

Cloud Firestore.

## Functions

|                                                                            Function                                                                             |                                                                                  Description                                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [getFirestore()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.firestore.md#getfirestore)                                                | Gets the default [Firestore](https://googleapis.dev/nodejs/firestore/latest/Firestore.html) service for the default app.                                                       |
| [getFirestore(app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.firestore.md#getfirestore_8a40afc)                                     | Gets the default [Firestore](https://googleapis.dev/nodejs/firestore/latest/Firestore.html) service for the given app.                                                         |
| [getFirestore(databaseId)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.firestore.md#getfirestore_53dc891)                              | ***(BETA)*** Gets the named [Firestore](https://googleapis.dev/nodejs/firestore/latest/Firestore.html) service for the default app.                                            |
| [getFirestore(app, databaseId)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.firestore.md#getfirestore_1ae3925)                         | ***(BETA)*** Gets the named [Firestore](https://googleapis.dev/nodejs/firestore/latest/Firestore.html) service for the given app.                                              |
| [initializeFirestore(app, settings)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.firestore.md#initializefirestore_be9f1d9)             | Gets the default [Firestore](https://googleapis.dev/nodejs/firestore/latest/Firestore.html) service for the given app, passing extra parameters to its constructor.            |
| [initializeFirestore(app, settings, databaseId)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.firestore.md#initializefirestore_9036a4f) | ***(BETA)*** Gets the named [Firestore](https://googleapis.dev/nodejs/firestore/latest/Firestore.html) service for the given app, passing extra parameters to its constructor. |

## Classes

|                                                                              Class                                                                              |                             Description                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [FirebaseFirestoreError](https://firebase.google.com/docs/reference/admin/node/firebase-admin.firestore.firebasefirestoreerror.md#firebasefirestoreerror_class) | Firebase Firestore error code structure. This extends FirebaseError. |

## Interfaces

|                                                                      Interface                                                                       |                  Description                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| [FirestoreSettings](https://firebase.google.com/docs/reference/admin/node/firebase-admin.firestore.firestoresettings.md#firestoresettings_interface) | Settings to pass to the Firestore constructor. |

## getFirestore()

Gets the default [Firestore](https://googleapis.dev/nodejs/firestore/latest/Firestore.html) service for the default app.

**Signature:**  

    export declare function getFirestore(): Firestore;

**Returns:**

Firestore

The default [Firestore](https://googleapis.dev/nodejs/firestore/latest/Firestore.html) service for the default app.

### Example

    // Get the default Firestore service for the default app
    const defaultFirestore = getFirestore();

## getFirestore(app)

Gets the default [Firestore](https://googleapis.dev/nodejs/firestore/latest/Firestore.html) service for the given app.

**Signature:**  

    export declare function getFirestore(app: App): Firestore;

### Parameters

| Parameter | Type |             Description              |
|-----------|------|--------------------------------------|
| app       | App  | which `Firestore` service to return. |

**Returns:**

Firestore

The default [Firestore](https://googleapis.dev/nodejs/firestore/latest/Firestore.html) service associated with the provided app.

### Example

    // Get the default Firestore service for a specific app
    const otherFirestore = getFirestore(app);

## getFirestore(databaseId)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Gets the named [Firestore](https://googleapis.dev/nodejs/firestore/latest/Firestore.html) service for the default app.

**Signature:**  

    export declare function getFirestore(databaseId: string): Firestore;

### Parameters

| Parameter  |  Type  |         Description         |
|------------|--------|-----------------------------|
| databaseId | string | name of database to return. |

**Returns:**

Firestore

The named [Firestore](https://googleapis.dev/nodejs/firestore/latest/Firestore.html) service for the default app.

### Example

    // Get the Firestore service for a named database and default app
    const otherFirestore = getFirestore('otherDb');

## getFirestore(app, databaseId)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Gets the named [Firestore](https://googleapis.dev/nodejs/firestore/latest/Firestore.html) service for the given app.

**Signature:**  

    export declare function getFirestore(app: App, databaseId: string): Firestore;

### Parameters

| Parameter  |  Type  |             Description              |
|------------|--------|--------------------------------------|
| app        | App    | which `Firestore` service to return. |
| databaseId | string | name of database to return.          |

**Returns:**

Firestore

The named [Firestore](https://googleapis.dev/nodejs/firestore/latest/Firestore.html) service associated with the provided app.

### Example

    // Get the Firestore service for a named database and specific app.
    const otherFirestore = getFirestore('otherDb');

## initializeFirestore(app, settings)

Gets the default [Firestore](https://googleapis.dev/nodejs/firestore/latest/Firestore.html) service for the given app, passing extra parameters to its constructor.

**Signature:**  

    export declare function initializeFirestore(app: App, settings?: FirestoreSettings): Firestore;

### Parameters

| Parameter |                                                                         Type                                                                         |                   Description                    |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| app       | App                                                                                                                                                  | which `Firestore` service to return.             |
| settings  | [FirestoreSettings](https://firebase.google.com/docs/reference/admin/node/firebase-admin.firestore.firestoresettings.md#firestoresettings_interface) | Settings object to be passed to the constructor. |

**Returns:**

Firestore

The default `Firestore` service associated with the provided app and settings.

### Example

    // Get the Firestore service for a specific app, require HTTP/1.1 REST transport
    const otherFirestore = initializeFirestore(app, {preferRest: true});

## initializeFirestore(app, settings, databaseId)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Gets the named [Firestore](https://googleapis.dev/nodejs/firestore/latest/Firestore.html) service for the given app, passing extra parameters to its constructor.

**Signature:**  

    export declare function initializeFirestore(app: App, settings: FirestoreSettings, databaseId: string): Firestore;

### Parameters

| Parameter  |                                                                         Type                                                                         |                   Description                    |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| app        | App                                                                                                                                                  | which `Firestore` service to return.             |
| settings   | [FirestoreSettings](https://firebase.google.com/docs/reference/admin/node/firebase-admin.firestore.firestoresettings.md#firestoresettings_interface) | Settings object to be passed to the constructor. |
| databaseId | string                                                                                                                                               | name of database to return.                      |

**Returns:**

Firestore

The named `Firestore` service associated with the provided app and settings.

### Example

    // Get the Firestore service for a specific app, require HTTP/1.1 REST transport
    const otherFirestore = initializeFirestore(app, {preferRest: true}, 'otherDb');