# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.Transaction.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Transaction.md.txt

# Transaction | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [firestore](https://firebase.google.com/docs/reference/js/v8/firebase.firestore).
- Transaction

A reference to a transaction.
The `Transaction` object passed to a transaction's updateFunction provides
the methods to read and write data within the transaction context. See
`Firestore.runTransaction()`.

## Index

### Constructors

- [constructor](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Transaction#constructor)

### Methods

- [delete](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Transaction#delete)
- [get](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Transaction#get)
- [set](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Transaction#set)
- [update](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Transaction#update)

## Constructors

### Private constructor

- new Transaction ( ) : [Transaction](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Transaction)
-

  #### Returns [Transaction](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Transaction)

## Methods

### delete

- delete ( documentRef : [DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference) \< any \> ) : [Transaction](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Transaction)
- Deletes the document referred to by the provided `DocumentReference`.

  #### Parameters

  -

    ##### documentRef: [DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference)\<any\>

    A reference to the document to be deleted.

  #### Returns [Transaction](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Transaction)

  This `Transaction` instance. Used for chaining method calls.

### get

- get \< T \> ( documentRef : [DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference) \< T \> ) : Promise \< [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot) \< T \> \>
- Reads the document referenced by the provided `DocumentReference.`

  #### Type parameters

  -

    #### T

  #### Parameters

  -

    ##### documentRef: [DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference)\<T\>

    A reference to the document to be read.

  #### Returns Promise\<[DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot)\<T\>\>

  A DocumentSnapshot for the read data.

### set

- set \< T \> ( documentRef : [DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference) \< T \> , data : Partial \< T \> , options : [SetOptions](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SetOptions) ) : [Transaction](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Transaction)
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

  #### Returns [Transaction](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Transaction)

  This `Transaction` instance. Used for chaining method calls.
- set \< T \> ( documentRef : [DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference) \< T \> , data : T ) : [Transaction](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Transaction)
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

  #### Returns [Transaction](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Transaction)

  This `Transaction` instance. Used for chaining method calls.

### update

- update ( documentRef : [DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference) \< any \> , data : [UpdateData](https://firebase.google.com/docs/reference/js/v8/firebase.firestore#updatedata) ) : [Transaction](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Transaction)
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

  #### Returns [Transaction](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Transaction)

  This `Transaction` instance. Used for chaining method calls.
- update ( documentRef : [DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference) \< any \> , field : string \| [FieldPath](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldPath) , value : any , ... moreFieldsAndValues : any \[\] ) : [Transaction](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Transaction)
- Updates fields in the document referred to by the provided
  `DocumentReference`. The update will fail if applied to a document that
  does not exist.

  Nested fields can be updated by providing dot-separated field path
  strings or by providing FieldPath objects.

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

    Additional key/value pairs.

  #### Returns [Transaction](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Transaction)

  A Promise resolved once the data has been successfully written
to the backend (Note that it won't resolve while you're offline).