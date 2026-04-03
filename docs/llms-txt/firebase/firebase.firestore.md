# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.md.txt

# firestore | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/node/firebase).
- firestore

### Callable

- firestore ( app ? : [App](https://firebase.google.com/docs/reference/node/firebase.app.App) ) : [Firestore](https://firebase.google.com/docs/reference/node/firebase.firestore.Firestore)
-

  #### Parameters

  -

    ##### Optional app: [App](https://firebase.google.com/docs/reference/node/firebase.app.App)

  #### Returns [Firestore](https://firebase.google.com/docs/reference/node/firebase.firestore.Firestore)

## Index

### Classes

- [Blob](https://firebase.google.com/docs/reference/node/firebase.firestore.Blob)
- [CollectionReference](https://firebase.google.com/docs/reference/node/firebase.firestore.CollectionReference)
- [DocumentReference](https://firebase.google.com/docs/reference/node/firebase.firestore.DocumentReference)
- [DocumentSnapshot](https://firebase.google.com/docs/reference/node/firebase.firestore.DocumentSnapshot)
- [FieldPath](https://firebase.google.com/docs/reference/node/firebase.firestore.FieldPath)
- [FieldValue](https://firebase.google.com/docs/reference/node/firebase.firestore.FieldValue)
- [Firestore](https://firebase.google.com/docs/reference/node/firebase.firestore.Firestore)
- [GeoPoint](https://firebase.google.com/docs/reference/node/firebase.firestore.GeoPoint)
- [Query](https://firebase.google.com/docs/reference/node/firebase.firestore.Query)
- [QueryDocumentSnapshot](https://firebase.google.com/docs/reference/node/firebase.firestore.QueryDocumentSnapshot)
- [QuerySnapshot](https://firebase.google.com/docs/reference/node/firebase.firestore.QuerySnapshot)
- [Timestamp](https://firebase.google.com/docs/reference/node/firebase.firestore.Timestamp)
- [Transaction](https://firebase.google.com/docs/reference/node/firebase.firestore.Transaction)
- [WriteBatch](https://firebase.google.com/docs/reference/node/firebase.firestore.WriteBatch)

### Interfaces

- [DocumentChange](https://firebase.google.com/docs/reference/node/firebase.firestore.DocumentChange)
- [FirestoreDataConverter](https://firebase.google.com/docs/reference/node/firebase.firestore.FirestoreDataConverter)
- [FirestoreError](https://firebase.google.com/docs/reference/node/firebase.firestore.FirestoreError)
- [GetOptions](https://firebase.google.com/docs/reference/node/firebase.firestore.GetOptions)
- [LoadBundleTask](https://firebase.google.com/docs/reference/node/firebase.firestore.LoadBundleTask)
- [LoadBundleTaskProgress](https://firebase.google.com/docs/reference/node/firebase.firestore.LoadBundleTaskProgress)
- [PersistenceSettings](https://firebase.google.com/docs/reference/node/firebase.firestore.PersistenceSettings)
- [SetOptions](https://firebase.google.com/docs/reference/node/firebase.firestore.SetOptions)
- [Settings](https://firebase.google.com/docs/reference/node/firebase.firestore.Settings)
- [SnapshotListenOptions](https://firebase.google.com/docs/reference/node/firebase.firestore.SnapshotListenOptions)
- [SnapshotMetadata](https://firebase.google.com/docs/reference/node/firebase.firestore.SnapshotMetadata)
- [SnapshotOptions](https://firebase.google.com/docs/reference/node/firebase.firestore.SnapshotOptions)

### Type aliases

- [DocumentChangeType](https://firebase.google.com/docs/reference/node/firebase.firestore#documentchangetype)
- [DocumentData](https://firebase.google.com/docs/reference/node/firebase.firestore#documentdata)
- [EmulatorMockTokenOptions](https://firebase.google.com/docs/reference/node/firebase.firestore#emulatormocktokenoptions)
- [FirestoreErrorCode](https://firebase.google.com/docs/reference/node/firebase.firestore#firestoreerrorcode)
- [LogLevel](https://firebase.google.com/docs/reference/node/firebase.firestore#loglevel)
- [OrderByDirection](https://firebase.google.com/docs/reference/node/firebase.firestore#orderbydirection)
- [TaskState](https://firebase.google.com/docs/reference/node/firebase.firestore#taskstate)
- [UpdateData](https://firebase.google.com/docs/reference/node/firebase.firestore#updatedata)
- [WhereFilterOp](https://firebase.google.com/docs/reference/node/firebase.firestore#wherefilterop)

### Variables

- [CACHE_SIZE_UNLIMITED](https://firebase.google.com/docs/reference/node/firebase.firestore#cache_size_unlimited)

### Functions

- [setLogLevel](https://firebase.google.com/docs/reference/node/firebase.firestore#setloglevel)

## Type aliases

### DocumentChangeType

DocumentChangeType: "added" \| "removed" \| "modified"  
The type of a `DocumentChange` may be 'added', 'removed', or 'modified'.

### DocumentData

DocumentData: {}  
Document data (for use with `DocumentReference.set()`) consists of fields
mapped to values.  

#### Type declaration

-

  ##### \[field: string\]: any

### EmulatorMockTokenOptions

EmulatorMockTokenOptions: [EmulatorMockTokenOptions](https://firebase.google.com/docs/reference/node/firebase#emulatormocktokenoptions)

### FirestoreErrorCode

FirestoreErrorCode: "cancelled" \| "unknown" \| "invalid-argument" \| "deadline-exceeded" \| "not-found" \| "already-exists" \| "permission-denied" \| "resource-exhausted" \| "failed-precondition" \| "aborted" \| "out-of-range" \| "unimplemented" \| "internal" \| "unavailable" \| "data-loss" \| "unauthenticated"  
The set of Firestore status codes. The codes are the same at the ones
exposed by gRPC here:
<https://github.com/grpc/grpc/blob/master/doc/statuscodes.md>

Possible values:

- 'cancelled': The operation was cancelled (typically by the caller).
- 'unknown': Unknown error or an error from a different error domain.
- 'invalid-argument': Client specified an invalid argument. Note that this differs from 'failed-precondition'. 'invalid-argument' indicates arguments that are problematic regardless of the state of the system (e.g. an invalid field name).
- 'deadline-exceeded': Deadline expired before operation could complete. For operations that change the state of the system, this error may be returned even if the operation has completed successfully. For example, a successful response from a server could have been delayed long enough for the deadline to expire.
- 'not-found': Some requested document was not found.
- 'already-exists': Some document that we attempted to create already exists.
- 'permission-denied': The caller does not have permission to execute the specified operation.
- 'resource-exhausted': Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system is out of space.
- 'failed-precondition': Operation was rejected because the system is not in a state required for the operation's execution.
- 'aborted': The operation was aborted, typically due to a concurrency issue like transaction aborts, etc.
- 'out-of-range': Operation was attempted past the valid range.
- 'unimplemented': Operation is not implemented or not supported/enabled.
- 'internal': Internal errors. Means some invariants expected by underlying system has been broken. If you see one of these errors, something is very broken.
- 'unavailable': The service is currently unavailable. This is most likely a transient condition and may be corrected by retrying with a backoff.
- 'data-loss': Unrecoverable data loss or corruption.
- 'unauthenticated': The request does not have valid authentication credentials for the operation.

### LogLevel

LogLevel: "debug" \| "error" \| "silent"

### OrderByDirection

OrderByDirection: "desc" \| "asc"  
The direction of a `Query.orderBy()` clause is specified as 'desc' or 'asc'
(descending or ascending).

### TaskState

TaskState: "Error" \| "Running" \| "Success"  
Represents the state of bundle loading tasks.

Both 'Error' and 'Success' are sinking state: task will abort or complete and there will
be no more updates after they are reported.

### UpdateData

UpdateData: {}  
Update data (for use with `DocumentReference.update()`) consists of field
paths (e.g. 'foo' or 'foo.baz') mapped to values. Fields that contain dots
reference nested fields within the document.  

#### Type declaration

-

  ##### \[fieldPath: string\]: any

### WhereFilterOp

WhereFilterOp: "\<" \| "\<=" \| "==" \| "!=" \| "\>=" \| "\>" \| "array-contains" \| "in" \| "array-contains-any" \| "not-in"  
Filter conditions in a `Query.where()` clause are specified using the
strings '\<', '\<=', '==', '!=', '\>=', '\>', 'array-contains', 'in',
'array-contains-any', and 'not-in'.

## Variables

### Const CACHE_SIZE_UNLIMITED

CACHE_SIZE_UNLIMITED: number  
Constant used to indicate the LRU garbage collection should be disabled.
Set this value as the `cacheSizeBytes` on the settings passed to the
`Firestore` instance.

## Functions

### setLogLevel

- setLogLevel ( logLevel : [LogLevel](https://firebase.google.com/docs/reference/node/firebase.firestore#loglevel) ) : void
- Sets the verbosity of Cloud Firestore logs (debug, error, or silent).

  #### Parameters

  -

    ##### logLevel: [LogLevel](https://firebase.google.com/docs/reference/node/firebase.firestore#loglevel)

    The verbosity you set for activity and error logging. Can be any of
    the following values:
    - `debug` for the most verbose logging level, primarily for debugging.
    - `error` to log errors only.
    - `silent` to turn off logging.

  #### Returns void