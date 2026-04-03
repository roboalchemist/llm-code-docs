# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.WriteBatch.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.WriteBatch.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.WriteBatch.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.WriteBatch.md.txt

# WriteBatch | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [firestore](https://firebase.google.com/docs/reference/js/v8/firebase.firestore).
- WriteBatch

A write batch, used to perform multiple writes as a single atomic unit.

A `WriteBatch` object can be acquired by calling `Firestore.batch()`. It
provides methods for adding writes to the write batch. None of the
writes will be committed (or visible locally) until `WriteBatch.commit()`
is called.

Unlike transactions, write batches are persisted offline and therefore are
preferable when you don't need to condition your writes on read data.

## Index

### Constructors

- [constructor](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.WriteBatch#constructor)

### Methods

- [commit](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.WriteBatch#commit)
- [delete](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.WriteBatch#delete)
- [set](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.WriteBatch#set)
- [update](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.WriteBatch#update)

## Constructors

### Private constructor

- new WriteBatch ( ) : [WriteBatch](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.WriteBatch)
-

  #### Returns [WriteBatch](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.WriteBatch)

## Methods

### commit

- commit ( ) : Promise \< void \>
- Commits all of the writes in this write batch as a single atomic unit.

  #### Returns Promise\<void\>

  A Promise resolved once all of the writes in the batch have been
  successfully written to the backend as an atomic unit. Note that it won't
  resolve while you're offline.

### delete

- delete ( documentRef : [DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference) \< any \> ) : [WriteBatch](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.WriteBatch)
- Deletes the document referred to by the provided `DocumentReference`.

  #### Parameters

  -

    ##### documentRef: [DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference)\<any\>

    A reference to the document to be deleted.

  #### Returns [WriteBatch](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.WriteBatch)

  This `WriteBatch` instance. Used for chaining method calls.

### set

- set \< T \> ( documentRef : [DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference) \< T \> , data : Partial \< T \> , options : [SetOptions](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SetOptions) ) : [WriteBatch](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.WriteBatch)
- Writes to the document referred to by the provided `DocumentReference`.
  If the document does not exist yet, it will be created. If you pass
  `SetOptions`, the provided data can be merged into the existing document.

  #### Type parameters

  -

    #### T

  #### Parameters

  -

    ##### documentRef: [DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference)\<T\>

    A reference to the document to be set.
  -

    ##### data: Partial\<T\>

    An object of the fields and values for the document.
  -

    ##### options: [SetOptions](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SetOptions)

    An object to configure the set behavior.

  #### Returns [WriteBatch](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.WriteBatch)

  This `WriteBatch` instance. Used for chaining method calls.
- set \< T \> ( documentRef : [DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference) \< T \> , data : T ) : [WriteBatch](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.WriteBatch)
- Writes to the document referred to by the provided `DocumentReference`.
  If the document does not exist yet, it will be created. If you pass
  `SetOptions`, the provided data can be merged into the existing document.

  #### Type parameters

  -

    #### T

  #### Parameters

  -

    ##### documentRef: [DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference)\<T\>

    A reference to the document to be set.
  -

    ##### data: T

    An object of the fields and values for the document.

  #### Returns [WriteBatch](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.WriteBatch)

  This `WriteBatch` instance. Used for chaining method calls.

### update

- update ( documentRef : [DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference) \< any \> , data : [UpdateData](https://firebase.google.com/docs/reference/js/v8/firebase.firestore#updatedata) ) : [WriteBatch](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.WriteBatch)
- Updates fields in the document referred to by the provided
  `DocumentReference`. The update will fail if applied to a document that
  does not exist.

  #### Parameters

  -

    ##### documentRef: [DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference)\<any\>

    A reference to the document to be updated.
  -

    ##### data: [UpdateData](https://firebase.google.com/docs/reference/js/v8/firebase.firestore#updatedata)

    An object containing the fields and values with which to
    update the document. Fields can contain dots to reference nested fields
    within the document.

  #### Returns [WriteBatch](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.WriteBatch)

  This `WriteBatch` instance. Used for chaining method calls.
- update ( documentRef : [DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference) \< any \> , field : string \| [FieldPath](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldPath) , value : any , ... moreFieldsAndValues : any \[\] ) : [WriteBatch](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.WriteBatch)
- Updates fields in the document referred to by this `DocumentReference`.
  The update will fail if applied to a document that does not exist.

  Nested fields can be update by providing dot-separated field path strings
  or by providing FieldPath objects.

  #### Parameters

  -

    ##### documentRef: [DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference)\<any\>

    A reference to the document to be updated.
  -

    ##### field: string \| [FieldPath](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldPath)

    The first field to update.
  -

    ##### value: any

    The first value.
  -

    ##### Rest ...moreFieldsAndValues: any\[\]

    Additional key value pairs.

  #### Returns [WriteBatch](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.WriteBatch)

  A Promise resolved once the data has been successfully written
to the backend (Note that it won't resolve while you're offline).