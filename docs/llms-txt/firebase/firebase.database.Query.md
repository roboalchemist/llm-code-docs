# Source: https://firebase.google.com/docs/reference/node/firebase.database.Query.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.database.Query.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.database.Query.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.database.Query.md.txt

# Query | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [database](https://firebase.google.com/docs/reference/js/v8/firebase.database).
- Query

A `Query` sorts and filters the data at a Database location so only a subset
of the child data is included. This can be used to order a collection of
data by some attribute (for example, height of dinosaurs) as well as to
restrict a large list of items (for example, chat messages) down to a number
suitable for synchronizing to the client. Queries are created by chaining
together one or more of the filter methods defined here.

Just as with a `Reference`, you can receive data from a `Query` by using the
`on()` method. You will only receive events and `DataSnapshot`s for the
subset of the data that matches your query.

Read our documentation on
[Sorting and filtering data](https://firebase.google.com/docs/database/web/lists-of-data#sorting_and_filtering_data) for more information.

## Index

### Properties

- [ref](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query#ref)

### Methods

- [endAt](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query#endat)
- [endBefore](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query#endbefore)
- [equalTo](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query#equalto)
- [get](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query#get)
- [isEqual](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query#isequal)
- [limitToFirst](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query#limittofirst)
- [limitToLast](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query#limittolast)
- [off](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query#off)
- [on](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query#on)
- [once](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query#once)
- [orderByChild](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query#orderbychild)
- [orderByKey](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query#orderbykey)
- [orderByPriority](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query#orderbypriority)
- [orderByValue](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query#orderbyvalue)
- [startAfter](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query#startafter)
- [startAt](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query#startat)
- [toJSON](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query#tojson)
- [toString](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query#tostring)

## Properties

### ref

ref: [Reference](https://firebase.google.com/docs/reference/js/v8/firebase.database.Reference)  
Returns a `Reference` to the `Query`'s location.

## Methods

### endAt

- endAt ( value : number \| string \| boolean \| null , key ? : string ) : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query)
- Creates a `Query` with the specified ending point.

  Using `startAt()`, `startAfter()`, `endBefore()`, `endAt()` and `equalTo()`
  allows you to choose arbitrary starting and ending points for your queries.

  The ending point is inclusive, so children with exactly the specified value
  will be included in the query. The optional key argument can be used to
  further limit the range of the query. If it is specified, then children that
  have exactly the specified value must also have a key name less than or equal
  to the specified key.

  You can read more about `endAt()` in
  [Filtering data](https://firebase.google.com/docs/database/web/lists-of-data#filtering_data).

  example
  :

          // Find all dinosaurs whose names come before Pterodactyl lexicographically.
          // Include Pterodactyl in the result.
          var ref = firebase.database().ref("dinosaurs");
          ref.orderByKey().endAt("pterodactyl").on("child_added", function(snapshot) {
            console.log(snapshot.key);
          });


  #### Parameters

  -

    ##### value: number \| string \| boolean \| null

    The value to end at. The argument
    type depends on which `orderBy*()` function was used in this query.
    Specify a value that matches the `orderBy*()` type. When used in
    combination with `orderByKey()`, the value must be a string.
  -

    ##### Optional key: string

    The child key to end at, among the children with the
    previously specified priority. This argument is only allowed if ordering by
    child, value, or priority.

  #### Returns [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query)

### endBefore

- endBefore ( value : number \| string \| boolean \| null , key ? : string ) : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query)
- Creates a `Query` with the specified ending point (exclusive).

  Using `startAt()`, `startAfter()`, `endBefore()`, `endAt()` and `equalTo()`
  allows you to choose arbitrary starting and ending points for your queries.

  The ending point is exclusive. If only a value is provided, children
  with a value less than the specified value will be included in the query.
  If a key is specified, then children must have a value lesss than or equal
  to the specified value and a a key name less than the specified key.

  example
  :

          // Find all dinosaurs whose names come before Pterodactyl lexicographically.
          // Do not include Pterodactyl in the result.
          var ref = firebase.database().ref("dinosaurs");
          ref.orderByKey().endBefore("pterodactyl").on("child_added", function(snapshot) {
            console.log(snapshot.key);
          });

          @param value The value to end before. The argument
            type depends on which `orderBy*()` function was used in this query.
            Specify a value that matches the `orderBy*()` type. When used in
            combination with `orderByKey()`, the value must be a string.
          @param key The child key to end before, among the children with the
            previously specified priority. This argument is only allowed if ordering by
            child, value, or priority.


  #### Parameters

  -

    ##### value: number \| string \| boolean \| null

  -

    ##### Optional key: string

  #### Returns [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query)

### equalTo

- equalTo ( value : number \| string \| boolean \| null , key ? : string ) : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query)
- Creates a `Query` that includes children that match the specified value.

  Using `startAt()`, `startAfter()`, `endBefore()`, `endAt()` and `equalTo()`
  allows you to choose arbitrary starting and ending points for your queries.

  The optional key argument can be used to further limit the range of the
  query. If it is specified, then children that have exactly the specified
  value must also have exactly the specified key as their key name. This can be
  used to filter result sets with many matches for the same value.

  You can read more about `equalTo()` in
  [Filtering data](https://firebase.google.com/docs/database/web/lists-of-data#filtering_data).

  example
  :

          // Find all dinosaurs whose height is exactly 25 meters.
          var ref = firebase.database().ref("dinosaurs");
          ref.orderByChild("height").equalTo(25).on("child_added", function(snapshot) {
            console.log(snapshot.key);
          });


  #### Parameters

  -

    ##### value: number \| string \| boolean \| null

    The value to match for. The
    argument type depends on which `orderBy*()` function was used in this
    query. Specify a value that matches the `orderBy*()` type. When used in
    combination with `orderByKey()`, the value must be a string.
  -

    ##### Optional key: string

    The child key to start at, among the children with the
    previously specified priority. This argument is only allowed if ordering by
    child, value, or priority.

  #### Returns [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query)

### get

- get ( ) : Promise \< [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot) \>
- Gets the most up-to-date result for this query.

  #### Returns Promise\<[DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot)\>

  A promise which resolves to the resulting DataSnapshot if
  a value is available, or rejects if the client is unable to return
  a value (e.g., if the server is unreachable and there is nothing
  cached).

### isEqual

- isEqual ( other : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query) \| null ) : boolean
- Returns whether or not the current and provided queries represent the same
  location, have the same query parameters, and are from the same instance of
  `firebase.app.App`.

  Two `Reference` objects are equivalent if they represent the same location
  and are from the same instance of `firebase.app.App`.

  Two `Query` objects are equivalent if they represent the same location, have
  the same query parameters, and are from the same instance of
  `firebase.app.App`. Equivalent queries share the same sort order, limits, and
  starting and ending points.

  example
  :

          var rootRef = firebase.database.ref();
          var usersRef = rootRef.child("users");

          usersRef.isEqual(rootRef);  // false
          usersRef.isEqual(rootRef.child("users"));  // true
          usersRef.parent.isEqual(rootRef);  // true


  example
  :

          var rootRef = firebase.database.ref();
          var usersRef = rootRef.child("users");
          var usersQuery = usersRef.limitToLast(10);

          usersQuery.isEqual(usersRef);  // false
          usersQuery.isEqual(usersRef.limitToLast(10));  // true
          usersQuery.isEqual(rootRef.limitToLast(10));  // false
          usersQuery.isEqual(usersRef.orderByKey().limitToLast(10));  // false


  #### Parameters

  -

    ##### other: [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query) \| null

    The query to compare against.

  #### Returns boolean

  Whether or not the current and provided queries are
  equivalent.

### limitToFirst

- limitToFirst ( limit : number ) : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query)
- Generates a new `Query` limited to the first specific number of children.

  The `limitToFirst()` method is used to set a maximum number of children to be
  synced for a given callback. If we set a limit of 100, we will initially only
  receive up to 100 `child_added` events. If we have fewer than 100 messages
  stored in our Database, a `child_added` event will fire for each message.
  However, if we have over 100 messages, we will only receive a `child_added`
  event for the first 100 ordered messages. As items change, we will receive
  `child_removed` events for each item that drops out of the active list so
  that the total number stays at 100.

  You can read more about `limitToFirst()` in
  [Filtering data](https://firebase.google.com/docs/database/web/lists-of-data#filtering_data).

  example
  :

          // Find the two shortest dinosaurs.
          var ref = firebase.database().ref("dinosaurs");
          ref.orderByChild("height").limitToFirst(2).on("child_added", function(snapshot) {
            // This will be called exactly two times (unless there are less than two
            // dinosaurs in the Database).

            // It will also get fired again if one of the first two dinosaurs is
            // removed from the data set, as a new dinosaur will now be the second
            // shortest.
            console.log(snapshot.key);
          });


  #### Parameters

  -

    ##### limit: number

    The maximum number of nodes to include in this query.

  #### Returns [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query)

### limitToLast

- limitToLast ( limit : number ) : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query)
- Generates a new `Query` object limited to the last specific number of
  children.

  The `limitToLast()` method is used to set a maximum number of children to be
  synced for a given callback. If we set a limit of 100, we will initially only
  receive up to 100 `child_added` events. If we have fewer than 100 messages
  stored in our Database, a `child_added` event will fire for each message.
  However, if we have over 100 messages, we will only receive a `child_added`
  event for the last 100 ordered messages. As items change, we will receive
  `child_removed` events for each item that drops out of the active list so
  that the total number stays at 100.

  You can read more about `limitToLast()` in
  [Filtering data](https://firebase.google.com/docs/database/web/lists-of-data#filtering_data).

  example
  :

          // Find the two heaviest dinosaurs.
          var ref = firebase.database().ref("dinosaurs");
          ref.orderByChild("weight").limitToLast(2).on("child_added", function(snapshot) {
            // This callback will be triggered exactly two times, unless there are
            // fewer than two dinosaurs stored in the Database. It will also get fired
            // for every new, heavier dinosaur that gets added to the data set.
            console.log(snapshot.key);
          });


  #### Parameters

  -

    ##### limit: number

    The maximum number of nodes to include in this query.

  #### Returns [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query)

### off

- off ( eventType ? : [EventType](https://firebase.google.com/docs/reference/js/v8/firebase.database#eventtype) , callback ? : ( a : [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot) , b ? : string \| null ) =\> any , context ? : Object \| null ) : void
- Detaches a callback previously attached with `on()`.

  Detach a callback previously attached with `on()`. Note that if `on()` was
  called multiple times with the same eventType and callback, the callback
  will be called multiple times for each event, and `off()` must be called
  multiple times to remove the callback. Calling `off()` on a parent listener
  will not automatically remove listeners registered on child nodes, `off()`
  must also be called on any child listeners to remove the callback.

  If a callback is not specified, all callbacks for the specified eventType
  will be removed. Similarly, if no eventType is specified, all callbacks
  for the `Reference` will be removed.

  example
  :

          var onValueChange = function(dataSnapshot) {  ... };
          ref.on('value', onValueChange);
          ref.child('meta-data').on('child_added', onChildAdded);
          // Sometime later...
          ref.off('value', onValueChange);

          // You must also call off() for any child listeners on ref
          // to cancel those callbacks
          ref.child('meta-data').off('child_added', onValueAdded);


  example
  :

          // Or you can save a line of code by using an inline function
          // and on()'s return value.
          var onValueChange = ref.on('value', function(dataSnapshot) { ... });
          // Sometime later...
          ref.off('value', onValueChange);


  #### Parameters

  -

    ##### Optional eventType: [EventType](https://firebase.google.com/docs/reference/js/v8/firebase.database#eventtype)

    One of the following strings: "value",
    "child_added", "child_changed", "child_removed", or "child_moved." If
    omitted, all callbacks for the `Reference` will be removed.
  -

    ##### Optional callback: (a: [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot), b?: string \| null) =\> any

    The callback function that was passed to `on()` or
    `undefined` to remove all callbacks.
    -
      - (a: [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot), b?: string \| null): any

      <!-- -->

      -

        #### Parameters

        -

          ##### a: [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot)

        -

          ##### Optional b: string \| null

        #### Returns any

  -

    ##### Optional context: Object \| null

    The context that was passed to `on()`.

  #### Returns void

### on

- on ( eventType : [EventType](https://firebase.google.com/docs/reference/js/v8/firebase.database#eventtype) , callback : ( a : [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot) , b ? : string \| null ) =\> any , cancelCallbackOrContext ? : ( ( a : [Error](https://firebase.google.com/docs/reference/js/v8/firebase.functions.HttpsError#error) ) =\> any ) \| Object \| null , context ? : Object \| null ) : ( a : [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot) \| null , b ? : string \| null ) =\> any
- Listens for data changes at a particular location.

  This is the primary way to read data from a Database. Your callback
  will be triggered for the initial data and again whenever the data changes.
  Use `off( )` to stop receiving updates. See
  [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data)
  for more details.

  #### value event

  This event will trigger once with the initial data stored at this location,
  and then trigger again each time the data changes. The `DataSnapshot` passed
  to the callback will be for the location at which `on()` was called. It
  won't trigger until the entire contents has been synchronized. If the
  location has no data, it will be triggered with an empty `DataSnapshot`
  (`val()` will return `null`).

  #### child_added event

  This event will be triggered once for each initial child at this location,
  and it will be triggered again every time a new child is added. The
  `DataSnapshot` passed into the callback will reflect the data for the
  relevant child. For ordering purposes, it is passed a second argument which
  is a string containing the key of the previous sibling child by sort order,
  or `null` if it is the first child.

  #### child_removed event

  This event will be triggered once every time a child is removed. The
  `DataSnapshot` passed into the callback will be the old data for the child
  that was removed. A child will get removed when either:
  - a client explicitly calls `remove()` on that child or one of its ancestors
  - a client calls `set(null)` on that child or one of its ancestors
  - that child has all of its children removed
  - there is a query in effect which now filters out the child (because it's sort order changed or the max limit was hit)

  #### child_changed event

  This event will be triggered when the data stored in a child (or any of its
  descendants) changes. Note that a single `child_changed` event may represent
  multiple changes to the child. The `DataSnapshot` passed to the callback will
  contain the new child contents. For ordering purposes, the callback is also
  passed a second argument which is a string containing the key of the previous
  sibling child by sort order, or `null` if it is the first child.

  #### child_moved event

  This event will be triggered when a child's sort order changes such that its
  position relative to its siblings changes. The `DataSnapshot` passed to the
  callback will be for the data of the child that has moved. It is also passed
  a second argument which is a string containing the key of the previous
  sibling child by sort order, or `null` if it is the first child.

  example

  :   **Handle a new value:**

          ref.on('value', function(dataSnapshot) {
            ...
          });

  example

  :   **Handle a new child:**

          ref.on('child_added', function(childSnapshot, prevChildKey) {
            ...
          });

  example

  :   **Handle child removal:**

          ref.on('child_removed', function(oldChildSnapshot) {
            ...
          });

  example

  :   **Handle child data changes:**

          ref.on('child_changed', function(childSnapshot, prevChildKey) {
            ...
          });

  example

  :   **Handle child ordering changes:**

          ref.on('child_moved', function(childSnapshot, prevChildKey) {
            ...
          });

  #### Parameters

  -

    ##### eventType: [EventType](https://firebase.google.com/docs/reference/js/v8/firebase.database#eventtype)

    One of the following strings: "value",
    "child_added", "child_changed", "child_removed", or "child_moved."
  -

    ##### callback: (a: [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot), b?: string \| null) =\> any

    A
    callback that fires when the specified event occurs. The callback will be
    passed a DataSnapshot. For ordering purposes, "child_added",
    "child_changed", and "child_moved" will also be passed a string containing
    the key of the previous child, by sort order, or `null` if it is the
    first child.
    -
      - (a: [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot), b?: string \| null): any

      <!-- -->

      -

        #### Parameters

        -

          ##### a: [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot)

        -

          ##### Optional b: string \| null

        #### Returns any

  -

    ##### Optional cancelCallbackOrContext: ((a: [Error](https://firebase.google.com/docs/reference/js/v8/firebase.functions.HttpsError#error)) =\> any) \| Object \| null

    An optional
    callback that will be notified if your event subscription is ever canceled
    because your client does not have permission to read this data (or it had
    permission but has now lost it). This callback will be passed an `Error`
    object indicating why the failure occurred.
  -

    ##### Optional context: Object \| null

    If provided, this object will be used as `this`
    when calling your callback(s).

  #### Returns (a: [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot) \| null, b?: string \| null) =\> any

  The provided
  callback function is returned unmodified. This is just for convenience if
  you want to pass an inline function to `on()` but store the callback
  function for later passing to `off()`.
  -
    - (a: [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot) \| null, b?: string \| null): any

    <!-- -->

    -

      #### Parameters

      -

        ##### a: [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot) \| null

      -

        ##### Optional b: string \| null

      #### Returns any

### once

- once ( eventType : [EventType](https://firebase.google.com/docs/reference/js/v8/firebase.database#eventtype) , successCallback ? : ( a : [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot) , b ? : string \| null ) =\> any , failureCallbackOrContext ? : ( ( a : [Error](https://firebase.google.com/docs/reference/js/v8/firebase.functions.HttpsError#error) ) =\> void ) \| Object \| null , context ? : Object \| null ) : Promise \< [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot) \>
- Listens for exactly one event of the specified event type, and then stops
  listening.

  This is equivalent to calling [`on()`](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query#on), and
  then calling [`off()`](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query#off) inside the callback
  function. See [`on()`](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query#on) for details on the
  event types.

  example
  :

          // Basic usage of .once() to read the data located at ref.
          ref.once('value')
            .then(function(dataSnapshot) {
              // handle read data.
            });


  #### Parameters

  -

    ##### eventType: [EventType](https://firebase.google.com/docs/reference/js/v8/firebase.database#eventtype)

    One of the following strings: "value",
    "child_added", "child_changed", "child_removed", or "child_moved."
  -

    ##### Optional successCallback: (a: [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot), b?: string \| null) =\> any

    A
    callback that fires when the specified event occurs. The callback will be
    passed a DataSnapshot. For ordering purposes, "child_added",
    "child_changed", and "child_moved" will also be passed a string containing
    the key of the previous child by sort order, or `null` if it is the
    first child.
    -
      - (a: [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot), b?: string \| null): any

      <!-- -->

      -

        #### Parameters

        -

          ##### a: [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot)

        -

          ##### Optional b: string \| null

        #### Returns any

  -

    ##### Optional failureCallbackOrContext: ((a: [Error](https://firebase.google.com/docs/reference/js/v8/firebase.functions.HttpsError#error)) =\> void) \| Object \| null

    An optional
    callback that will be notified if your client does not have permission to
    read the data. This callback will be passed an `Error` object indicating
    why the failure occurred.
  -

    ##### Optional context: Object \| null

    If provided, this object will be used as `this`
    when calling your callback(s).

  #### Returns Promise\<[DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot)\>

### orderByChild

- orderByChild ( path : string ) : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query)
- Generates a new `Query` object ordered by the specified child key.

  Queries can only order by one key at a time. Calling `orderByChild()`
  multiple times on the same query is an error.

  Firebase queries allow you to order your data by any child key on the fly.
  However, if you know in advance what your indexes will be, you can define
  them via the .indexOn rule in your Security Rules for better performance. See
  the [.indexOn](https://firebase.google.com/docs/database/security/indexing-data) rule for more information.

  You can read more about `orderByChild()` in
  [Sort data](https://firebase.google.com/docs/database/web/lists-of-data#sort_data).

  example
  :

          var ref = firebase.database().ref("dinosaurs");
          ref.orderByChild("height").on("child_added", function(snapshot) {
            console.log(snapshot.key + " was " + snapshot.val().height + " m tall");
          });


  #### Parameters

  -

    ##### path: string

  #### Returns [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query)

### orderByKey

- orderByKey ( ) : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query)
- Generates a new `Query` object ordered by key.

  Sorts the results of a query by their (ascending) key values.

  You can read more about `orderByKey()` in
  [Sort data](https://firebase.google.com/docs/database/web/lists-of-data#sort_data).

  example
  :

          var ref = firebase.database().ref("dinosaurs");
          ref.orderByKey().on("child_added", function(snapshot) {
            console.log(snapshot.key);
          });


  #### Returns [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query)

### orderByPriority

- orderByPriority ( ) : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query)
- Generates a new `Query` object ordered by priority.

  Applications need not use priority but can order collections by
  ordinary properties (see
  [Sort data](https://firebase.google.com/docs/database/web/lists-of-data#sort_data) for alternatives to priority.

  #### Returns [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query)

### orderByValue

- orderByValue ( ) : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query)
- Generates a new `Query` object ordered by value.

  If the children of a query are all scalar values (string, number, or
  boolean), you can order the results by their (ascending) values.

  You can read more about `orderByValue()` in
  [Sort data](https://firebase.google.com/docs/database/web/lists-of-data#sort_data).

  example
  :

          var scoresRef = firebase.database().ref("scores");
          scoresRef.orderByValue().limitToLast(3).on("value", function(snapshot) {
            snapshot.forEach(function(data) {
              console.log("The " + data.key + " score is " + data.val());
            });
          });


  #### Returns [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query)

### startAfter

- startAfter ( value : number \| string \| boolean \| null , key ? : string ) : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query)
- Creates a `Query` with the specified starting point (exclusive).

  Using `startAt()`, `startAfter()`, `endBefore()`, `endAt()` and `equalTo()`
  allows you to choose arbitrary starting and ending points for your queries.

  The starting point is exclusive. If only a value is provided, children
  with a value greater than the specified value will be included in the query.
  If a key is specified, then children must have a value greater than or equal
  to the specified value and a a key name greater than the specified key.

  example
  :

          // Find all dinosaurs that are more than three meters tall.
          var ref = firebase.database().ref("dinosaurs");
          ref.orderByChild("height").startAfter(3).on("child_added", function(snapshot) {
            console.log(snapshot.key)
          });


  #### Parameters

  -

    ##### value: number \| string \| boolean \| null

    The value to start after. The argument
    type depends on which `orderBy*()` function was used in this query.
    Specify a value that matches the `orderBy*()` type. When used in
    combination with `orderByKey()`, the value must be a string.
  -

    ##### Optional key: string

    The child key to start after. This argument is only allowed
    if ordering by child, value, or priority.

  #### Returns [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query)

### startAt

- startAt ( value : number \| string \| boolean \| null , key ? : string ) : [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query)
- Creates a `Query` with the specified starting point.

  Using `startAt()`, `startAfter()`, `endBefore()`, `endAt()` and `equalTo()`
  allows you to choose arbitrary starting and ending points for your queries.

  The starting point is inclusive, so children with exactly the specified value
  will be included in the query. The optional key argument can be used to
  further limit the range of the query. If it is specified, then children that
  have exactly the specified value must also have a key name greater than or
  equal to the specified key.

  You can read more about `startAt()` in
  [Filtering data](https://firebase.google.com/docs/database/web/lists-of-data#filtering_data).

  example
  :

          // Find all dinosaurs that are at least three meters tall.
          var ref = firebase.database().ref("dinosaurs");
          ref.orderByChild("height").startAt(3).on("child_added", function(snapshot) {
            console.log(snapshot.key)
          });


  #### Parameters

  -

    ##### value: number \| string \| boolean \| null

    The value to start at. The argument
    type depends on which `orderBy*()` function was used in this query.
    Specify a value that matches the `orderBy*()` type. When used in
    combination with `orderByKey()`, the value must be a string.
  -

    ##### Optional key: string

    The child key to start at. This argument is only allowed
    if ordering by child, value, or priority.

  #### Returns [Query](https://firebase.google.com/docs/reference/js/v8/firebase.database.Query)

### toJSON

- toJSON ( ) : Object
- Returns a JSON-serializable representation of this object.

  #### Returns Object

  A JSON-serializable representation of this object.

### toString

- toString ( ) : string
- Gets the absolute URL for this location.

  The `toString()` method returns a URL that is ready to be put into a browser,
  curl command, or a `firebase.database().refFromURL()` call. Since all of
  those expect the URL to be url-encoded, `toString()` returns an encoded URL.

  Append '.json' to the returned URL when typed into a browser to download
  JSON-formatted data. If the location is secured (that is, not publicly
  readable), you will get a permission-denied error.

  example
  :

          // Calling toString() on a root Firebase reference returns the URL where its
          // data is stored within the Database:
          var rootRef = firebase.database().ref();
          var rootUrl = rootRef.toString();
          // rootUrl === "https://sample-app.firebaseio.com/".

          // Calling toString() at a deeper Firebase reference returns the URL of that
          // deep path within the Database:
          var adaRef = rootRef.child('users/ada');
          var adaURL = adaRef.toString();
          // adaURL === "https://sample-app.firebaseio.com/users/ada".


  #### Returns string

The absolute URL for this location.