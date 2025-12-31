# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.QuerySnapshot.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot.md.txt

# QuerySnapshot | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [firestore](https://firebase.google.com/docs/reference/js/v8/firebase.firestore).
- QuerySnapshot
\< T \>

A `QuerySnapshot` contains zero or more `DocumentSnapshot` objects
representing the results of a query. The documents can be accessed as an
array via the `docs` property or enumerated using the `forEach` method. The
number of documents can be determined via the `empty` and `size`
properties.

### Type parameters

-

  #### T

## Index

### Constructors

- [constructor](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot#constructor)

### Properties

- [docs](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot#docs)
- [empty](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot#empty)
- [metadata](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot#metadata)
- [query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot#query)
- [size](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot#size)

### Methods

- [docChanges](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot#docchanges)
- [forEach](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot#foreach)
- [isEqual](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot#isequal)

## Constructors

### Private constructor

- new QuerySnapshot ( ) : [QuerySnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot)
-

  #### Returns [QuerySnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot)

## Properties

### docs

docs: Array\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QueryDocumentSnapshot)\<T\>\>  
An array of all the documents in the `QuerySnapshot`.

### empty

empty: boolean  
True if there are no documents in the `QuerySnapshot`.

### metadata

metadata: [SnapshotMetadata](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SnapshotMetadata)  
Metadata about this snapshot, concerning its source and if it has local
modifications.

### query

query: [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query)\<T\>  
The query on which you called `get` or `onSnapshot` in order to get this
`QuerySnapshot`.

### size

size: number  
The number of documents in the `QuerySnapshot`.

## Methods

### docChanges

- docChanges ( options ? : [SnapshotListenOptions](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SnapshotListenOptions) ) : Array \< [DocumentChange](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentChange) \< T \> \>
- Returns an array of the documents changes since the last snapshot. If this
  is the first snapshot, all documents will be in the list as added changes.

  #### Parameters

  -

    ##### Optional options: [SnapshotListenOptions](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SnapshotListenOptions)

    `SnapshotListenOptions` that control whether metadata-only
    changes (i.e. only `DocumentSnapshot.metadata` changed) should trigger
    snapshot events.

  #### Returns Array\<[DocumentChange](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentChange)\<T\>\>

### forEach

- forEach ( callback : ( result : [QueryDocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QueryDocumentSnapshot) \< T \> ) =\> void , thisArg ? : any ) : void
- Enumerates all of the documents in the `QuerySnapshot`.

  #### Parameters

  -

    ##### callback: (result: [QueryDocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QueryDocumentSnapshot)\<T\>) =\> void

    A callback to be called with a `QueryDocumentSnapshot` for
    each document in the snapshot.
    -
      - (result: [QueryDocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QueryDocumentSnapshot)\<T\>): void

      <!-- -->

      -

        #### Parameters

        -

          ##### result: [QueryDocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QueryDocumentSnapshot)\<T\>

        #### Returns void

  -

    ##### Optional thisArg: any

    The `this` binding for the callback.

  #### Returns void

### isEqual

- isEqual ( other : [QuerySnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot) \< T \> ) : boolean
- Returns true if this `QuerySnapshot` is equal to the provided one.

  #### Parameters

  -

    ##### other: [QuerySnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot)\<T\>

    The `QuerySnapshot` to compare against.

  #### Returns boolean

true if this `QuerySnapshot` is equal to the provided one.