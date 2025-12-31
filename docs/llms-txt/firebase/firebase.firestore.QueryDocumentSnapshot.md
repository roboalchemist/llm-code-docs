# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.QueryDocumentSnapshot.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QueryDocumentSnapshot.md.txt

# QueryDocumentSnapshot | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [firestore](https://firebase.google.com/docs/reference/js/v8/firebase.firestore).
- QueryDocumentSnapshot
\< T \>

A `QueryDocumentSnapshot` contains data read from a document in your
Firestore database as part of a query. The document is guaranteed to exist
and its data can be extracted with `.data()` or `.get(<field>)` to get a
specific field.

A `QueryDocumentSnapshot` offers the same API surface as a
`DocumentSnapshot`. Since query results contain only existing documents, the
`exists` property will always be true and `data()` will never return
'undefined'.

### Type parameters

-

  #### T

## Index

### Constructors

- [constructor](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QueryDocumentSnapshot#constructor)

### Properties

- [exists](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QueryDocumentSnapshot#exists)
- [id](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QueryDocumentSnapshot#id)
- [metadata](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QueryDocumentSnapshot#metadata)
- [ref](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QueryDocumentSnapshot#ref)

### Methods

- [data](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QueryDocumentSnapshot#data)
- [get](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QueryDocumentSnapshot#get)
- [isEqual](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QueryDocumentSnapshot#isequal)

## Constructors

### Private constructor

- new QueryDocumentSnapshot ( ) : [QueryDocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QueryDocumentSnapshot)
-
  | Overrides [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot).[constructor](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot#constructor)

  #### Returns [QueryDocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QueryDocumentSnapshot)

## Properties

### exists

exists: boolean
Inherited from [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot).[exists](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot#exists)  
Property of the `DocumentSnapshot` that signals whether or not the data
exists. True if the document exists.

### id

id: string
Inherited from [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot).[id](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot#id)  
Property of the `DocumentSnapshot` that provides the document's ID.

### metadata

metadata: [SnapshotMetadata](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SnapshotMetadata)
Inherited from [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot).[metadata](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot#metadata)  
Metadata about the `DocumentSnapshot`, including information about its
source and local modifications.

### ref

ref: [DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference)\<T\>
Inherited from [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot).[ref](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot#ref)  
The `DocumentReference` for the document included in the `DocumentSnapshot`.

## Methods

### data

- data ( options ? : [SnapshotOptions](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SnapshotOptions) ) : T
-
  Overrides [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot).[data](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot#data)  
  Retrieves all fields in the document as an Object.

  By default, `FieldValue.serverTimestamp()` values that have not yet been
  set to their final value will be returned as `null`. You can override
  this by passing an options object.

  override
  :

  #### Parameters

  -

    ##### Optional options: [SnapshotOptions](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SnapshotOptions)

    An options object to configure how data is retrieved from
    the snapshot (e.g. the desired behavior for server timestamps that have
    not yet been set to their final value).

  #### Returns T

  An Object containing all fields in the document.

### get

- get ( fieldPath : string \| [FieldPath](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldPath) , options ? : [SnapshotOptions](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SnapshotOptions) ) : any
-
  Inherited from [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot).[get](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot#get)  
  Retrieves the field specified by `fieldPath`. Returns `undefined` if the
  document or field doesn't exist.

  By default, a `FieldValue.serverTimestamp()` that has not yet been set to
  its final value will be returned as `null`. You can override this by
  passing an options object.

  #### Parameters

  -

    ##### fieldPath: string \| [FieldPath](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldPath)

    The path (e.g. 'foo' or 'foo.bar') to a specific field.
  -

    ##### Optional options: [SnapshotOptions](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SnapshotOptions)

    An options object to configure how the field is retrieved
    from the snapshot (e.g. the desired behavior for server timestamps that have
    not yet been set to their final value).

  #### Returns any

  The data at the specified field location or undefined if no such
  field exists in the document.

### isEqual

- isEqual ( other : [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot) \< T \> ) : boolean
-
  Inherited from [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot).[isEqual](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot#isequal)  
  Returns true if this `DocumentSnapshot` is equal to the provided one.

  #### Parameters

  -

    ##### other: [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot)\<T\>

    The `DocumentSnapshot` to compare against.

  #### Returns boolean

true if this `DocumentSnapshot` is equal to the provided one.