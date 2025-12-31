# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.DocumentReference.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference.md.txt

# DocumentReference | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [firestore](https://firebase.google.com/docs/reference/js/v8/firebase.firestore).
- DocumentReference
\< T \>

A `DocumentReference` refers to a document location in a Firestore database
and can be used to write, read, or listen to the location. The document at
the referenced location may or may not exist. A `DocumentReference` can
also be used to create a `CollectionReference` to a subcollection.

### Type parameters

-

  #### T

## Index

### Constructors

- [constructor](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference#constructor)

### Properties

- [firestore](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference#firestore)
- [id](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference#id)
- [parent](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference#parent)
- [path](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference#path)

### Methods

- [collection](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference#collection)
- [delete](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference#delete)
- [get](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference#get)
- [isEqual](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference#isequal)
- [onSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference#onsnapshot)
- [set](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference#set)
- [update](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference#update)
- [withConverter](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference#withconverter)

## Constructors

### Private constructor

- new DocumentReference ( ) : [DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference)
-

  #### Returns [DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference)

## Properties

### firestore

firestore: [Firestore](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Firestore)  
The [firebase.firestore.Firestore](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Firestore) the document is in.
This is useful for performing transactions, for example.

### id

id: string  
The document's identifier within its collection.

### parent

parent: [CollectionReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.CollectionReference)\<T\>  
The Collection this `DocumentReference` belongs to.

### path

path: string  
A string representing the path of the referenced document (relative
to the root of the database).

## Methods

### collection

- collection ( collectionPath : string ) : [CollectionReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.CollectionReference) \< [DocumentData](https://firebase.google.com/docs/reference/js/v8/firebase.firestore#documentdata) \>
- Gets a `CollectionReference` instance that refers to the collection at
  the specified path.

  #### Parameters

  -

    ##### collectionPath: string

    A slash-separated path to a collection.

  #### Returns [CollectionReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.CollectionReference)\<[DocumentData](https://firebase.google.com/docs/reference/js/v8/firebase.firestore#documentdata)\>

  The `CollectionReference` instance.

### delete

- delete ( ) : Promise \< void \>
- Deletes the document referred to by this `DocumentReference`.

  #### Returns Promise\<void\>

  A Promise resolved once the document has been successfully
  deleted from the backend (Note that it won't resolve while you're
  offline).

### get

- get ( options ? : [GetOptions](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.GetOptions) ) : Promise \< [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot) \< T \> \>
- Reads the document referred to by this `DocumentReference`.

  Note: By default, get() attempts to provide up-to-date data when possible
  by waiting for data from the server, but it may return cached data or fail
  if you are offline and the server cannot be reached. This behavior can be
  altered via the `GetOptions` parameter.

  #### Parameters

  -

    ##### Optional options: [GetOptions](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.GetOptions)

    An object to configure the get behavior.

  #### Returns Promise\<[DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot)\<T\>\>

  A Promise resolved with a DocumentSnapshot containing the
  current document contents.

### isEqual

- isEqual ( other : [DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference) \< T \> ) : boolean
- Returns true if this `DocumentReference` is equal to the provided one.

  #### Parameters

  -

    ##### other: [DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference)\<T\>

    The `DocumentReference` to compare against.

  #### Returns boolean

  true if this `DocumentReference` is equal to the provided one.

### onSnapshot

- onSnapshot ( observer : { complete ?: ( ) =\> void ; error ?: ( error : [FirestoreError](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreError) ) =\> void ; next ?: ( snapshot : [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot) \< T \> ) =\> void } ) : ( ) =\> void
- Attaches a listener for DocumentSnapshot events. You may either pass
  individual `onNext` and `onError` callbacks or pass a single observer
  object with `next` and `error` callbacks.

  NOTE: Although an `onCompletion` callback can be provided, it will
  never be called because the snapshot stream is never-ending.

  #### Parameters

  -

    ##### observer: { complete?: () =\> void; error?: (error: [FirestoreError](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreError)) =\> void; next?: (snapshot: [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot)\<T\>) =\> void }

    A single object containing `next` and `error` callbacks.
    -

      ##### Optional complete?: () =\> void

      -
        - (): void

        <!-- -->

        -

          #### Returns void

    -

      ##### Optional error?: (error: [FirestoreError](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreError)) =\> void

      -
        - (error: [FirestoreError](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreError)): void

        <!-- -->

        -

          #### Parameters

          -

            ##### error: [FirestoreError](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreError)

          #### Returns void

    -

      ##### Optional next?: (snapshot: [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot)\<T\>) =\> void

      -
        - (snapshot: [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot)\<T\>): void

        <!-- -->

        -

          #### Parameters

          -

            ##### snapshot: [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot)\<T\>

          #### Returns void

  #### Returns () =\> void

  An unsubscribe function that can be called to cancel
  the snapshot listener.
  -
    - (): void

    <!-- -->

    -

      #### Returns void

- onSnapshot ( options : [SnapshotListenOptions](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SnapshotListenOptions) , observer : { complete ?: ( ) =\> void ; error ?: ( error : [FirestoreError](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreError) ) =\> void ; next ?: ( snapshot : [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot) \< T \> ) =\> void } ) : ( ) =\> void
- Attaches a listener for DocumentSnapshot events. You may either pass
  individual `onNext` and `onError` callbacks or pass a single observer
  object with `next` and `error` callbacks.

  NOTE: Although an `onCompletion` callback can be provided, it will
  never be called because the snapshot stream is never-ending.

  #### Parameters

  -

    ##### options: [SnapshotListenOptions](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SnapshotListenOptions)

    Options controlling the listen behavior.
  -

    ##### observer: { complete?: () =\> void; error?: (error: [FirestoreError](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreError)) =\> void; next?: (snapshot: [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot)\<T\>) =\> void }

    A single object containing `next` and `error` callbacks.
    -

      ##### Optional complete?: () =\> void

      -
        - (): void

        <!-- -->

        -

          #### Returns void

    -

      ##### Optional error?: (error: [FirestoreError](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreError)) =\> void

      -
        - (error: [FirestoreError](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreError)): void

        <!-- -->

        -

          #### Parameters

          -

            ##### error: [FirestoreError](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreError)

          #### Returns void

    -

      ##### Optional next?: (snapshot: [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot)\<T\>) =\> void

      -
        - (snapshot: [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot)\<T\>): void

        <!-- -->

        -

          #### Parameters

          -

            ##### snapshot: [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot)\<T\>

          #### Returns void

  #### Returns () =\> void

  An unsubscribe function that can be called to cancel
  the snapshot listener.
  -
    - (): void

    <!-- -->

    -

      #### Returns void

- onSnapshot ( onNext : ( snapshot : [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot) \< T \> ) =\> void , onError ? : ( error : [FirestoreError](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreError) ) =\> void , onCompletion ? : ( ) =\> void ) : ( ) =\> void
- Attaches a listener for DocumentSnapshot events. You may either pass
  individual `onNext` and `onError` callbacks or pass a single observer
  object with `next` and `error` callbacks.

  NOTE: Although an `onCompletion` callback can be provided, it will
  never be called because the snapshot stream is never-ending.

  #### Parameters

  -

    ##### onNext: (snapshot: [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot)\<T\>) =\> void

    A callback to be called every time a new `DocumentSnapshot`
    is available.
    -
      - (snapshot: [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot)\<T\>): void

      <!-- -->

      -

        #### Parameters

        -

          ##### snapshot: [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot)\<T\>

        #### Returns void

  -

    ##### Optional onError: (error: [FirestoreError](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreError)) =\> void

    A callback to be called if the listen fails or is
    cancelled. No further callbacks will occur.
    -
      - (error: [FirestoreError](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreError)): void

      <!-- -->

      -

        #### Parameters

        -

          ##### error: [FirestoreError](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreError)

        #### Returns void

  -

    ##### Optional onCompletion: () =\> void

    -
      - (): void

      <!-- -->

      -

        #### Returns void

  #### Returns () =\> void

  An unsubscribe function that can be called to cancel
  the snapshot listener.
  -
    - (): void

    <!-- -->

    -

      #### Returns void

- onSnapshot ( options : [SnapshotListenOptions](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SnapshotListenOptions) , onNext : ( snapshot : [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot) \< T \> ) =\> void , onError ? : ( error : [FirestoreError](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreError) ) =\> void , onCompletion ? : ( ) =\> void ) : ( ) =\> void
- Attaches a listener for DocumentSnapshot events. You may either pass
  individual `onNext` and `onError` callbacks or pass a single observer
  object with `next` and `error` callbacks.

  NOTE: Although an `onCompletion` callback can be provided, it will
  never be called because the snapshot stream is never-ending.

  #### Parameters

  -

    ##### options: [SnapshotListenOptions](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SnapshotListenOptions)

    Options controlling the listen behavior.
  -

    ##### onNext: (snapshot: [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot)\<T\>) =\> void

    A callback to be called every time a new `DocumentSnapshot`
    is available.
    -
      - (snapshot: [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot)\<T\>): void

      <!-- -->

      -

        #### Parameters

        -

          ##### snapshot: [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot)\<T\>

        #### Returns void

  -

    ##### Optional onError: (error: [FirestoreError](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreError)) =\> void

    A callback to be called if the listen fails or is
    cancelled. No further callbacks will occur.
    -
      - (error: [FirestoreError](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreError)): void

      <!-- -->

      -

        #### Parameters

        -

          ##### error: [FirestoreError](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreError)

        #### Returns void

  -

    ##### Optional onCompletion: () =\> void

    -
      - (): void

      <!-- -->

      -

        #### Returns void

  #### Returns () =\> void

  An unsubscribe function that can be called to cancel
  the snapshot listener.
  -
    - (): void

    <!-- -->

    -

      #### Returns void

### set

- set ( data : Partial \< T \> , options : [SetOptions](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SetOptions) ) : Promise \< void \>
- Writes to the document referred to by this `DocumentReference`. If the
  document does not yet exist, it will be created. If you pass
  `SetOptions`, the provided data can be merged into an existing document.

  #### Parameters

  -

    ##### data: Partial\<T\>

    A map of the fields and values for the document.
  -

    ##### options: [SetOptions](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SetOptions)

    An object to configure the set behavior.

  #### Returns Promise\<void\>

  A Promise resolved once the data has been successfully written
  to the backend (Note that it won't resolve while you're offline).
- set ( data : T ) : Promise \< void \>
- Writes to the document referred to by this `DocumentReference`. If the
  document does not yet exist, it will be created. If you pass
  `SetOptions`, the provided data can be merged into an existing document.

  #### Parameters

  -

    ##### data: T

    A map of the fields and values for the document.

  #### Returns Promise\<void\>

  A Promise resolved once the data has been successfully written
  to the backend (Note that it won't resolve while you're offline).

### update

- update ( data : [UpdateData](https://firebase.google.com/docs/reference/js/v8/firebase.firestore#updatedata) ) : Promise \< void \>
- Updates fields in the document referred to by this `DocumentReference`.
  The update will fail if applied to a document that does not exist.

  #### Parameters

  -

    ##### data: [UpdateData](https://firebase.google.com/docs/reference/js/v8/firebase.firestore#updatedata)

    An object containing the fields and values with which to
    update the document. Fields can contain dots to reference nested fields
    within the document.

  #### Returns Promise\<void\>

  A Promise resolved once the data has been successfully written
  to the backend (Note that it won't resolve while you're offline).
- update ( field : string \| [FieldPath](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldPath) , value : any , ... moreFieldsAndValues : any \[\] ) : Promise \< void \>
- Updates fields in the document referred to by this `DocumentReference`.
  The update will fail if applied to a document that does not exist.

  Nested fields can be updated by providing dot-separated field path
  strings or by providing FieldPath objects.

  #### Parameters

  -

    ##### field: string \| [FieldPath](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldPath)

    The first field to update.
  -

    ##### value: any

    The first value.
  -

    ##### Rest ...moreFieldsAndValues: any\[\]

    Additional key value pairs.

  #### Returns Promise\<void\>

  A Promise resolved once the data has been successfully written
  to the backend (Note that it won't resolve while you're offline).

### withConverter

- withConverter ( converter : null ) : [DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference) \< [DocumentData](https://firebase.google.com/docs/reference/js/v8/firebase.firestore#documentdata) \>
- Applies a custom data converter to this DocumentReference, allowing you
  to use your own custom model objects with Firestore. When you call
  set(), get(), etc. on the returned DocumentReference instance, the
  provided converter will convert between Firestore data and your custom
  type U.

  Passing in `null` as the converter parameter removes the current
  converter.

  #### Parameters

  -

    ##### converter: null

    Converts objects to and from Firestore. Passing in
    `null` removes the current converter.

  #### Returns [DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference)\<[DocumentData](https://firebase.google.com/docs/reference/js/v8/firebase.firestore#documentdata)\>

  A DocumentReferencethat uses the provided converter.
- withConverter \< U \> ( converter : [FirestoreDataConverter](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreDataConverter) \< U \> ) : [DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference) \< U \>
- Applies a custom data converter to this DocumentReference, allowing you
to use your own custom model objects with Firestore. When you call
set(), get(), etc. on the returned DocumentReference instance, the
provided converter will convert between Firestore data and your custom
type U.
Passing in `null` as the converter parameter removes the current
converter.
#### Type parameters
-
#### U
#### Parameters
-
##### converter: [FirestoreDataConverter](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreDataConverter)\<U\>
Converts objects to and from Firestore. Passing in
`null` removes the current converter.
#### Returns [DocumentReference](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentReference)\<U\>
A DocumentReferencethat uses the provided converter.