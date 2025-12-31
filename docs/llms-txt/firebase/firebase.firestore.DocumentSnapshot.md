# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.DocumentSnapshot.md.txt

# DocumentSnapshot | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/node/firebase).
- [firestore](https://firebase.google.com/docs/reference/node/firebase.firestore).
- DocumentSnapshot
\< T \>

A `DocumentSnapshot` contains data read from a document in your Firestore
database. The data can be extracted with `.data()` or `.get(<field>)` to
get a specific field.

For a `DocumentSnapshot` that points to a non-existing document, any data
access will return 'undefined'. You can use the `exists` property to
explicitly verify a document's existence.

### Type parameters

-

  #### T

## Index

### Constructors

- [constructor](https://firebase.google.com/docs/reference/node/firebase.firestore.DocumentSnapshot#constructor)

### Properties

- [exists](https://firebase.google.com/docs/reference/node/firebase.firestore.DocumentSnapshot#exists)
- [id](https://firebase.google.com/docs/reference/node/firebase.firestore.DocumentSnapshot#id)
- [metadata](https://firebase.google.com/docs/reference/node/firebase.firestore.DocumentSnapshot#metadata)
- [ref](https://firebase.google.com/docs/reference/node/firebase.firestore.DocumentSnapshot#ref)

### Methods

- [data](https://firebase.google.com/docs/reference/node/firebase.firestore.DocumentSnapshot#data)
- [get](https://firebase.google.com/docs/reference/node/firebase.firestore.DocumentSnapshot#get)
- [isEqual](https://firebase.google.com/docs/reference/node/firebase.firestore.DocumentSnapshot#isequal)

## Constructors

### Protected constructor

- new DocumentSnapshot ( ) : [DocumentSnapshot](https://firebase.google.com/docs/reference/node/firebase.firestore.DocumentSnapshot)
-

  #### Returns [DocumentSnapshot](https://firebase.google.com/docs/reference/node/firebase.firestore.DocumentSnapshot)

## Properties

### exists

exists: boolean  
Property of the `DocumentSnapshot` that signals whether or not the data
exists. True if the document exists.

### id

id: string  
Property of the `DocumentSnapshot` that provides the document's ID.

### metadata

metadata: [SnapshotMetadata](https://firebase.google.com/docs/reference/node/firebase.firestore.SnapshotMetadata)  
Metadata about the `DocumentSnapshot`, including information about its
source and local modifications.

### ref

ref: [DocumentReference](https://firebase.google.com/docs/reference/node/firebase.firestore.DocumentReference)\<T\>  
The `DocumentReference` for the document included in the `DocumentSnapshot`.

## Methods

### data

- data ( options ? : [SnapshotOptions](https://firebase.google.com/docs/reference/node/firebase.firestore.SnapshotOptions) ) : T \| undefined
- Retrieves all fields in the document as an Object. Returns 'undefined' if
  the document doesn't exist.

  By default, `FieldValue.serverTimestamp()` values that have not yet been
  set to their final value will be returned as `null`. You can override
  this by passing an options object.

  #### Parameters

  -

    ##### Optional options: [SnapshotOptions](https://firebase.google.com/docs/reference/node/firebase.firestore.SnapshotOptions)

    An options object to configure how data is retrieved from
    the snapshot (e.g. the desired behavior for server timestamps that have
    not yet been set to their final value).

  #### Returns T \| undefined

  An Object containing all fields in the document or 'undefined' if
  the document doesn't exist.

### get

- get ( fieldPath : string \| [FieldPath](https://firebase.google.com/docs/reference/node/firebase.firestore.FieldPath) , options ? : [SnapshotOptions](https://firebase.google.com/docs/reference/node/firebase.firestore.SnapshotOptions) ) : any
- Retrieves the field specified by `fieldPath`. Returns `undefined` if the
  document or field doesn't exist.

  By default, a `FieldValue.serverTimestamp()` that has not yet been set to
  its final value will be returned as `null`. You can override this by
  passing an options object.

  #### Parameters

  -

    ##### fieldPath: string \| [FieldPath](https://firebase.google.com/docs/reference/node/firebase.firestore.FieldPath)

    The path (e.g. 'foo' or 'foo.bar') to a specific field.
  -

    ##### Optional options: [SnapshotOptions](https://firebase.google.com/docs/reference/node/firebase.firestore.SnapshotOptions)

    An options object to configure how the field is retrieved
    from the snapshot (e.g. the desired behavior for server timestamps that have
    not yet been set to their final value).

  #### Returns any

  The data at the specified field location or undefined if no such
  field exists in the document.

### isEqual

- isEqual ( other : [DocumentSnapshot](https://firebase.google.com/docs/reference/node/firebase.firestore.DocumentSnapshot) \< T \> ) : boolean
- Returns true if this `DocumentSnapshot` is equal to the provided one.

  #### Parameters

  -

    ##### other: [DocumentSnapshot](https://firebase.google.com/docs/reference/node/firebase.firestore.DocumentSnapshot)\<T\>

    The `DocumentSnapshot` to compare against.

  #### Returns boolean

true if this `DocumentSnapshot` is equal to the provided one.