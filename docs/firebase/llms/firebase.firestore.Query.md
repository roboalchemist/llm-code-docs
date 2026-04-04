# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.Query.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query.md.txt

# Query | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [firestore](https://firebase.google.com/docs/reference/js/v8/firebase.firestore).
- Query
\< T \>

A `Query` refers to a Query which you can read or listen to. You can also
construct refined `Query` objects by adding filters and ordering.

### Type parameters

-

  #### T

## Index

### Constructors

- [constructor](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query#constructor)

### Properties

- [firestore](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query#firestore)

### Methods

- [endAt](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query#endat)
- [endBefore](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query#endbefore)
- [get](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query#get)
- [isEqual](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query#isequal)
- [limit](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query#limit)
- [limitToLast](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query#limittolast)
- [onSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query#onsnapshot)
- [orderBy](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query#orderby)
- [startAfter](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query#startafter)
- [startAt](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query#startat)
- [where](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query#where)
- [withConverter](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query#withconverter)

## Constructors

### Protected constructor

- new Query ( ) : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query)
-

  #### Returns [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query)

## Properties

### firestore

firestore: [Firestore](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Firestore)  
The `Firestore` for the Firestore database (useful for performing
transactions, etc.).

## Methods

### endAt

- endAt ( snapshot : [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot) \< any \> ) : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query) \< T \>
- Creates and returns a new Query that ends at the provided document
  (inclusive). The end position is relative to the order of the query. The
  document must contain all of the fields provided in the orderBy of this
  query.

  #### Parameters

  -

    ##### snapshot: [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot)\<any\>

    The snapshot of the document to end at.

  #### Returns [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query)\<T\>

  The created Query.
- endAt ( ... fieldValues : any \[\] ) : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query) \< T \>
- Creates and returns a new Query that ends at the provided fields
  relative to the order of the query. The order of the field values
  must match the order of the order by clauses of the query.

  #### Parameters

  -

    ##### Rest ...fieldValues: any\[\]

    The field values to end this query at, in order
    of the query's order by.

  #### Returns [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query)\<T\>

  The created Query.

### endBefore

- endBefore ( snapshot : [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot) \< any \> ) : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query) \< T \>
- Creates and returns a new Query that ends before the provided document
  (exclusive). The end position is relative to the order of the query. The
  document must contain all of the fields provided in the orderBy of this
  query.

  #### Parameters

  -

    ##### snapshot: [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot)\<any\>

    The snapshot of the document to end before.

  #### Returns [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query)\<T\>

  The created Query.
- endBefore ( ... fieldValues : any \[\] ) : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query) \< T \>
- Creates and returns a new Query that ends before the provided fields
  relative to the order of the query. The order of the field values
  must match the order of the order by clauses of the query.

  #### Parameters

  -

    ##### Rest ...fieldValues: any\[\]

    The field values to end this query before, in order
    of the query's order by.

  #### Returns [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query)\<T\>

  The created Query.

### get

- get ( options ? : [GetOptions](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.GetOptions) ) : Promise \< [QuerySnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot) \< T \> \>
- Executes the query and returns the results as a `QuerySnapshot`.

  Note: By default, get() attempts to provide up-to-date data when possible
  by waiting for data from the server, but it may return cached data or fail
  if you are offline and the server cannot be reached. This behavior can be
  altered via the `GetOptions` parameter.

  #### Parameters

  -

    ##### Optional options: [GetOptions](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.GetOptions)

    An object to configure the get behavior.

  #### Returns Promise\<[QuerySnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot)\<T\>\>

  A Promise that will be resolved with the results of the Query.

### isEqual

- isEqual ( other : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query) \< T \> ) : boolean
- Returns true if this `Query` is equal to the provided one.

  #### Parameters

  -

    ##### other: [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query)\<T\>

    The `Query` to compare against.

  #### Returns boolean

  true if this `Query` is equal to the provided one.

### limit

- limit ( limit : number ) : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query) \< T \>
- Creates and returns a new Query that only returns the first matching
  documents.

  #### Parameters

  -

    ##### limit: number

    The maximum number of items to return.

  #### Returns [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query)\<T\>

  The created Query.

### limitToLast

- limitToLast ( limit : number ) : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query) \< T \>
- Creates and returns a new Query that only returns the last matching
  documents.

  You must specify at least one `orderBy` clause for `limitToLast` queries,
  otherwise an exception will be thrown during execution.

  #### Parameters

  -

    ##### limit: number

    The maximum number of items to return.

  #### Returns [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query)\<T\>

  The created Query.

### onSnapshot

- onSnapshot ( observer : { complete ?: ( ) =\> void ; error ?: ( error : [FirestoreError](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreError) ) =\> void ; next ?: ( snapshot : [QuerySnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot) \< T \> ) =\> void } ) : ( ) =\> void
- Attaches a listener for QuerySnapshot events. You may either pass
  individual `onNext` and `onError` callbacks or pass a single observer
  object with `next` and `error` callbacks. The listener can be cancelled by
  calling the function that is returned when `onSnapshot` is called.

  NOTE: Although an `onCompletion` callback can be provided, it will
  never be called because the snapshot stream is never-ending.

  #### Parameters

  -

    ##### observer: { complete?: () =\> void; error?: (error: [FirestoreError](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreError)) =\> void; next?: (snapshot: [QuerySnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot)\<T\>) =\> void }

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

      ##### Optional next?: (snapshot: [QuerySnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot)\<T\>) =\> void

      -
        - (snapshot: [QuerySnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot)\<T\>): void

        <!-- -->

        -

          #### Parameters

          -

            ##### snapshot: [QuerySnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot)\<T\>

          #### Returns void

  #### Returns () =\> void

  An unsubscribe function that can be called to cancel
  the snapshot listener.
  -
    - (): void

    <!-- -->

    -

      #### Returns void

- onSnapshot ( options : [SnapshotListenOptions](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SnapshotListenOptions) , observer : { complete ?: ( ) =\> void ; error ?: ( error : [FirestoreError](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreError) ) =\> void ; next ?: ( snapshot : [QuerySnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot) \< T \> ) =\> void } ) : ( ) =\> void
- Attaches a listener for QuerySnapshot events. You may either pass
  individual `onNext` and `onError` callbacks or pass a single observer
  object with `next` and `error` callbacks. The listener can be cancelled by
  calling the function that is returned when `onSnapshot` is called.

  NOTE: Although an `onCompletion` callback can be provided, it will
  never be called because the snapshot stream is never-ending.

  #### Parameters

  -

    ##### options: [SnapshotListenOptions](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SnapshotListenOptions)

    Options controlling the listen behavior.
  -

    ##### observer: { complete?: () =\> void; error?: (error: [FirestoreError](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreError)) =\> void; next?: (snapshot: [QuerySnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot)\<T\>) =\> void }

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

      ##### Optional next?: (snapshot: [QuerySnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot)\<T\>) =\> void

      -
        - (snapshot: [QuerySnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot)\<T\>): void

        <!-- -->

        -

          #### Parameters

          -

            ##### snapshot: [QuerySnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot)\<T\>

          #### Returns void

  #### Returns () =\> void

  An unsubscribe function that can be called to cancel
  the snapshot listener.
  -
    - (): void

    <!-- -->

    -

      #### Returns void

- onSnapshot ( onNext : ( snapshot : [QuerySnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot) \< T \> ) =\> void , onError ? : ( error : [FirestoreError](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreError) ) =\> void , onCompletion ? : ( ) =\> void ) : ( ) =\> void
- Attaches a listener for QuerySnapshot events. You may either pass
  individual `onNext` and `onError` callbacks or pass a single observer
  object with `next` and `error` callbacks. The listener can be cancelled by
  calling the function that is returned when `onSnapshot` is called.

  NOTE: Although an `onCompletion` callback can be provided, it will
  never be called because the snapshot stream is never-ending.

  #### Parameters

  -

    ##### onNext: (snapshot: [QuerySnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot)\<T\>) =\> void

    A callback to be called every time a new `QuerySnapshot`
    is available.
    -
      - (snapshot: [QuerySnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot)\<T\>): void

      <!-- -->

      -

        #### Parameters

        -

          ##### snapshot: [QuerySnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot)\<T\>

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

- onSnapshot ( options : [SnapshotListenOptions](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SnapshotListenOptions) , onNext : ( snapshot : [QuerySnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot) \< T \> ) =\> void , onError ? : ( error : [FirestoreError](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreError) ) =\> void , onCompletion ? : ( ) =\> void ) : ( ) =\> void
- Attaches a listener for QuerySnapshot events. You may either pass
  individual `onNext` and `onError` callbacks or pass a single observer
  object with `next` and `error` callbacks. The listener can be cancelled by
  calling the function that is returned when `onSnapshot` is called.

  NOTE: Although an `onCompletion` callback can be provided, it will
  never be called because the snapshot stream is never-ending.

  #### Parameters

  -

    ##### options: [SnapshotListenOptions](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.SnapshotListenOptions)

    Options controlling the listen behavior.
  -

    ##### onNext: (snapshot: [QuerySnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot)\<T\>) =\> void

    A callback to be called every time a new `QuerySnapshot`
    is available.
    -
      - (snapshot: [QuerySnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot)\<T\>): void

      <!-- -->

      -

        #### Parameters

        -

          ##### snapshot: [QuerySnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.QuerySnapshot)\<T\>

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

### orderBy

- orderBy ( fieldPath : string \| [FieldPath](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldPath) , directionStr ? : [OrderByDirection](https://firebase.google.com/docs/reference/js/v8/firebase.firestore#orderbydirection) ) : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query) \< T \>
- Creates and returns a new Query that's additionally sorted by the
  specified field, optionally in descending order instead of ascending.

  #### Parameters

  -

    ##### fieldPath: string \| [FieldPath](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldPath)

    The field to sort by.
  -

    ##### Optional directionStr: [OrderByDirection](https://firebase.google.com/docs/reference/js/v8/firebase.firestore#orderbydirection)

    Optional direction to sort by (`asc` or `desc`). If
    not specified, order will be ascending.

  #### Returns [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query)\<T\>

  The created Query.

### startAfter

- startAfter ( snapshot : [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot) \< any \> ) : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query) \< T \>
- Creates and returns a new Query that starts after the provided document
  (exclusive). The starting position is relative to the order of the query.
  The document must contain all of the fields provided in the orderBy of
  this query.

  #### Parameters

  -

    ##### snapshot: [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot)\<any\>

    The snapshot of the document to start after.

  #### Returns [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query)\<T\>

  The created Query.
- startAfter ( ... fieldValues : any \[\] ) : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query) \< T \>
- Creates and returns a new Query that starts after the provided fields
  relative to the order of the query. The order of the field values
  must match the order of the order by clauses of the query.

  #### Parameters

  -

    ##### Rest ...fieldValues: any\[\]

    The field values to start this query after, in order
    of the query's order by.

  #### Returns [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query)\<T\>

  The created Query.

### startAt

- startAt ( snapshot : [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot) \< any \> ) : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query) \< T \>
- Creates and returns a new Query that starts at the provided document
  (inclusive). The starting position is relative to the order of the query.
  The document must contain all of the fields provided in the `orderBy` of
  this query.

  #### Parameters

  -

    ##### snapshot: [DocumentSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentSnapshot)\<any\>

    The snapshot of the document to start at.

  #### Returns [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query)\<T\>

  The created Query.
- startAt ( ... fieldValues : any \[\] ) : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query) \< T \>
- Creates and returns a new Query that starts at the provided fields
  relative to the order of the query. The order of the field values
  must match the order of the order by clauses of the query.

  #### Parameters

  -

    ##### Rest ...fieldValues: any\[\]

    The field values to start this query at, in order
    of the query's order by.

  #### Returns [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query)\<T\>

  The created Query.

### where

- where ( fieldPath : string \| [FieldPath](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldPath) , opStr : [WhereFilterOp](https://firebase.google.com/docs/reference/js/v8/firebase.firestore#wherefilterop) , value : any ) : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query) \< T \>
- Creates and returns a new Query with the additional filter that documents
  must contain the specified field and the value should satisfy the
  relation constraint provided.

  #### Parameters

  -

    ##### fieldPath: string \| [FieldPath](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldPath)

    The path to compare
  -

    ##### opStr: [WhereFilterOp](https://firebase.google.com/docs/reference/js/v8/firebase.firestore#wherefilterop)

    The operation string (e.g "\<", "\<=", "==", "\>", "\>=").
  -

    ##### value: any

    The value for comparison

  #### Returns [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query)\<T\>

  The created Query.

### withConverter

- withConverter ( converter : null ) : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query) \< [DocumentData](https://firebase.google.com/docs/reference/js/v8/firebase.firestore#documentdata) \>
- Applies a custom data converter to this Query, allowing you to use your
  own custom model objects with Firestore. When you call get() on the
  returned Query, the provided converter will convert between Firestore
  data and your custom type U.

  Passing in `null` as the converter parameter removes the current
  converter.

  #### Parameters

  -

    ##### converter: null

    Converts objects to and from Firestore. Passing in
    `null` removes the current converter.

  #### Returns [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query)\<[DocumentData](https://firebase.google.com/docs/reference/js/v8/firebase.firestore#documentdata)\>

  A Querythat uses the provided converter.
- withConverter \< U \> ( converter : [FirestoreDataConverter](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreDataConverter) \< U \> ) : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query) \< U \>
- Applies a custom data converter to this Query, allowing you to use your
own custom model objects with Firestore. When you call get() on the
returned Query, the provided converter will convert between Firestore
data and your custom type U.
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
#### Returns [Query](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Query)\<U\>
A Querythat uses the provided converter.